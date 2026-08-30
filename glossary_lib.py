"""
Shared logic to turn glossary rows (in the raw_data.json schema) into
glossary.json, glossary.csv and README.md.

Used by both:
- build_glossary.py   (reads raw_data.json, for manual/offline rebuilds)
- sync_and_push.py    (fetches fresh rows from the Notion API, then calls this)

Save location: C:\\NCKH\\glossary-en-vi\\glossary_lib.py
"""
import json
import csv
from collections import defaultdict

TOPIC_ORDER = [
    "Toán", "ML cơ bản", "Deep Learning", "CNN", "Autoencoder",
    "Transformer/CLIP", "XAI", "CBM", "Khác",
]


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
    """Writes glossary.json, glossary.csv and README.md into out_dir."""
    import os

    # --- glossary.json ---
    with open(os.path.join(out_dir, "glossary.json"), "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    # --- glossary.csv ---
    with open(os.path.join(out_dir, "glossary.csv"), "w", encoding="utf-8", newline="") as f:
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

    all_topics = TOPIC_ORDER + [t for t in sorted(by_topic) if t not in TOPIC_ORDER]

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
            anchor = t.lower().replace(" ", "-").replace("/", "")
            lines.append(f"- [{t}](#{anchor})")
    lines.append("")

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

    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
