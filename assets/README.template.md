<!-- ⚠️ README.md is AUTO-GENERATED from data/*.yaml by scripts/build_readme.py.
     Edit assets/README.template.md or data/papers.yaml instead. -->
<a id="top"></a>
<div align="center">

# Awesome LLM-based Multi-Agent Systems [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated, continuously updated collection of papers on Large Language Model (LLM)-driven Multi-Agent Systems (MAS).**

[![Papers](https://img.shields.io/badge/Papers-{{PAPER_COUNT}}-blue)](#-table-of-contents)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Commit](https://img.shields.io/github/last-commit/chen742/Awesome_multi-agent-system)](https://github.com/chen742/Awesome_multi-agent-system/commits)
[![GitHub Stars](https://img.shields.io/github/stars/chen742/Awesome_multi-agent-system?style=social)](https://github.com/chen742/Awesome_multi-agent-system/stargazers)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

**English** | [简体中文](README_zh.md)

</div>

When one LLM is not enough, many LLM agents **talk, debate, divide labor, and self-organize**. This repository tracks the research frontier of LLM-based multi-agent systems — from surveys and frameworks, to communication topologies, automated system design, multi-agent reinforcement learning, benchmarks, failure analysis, safety, and real-world applications.

- 📚 Papers are sorted **newest first** within each category, tagged with `[YYYY/MM]` (arXiv date), venue badge, and code link.
- :star: marks **must-read** papers — start here if you are new to the field.
- 🤝 **Contributions are very welcome!** Found a missing paper? [Open an issue](https://github.com/chen742/Awesome_multi-agent-system/issues/new/choose) or submit a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).

If you find this repository helpful, please give it a ⭐ — it helps more researchers discover it!

## 🔥 News

- **[2026/09]** 🤖 Added one-line TL;DRs (💡) for must-read and recent papers, taxonomy & trend figures, and a daily arXiv watcher that proposes new papers as issues.
- **[2026/09]** 🎉 Repository launched with {{PAPER_COUNT}} curated papers across 20+ categories!

## 🗺️ Taxonomy

<p align="center"><img src="assets/taxonomy.svg" width="860" alt="Taxonomy of LLM-based multi-agent systems"></p>

## 🌟 Must-Read Papers

New to LLM multi-agent systems? Start with these milestone papers (in chronological order).

{{MUST_READ}}

## 📊 Statistics

<p align="center"><img src="assets/trend.svg" width="860" alt="Papers per quarter"></p>

## 📑 Table of Contents

{{TOC}}
- [Related Awesome Lists](#-related-awesome-lists)
- [Contributing](#-contributing)
- [Star History](#-star-history)

{{PAPERS}}

## 🔗 Related Awesome Lists

- [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) — The Rise and Potential of LLM-based Agents.
- [taichengguo/LLM_MultiAgents_Survey_Papers](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers) — LLM-based Multi-Agents: A Survey of Progress and Challenges.
- [Paitesanshi/LLM-Agent-Survey](https://github.com/Paitesanshi/LLM-Agent-Survey) — A Survey on LLM-based Autonomous Agents.
- [zjunlp/LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) — Must-read papers on LLM agents.
- [AGI-Edgerunners/LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) — Papers on LLM agents.
- [FoundationAgents/awesome-foundation-agents](https://github.com/FoundationAgents/awesome-foundation-agents) — Advances and Challenges in Foundation Agents.
- [kyegomez/awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers) — Multi-agent papers.
- [Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) — Memory in the age of AI agents.
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI agent products and open-source projects.
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — Awesome LLM resources.

## 🤝 Contributing

This list is **generated from [`data/papers.yaml`](data/papers.yaml)**, so adding a paper takes one short YAML block:

```yaml
- title: "Your Paper Title"
  authors: "First Author et al."
  venue: "NeurIPS 2025"      # or "arXiv 2026"
  year: 2025
  arxiv: "2501.12345"        # or `url:` for non-arXiv papers
  code: "https://github.com/owner/repo"
  category: debate           # see data/categories.yaml
```

Then run `python scripts/validate.py && python scripts/build_readme.py` and open a PR. Not comfortable with PRs? Just [open an issue](https://github.com/chen742/Awesome_multi-agent-system/issues/new/choose) with the paper link. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Thanks to all contributors!**

<a href="https://github.com/chen742/Awesome_multi-agent-system/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=chen742/Awesome_multi-agent-system" />
</a>

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=chen742/Awesome_multi-agent-system&type=Date)](https://star-history.com/#chen742/Awesome_multi-agent-system&Date)

## 📝 Citation

If you find this repository useful in your research, please consider citing it:

```bibtex
@misc{awesome-llm-mas,
  title        = {Awesome LLM-based Multi-Agent Systems},
  author       = {chen742 and contributors},
  year         = {2026},
  howpublished = {\url{https://github.com/chen742/Awesome_multi-agent-system}}
}
```

<p align="center"><sub>Last updated: {{LAST_UPDATED}} · Generated by <a href="scripts/build_readme.py">build_readme.py</a></sub></p>
