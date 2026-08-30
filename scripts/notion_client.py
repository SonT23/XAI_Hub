"""
Cac ham goi thang Notion REST API (khong dung SDK, chi can `requests`).

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\notion_client.py
"""
import os
import requests

NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"


def load_env(path):
    """Doc file .env don gian (KEY=VALUE moi dong)."""
    env = {}
    if not os.path.exists(path):
        return env
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def normalize_id(page_id):
    """Bo dau gach ngang de so sanh ID nhat quan (Notion chap nhan ca 2 dang)."""
    return (page_id or "").replace("-", "").lower()


def get_block_children_all(block_id, headers):
    """Lay TOAN BO children cua 1 block/page (co phan trang)."""
    results = []
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        resp = requests.get(
            f"{API_BASE}/blocks/{block_id}/children",
            headers=headers, params=params, timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        results.extend(data.get("results", []))
        if data.get("has_more"):
            cursor = data.get("next_cursor")
        else:
            break
    return results


def fetch_block_tree(block_id, headers, _depth=0, _max_depth=8):
    """Lay children de quy (bao gom ca bang, callout long nhau, columns...).
    KHONG de quy vao child_page / child_database — do la trang rieng, phai
    duoc dong bo nhu 1 entry rieng trong manifest, khong duoc gop noi dung
    vao trang cha mot cach am tham.
    """
    if _depth > _max_depth:
        return []
    children = get_block_children_all(block_id, headers)
    for b in children:
        btype = b.get("type")
        if b.get("has_children") and btype not in ("child_page", "child_database"):
            b["_children"] = fetch_block_tree(b["id"], headers, _depth + 1, _max_depth)
        else:
            b["_children"] = []
    return children


def get_page_title(page_id, headers):
    """Lay tieu de mot page qua endpoint /pages/{id} (doc property kieu 'title')."""
    resp = requests.get(f"{API_BASE}/pages/{page_id}", headers=headers, timeout=30)
    resp.raise_for_status()
    props = resp.json().get("properties", {})
    for prop in props.values():
        if prop.get("type") == "title":
            return "".join(rt.get("plain_text", "") for rt in prop.get("title", []))
    return "(không có tiêu đề)"
