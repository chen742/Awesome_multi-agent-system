#!/usr/bin/env python3
"""Generate README.md and README_zh.md from data/categories.yaml + data/papers.yaml.

Usage:
    python scripts/build_readme.py          # write README.md
    python scripts/build_readme.py --check  # exit 1 if README.md is stale
"""
import datetime
import re
import sys
from collections import OrderedDict
from pathlib import Path

import yaml
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
# (template, output) pairs sharing the same generated paper list.
TARGETS = [
    (ROOT / "assets" / "README.template.md", ROOT / "README.md"),
    (ROOT / "assets" / "README_zh.template.md", ROOT / "README_zh.md"),
]

BEGIN = "<!-- BEGIN GENERATED -->"
END = "<!-- END GENERATED -->"


def load():
    cats = yaml.safe_load((DATA / "categories.yaml").read_text(encoding="utf-8"))
    papers = yaml.safe_load((DATA / "papers.yaml").read_text(encoding="utf-8")) or []
    return cats, papers


def anchor(title):
    """GitHub-style heading anchor."""
    a = title.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def arxiv_id(p):
    return str(p.get("arxiv") or "").strip()


def sort_key(p):
    # Newest first: arXiv IDs (YYMM.NNNNN) sort chronologically; fall back to year.
    aid = arxiv_id(p)
    if re.match(r"^\d{4}\.\d{4,5}$", aid):
        yymm, num = aid.split(".")
        return (int(yymm), int(num))
    return (int(str(p.get("year", 2000))[2:]) * 100 + 12, 0)


def date_tag(p):
    aid = arxiv_id(p)
    if re.match(r"^\d{4}\.\d{4,5}$", aid):
        return f"20{aid[:2]}/{aid[2:4]}"
    return str(p.get("year", ""))


def venue_badge(venue):
    if not venue:
        return ""
    label = quote(venue.replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")
    color = "lightgrey" if venue.lower().startswith("arxiv") else "blue"
    return f"![{venue}](https://img.shields.io/badge/{label}-{color})"


def star_badge(code):
    m = re.match(r"https://github\.com/([^/\s]+)/([^/\s#?]+)", code or "")
    if not m:
        return ""
    repo = f"{m.group(1)}/{m.group(2).removesuffix('.git')}"
    return f"![Stars](https://img.shields.io/github/stars/{repo}?style=social)"


def render_entry(p):
    url = p.get("url") or (f"https://arxiv.org/abs/{arxiv_id(p)}" if arxiv_id(p) else "")
    star = " :star:" if p.get("highlight") else ""
    title = p["title"].strip()
    sep = "" if title[-1] in ".?!" else "."
    line = f"- `[{date_tag(p)}]` **{title}**{sep}{star}"
    if p.get("authors"):
        authors = p["authors"].strip()
        line += f" *{authors}*" + ("" if authors.endswith(".") else ".")
    badge = venue_badge(p.get("venue"))
    if badge:
        line += f" {badge}"
    links = []
    if url:
        links.append(f"[[Paper]({url})]")
    if p.get("code"):
        links.append(f"[[Code]({p['code']})]")
    if p.get("project"):
        links.append(f"[[Project]({p['project']})]")
    if links:
        line += " " + " ".join(links)
    sb = star_badge(p.get("code"))
    if sb:
        line += " " + sb
    if p.get("tldr"):
        line += f"\n  <br>💡 {p['tldr']}"
    return line


def build(cats, papers):
    by_cat = OrderedDict()
    for p in papers:
        by_cat.setdefault(p["category"], []).append(p)

    toc, body = [], []
    for sec in cats:
        sec_title = sec["title"]
        toc.append(f"- [{sec_title}](#{anchor(sec_title)})")
        body.append(f"## {sec_title}\n")
        if sec.get("description"):
            body.append(f"> {sec['description']}\n")
        for sub in sec.get("subcategories", []):
            items = sorted(by_cat.get(sub["id"], []), key=sort_key, reverse=True)
            toc.append(f"  - [{sub['title']}](#{anchor(sub['title'])})")
            body.append(f"### {sub['title']}\n")
            if sub.get("description"):
                body.append(f"{sub['description']}\n")
            body.append("\n".join(render_entry(p) for p in items) if items else "*Coming soon — PRs welcome!*")
            body.append("\n<p align=\"right\">(<a href=\"#top\">back to top</a>)</p>\n")
    return "\n".join(toc), "\n".join(body)


def must_read(papers):
    items = sorted((p for p in papers if p.get("highlight")), key=sort_key)
    return "\n".join(render_entry(p) for p in items)


def render(tpl, toc, body, n, must=""):
    return (
        tpl.replace("{{TOC}}", toc)
        .replace("{{MUST_READ}}", must)
        .replace("{{PAPERS}}", f"{BEGIN}\n\n{body}\n{END}")
        .replace("{{PAPER_COUNT}}", str(n))
    )


def main():
    cats, papers = load()
    if "--check" not in sys.argv:
        import make_figures
        make_figures.main()
    toc, body = build(cats, papers)
    check = "--check" in sys.argv
    # Ignore the auto-updated date line when checking staleness.
    strip = lambda s: re.sub(r"Last updated: \d{4}-\d{2}-\d{2}", "Last updated: ", s)
    stale = []
    for tpl_path, out_path in TARGETS:
        out = render(tpl_path.read_text(encoding="utf-8"), toc, body, len(papers), must_read(papers))
        if check:
            cur = out_path.read_text(encoding="utf-8") if out_path.exists() else ""
            if strip(cur) != strip(out.replace("{{LAST_UPDATED}}", "")):
                stale.append(out_path.name)
            continue
        out = out.replace("{{LAST_UPDATED}}", datetime.date.today().isoformat())
        out_path.write_text(out, encoding="utf-8")
        print(f"Wrote {out_path.name} with {len(papers)} papers.")
    if stale:
        print(f"{', '.join(stale)} out of date. Run: python scripts/build_readme.py")
        sys.exit(1)
    if check:
        print("README files are up to date.")


if __name__ == "__main__":
    main()
