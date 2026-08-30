#!/usr/bin/env python3
"""
Build glossary.json, glossary.csv, and README.md from the raw Notion export.
Source of truth: raw_data.json (exported manually from the Notion database
"Thuật ngữ Anh - Việt"). Re-run this script after refreshing raw_data.json.

Save location: /home/claude/glossary-en-vi/ (cloud workspace)
"""
import json
import csv
from collections import defaultdict

with open("raw_data.json", encoding="utf-8") as f:
    rows = json.load(f)

# Normalize: parse "Chủ đề" from JSON-string-of-list to a real list
entries = []
for r in rows:
    topics = r.get("Chủ đề")
    if isinstance(topics, str):
        try:
            topics = json.loads(topics)
        except Exception:
            topics = [topics] if topics else []
    elif topics is None:
        topics = []
    entries.append({
        "term_en": r.get("Thuật ngữ (EN)") or "",
        "term_vi": r.get("Tiếng Việt") or "",
        "abbr": r.get("Viết tắt") or "",
        "definition": r.get("Định nghĩa ngắn") or "",
        "topics": topics,
        "confused_with": r.get("Dễ nhầm với") or "",
    })

entries.sort(key=lambda e: e["term_en"].lower())

# --- glossary.json ---
with open("glossary.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

# --- glossary.csv ---
with open("glossary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["term_en", "term_vi", "abbr", "definition", "topics", "confused_with"])
    for e in entries:
        writer.writerow([
            e["term_en"], e["term_vi"], e["abbr"], e["definition"],
            "; ".join(e["topics"]), e["confused_with"],
        ])

# --- README.md, grouped by topic, sorted A-Z within each topic ---
by_topic = defaultdict(list)
for e in entries:
    if e["topics"]:
        for t in e["topics"]:
            by_topic[t].append(e)
    else:
        by_topic["Khác"].append(e)

topic_order = [
    "Toán", "ML cơ bản", "Deep Learning", "CNN", "Autoencoder",
    "Transformer/CLIP", "XAI", "CBM", "Khác",
]
# include any topics not in the predefined order at the end
all_topics = topic_order + [t for t in sorted(by_topic) if t not in topic_order]

lines = []
lines.append("# Bilingual Glossary: Explainable AI & Computer Vision (EN-VI)")
lines.append("")
lines.append(
    "A bilingual (English-Vietnamese) glossary of terms used in machine "
    "learning, computer vision, and Explainable AI (XAI), with a focus on "
    "Concept Bottleneck Models (CBM). Source of truth is a Notion database; "
    "this repo is a periodically refreshed export for public reference."
)
lines.append("")
lines.append(f"**Total terms:** {len(entries)}")
lines.append("")
lines.append("## Table of contents")
lines.append("")
for t in all_topics:
    if t in by_topic:
        anchor = t.lower().replace(" ", "-").replace("/", "").replace("ơ", "o").replace("ả", "a")
        lines.append(f"- [{t}](#{anchor})")
lines.append("")

def slugify(t):
    return t.lower().replace(" ", "-").replace("/", "")

for t in all_topics:
    if t not in by_topic:
        continue
    lines.append(f"## {t}")
    lines.append("")
    lines.append("| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |")
    lines.append("|---|---|---|---|---|")
    for e in sorted(by_topic[t], key=lambda x: x["term_en"].lower()):
        def esc(s):
            return (s or "").replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {esc(e['term_en'])} | {esc(e['term_vi'])} | {esc(e['abbr'])} | "
            f"{esc(e['definition'])} | {esc(e['confused_with'])} |"
        )
    lines.append("")

lines.append("---")
lines.append("")
lines.append(
    "Source of truth: a Notion database maintained during NCKH research on "
    "Explainable AI for Computer Vision. Data files (`glossary.json`, "
    "`glossary.csv`) are machine-readable exports kept in sync with this README."
)
lines.append("")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Done. {len(entries)} terms written to glossary.json, glossary.csv, README.md")
