#!/usr/bin/env python3
"""
Build glossary.json, glossary.csv, and README.md from raw_data.json
(a manually exported snapshot of the Notion database).

For a fully automatic version that pulls straight from Notion and pushes to
git, use sync_and_push.py instead.

Save location: C:\\NCKH\\glossary-en-vi\\build_glossary.py
"""
import json
from glossary_lib import normalize_rows, write_outputs, write_mkdocs_docs

with open("raw_data.json", encoding="utf-8") as f:
    rows = json.load(f)

entries = normalize_rows(rows)
write_outputs(entries, out_dir=".")
topics = write_mkdocs_docs(entries, docs_dir="docs")

print(f"Done. {len(entries)} terms written to glossary.json, glossary.csv, README.md")
print(f"MkDocs pages written to docs/ for topics: {', '.join(topics)}")
