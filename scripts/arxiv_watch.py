#!/usr/bin/env python3
"""Find new arXiv papers on LLM-based multi-agent systems and draft an issue.

Queries the arXiv API for recent papers mentioning both multi-agent and LLM
terms, drops papers already in data/papers.yaml (and IDs passed via
--seen-file, e.g. from earlier watch issues), and writes a markdown issue
body with a suggested category and a ready-to-paste YAML entry per paper.

Usage:
    python scripts/arxiv_watch.py --days 7 --out issue.md [--seen-file seen.txt]
    python scripts/arxiv_watch.py --feed saved_feed.xml --out issue.md   # offline

Exit code 0 always; the output file is only written when there are new papers.
"""
import argparse
import datetime as dt
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}

MA_TERMS = r"multi[- ]?agent|agent (?:collaboration|societ|team|network|swarm)|agentic workflow|agent debate"
LLM_TERMS = r"\bLLMs?\b|large language model|language agents?|foundation model|\bGPT"
QUERY = ('(abs:"multi-agent" OR abs:"multiagent" OR abs:"multi agent" OR ti:"agents")'
         ' AND (abs:"large language model" OR abs:"LLM" OR abs:"LLMs" OR abs:"language agents")'
         ' AND (cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR cat:cs.MA OR cat:cs.SE OR cat:cs.CR OR cat:cs.RO)')

# First match wins; ordered from most to least specific.
CATEGORY_RULES = [
    ("survey-mas", r"\bsurvey\b|\breview of\b|\bsystematic review\b"),
    ("safety", r"attack|jailbreak|adversar|malicious|safety|secur|backdoor|privacy|poison"),
    ("analysis", r"failure|attribution|why .* fail|scaling law|diagnos"),
    ("benchmark", r"benchmark|\barena\b|evaluation suite|testbed"),
    ("training", r"reinforcement learning|\bRL\b|GRPO|PPO|fine-?tun|post-?train|self-play|co-evol"),
    ("auto-design", r"automat\w* design|architecture search|workflow (?:search|optimi|generation)|meta[- ]agent"),
    ("protocol", r"\bMCP\b|model context protocol|\bA2A\b|protocol|interoperab"),
    ("topology", r"topolog|communication graph|pruning|orchestrat|routing|hierarch"),
    ("memory", r"memory"),
    ("debate", r"debate|consensus|voting|deliberat"),
    ("app-software", r"code generation|software|program repair|\bSWE\b|coding"),
    ("app-science", r"scientific|research assistant|chemistry|biolog|material|discovery"),
    ("app-medical", r"medical|clinical|health|diagnos|patient"),
    ("app-finance", r"financ|trading|stock|econom"),
    ("app-social", r"simulat\w* (?:society|social|human)|social simulation|opinion|population"),
    ("app-embodied", r"robot|embodied|minecraft|game|navigation"),
    ("framework", r"framework|platform|library|toolkit"),
    ("roleplay", r"role-?play|persona|theory of mind|negotiat|cooperat"),
]


def fetch(days, max_results=300):
    params = {"search_query": QUERY, "sortBy": "submittedDate", "sortOrder": "descending",
              "start": 0, "max_results": max_results}
    url = f"{API}?{urllib.parse.urlencode(params)}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception:  # arXiv API is occasionally flaky
            if attempt == 3:
                raise
            time.sleep(5 * 2 ** attempt)


def parse(feed, days):
    root = ET.fromstring(feed)
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)
    out = []
    for e in root.findall("a:entry", NS):
        published = dt.datetime.fromisoformat(e.findtext("a:published", "", NS).replace("Z", "+00:00"))
        if published < cutoff:
            continue
        m = re.search(r"abs/(\d{4}\.\d{4,5})", e.findtext("a:id", "", NS))
        if not m:
            continue
        title = " ".join(e.findtext("a:title", "", NS).split())
        abstract = " ".join(e.findtext("a:summary", "", NS).split())
        authors = [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)]
        out.append({"arxiv": m.group(1), "title": title, "abstract": abstract,
                    "authors": authors, "date": published.date().isoformat()})
    return out


def relevant(p):
    text = f"{p['title']} {p['abstract']}"
    return re.search(MA_TERMS, text, re.I) and re.search(LLM_TERMS, text, re.I)


def suggest_category(p):
    # Title is the strongest signal; fall back to the abstract.
    for field in (p["title"], p["abstract"]):
        for cat, pat in CATEGORY_RULES:
            if re.search(pat, field, re.I):
                return cat
    return "topology"


MAX_PAPERS = 50          # keep one issue reviewable
MAX_BODY = 60000         # GitHub caps issue bodies at 65536 chars


def render(papers, days, with_abstract=True):
    today = dt.date.today().isoformat()
    lines = [f"Found **{len(papers)}** new arXiv papers on LLM-based multi-agent systems "
             f"(submitted in the last {days} days, not yet in the list)."
             + (f" Showing the newest {MAX_PAPERS}; the rest will appear in the next run." if len(papers) > MAX_PAPERS else ""),
             "",
             "Tick the ones worth adding, then copy their YAML into `data/papers.yaml` "
             "(adjust `category` if needed) and run `python scripts/build_readme.py`.",
             ""]
    for p in papers[:MAX_PAPERS]:
        first = p["authors"][0] if p["authors"] else ""
        authors = f"{first} et al." if len(p["authors"]) > 1 else first
        cat = suggest_category(p)
        snippet = yaml.safe_dump([{"title": p["title"], "authors": authors, "venue": f"arXiv {p['date'][:4]}",
                                   "year": int(p["date"][:4]), "arxiv": p["arxiv"], "category": cat}],
                                 allow_unicode=True, sort_keys=False, width=200).rstrip()
        abstract = p["abstract"] if len(p["abstract"]) <= 500 else p["abstract"][:500].rsplit(" ", 1)[0] + " ..."
        lines += [f"- [ ] **[{p['title']}](https://arxiv.org/abs/{p['arxiv']})** · {authors} · "
                  f"`{p['date']}` · suggested: `{cat}`",
                  "  <details><summary>Abstract & YAML</summary>",
                  "",
                  *([f"  > {abstract}", ""] if with_abstract else []),
                  "  ```yaml",
                  *[f"  {l}" for l in snippet.splitlines()],
                  "  ```",
                  "  </details>",
                  ""]
    lines.append(f"<sub>Generated by `scripts/arxiv_watch.py` on {today}.</sub>")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--out", default="arxiv_issue.md")
    ap.add_argument("--seen-file", help="file with arXiv IDs already reported (any text; IDs are extracted)")
    ap.add_argument("--feed", help="read an Atom feed from disk instead of the API (for testing)")
    args = ap.parse_args()

    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8")) or []
    known = {str(p.get("arxiv")) for p in papers if p.get("arxiv")}
    if args.seen_file and Path(args.seen_file).exists():
        known |= set(re.findall(r"\d{4}\.\d{4,5}", Path(args.seen_file).read_text(encoding="utf-8")))

    feed = Path(args.feed).read_bytes() if args.feed else fetch(args.days)
    new = [p for p in parse(feed, args.days) if p["arxiv"] not in known and relevant(p)]
    print(f"{len(new)} new relevant papers.")
    if new:
        body = render(new, args.days)
        if len(body) > MAX_BODY:
            body = render(new, args.days, with_abstract=False)
        Path(args.out).write_text(body, encoding="utf-8")
        print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
