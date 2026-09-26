<!-- ⚠️ README_zh.md 由 scripts/build_readme.py 根据 data/*.yaml 自动生成，请勿直接编辑。 -->
<a id="top"></a>
<div align="center">

# Awesome LLM-based Multi-Agent Systems [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**大语言模型（LLM）驱动的多智能体系统（MAS）论文合集 —— 精选、分类、持续更新。**

[![Papers](https://img.shields.io/badge/Papers-{{PAPER_COUNT}}-blue)](#-目录)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Commit](https://img.shields.io/github/last-commit/chen742/Awesome_multi-agent-system)](https://github.com/chen742/Awesome_multi-agent-system/commits)
[![GitHub Stars](https://img.shields.io/github/stars/chen742/Awesome_multi-agent-system?style=social)](https://github.com/chen742/Awesome_multi-agent-system/stargazers)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

[English](README.md) | **简体中文**

</div>

当一个 LLM 不够用时，多个 LLM 智能体可以**对话、辩论、分工协作、自组织**。本仓库系统整理 LLM 多智能体系统的研究前沿：综述、框架、通信拓扑、自动化系统设计、多智能体强化学习、评测基准、失败分析、安全，以及各领域应用。

- 📚 每个类别内论文按**时间倒序**排列，标注 `[YYYY/MM]`（arXiv 日期）、会议/期刊徽章和代码链接。
- :star: 表示**必读论文**，新入门的同学可以从这些开始。
- 🤝 **非常欢迎贡献！** 发现遗漏的论文？请[提交 Issue](https://github.com/chen742/Awesome_multi-agent-system/issues/new/choose) 或 PR，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果本仓库对你有帮助，欢迎点一个 ⭐，让更多研究者看到它！

## 🔥 最新动态

- **[2026/09]** 🤖 为必读论文和近期论文添加一句话总结（💡）、分类体系图与趋势图，并上线每日 arXiv 追踪（自动以 Issue 形式推荐新论文）。
- **[2026/09]** 🎉 仓库上线，收录 {{PAPER_COUNT}} 篇精选论文，覆盖 20+ 个类别！

## 🗺️ 分类体系

<p align="center"><img src="assets/taxonomy.svg" width="860" alt="Taxonomy of LLM-based multi-agent systems"></p>

## 🌟 必读论文

刚接触 LLM 多智能体系统？建议从这些里程碑论文开始（按时间顺序）。

{{MUST_READ}}

## 📊 统计

<p align="center"><img src="assets/trend.svg" width="860" alt="Papers per quarter"></p>

## 📑 目录

{{TOC}}
- [贡献指南](#-贡献指南)

{{PAPERS}}

## 🤝 贡献指南

论文列表由 [`data/papers.yaml`](data/papers.yaml) **自动生成**，添加一篇论文只需要一段 YAML：

```yaml
- title: "Your Paper Title"
  authors: "First Author et al."
  venue: "NeurIPS 2025"      # 或 "arXiv 2026"
  year: 2025
  arxiv: "2501.12345"        # 非 arXiv 论文请用 `url:`
  code: "https://github.com/owner/repo"
  category: debate           # 见 data/categories.yaml
```

然后运行 `python scripts/validate.py && python scripts/build_readme.py` 并提交 PR。不熟悉 PR？直接[提交 Issue](https://github.com/chen742/Awesome_multi-agent-system/issues/new/choose) 附上论文链接即可。

<a href="https://github.com/chen742/Awesome_multi-agent-system/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=chen742/Awesome_multi-agent-system" />
</a>

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=chen742/Awesome_multi-agent-system&type=Date)](https://star-history.com/#chen742/Awesome_multi-agent-system&Date)

<p align="center"><sub>Last updated: {{LAST_UPDATED}} · 由 <a href="scripts/build_readme.py">build_readme.py</a> 自动生成</sub></p>
