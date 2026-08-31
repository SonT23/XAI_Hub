"""
Chuyen doi block tree cua Notion (lay tu notion_client.fetch_block_tree)
sang noi dung Markdown cho MkDocs.

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\notion_to_md.py

Quy tac chuyen doi (giong voi cach da lam thu cong truoc do):
- callout          -> blockquote "> " (giu icon inline neu co)
- columns/column   -> lam phang, giu noi dung theo thu tu
- table            -> bang Markdown chuan (GFM)
- code (mermaid)   -> giu nguyen fence ```mermaid (MkDocs render native)
- code (khac)      -> fence ```<language>
- equation (block) -> $$...$$
- equation (inline)-> $...$
- mention page/database -> link tuong doi neu biet trong manifest (Context.link_map),
  neu khong biet thi in DAM plain text (KHONG BAO GIO tao link chet)
- image (external) -> ![alt](url)
- image (file/temporary S3 url) -> TAI VE NGAY va luu vao docs/assets/images/...,
  roi nhung nhu anh binh thuong bang duong dan tuong doi (chi con canh bao
  neu tai that bai, vi du URL da het han truoc khi kip dong bo)
- child_page/child_database -> KHONG duyet vao, chi ghi chu bang link (neu co trong link_map)
  hoac ten trang in nghieng (dong bo nhu 1 entry rieng trong manifest)
- toggle           -> <details><summary>...</summary> ... </details>
- divider          -> "---"
- table_of_contents, breadcrumb... (Notion tra ve it dùng qua block children) -> bo qua
"""
import os

from notion_client import download_file


class Context:
    """
    link_map: dict normalize(page_id) -> duong dan tuong doi (vd "../glossary/all.md")
              dung de chuyen <mention page> thanh link that thay vi chu in dam.
    paper_map: dict normalize(page_id) -> {"title":..., "link": external_url}
              rieng cho cac trang la row trong database "Thu vien bai bao".
    image_save_dir: duong dan TUYET DOI (tren o dia) toi thu muc se luu anh
              cua rieng trang dang render (vd "...\\docs\\assets\\images\\xai\\bai-1").
              None = khong tai anh (chi ghi chu canh bao nhu truoc).
    image_url_prefix: duong dan TUONG DOI tu file .md dang render toi thu muc
              tren (vd "../assets/images/xai/bai-1"), dung de chen vao the
              ![]() trong Markdown.
    """

    def __init__(self, link_map=None, paper_map=None, image_save_dir=None, image_url_prefix=None):
        self.link_map = link_map or {}
        self.paper_map = paper_map or {}
        self.image_save_dir = image_save_dir
        self.image_url_prefix = image_url_prefix
        self._image_counter = 0


def _normalize_id(page_id):
    return (page_id or "").replace("-", "").lower()


def _guess_image_ext(url):
    """Doan phan mo rong file anh tu URL (bo qua phan query string ?X-Amz-...)."""
    from urllib.parse import urlparse
    path = urlparse(url).path
    _, ext = os.path.splitext(path)
    if ext and 2 <= len(ext) <= 5:
        return ext.lower()
    return ".png"


def resolve_mention(ctx, page_id, fallback_text):
    """Tra ve chuoi Markdown cho 1 mention page/database."""
    nid = _normalize_id(page_id)
    if nid in ctx.link_map:
        return f"[{fallback_text}]({ctx.link_map[nid]})"
    if nid in ctx.paper_map:
        info = ctx.paper_map[nid]
        if info.get("link"):
            return f"[{fallback_text}]({info['link']})"
    return f"**{fallback_text}**"


def rich_text_to_md(rich_text_list, ctx):
    """Chuyen 1 danh sach rich_text object cua Notion sang chuoi Markdown."""
    if not rich_text_list:
        return ""
    parts = []
    for rt in rich_text_list:
        rtype = rt.get("type")
        plain = rt.get("plain_text", "")

        if rtype == "equation":
            expr = rt.get("equation", {}).get("expression", "")
            parts.append(f"${expr}$")
            continue

        if rtype == "mention":
            mention = rt.get("mention", {})
            mtype = mention.get("type")
            if mtype == "page":
                page_id = mention.get("page", {}).get("id", "")
                parts.append(resolve_mention(ctx, page_id, plain or "(trang không tên)"))
                continue
            elif mtype == "database":
                db_id = mention.get("database", {}).get("id", "")
                parts.append(resolve_mention(ctx, db_id, plain or "(cơ sở dữ liệu)"))
                continue
            elif mtype == "date":
                parts.append(plain)
                continue
            else:
                parts.append(plain)
                continue

        # text hoac loai khac: ap dung annotation
        text = plain
        ann = rt.get("annotations", {})
        href = rt.get("href") or (rt.get("text", {}) or {}).get("link", {})
        href_url = None
        if isinstance(href, dict):
            href_url = href.get("url")
        elif isinstance(href, str):
            href_url = href

        if not text:
            continue

        # escape ky tu markdown de tranh vo dinh dang khong mong muon o mep chu
        if ann.get("code"):
            text = f"`{text}`"
        else:
            if ann.get("bold") and ann.get("italic"):
                text = f"***{text}***"
            elif ann.get("bold"):
                text = f"**{text}**"
            elif ann.get("italic"):
                text = f"*{text}*"
            if ann.get("strikethrough"):
                text = f"~~{text}~~"

        if href_url:
            text = f"[{text}]({href_url})"

        parts.append(text)
    return "".join(parts)


def render_table(block, ctx):
    """block la loai 'table', children (_children) la danh sach 'table_row'."""
    rows = block.get("_children", [])
    if not rows:
        return ""
    has_header = block.get("table", {}).get("has_column_header", False)
    lines = []
    for i, row in enumerate(rows):
        cells = row.get("table_row", {}).get("cells", [])
        cell_texts = [rich_text_to_md(c, ctx).replace("\n", " ").strip() or " " for c in cells]
        lines.append("| " + " | ".join(cell_texts) + " |")
        if i == 0:
            sep = "|" + "|".join([" --- " for _ in cell_texts]) + "|"
            lines.append(sep)
    if not has_header:
        # neu khong co header, van gia lap 1 dong sep sau dong dau de bang render dung GFM
        pass
    return "\n".join(lines)


def render_blocks(blocks, ctx, _list_stack=None):
    """Chuyen danh sach block (co _children de quy) sang Markdown, tra ve list dong."""
    out = []
    prev_type = None
    numbered_counter = 0

    for block in blocks:
        btype = block.get("type")
        data = block.get(btype, {}) if btype else {}

        if btype != "numbered_list_item":
            numbered_counter = 0

        if btype == "paragraph":
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            out.append(text)
            out.append("")

        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = {"heading_1": "##", "heading_2": "###", "heading_3": "####"}[btype]
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            out.append(f"{level} {text}")
            out.append("")

        elif btype == "bulleted_list_item":
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            out.append(f"- {text}")
            if block.get("_children"):
                sub = render_blocks(block["_children"], ctx)
                for line in sub:
                    out.append(f"    {line}" if line else "")
            out.append("")

        elif btype == "numbered_list_item":
            numbered_counter += 1
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            out.append(f"{numbered_counter}. {text}")
            if block.get("_children"):
                sub = render_blocks(block["_children"], ctx)
                for line in sub:
                    out.append(f"    {line}" if line else "")
            out.append("")

        elif btype == "to_do":
            checked = data.get("checked", False)
            mark = "x" if checked else " "
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            out.append(f"- [{mark}] {text}")
            out.append("")

        elif btype == "quote":
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            for line in text.split("\n"):
                out.append(f"> {line}")
            out.append("")

        elif btype == "callout":
            icon = data.get("icon", {})
            icon_str = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            prefix = f"{icon_str} " if icon_str else ""
            first = True
            for line in text.split("\n"):
                out.append(f"> {prefix if first else ''}{line}")
                first = False
            if block.get("_children"):
                sub = render_blocks(block["_children"], ctx)
                for line in sub:
                    out.append(f"> {line}" if line else ">")
            out.append("")

        elif btype == "divider":
            out.append("---")
            out.append("")

        elif btype == "code":
            language = data.get("language", "") or ""
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            lang_tag = "mermaid" if language == "mermaid" else language
            out.append(f"```{lang_tag}")
            out.append(text)
            out.append("```")
            out.append("")

        elif btype == "equation":
            expr = data.get("expression", "")
            out.append(f"$${expr}$$")
            out.append("")

        elif btype == "table":
            out.append(render_table(block, ctx))
            out.append("")

        elif btype == "column_list":
            # lam phang: render tung column theo thu tu, khong dung tag <columns>
            for col in block.get("_children", []):
                sub = render_blocks(col.get("_children", []), ctx)
                out.extend(sub)

        elif btype == "column":
            sub = render_blocks(block.get("_children", []), ctx)
            out.extend(sub)

        elif btype == "toggle":
            text = rich_text_to_md(data.get("rich_text", []), ctx)
            # markdown="1" bat buoc phai co de MkDocs (python-markdown, extension
            # md_in_html trong mkdocs.yml) chiu xu ly Markdown long ben trong the
            # HTML nay (dam, danh sach, ...) thay vi coi toan bo la HTML tho.
            out.append('<details markdown="1">')
            out.append(f"<summary>{text}</summary>")
            out.append("")
            if block.get("_children"):
                sub = render_blocks(block["_children"], ctx)
                out.extend(sub)
            out.append("</details>")
            out.append("")

        elif btype == "image":
            img = data
            itype = img.get("type")
            caption = rich_text_to_md(img.get("caption", []), ctx)
            if itype == "external":
                url = img.get("external", {}).get("url", "")
                out.append(f"![{caption}]({url})")
                out.append("")
            else:
                # file type: URL tam thoi (S3, se het han sau vai gio) -> tai
                # ngay ve va luu vao repo (docs/assets/images/...) de co duong
                # dan vinh vien, khong phu thuoc Notion nua. Chi khi tai that
                # bai (mang loi, URL da het han truoc khi kip dong bo, ...)
                # moi rot ve ghi chu canh bao nhu truoc.
                file_url = img.get("file", {}).get("url", "")
                saved_rel_url = None
                if file_url and ctx.image_save_dir and ctx.image_url_prefix:
                    try:
                        ctx._image_counter += 1
                        ext = _guess_image_ext(file_url)
                        filename = f"img-{ctx._image_counter}{ext}"
                        dest_path = os.path.join(ctx.image_save_dir, filename)
                        download_file(file_url, dest_path)
                        saved_rel_url = f"{ctx.image_url_prefix}/{filename}"
                    except Exception:
                        saved_rel_url = None
                if saved_rel_url:
                    out.append(f"![{caption}]({saved_rel_url})")
                else:
                    out.append(f"_[Hình ảnh không thể tự động chuyển đổi — URL tạm thời của Notion đã hết hạn hoặc tải xuống thất bại. Vui lòng cập nhật thủ công nếu cần: {caption or '(không có mô tả)'}]_")
                out.append("")

        elif btype == "bookmark":
            url = data.get("url", "")
            caption = rich_text_to_md(data.get("caption", []), ctx)
            label = caption or url
            out.append(f"[{label}]({url})")
            out.append("")

        elif btype in ("child_page", "child_database"):
            title = data.get("title", "(trang con)")
            block_id = _normalize_id(block.get("id", ""))
            if block_id in ctx.link_map:
                out.append(f"- [{title}]({ctx.link_map[block_id]})")
            else:
                out.append(f"- _{title}_ (chưa được đồng bộ riêng)")
            out.append("")

        elif btype in ("table_of_contents", "breadcrumb", "unsupported"):
            pass  # bo qua, MkDocs Material da tu sinh muc luc rieng

        else:
            # loai block khong xu ly rieng: co gang lay rich_text neu co
            text = rich_text_to_md(data.get("rich_text", []), ctx) if isinstance(data, dict) else ""
            if text:
                out.append(text)
                out.append("")

        prev_type = btype

    return out


def blocks_to_markdown(blocks, ctx):
    lines = render_blocks(blocks, ctx)
    # gon bot qua nhieu dong trong lien tiep
    result = []
    blank = False
    for line in lines:
        if line == "":
            if blank:
                continue
            blank = True
        else:
            blank = False
        result.append(line)
    return "\n".join(result).strip() + "\n"
