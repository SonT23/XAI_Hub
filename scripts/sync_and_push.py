#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tự động: (1) lấy toàn bộ dữ liệu từ database Notion "Thuật ngữ Anh - Việt",
(2) build lại data/raw_data.json, data/glossary.json, data/glossary.csv, và
các trang docs/glossary/*.md, (3) git add + commit (message = thời gian
chạy) + git push.

Vị trí lưu: C:\\NCKH\\nckh-wiki\\scripts\\sync_and_push.py
Chạy từ thư mục gốc project qua update_and_push.bat (khuyên dùng), hoặc
thủ công: python scripts\\sync_and_push.py

Yêu cầu trước khi chạy:
  1. Cài thư viện: pip install -r requirements.txt
  2. Tạo file .env (copy từ .env.example) TẠI THƯ MỤC GỐC project (cùng cấp
     với mkdocs.yml, KHÔNG phải trong scripts/), điền:
       NOTION_TOKEN=secret_xxx...
       NOTION_DATABASE_ID=4a41d94b-9d22-436a-9786-9a650f57bf2d
     (Xem MAINTENANCE.md để biết cách lấy 2 giá trị này.)
  3. Repo git đã init, remote đã cấu hình, và bạn đã push thành công ít
     nhất 1 lần thủ công (để chắc chắn SSH/HTTPS auth đã hoạt động).
"""
import json
import os
import subprocess
import sys
from datetime import datetime

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from glossary_lib import normalize_rows, write_outputs, write_mkdocs_docs

ENV_PATH = os.path.join(PROJECT_ROOT, ".env")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

def load_env(path):
    """Đọc file .env đơn giản (KEY=VALUE mỗi dòng), không cần cài python-dotenv."""
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


def get_plain_text(rich_text_list):
    return "".join(rt.get("plain_text", "") for rt in (rich_text_list or []))


def get_prop_title(props, name):
    prop = props.get(name) or {}
    return get_plain_text(prop.get("title"))


def get_prop_rich_text(props, name):
    prop = props.get(name) or {}
    return get_plain_text(prop.get("rich_text"))


def get_prop_multi_select(props, name):
    prop = props.get(name) or {}
    return [o.get("name", "") for o in (prop.get("multi_select") or [])]


def fetch_all_rows(token, database_id):
    """Query toàn bộ database Notion (có phân trang) qua REST API chính thức."""
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    rows = []
    payload = {"page_size": 100}
    while True:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code != 200:
            raise RuntimeError(
                f"Notion API trả lỗi {resp.status_code}: {resp.text}\n"
                "Kiểm tra lại NOTION_TOKEN và NOTION_DATABASE_ID trong file .env, "
                "và đảm bảo integration đã được share vào database (xem MAINTENANCE.md)."
            )
        data = resp.json()
        for page in data.get("results", []):
            props = page.get("properties", {})
            rows.append({
                "Thuật ngữ (EN)": get_prop_title(props, "Thuật ngữ (EN)"),
                "Tiếng Việt": get_prop_rich_text(props, "Tiếng Việt"),
                "Viết tắt": get_prop_rich_text(props, "Viết tắt"),
                "Định nghĩa ngắn": get_prop_rich_text(props, "Định nghĩa ngắn"),
                "Chủ đề": get_prop_multi_select(props, "Chủ đề"),
                "Dễ nhầm với": get_prop_rich_text(props, "Dễ nhầm với"),
            })
        if data.get("has_more"):
            payload["start_cursor"] = data.get("next_cursor")
        else:
            break
    return rows


def run_git(args, cwd):
    result = subprocess.run(
        ["git"] + args, cwd=cwd, capture_output=True, text=True, encoding="utf-8"
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def git_commit_and_push(repo_dir):
    code, out, err = run_git(["status", "--porcelain"], repo_dir)
    if code != 0:
        print(f"[LỖI] git status thất bại: {err}")
        return False
    if not out.strip():
        print("Không có thay đổi nào so với lần trước — không cần commit/push.")
        return True

    code, out, err = run_git(["add", "."], repo_dir)
    if code != 0:
        print(f"[LỖI] git add thất bại: {err}")
        return False

    commit_message = f"Auto update from Notion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    code, out, err = run_git(["commit", "-m", commit_message], repo_dir)
    if code != 0:
        print(f"[LỖI] git commit thất bại: {err}")
        return False
    print(f"Đã commit: \"{commit_message}\"")

    code, out, err = run_git(["push"], repo_dir)
    if code != 0:
        print(f"[LỖI] git push thất bại:\n{err}")
        print("Bạn có thể cần push thủ công 1 lần để xác thực (SSH key / token), rồi chạy lại script.")
        return False
    print("Đã push lên GitHub thành công.")
    return True


def main():
    env = load_env(ENV_PATH)
    token = env.get("NOTION_TOKEN") or os.environ.get("NOTION_TOKEN")
    database_id = env.get("NOTION_DATABASE_ID") or os.environ.get("NOTION_DATABASE_ID")

    if not token or not database_id:
        print(
            "[LỖI] Thiếu NOTION_TOKEN hoặc NOTION_DATABASE_ID.\n"
            f"Tạo file .env tại: {ENV_PATH}\n"
            "Xem hướng dẫn chi tiết trong MAINTENANCE.md."
        )
        sys.exit(1)

    print("Đang lấy dữ liệu mới nhất từ Notion...")
    rows = fetch_all_rows(token, database_id)
    print(f"Lấy được {len(rows)} thuật ngữ.")

    os.makedirs(DATA_DIR, exist_ok=True)
    # Cập nhật raw_data.json để giữ bản ghi lịch sử đồng bộ với glossary.json/csv
    with open(os.path.join(DATA_DIR, "raw_data.json"), "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    entries = normalize_rows(rows)
    write_outputs(entries, out_dir=DATA_DIR)
    write_mkdocs_docs(entries, docs_dir=DOCS_DIR)
    print(f"Đã tạo lại data/glossary.json, data/glossary.csv, và các trang docs/glossary/ ({len(entries)} thuật ngữ).")

    git_commit_and_push(PROJECT_ROOT)


if __name__ == "__main__":
    main()
