#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dong bo TOAN BO cac trang kien thuc (Toan, ML co ban, Deep Learning, XAI,
Ky nang nghien cuu) tu Notion sang cac file docs/*.md, dua vao
scripts/pages_manifest.json.

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\sync_pages.py
Chay doc lap de test:  python scripts\\sync_pages.py
Bo qua cache, ep dong bo lai TAT CA (vi du sau khi sua loi trong chinh script
chuyen doi, noi dung Notion khong doi nhung code chuyen doi doi):
    python scripts\\sync_pages.py --force

Tinh nang (cap nhat 30/08/2026):
  1. TU DONG PHAT HIEN trang moi: neu ban tao 1 trang kien thuc moi ngay
     BEN TRONG 1 trong 4 hub (Toan/ML/Deep Learning/XAI), script se tu tim
     thay (khong can copy ID tay), tu them vao pages_manifest.json va tu
     them 1 dong vao muc luc (nav) trong mkdocs.yml.
  2. DONG BO CO CHON LOC (giong git): moi trang duoc kiem tra "last_edited_time"
     (chi 1 lan goi API nhe, khong can tai toan bo noi dung) truoc - neu
     khong doi so voi lan dong bo truoc va file .md da ton tai, BO QUA luon,
     khong ton thoi gian tai + render lai. Cache luu o scripts/.sync_cache.json.

LUU Y QUAN TRONG: day la code MOI, CHUA duoc chay thu voi Notion token that
cua ban. Rat co the lan chay dau tien se gap loi can sua cung nhau (vi du:
loai block Notion chua duoc xu ly, gioi han API, ...). Neu gap loi, cop
nguyen thong bao loi gui lai de debug.
"""
import argparse
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from notion_client import load_env, get_headers, normalize_id, fetch_block_tree, get_page_meta
from notion_to_md import Context, blocks_to_markdown
from discover_pages import discover_new_pages, append_nav_entries, MKDOCS_YML_PATH
from util import load_cache, save_cache

ENV_PATH = os.path.join(PROJECT_ROOT, ".env")
MANIFEST_PATH = os.path.join(SCRIPT_DIR, "pages_manifest.json")
PAPERS_RAW_PATH = os.path.join(PROJECT_ROOT, "data", "papers_raw.json")
CACHE_PATH = os.path.join(SCRIPT_DIR, ".sync_cache.json")


def _rel_link(from_output, to_output):
    """Tinh duong dan tuong doi tu 1 file docs/... toi 1 file docs/... khac."""
    from_dir = os.path.dirname(from_output)
    rel = os.path.relpath(to_output, from_dir)
    return rel.replace(os.sep, "/")


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_manifest(manifest):
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def build_paper_map():
    """Doc data/papers_raw.json, tra ve dict normalize(id) -> {title, link}."""
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


def render_page_content(page_id, headers, ctx, out_output_path):
    blocks = fetch_block_tree(page_id, headers)
    local_ctx = Context(
        link_map={
            pid: (_rel_link(out_output_path, out) if not out.startswith("http") else out)
            for pid, out in ctx.link_map.items()
        },
        paper_map=ctx.paper_map,
    )
    return blocks_to_markdown(blocks, local_ctx)


def sync_all_pages(verbose=True, force=False):
    """Dong bo toan bo trang trong manifest['pages'] (+ tu dong phat hien
    trang moi truoc khi bat dau). Tra ve (so_thanh_cong, so_loi, danh_sach_loi)."""
    env = load_env(ENV_PATH)
    token = env.get("NOTION_TOKEN") or os.environ.get("NOTION_TOKEN")
    if not token:
        raise RuntimeError(
            "Không tìm thấy NOTION_TOKEN trong .env (cần cùng token đã dùng cho glossary)."
        )
    headers = get_headers(token)

    manifest = load_manifest()

    # Buoc 1: tu dong phat hien trang moi duoi 4 hub, neu co thi luu lai
    # manifest va them dong vao nav ngay (truoc khi dong bo noi dung).
    if verbose:
        print("Đang quét các hub để tìm trang mới...")
    new_entries = discover_new_pages(manifest, headers, verbose=verbose)
    if new_entries:
        clean_entries = [{"id": e["id"], "output": e["output"]} for e in new_entries]
        manifest.setdefault("pages", []).extend(clean_entries)
        save_manifest(manifest)
        appended = append_nav_entries(MKDOCS_YML_PATH, new_entries)
        if verbose:
            print(f"Đã tự thêm {len(new_entries)} trang mới vào pages_manifest.json"
                  + (f" và vào menu (mkdocs.yml) cho mục: {', '.join(appended)}" if appended else ""))
    elif verbose:
        print("Không có trang mới nào dưới 4 hub.")

    link_map = build_link_map(manifest)
    paper_map = build_paper_map()
    ctx = Context(link_map=link_map, paper_map=paper_map)

    cache = {} if force else load_cache(CACHE_PATH)
    new_cache = dict(cache)

    ok, skipped, errors = 0, 0, []

    for entry in manifest.get("pages", []):
        out_rel = entry["output"]
        out_abs = os.path.join(PROJECT_ROOT, out_rel)
        sources = entry.get("sources") or [entry.get("id")]
        cache_key = "|".join(normalize_id(s) for s in sources)

        try:
            metas = [get_page_meta(s, headers) for s in sources]
            edit_signature = "|".join(m["last_edited_time"] or "" for m in metas)

            if (not force) and os.path.exists(out_abs) and cache.get(cache_key) == edit_signature:
                skipped += 1
                if verbose:
                    print(f"  BỎ QUA (không đổi) {out_rel}")
                new_cache[cache_key] = edit_signature
                continue

            if len(sources) == 1:
                body = render_page_content(sources[0], headers, ctx, out_rel)
                content = f"# {metas[0]['title']}\n\n{body}"
            else:
                parts = []
                for i, src_id in enumerate(sources):
                    body = render_page_content(src_id, headers, ctx, out_rel)
                    heading = "#" if i == 0 else "##"
                    parts.append(f"{heading} {metas[i]['title']}\n\n{body}")
                content = "\n\n---\n\n".join(parts)

            os.makedirs(os.path.dirname(out_abs), exist_ok=True)
            with open(out_abs, "w", encoding="utf-8") as f:
                f.write(content)

            new_cache[cache_key] = edit_signature
            ok += 1
            if verbose:
                print(f"  OK  {out_rel}")
        except Exception as e:  # noqa: BLE001 - bat moi loi de tiep tuc dong bo cac trang khac
            errors.append((out_rel, str(e)))
            if verbose:
                print(f"  LỖI {out_rel}: {e}")

    save_cache(CACHE_PATH, new_cache)

    if verbose:
        print(
            f"\nHoàn tất đồng bộ trang: {ok} cập nhật, {skipped} bỏ qua (không đổi), "
            f"{len(errors)} lỗi."
        )
        if errors:
            print("Các trang gặp lỗi (nội dung cũ trên máy KHÔNG bị mất, script chỉ bỏ qua):")
            for out_rel, msg in errors:
                print(f"  - {out_rel}: {msg}")

    return ok, len(errors), errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force", action="store_true",
        help="Bỏ qua cache, đồng bộ lại TẤT CẢ các trang dù không đổi."
    )
    args = parser.parse_args()
    sync_all_pages(force=args.force)
