"""
Cac ham tien ich dung chung: chuyen tieu de tieng Viet thanh slug (ten file
khong dau, khong khoang trang), va doc/ghi cache "lan sua doi cuoi cung" cua
tung trang Notion (dung de bo qua trang khong doi, giong co che cua git).

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\util.py
"""
import json
import os
import re
import unicodedata


def slugify(title):
    """Chuyen tieu de tieng Viet (co the co emoji, so thu tu...) thanh slug
    an toan de lam ten file, vi du 'Machine Learning cơ bản' -> 'machine-learning-co-ban'."""
    s = (title or "").strip()
    s = s.replace("Đ", "D").replace("đ", "d")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "trang-khong-ten"


def load_cache(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_cache(path, cache):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
