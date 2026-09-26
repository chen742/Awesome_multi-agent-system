#!/usr/bin/env python3
"""Generate assets/taxonomy.svg and assets/trend.svg from data/*.yaml.

Both SVGs carry their own light/dark colors via prefers-color-scheme, so they
read well on GitHub's light and dark themes. Called by build_readme.py.
"""
import re
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

import yaml

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# Shared theme tokens (reference palette: surfaces, text inks, blue sequential,
# categorical slots in their fixed order).
STYLE = """
  .surface {{ fill: #fcfcfb; }}
  .card {{ fill: #ffffff; stroke: #e4e3df; }}
  .ink1 {{ fill: #0b0b0b; }}
  .ink2 {{ fill: #52514e; }}
  .ink3 {{ fill: #7a7975; }}
  .grid {{ stroke: #e4e3df; }}
  .axis {{ stroke: #b9b8b3; }}
  .bar {{ fill: #2a78d6; }}
{light_slots}
  @media (prefers-color-scheme: dark) {{
    .surface {{ fill: #1a1a19; }}
    .card {{ fill: #232322; stroke: #383835; }}
    .ink1 {{ fill: #ffffff; }}
    .ink2 {{ fill: #c3c2b7; }}
    .ink3 {{ fill: #9a998f; }}
    .grid {{ stroke: #383835; }}
    .axis {{ stroke: #5a5955; }}
    .bar {{ fill: #3987e5; }}
{dark_slots}
  }}
  text {{ font-family: {font}; }}
"""
SLOTS_LIGHT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
SLOTS_DARK = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"]


def style():
    light = "\n".join(f"  .s{i} {{ fill: {c}; }}" for i, c in enumerate(SLOTS_LIGHT))
    dark = "\n".join(f"    .s{i} {{ fill: {c}; }}" for i, c in enumerate(SLOTS_DARK))
    return STYLE.format(light_slots=light, dark_slots=dark, font=FONT)


# Shorter labels for the figure; the README uses the full titles.
SHORT = {
    "survey-mas": "Multi-agent system surveys",
    "survey-agent": "LLM agent surveys",
    "survey-topic": "Topic-specific surveys",
    "framework": "AutoGen · MetaGPT · CAMEL · ...",
    "topology": "Communication topology",
    "auto-design": "Automated MAS design",
    "protocol": "Protocols (MCP, A2A, ...)",
    "memory": "Memory & context sharing",
    "debate": "Multi-agent debate",
    "roleplay": "Role-play & cooperation",
    "training": "Multi-agent fine-tuning & RL",
    "benchmark": "Benchmarks & environments",
    "analysis": "Failure analysis & scaling",
    "safety": "Attacks, defenses, robustness",
    "app-software": "Software engineering",
    "app-science": "Scientific discovery",
    "app-social": "Social simulation",
    "app-embodied": "Games, embodied & robotics",
    "app-medical": "Medicine & healthcare",
    "app-finance": "Finance & economics",
    "app-other": "Law, GUI, education, ...",
}


def taxonomy_svg(cats, papers):
    counts = Counter(p["category"] for p in papers)
    W, PAD, GAP = 960, 24, 16
    col_w = (W - 2 * PAD - GAP) / 2
    head_h, line_h, card_pad = 40, 24, 14
    top = 92

    # Masonry: place each section card in the currently shorter column.
    cols = [top, top]
    cards = []
    for i, sec in enumerate(cats):
        subs = sec.get("subcategories", [])
        h = head_h + len(subs) * line_h + card_pad
        c = 0 if cols[0] <= cols[1] else 1
        cards.append((i, sec, subs, PAD + c * (col_w + GAP), cols[c], h))
        cols[c] += h + GAP
    H = int(max(cols) + PAD - GAP + 8)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
           f'role="img" aria-labelledby="t d">',
           '<title id="t">Taxonomy of LLM-based multi-agent systems</title>',
           f'<desc id="d">{len(cats)} research areas with paper counts per sub-topic.</desc>',
           f"<style>{style()}</style>",
           f'<rect class="surface" width="{W}" height="{H}" rx="12"/>',
           f'<text class="ink1" x="{W / 2}" y="44" text-anchor="middle" font-size="24" font-weight="700">'
           f"LLM-based Multi-Agent Systems</text>",
           f'<text class="ink2" x="{W / 2}" y="70" text-anchor="middle" font-size="14">'
           f"Taxonomy of this list · {len(papers)} papers</text>"]
    for i, sec, subs, x, y, h in cards:
        total = sum(counts[s["id"]] for s in subs)
        slot = f"s{i % len(SLOTS_LIGHT)}"
        out.append(f'<rect class="card" x="{x}" y="{y}" width="{col_w}" height="{h}" rx="10"/>')
        out.append(f'<rect class="{slot}" x="{x}" y="{y + 12}" width="4" height="{h - 24}" rx="2"/>')
        out.append(f'<text class="ink1" x="{x + 20}" y="{y + 27}" font-size="16" font-weight="700">'
                   f"{escape(sec['title'])}</text>")
        out.append(f'<text class="ink2" x="{x + col_w - 16}" y="{y + 27}" text-anchor="end" font-size="13" '
                   f'font-weight="600">{total}</text>')
        for j, s in enumerate(subs):
            ly = y + head_h + j * line_h + 12
            out.append(f'<text class="ink2" x="{x + 20}" y="{ly}" font-size="13.5">'
                       f"{escape(SHORT.get(s['id'], s['title']))}</text>")
            out.append(f'<text class="ink3" x="{x + col_w - 16}" y="{ly}" text-anchor="end" font-size="13">'
                       f"{counts[s['id']]}</text>")
    out.append("</svg>")
    return "\n".join(out)


def quarter(p):
    aid = str(p.get("arxiv") or "")
    if not re.match(r"^\d{4}\.\d{4,5}$", aid):
        return None
    yy, mm = int(aid[:2]), int(aid[2:4])
    return 2000 + yy, (mm - 1) // 3 + 1


def trend_svg(papers):
    q = Counter(filter(None, (quarter(p) for p in papers)))
    first, last = min(q), max(q)
    keys, (y, qq) = [], first
    while (y, qq) <= last:
        keys.append((y, qq))
        y, qq = (y + 1, 1) if qq == 4 else (y, qq + 1)
    vals = [q.get(k, 0) for k in keys]

    W, H = 960, 360
    L, R, T, B = 56, 24, 76, 56
    pw, ph = W - L - R, H - T - B
    step = pw / len(keys)
    bw = min(34, step * 0.6)
    vmax = max(vals)
    tick = 10 if vmax <= 60 else 20
    top_v = ((vmax + tick - 1) // tick) * tick
    sy = lambda v: T + ph - v / top_v * ph

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
           f'role="img" aria-labelledby="t d">',
           '<title id="t">Papers in this list per quarter</title>',
           '<desc id="d">' + escape(", ".join(f"{y} Q{qq}: {v}" for (y, qq), v in zip(keys, vals))) + "</desc>",
           f"<style>{style()}</style>",
           f'<rect class="surface" width="{W}" height="{H}" rx="12"/>',
           f'<text class="ink1" x="{L}" y="36" font-size="18" font-weight="700">Papers in this list per quarter</text>',
           f'<text class="ink2" x="{L}" y="58" font-size="13">By arXiv submission date · '
           f"{sum(vals)} papers with arXiv IDs · {last[0]} Q{last[1]} still in progress</text>"]
    for v in range(0, top_v + 1, tick):
        yv = sy(v)
        cls = "axis" if v == 0 else "grid"
        out.append(f'<line class="{cls}" x1="{L}" x2="{W - R}" y1="{yv}" y2="{yv}" stroke-width="1"/>')
        out.append(f'<text class="ink3" x="{L - 8}" y="{yv + 4}" text-anchor="end" font-size="12">{v}</text>')
    peak = vals.index(vmax)
    for i, ((y, qq), v) in enumerate(zip(keys, vals)):
        cx = L + step * i + step / 2
        x0, y0 = cx - bw / 2, sy(v)
        h = T + ph - y0
        if v:
            r = min(4, h)
            # Rounded data-end on top, square on the baseline.
            out.append(f'<path class="bar" d="M{x0},{T + ph} V{y0 + r} Q{x0},{y0} {x0 + r},{y0} '
                       f'H{x0 + bw - r} Q{x0 + bw},{y0} {x0 + bw},{y0 + r} V{T + ph} Z">'
                       f"<title>{y} Q{qq}: {v} papers</title></path>")
        if i in (peak, len(vals) - 1):
            out.append(f'<text class="ink1" x="{cx}" y="{y0 - 8}" text-anchor="middle" font-size="12" '
                       f'font-weight="600">{v}</text>')
        out.append(f'<text class="ink3" x="{cx}" y="{T + ph + 18}" text-anchor="middle" font-size="11.5">Q{qq}</text>')
        if qq == 1 or i == 0:
            out.append(f'<text class="ink2" x="{cx}" y="{T + ph + 36}" text-anchor="middle" font-size="12.5" '
                       f'font-weight="600">{y}</text>')
    out.append("</svg>")
    return "\n".join(out)


def main():
    cats = yaml.safe_load((ROOT / "data" / "categories.yaml").read_text(encoding="utf-8"))
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8")) or []
    (ASSETS / "taxonomy.svg").write_text(taxonomy_svg(cats, papers), encoding="utf-8")
    (ASSETS / "trend.svg").write_text(trend_svg(papers), encoding="utf-8")
    print("Wrote assets/taxonomy.svg and assets/trend.svg")


if __name__ == "__main__":
    main()
