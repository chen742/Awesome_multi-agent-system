#!/usr/bin/env python3
"""Validate data/papers.yaml: schema, known categories, and duplicates."""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("title", "category")
ALLOWED = {"title", "authors", "venue", "year", "arxiv", "url", "code", "project",
           "category", "highlight", "tldr"}


def main():
    cats = yaml.safe_load((ROOT / "data" / "categories.yaml").read_text(encoding="utf-8"))
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8")) or []
    valid_cats = {s["id"] for c in cats for s in c.get("subcategories", [])}

    errors, seen_arxiv, seen_title = [], {}, {}
    for i, p in enumerate(papers):
        where = f"entry #{i + 1} ({p.get('title', '?')[:60]})"
        for k in REQUIRED:
            if not p.get(k):
                errors.append(f"{where}: missing '{k}'")
        for k in p:
            if k not in ALLOWED:
                errors.append(f"{where}: unknown field '{k}'")
        if p.get("category") and p["category"] not in valid_cats:
            errors.append(f"{where}: unknown category '{p['category']}'")
        aid = str(p.get("arxiv") or "")
        if aid and not re.match(r"^\d{4}\.\d{4,5}$", aid):
            errors.append(f"{where}: arxiv must look like 2401.12345, got '{aid}'")
        if not aid and not p.get("url"):
            errors.append(f"{where}: needs 'arxiv' or 'url'")
        if aid:
            if aid in seen_arxiv:
                errors.append(f"{where}: duplicate arXiv {aid} (also #{seen_arxiv[aid]})")
            seen_arxiv[aid] = i + 1
        key = re.sub(r"\W", "", str(p.get("title", "")).lower())
        if key in seen_title:
            errors.append(f"{where}: duplicate title (also #{seen_title[key]})")
        seen_title[key] = i + 1

    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {len(papers)} papers across {len(valid_cats)} categories.")


if __name__ == "__main__":
    main()
