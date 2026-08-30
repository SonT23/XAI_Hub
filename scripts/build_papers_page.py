#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build docs/papers/index.md tu du lieu tho cua database "Thu vien bai bao".
Chu y: KHONG dua truong "Trang thai" (tien do doc ca nhan) len trang cong khai.
Loai bo dong "MAU GHI CHU DOC BAI" (template, khong phai bai bao that).

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\build_papers_page.py
Chay tu thu muc goc project: python scripts\\build_papers_page.py

LUU Y: chua co script tu dong lay du lieu bang nay tu Notion API (khac voi
glossary). Hien tai vi cach cap nhat la: nho Claude query lai database "Thu
vien bai bao" tren Notion, ghi de data/papers_raw.json, roi chay lai file
nay. Xem MAINTENANCE.md.
"""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
RAW_PATH = os.path.join(PROJECT_ROOT, "data", "papers_raw.json")
OUT_PATH = os.path.join(PROJECT_ROOT, "docs", "papers", "index.md")

from collections import defaultdict

with open(RAW_PATH, encoding="utf-8") as f:
    rows = json.load(f)

papers = []
for r in rows:
    title = (r.get("Tên bài báo") or "").strip()
    if not title or title.startswith("MẪU GHI CHÚ"):
        continue
    topics = r.get("Chủ đề")
    if isinstance(topics, str):
        try:
            topics = json.loads(topics)
        except Exception:
            topics = [topics] if topics else []
    elif topics is None:
        topics = []
    papers.append({
        "title": title,
        "authors": r.get("Tác giả & Năm") or "",
        "link": r.get("Link") or "",
        "topics": topics,
    })

papers.sort(key=lambda p: p["title"].lower())

by_topic = defaultdict(list)
for p in papers:
    if p["topics"]:
        for t in p["topics"]:
            by_topic[t].append(p)
    else:
        by_topic["Khác"].append(p)

TOPIC_ORDER = [
    "CBM", "Concept-based", "Post-hoc", "XAI tổng quan", "Đánh giá XAI",
    "Autoencoder/VAE", "CNN", "Transformer/ViT", "Dataset", "Khác",
]
all_topics = TOPIC_ORDER + [t for t in sorted(by_topic) if t not in TOPIC_ORDER]

lines = []
lines.append("# Thư viện bài báo")
lines.append("")
lines.append(
    "Danh mục các bài báo khoa học đã/đang đọc trong quá trình nghiên cứu, "
    "dùng khi viết phần Related Work. Nguồn dữ liệu gốc là một database Notion "
    "(chỉ hiển thị thông tin thư mục — tên bài, tác giả, chủ đề, liên kết — "
    "không bao gồm ghi chú đọc cá nhân)."
)
lines.append("")
lines.append(f"**Tổng số bài báo:** {len(papers)}")
lines.append("")
lines.append("## Theo chủ đề")
lines.append("")
lines.append(
    "(dùng mục lục bên phải để nhảy nhanh tới từng chủ đề)"
)
lines.append("")
for t in all_topics:
    if t in by_topic:
        lines.append(f"- **{t}** ({len(by_topic[t])} bài)")
lines.append("")

for t in all_topics:
    if t not in by_topic:
        continue
    lines.append(f"## {t}")
    lines.append("")
    lines.append("| Bài báo | Tác giả & Năm |")
    lines.append("|---|---|")
    for p in sorted(by_topic[t], key=lambda x: x["title"].lower()):
        title_cell = f"[{p['title']}]({p['link']})" if p["link"] else p["title"]
        lines.append(f"| {title_cell} | {p['authors']} |")
    lines.append("")

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Done. {len(papers)} papers written to {OUT_PATH}")
