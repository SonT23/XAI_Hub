#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dong bo TOAN BO cac trang kien thuc (Toan, ML co ban, Deep Learning, XAI,
Ky nang nghien cuu) tu Notion sang cac file docs/*.md, dua vao
scripts/pages_manifest.json.

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\sync_pages.py
Chay doc lap de test:  python scripts\\sync_pages.py
(sync_and_push.py se tu goi ham sync_all_pages() ben duoi, khong can chay
file nay truc tiep trong quy trinh tu dong binh thuong)

LUU Y QUAN TRONG: day la code MOI, CHUA duoc chay thu voi Notion token that
cua ban. Rat co the lan chay dau tien se gap loi can sua cung nhau (vi du:
loai block Notion chua duoc xu ly, gioi han API, ...). Neu gap loi, cop
nguyen thong bao loi gui lai de debug.
"""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from notion_client import load_env, get_headers, normalize_id, fetch_block_tree, get_page_title
from notion_to_md import Context, blocks_to_markdown

ENV_PATH = os.path.join(PROJECT_ROOT, ".env")
MANIFEST_PATH = os.path.join(SCRIPT_DIR, "pages_manifest.json")
PAPERS_RAW_PATH = os.path.join(PROJECT_ROOT, "data", "papers_raw.json")


def _rel_link(from_output, to_output):
    """Tinh duong dan tuong doi tu 1 file docs/... toi 1 file docs/... khac,
    dung cho link markdown (MkDocs dung duong dan tuong doi kieu file, khong
    phai URL kieu web)."""
    from_dir = os.path.dirname(from_output)
    rel = os.path.relpath(to_output, from_dir)
    return rel.replace(os.sep, "/")


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def build_paper_map():
    """Doc data/papers_raw.json, tra ve dict normalize(id) -> {title, link}
    de resolve mention-page trong noi dung sang link ngoai (arXiv/journal)
    thay vi link noi bo (vi trang bai bao khong co file .md rieng cho tung
    bai)."""
    paper_map = {}
    if not os.path.exists(PAPERS_RAW_PATH):
        return paper_map
    with open(PAPERS_RAW_PATH, encoding="utf-8") as f:
        rows = json.load(f)
    for r in rows:
        page_id = r.get("_page_id") or r.get("id") or r.get("ID")
        if not page_id:
            continue
        paper_map[normalize_id(page_id)] = {
            "title": (r.get("Tên bài báo") or "").strip(),
            "link": r.get("Link") or "",
        }
    return paper_map


def build_link_map(manifest):
    """Tao dict normalize(page_id) -> duong dan output (dang docs/....md,
    se duoc chuyen thanh duong dan tuong doi khi render tung trang)."""
    link_map = {}
    for entry in manifest.get("pages", []):
        out = entry["output"]
        if "sources" in entry:
            for src_id in entry["sources"]:
                link_map[normalize_id(src_id)] = out
        else:
            link_map[normalize_id(entry["id"])] = out
    for entry in manifest.get("link_only", []):
        link_map[normalize_id(entry["id"])] = entry["output"]
    return link_map


def sync_one_page(page_id, headers, ctx, out_output_path):
    """Lay block tree cua 1 trang Notion, chuyen sang Markdown, tra ve chuoi
    noi dung (chua bao gom tieu de H1 - se duoc them rieng)."""
    blocks = fetch_block_tree(page_id, headers)
    # ctx.link_map dang chua duong dan dang "docs/xxx.md" (tuyet doi so voi
    # PROJECT_ROOT) -> can chuyen thanh duong dan TUONG DOI so voi trang dang
    # render truoc khi dua vao rich_text_to_md. Tao 1 ban link_map rieng cho
    # trang nay.
    local_ctx = Context(
        link_map={
            pid: _rel_link(out_output_path, out) if not out.startswith("http") else out
            for pid, out in ctx.link_map.items()
        },
        paper_map=ctx.paper_map,
    )
    return blocks_to_markdown(blocks, local_ctx)


def sync_all_pages(verbose=True):
    """Dong bo toan bo trang trong manifest['pages']. Tra ve (so_thanh_cong,
    so_loi, danh_sach_loi)."""
    env = load_env(ENV_PATH)
    token = env.get("NOTION_TOKEN") or os.environ.get("NOTION_TOKEN")
    if not token:
        raise RuntimeError(
            "Không tìm thấy NOTION_TOKEN trong .env (cần cùng token đã dùng cho glossary)."
        )
    headers = get_headers(token)

    manifest = load_manifest()
    link_map = build_link_map(manifest)
    paper_map = build_paper_map()
    ctx = Context(link_map=link_map, paper_map=paper_map)

    ok, errors = 0, []

    for entry in manifest.get("pages", []):
        out_rel = entry["output"]
        out_abs = os.path.join(PROJECT_ROOT, out_rel)
        sources = entry.get("sources") or [entry.get("id")]

        try:
            if len(sources) == 1:
                title = get_page_title(sources[0], headers)
                body = sync_one_page(sources[0], headers, ctx, out_rel)
                content = f"# {title}\n\n{body}"
            else:
                # gop nhieu trang con thanh 1 file (vd 04-cbm.md)
                parts = []
                for i, src_id in enumerate(sources):
                    title = get_page_title(src_id, headers)
                    body = sync_one_page(src_id, headers, ctx, out_rel)
                    heading = "#" if i == 0 else "##"
                    parts.append(f"{heading} {title}\n\n{body}")
                content = "\n\n---\n\n".join(parts)

            os.makedirs(os.path.dirname(out_abs), exist_ok=True)
            with open(out_abs, "w", encoding="utf-8") as f:
                f.write(content)

            ok += 1
            if verbose:
                print(f"  OK  {out_rel}")
        except Exception as e:  # noqa: BLE001 - muon bat moi loi de tiep tuc dong bo cac trang khac
            errors.append((out_rel, str(e)))
            if verbose:
                print(f"  LỖI {out_rel}: {e}")

    if verbose:
        print(f"\nHoàn tất đồng bộ trang: {ok} thành công, {len(errors)} lỗi.")
        if errors:
            print("Các trang gặp lỗi (nội dung cũ trên máy KHÔNG bị mất, script chỉ bỏ qua):")
            for out_rel, msg in errors:
                print(f"  - {out_rel}: {msg}")

    return ok, len(errors), errors


if __name__ == "__main__":
    sync_all_pages()
