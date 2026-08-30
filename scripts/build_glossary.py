#!/usr/bin/env python3
"""
Build glossary.json, glossary.csv (vao thu muc data/), va cac trang
docs/glossary/*.md tu data/raw_data.json (ban export thu cong tu Notion).

De tu dong lay du lieu thang tu Notion API roi push len git, dung
sync_and_push.py thay vi file nay.

Vi tri: C:\\NCKH\\nckh-wiki\\scripts\\build_glossary.py
Chay tu thu muc goc project: python scripts\\build_glossary.py
"""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from glossary_lib import normalize_rows, write_outputs, write_mkdocs_docs

RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw_data.json")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

with open(RAW_DATA_PATH, encoding="utf-8") as f:
    rows = json.load(f)

entries = normalize_rows(rows)
write_outputs(entries, out_dir=DATA_DIR)
topics = write_mkdocs_docs(entries, docs_dir=DOCS_DIR)

print(f"Done. {len(entries)} terms written to data/glossary.json, data/glossary.csv")
print(f"MkDocs pages written to docs/glossary/ for topics: {', '.join(topics)}")
