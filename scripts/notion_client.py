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
    return get_page_meta(page_id, headers)["title"]


def get_page_meta(page_id, headers):
    """Lay tieu de VA thoi diem sua doi cuoi cung (last_edited_time) cua 1 page,
    chi bang 1 lan goi GET /pages/{id} (khong can tai toan bo block).
    Dung last_edited_time de quyet dinh co can dong bo lai trang nay khong
    (giong co che 'da thay doi chua' cua git), tranh phai tai + render lai
    toan bo cay block cho nhung trang khong he doi gi ca."""
    resp = requests.get(f"{API_BASE}/pages/{page_id}", headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    props = data.get("properties", {})
    title = "(không có tiêu đề)"
    for prop in props.values():
        if prop.get("type") == "title":
            title = "".join(rt.get("plain_text", "") for rt in prop.get("title", []))
            break
    return {"title": title, "last_edited_time": data.get("last_edited_time")}


def list_child_page_blocks(block_id, headers):
    """Lay danh sach cac block con truc tiep co type == 'child_page' (khong de quy
    sau hon). Tra ve list {"id":..., "title":...} - tieu de lay truc tiep tu block
    (khong can goi them API rieng)."""
    children = get_block_children_all(block_id, headers)
    result = []
    for b in children:
        if b.get("type") == "child_page":
            title = b.get("child_page", {}).get("title", "(không có tiêu đề)")
            result.append({"id": b["id"], "title": title})
    return result
