#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tu dong phat hien trang con MOI duoc tao trong Notion, duoi 1 trong 4 trang
"hub" (Toan nen tang, ML co ban, Deep Learning, Explainable AI), va TU DONG
them vao pages_manifest.json + muc luc (nav) trong mkdocs.yml.

Muc dich: xoa bo buoc thu cong "copy ID tu URL" khi ban tao trang kien thuc
moi - chi can trang do nam ben trong (la trang con truc tiep cua) 1 trong 4
hub co san, script se tu tim thay khi chay dong bo.

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\discover_pages.py

GIOI HAN: chi phat hien trang con o dung 1 CAP (truc tiep duoi hub), khong
de quy sau hon - vi du neu ban tao 1 trang con nam trong 1 trang con khac
(long 2 cap), script se KHONG tu thay. Truong hop do van can them tay vao
pages_manifest.json nhu truoc (xem GHI_CHU_VAN_HANH trong Notion, muc 3).
"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from notion_client import list_child_page_blocks, normalize_id
from util import slugify

MKDOCS_YML_PATH = os.path.join(PROJECT_ROOT, "mkdocs.yml")


def _known_ids(manifest):
    known = set()
    for entry in manifest.get("pages", []):
        if "sources" in entry:
            known.update(normalize_id(s) for s in entry["sources"])
        elif "id" in entry:
            known.add(normalize_id(entry["id"]))
    return known


def discover_new_pages(manifest, headers, verbose=True):
    """Quet 4 hub trong manifest['auto_discover_hubs'], tra ve list cac entry
    MOI (dang giong format trong manifest['pages']: {"id":..., "output":...}),
    kem theo "_nav_section" va "_nav_label" de biet chen vao dau trong mkdocs.yml.
    KHONG tu ghi file - ham goi (sync_pages.py) chiu trach nhiem luu manifest
    va cap nhat mkdocs.yml sau khi nhan ket qua nay."""
    known = _known_ids(manifest)
    new_entries = []

    for hub in manifest.get("auto_discover_hubs", []):
        skip_ids = set(normalize_id(s) for s in hub.get("skip_ids", []))
        try:
            children = list_child_page_blocks(hub["hub_id"], headers)
        except Exception as e:  # noqa: BLE001
            if verbose:
                print(f"  [CẢNH BÁO] Không quét được hub '{hub.get('nav_section')}': {e}")
            continue

        for child in children:
            cid = normalize_id(child["id"])
            if cid in known or cid in skip_ids:
                continue
            slug = slugify(child["title"])
            output = f'{hub["folder"]}/{slug}.md'
            entry = {"id": child["id"], "output": output}
            new_entries.append({
                **entry,
                "_nav_section": hub["nav_section"],
                "_nav_label": child["title"],
            })
            known.add(cid)
            if verbose:
                print(f"  🆕 Phát hiện trang mới: \"{child['title']}\" → {output}")

    return new_entries


def append_nav_entries(mkdocs_path, entries):
    """Chen them dong nav moi vao dung muc (nav_section) trong mkdocs.yml,
    ngay sau muc con cuoi cung cua muc do - KHONG dong lai/format lai toan bo
    file, chi chen them dong, de khong lam hong comment/format san co."""
    if not entries:
        return []

    with open(mkdocs_path, encoding="utf-8") as f:
        lines = f.readlines()

    appended_for = []

    # gom theo section de chen 1 lan cho moi section (tranh lech chi so khi
    # chen nhieu dong lien tiep cho cung 1 section)
    by_section = {}
    for e in entries:
        by_section.setdefault(e["_nav_section"], []).append(e)

    for section, section_entries in by_section.items():
        # tim dong "  - <section>:"
        start_idx = None
        for i, line in enumerate(lines):
            if line.rstrip("\n") == f"  - {section}:":
                start_idx = i
                break
        if start_idx is None:
            print(f"  [CẢNH BÁO] Không tìm thấy mục \"{section}\" trong mkdocs.yml nav — "
                  f"cần tự thêm các trang sau vào menu thủ công: "
                  + ", ".join(e["_nav_label"] for e in section_entries))
            continue

        # tim dong cuoi cung con thuoc section nay (thut le sau hon dong start_idx)
        base_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip(" "))
        end_idx = start_idx + 1
        while end_idx < len(lines):
            line = lines[end_idx]
            if line.strip() == "":
                end_idx += 1
                continue
            indent = len(line) - len(line.lstrip(" "))
            if indent <= base_indent:
                break
            end_idx += 1

        child_indent_str = " " * (base_indent + 6) if lines[start_idx + 1:end_idx] else " " * (base_indent + 4)
        # doan nay lay theo dinh dang co san trong file (6 dau cach cho muc con,
        # dua tren cach mkdocs.yml hien tai dang dung); neu file rong thi mac dinh 4.
        if start_idx + 1 < end_idx:
            sample = lines[start_idx + 1]
            child_indent_str = " " * (len(sample) - len(sample.lstrip(" ")))

        new_lines = [f'{child_indent_str}- {e["_nav_label"]}: {e["output"][len("docs/"):]}\n' for e in section_entries]
        lines[end_idx:end_idx] = new_lines
        appended_for.append(section)

        # dieu chinh index cac section khac neu can (xu ly tuan tu tung section
        # roi ghi lai lines moi cho vong lap sau bang cach doc lai tu dau)

    with open(mkdocs_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    return appended_for
