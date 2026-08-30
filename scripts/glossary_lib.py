"""
Shared logic to turn glossary rows (from Notion) into glossary.json,
glossary.csv, and the MkDocs pages under docs/glossary/.

Used by both:
- build_glossary.py   (reads data/raw_data.json, for manual/offline rebuilds)
- sync_and_push.py    (fetches fresh rows from the Notion API, then calls this)

Save location: C:\\NCKH\\nckh-wiki\\scripts\\glossary_lib.py
"""
import json
import csv
from collections import defaultdict

TOPIC_ORDER = [
    "Toán", "ML cơ bản", "Deep Learning", "CNN", "Autoencoder",
    "Transformer/CLIP", "XAI", "CBM", "Khác",
]

# Slug dùng cho tên file .md của từng chủ đề trong trang MkDocs
TOPIC_SLUGS = {
    "Toán": "toan",
    "ML cơ bản": "ml-co-ban",
    "Deep Learning": "deep-learning",
    "CNN": "cnn",
    "Autoencoder": "autoencoder",
    "Transformer/CLIP": "transformer-clip",
    "XAI": "xai",
    "CBM": "cbm",
    "Khác": "khac",
}


def _topic_slug(topic):
    return TOPIC_SLUGS.get(topic, topic.lower().replace(" ", "-").replace("/", "-"))


def _group_by_topic(entries):
    by_topic = defaultdict(list)
    for e in entries:
        if e["topics"]:
            for t in e["topics"]:
                by_topic[t].append(e)
        else:
            by_topic["Khác"].append(e)
    all_topics = TOPIC_ORDER + [t for t in sorted(by_topic) if t not in TOPIC_ORDER]
    return by_topic, all_topics


def _esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def _table_rows(items):
    lines = ["| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |",
             "|---|---|---|---|---|"]
    for e in sorted(items, key=lambda x: x["term_en"].lower()):
        lines.append(
            f"| {_esc(e['term_en'])} | {_esc(e['term_vi'])} | {_esc(e['abbr'])} | "
            f"{_esc(e['definition'])} | {_esc(e['confused_with'])} |"
        )
    return lines


def normalize_rows(rows):
    """rows: list of dicts with keys matching the Notion column names
    (Thuật ngữ (EN), Tiếng Việt, Viết tắt, Định nghĩa ngắn, Chủ đề, Dễ nhầm với).
    'Chủ đề' may be a JSON-encoded string of a list, or an actual list.
    Returns a normalized, sorted list of entry dicts.
    """
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
    return entries


def write_outputs(entries, out_dir="."):
    """Writes glossary.json and glossary.csv (machine-readable exports) into out_dir.
    The human-facing output is the MkDocs site (write_mkdocs_docs), not these files."""
    import os

    with open(os.path.join(out_dir, "glossary.json"), "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    with open(os.path.join(out_dir, "glossary.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["term_en", "term_vi", "abbr", "definition", "topics", "confused_with"])
        for e in entries:
            writer.writerow([
                e["term_en"], e["term_vi"], e["abbr"], e["definition"],
                "; ".join(e["topics"]), e["confused_with"],
            ])


def write_mkdocs_docs(entries, docs_dir):
    """Sinh các trang Markdown cho phần Glossary trong MkDocs (1 trang mỗi
    chủ đề + 1 trang liệt kê toàn bộ) vào docs_dir/glossary/. KHÔNG đụng tới
    docs/index.md (trang chủ toàn site) — trang đó là nội dung tổng của cả
    NCKH, không riêng glossary, và được quản lý riêng.
    """
    import os

    os.makedirs(os.path.join(docs_dir, "glossary"), exist_ok=True)
    by_topic, all_topics = _group_by_topic(entries)
    present_topics = [t for t in all_topics if t in by_topic]

    # --- docs/glossary/<topic>.md, mỗi trang 1 chủ đề ---
    for t in present_topics:
        lines = [f"# {t}", ""]
        lines.extend(_table_rows(by_topic[t]))
        lines.append("")
        with open(os.path.join(docs_dir, "glossary", f"{_topic_slug(t)}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # --- docs/glossary/all.md, toàn bộ thuật ngữ A-Z (không chia chủ đề) ---
    all_lines = ["# Toàn bộ thuật ngữ (A-Z)", ""]
    all_lines.extend(_table_rows(entries))
    all_lines.append("")
    with open(os.path.join(docs_dir, "glossary", "all.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(all_lines))

    return present_topics
