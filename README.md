<!-- ⚠️ README.md is AUTO-GENERATED from data/*.yaml by scripts/build_readme.py.
     Edit assets/README.template.md or data/papers.yaml instead. -->
<a id="top"></a>
<div align="center">

# Awesome LLM-based Multi-Agent Systems [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated, continuously updated collection of papers on Large Language Model (LLM)-driven Multi-Agent Systems (MAS).**

[![Papers](https://img.shields.io/badge/Papers-76-blue)](#-table-of-contents)
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

- **[2026/09]** 🎉 Repository launched with 76 curated papers across 20+ categories!

## 🗺️ Taxonomy

```
LLM-based Multi-Agent Systems
├── Surveys ─────────────────── MAS surveys · agent surveys · topic surveys
├── Frameworks & Infrastructure ── AutoGen · MetaGPT · CAMEL · AgentScope · ...
├── Architecture & Organization
│   ├── Communication topology & organization structure
│   ├── Automated MAS design & agentic workflow optimization
│   ├── Communication protocols & interoperability (MCP, A2A, ...)
│   └── Memory & context sharing
├── Collaboration & Reasoning ── multi-agent debate · role-play · cooperation
├── Training Multi-Agent LLMs ── multi-agent fine-tuning · MARL for LLMs
├── Evaluation & Analysis ────── benchmarks · failure attribution · scaling
├── Safety & Security ───────── attacks · defenses · robustness
└── Applications ────────────── software · science · social simulation ·
                                 games & embodied · medicine · finance · ...
```

## 📑 Table of Contents

- [Surveys](#surveys)
  - [LLM-based Multi-Agent System Surveys](#llm-based-multi-agent-system-surveys)
  - [LLM Agent Surveys](#llm-agent-surveys)
  - [Topic-Specific Surveys](#topic-specific-surveys)
- [Frameworks & Infrastructure](#frameworks--infrastructure)
  - [Multi-Agent Frameworks](#multi-agent-frameworks)
- [Architecture & Organization](#architecture--organization)
  - [Communication Topology & Organization Structure](#communication-topology--organization-structure)
  - [Automated MAS Design & Agentic Workflow Optimization](#automated-mas-design--agentic-workflow-optimization)
  - [Agent Communication Protocols & Interoperability](#agent-communication-protocols--interoperability)
  - [Memory & Context Sharing](#memory--context-sharing)
- [Collaboration & Reasoning](#collaboration--reasoning)
  - [Multi-Agent Debate & Collaborative Reasoning](#multi-agent-debate--collaborative-reasoning)
  - [Role-Playing, Cooperation & Social Reasoning](#role-playing-cooperation--social-reasoning)
- [Training Multi-Agent LLMs](#training-multi-agent-llms)
  - [Multi-Agent Fine-Tuning & Reinforcement Learning](#multi-agent-fine-tuning--reinforcement-learning)
- [Evaluation & Analysis](#evaluation--analysis)
  - [Benchmarks & Environments](#benchmarks--environments)
  - [Failure Analysis, Attribution & Scaling](#failure-analysis-attribution--scaling)
- [Safety & Security](#safety--security)
  - [Safety, Security & Robustness](#safety-security--robustness)
- [Applications](#applications)
  - [Software Engineering & Coding](#software-engineering--coding)
  - [Scientific Discovery & Research](#scientific-discovery--research)
  - [Social Simulation & Human Behavior](#social-simulation--human-behavior)
  - [Games, Embodied AI & Robotics](#games-embodied-ai--robotics)
  - [Medicine & Healthcare](#medicine--healthcare)
  - [Finance & Economics](#finance--economics)
  - [Other Domains](#other-domains)
- [Related Awesome Lists](#-related-awesome-lists)
- [Contributing](#-contributing)
- [Star History](#-star-history)

<!-- BEGIN GENERATED -->

## Surveys

> Surveys, reviews and position papers — the best place to start.

### LLM-based Multi-Agent System Surveys

- `[2026/07]` **Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges**. *Quim Motger et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2607.26212)]
- `[2026/05]` **Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems**. *Shihao Qi et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2605.14892)]
- `[2026/05]` **Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces**. *Chenchen Zhang*. ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2605.02801)]
- `[2026/04]` **Multi-Agent Systems: From Classical Paradigms to Large Foundation Model-Enabled Futures**. *Zixiang Wang et al.* ![IEEE/CAA JAS 2026](https://img.shields.io/badge/IEEE%2FCAA_JAS_2026-blue) [[Paper](https://arxiv.org/abs/2604.18133)]
- `[2026/02]` **Towards a Science of Collective AI: LLM-based Multi-Agent Systems Need a Transition from Blind Trial-and-Error to Rigorous Science**. *Jingru Fan et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2602.05289)]
- `[2026/01]` **Game-Theoretic Lens on LLM-based Multi-Agent Systems**. *Jianing Hao et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2601.15047)]
- `[2025/05]` **Creativity in LLM-based Multi-Agent Systems: A Survey**. *Yi-Cheng Lin et al.* ![EMNLP 2025](https://img.shields.io/badge/EMNLP_2025-blue) [[Paper](https://arxiv.org/abs/2505.21116)]
- `[2025/05]` **A Survey on Large Language Model based Human-Agent Systems**. *Henry Peng Zou et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2505.00753)] [[Code](https://github.com/HenryPengZou/Awesome-LLM-Based-Human-Agent-System-Papers)] ![Stars](https://img.shields.io/github/stars/HenryPengZou/Awesome-LLM-Based-Human-Agent-System-Papers?style=social)
- `[2025/04]` **Meta-Thinking in LLMs via Multi-Agent Reinforcement Learning: A Survey**. *Ahsan Bilal et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2504.14520)]
- `[2025/04]` **LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems**. *R. M. Aratchige et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2504.01963)]
- `[2025/03]` **Why Do Multi-Agent LLM Systems Fail?** *Mert Cemri et al.* ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS_2025-blue) [[Paper](https://arxiv.org/abs/2503.13657)] [[Code](https://github.com/multi-agent-systems-failure-taxonomy/MAST)] ![Stars](https://img.shields.io/github/stars/multi-agent-systems-failure-taxonomy/MAST?style=social)
- `[2025/03]` **A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives**. *Weiqiang Jin et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.13415)]
- `[2025/02]` **Multi-Agent Coordination across Diverse Applications: A Survey**. *Lijun Sun et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2502.14743)]
- `[2025/01]` **Multi-Agent Collaboration Mechanisms: A Survey of LLMs**. *Khanh-Tung Tran et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2501.06322)]
- `[2024/12]` **A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application**. *Shuaihang Chen et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2412.17481)]
- `[2024/12]` **A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios**. *Xiachong Feng et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2412.03920)]
- `[2024]` **A Survey on LLM-based Multi-Agent Systems: Workflow, Infrastructure, and Challenges**. *Xinyi Li et al.* ![Vicinagearth 2024](https://img.shields.io/badge/Vicinagearth_2024-blue) [[Paper](https://link.springer.com/article/10.1007/s44336-024-00009-2)]
- `[2024/11]` **LLM-based Multi-Agent Systems: Techniques and Business Perspectives**. *Yingxuan Yang et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2411.14033)]
- `[2024/05]` **LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions**. *Chuanneng Sun et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2405.11106)]
- `[2024/02]` **LLM Multi-Agent Systems: Challenges and Open Problems**. *Shanshan Han et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2402.03578)]
- `[2024/02]` **Large Language Model based Multi-Agents: A Survey of Progress and Challenges**. *Taicheng Guo et al.* ![IJCAI 2024](https://img.shields.io/badge/IJCAI_2024-blue) [[Paper](https://arxiv.org/abs/2402.01680)] [[Code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)] ![Stars](https://img.shields.io/github/stars/taichengguo/LLM_MultiAgents_Survey_Papers?style=social)
- `[2023/10]` **Balancing Autonomy and Alignment: A Multi-Dimensional Taxonomy for Autonomous LLM-powered Multi-Agent Architectures**. *Thorsten Händler*. ![arXiv 2023](https://img.shields.io/badge/arXiv_2023-lightgrey) [[Paper](https://arxiv.org/abs/2310.03659)]

<p align="right">(<a href="#top">back to top</a>)</p>

### LLM Agent Surveys

- `[2026/02]` **A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents**. *Wei-Chieh Huang et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2602.06052)]
- `[2026/01]` **Agentic Reasoning for Large Language Models**. *Tianxin Wei et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2601.12538)] [[Code](https://github.com/weitianxin/Awesome-Agentic-Reasoning)] ![Stars](https://img.shields.io/github/stars/weitianxin/Awesome-Agentic-Reasoning?style=social)
- `[2025/12]` **Memory in the Age of AI Agents**. *Yuyang Hu et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2512.13564)] [[Code](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)] ![Stars](https://img.shields.io/github/stars/Shichun-Liu/Agent-Memory-Paper-List?style=social)
- `[2025/09]` **LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions**. *Xixun Lin et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2509.18970)]
- `[2025/09]` **The Landscape of Agentic Reinforcement Learning for LLMs: A Survey**. *Guibin Zhang et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2509.02547)] [[Code](https://github.com/xhyumiracle/Awesome-AgenticLLM-RL-Papers)] ![Stars](https://img.shields.io/github/stars/xhyumiracle/Awesome-AgenticLLM-RL-Papers?style=social)
- `[2025/08]` **A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems**. *Jinyuan Fang et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2508.07407)] [[Code](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents)] ![Stars](https://img.shields.io/github/stars/EvoAgentX/Awesome-Self-Evolving-Agents?style=social)
- `[2025/08]` **A Survey on Agent Workflow -- Status and Future**. *Chaojia Yu et al.* ![ICAIBD 2025](https://img.shields.io/badge/ICAIBD_2025-blue) [[Paper](https://arxiv.org/abs/2508.01186)]
- `[2025/07]` **A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence**. *Huan-ang Gao et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2507.21046)] [[Code](https://github.com/CharlesQ9/Self-Evolving-Agents)] ![Stars](https://img.shields.io/github/stars/CharlesQ9/Self-Evolving-Agents?style=social)
- `[2025/05]` **AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges**. *Ranjan Sapkota et al.* ![Information Fusion 2025](https://img.shields.io/badge/Information_Fusion_2025-blue) [[Paper](https://arxiv.org/abs/2505.10468)]
- `[2025/04]` **A Survey of Frontiers in LLM Reasoning: Inference Scaling, Learning to Reason, and Agentic Systems**. *Zixuan Ke et al.* ![TMLR 2025](https://img.shields.io/badge/TMLR_2025-blue) [[Paper](https://arxiv.org/abs/2504.09037)]
- `[2025/04]` **Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems**. *Bang Liu et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2504.01990)] [[Code](https://github.com/FoundationAgents/awesome-foundation-agents)] ![Stars](https://img.shields.io/github/stars/FoundationAgents/awesome-foundation-agents?style=social)
- `[2025/03]` **Agentic Large Language Models, a Survey**. *Aske Plaat et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.23037)]
- `[2025/03]` **Large Language Model Agent: A Survey on Methodology, Applications and Challenges**. *Junyu Luo et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.21460)] [[Code](https://github.com/luo-junyu/Awesome-Agent-Papers)] ![Stars](https://img.shields.io/github/stars/luo-junyu/Awesome-Agent-Papers?style=social)
- `[2025/02]` **Position: Stop Acting Like Language Model Agents Are Normal Agents**. *Elija Perrier et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2502.10420)]
- `[2024/09]` **Large Model Based Agents: State-of-the-Art, Cooperation Paradigms, Security and Privacy, and Future Trends**. *Yuntao Wang et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2409.14457)]
- `[2024/06]` **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning**. *Xinzhe Li*. ![COLING 2025](https://img.shields.io/badge/COLING_2025-blue) [[Paper](https://arxiv.org/abs/2406.05804)] [[Code](https://github.com/xinzhel/LLM-Agent-Survey)] ![Stars](https://img.shields.io/github/stars/xinzhel/LLM-Agent-Survey?style=social)
- `[2024/04]` **A Survey on the Memory Mechanism of Large Language Model based Agents**. *Zeyu Zhang et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2404.13501)] [[Code](https://github.com/nuster1128/LLM_Agent_Memory_Survey)] ![Stars](https://img.shields.io/github/stars/nuster1128/LLM_Agent_Memory_Survey?style=social)
- `[2024/04]` **The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey**. *Tula Masterman et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2404.11584)]
- `[2024/02]` **Understanding the Planning of LLM Agents: A Survey**. *Xu Huang et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2402.02716)]
- `[2024/01]` **Agent AI: Surveying the Horizons of Multimodal Interaction**. *Zane Durante et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2401.03568)]
- `[2023/09]` **An In-depth Survey of Large Language Model-based Artificial Intelligence Agents**. *Pengyu Zhao et al.* ![arXiv 2023](https://img.shields.io/badge/arXiv_2023-lightgrey) [[Paper](https://arxiv.org/abs/2309.14365)]
- `[2023/09]` **The Rise and Potential of Large Language Model Based Agents: A Survey**. *Zhiheng Xi et al.* ![SCIS 2025](https://img.shields.io/badge/SCIS_2025-blue) [[Paper](https://arxiv.org/abs/2309.07864)] [[Code](https://github.com/WooooDyy/LLM-Agent-Paper-List)] ![Stars](https://img.shields.io/github/stars/WooooDyy/LLM-Agent-Paper-List?style=social)
- `[2023/08]` **A Survey on Large Language Model based Autonomous Agents**. *Lei Wang et al.* ![Frontiers of Computer Science 2024](https://img.shields.io/badge/Frontiers_of_Computer_Science_2024-blue) [[Paper](https://arxiv.org/abs/2308.11432)] [[Code](https://github.com/Paitesanshi/LLM-Agent-Survey)] ![Stars](https://img.shields.io/github/stars/Paitesanshi/LLM-Agent-Survey?style=social)

<p align="right">(<a href="#top">back to top</a>)</p>

### Topic-Specific Surveys

- `[2026/09]` **SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems**. *Rui Yang et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2609.00595)]
- `[2026/06]` **A Technical Taxonomy of LLM Agent Communication Protocols**. *Linus Sander et al.* ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2606.19135)]
- `[2026/04]` **A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework**. *Kexin Chu*. ![arXiv 2026](https://img.shields.io/badge/arXiv_2026-lightgrey) [[Paper](https://arxiv.org/abs/2604.23338)]
- `[2025/07]` **Evaluation and Benchmarking of LLM Agents: A Survey**. *Mahmoud Mohammadi et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2507.21504)]
- `[2025/06]` **Evolutionary Perspectives on the Evaluation of LLM-Based AI Agents: A Comprehensive Survey**. *Jiachen Zhu et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2506.11102)]
- `[2025/06]` **Survey of LLM Agent Communication with MCP: A Software Design Pattern Centric Review**. *Anjana Sarkar et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2506.05364)]
- `[2025/06]` **TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems**. *Shaina Raza et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2506.04133)]
- `[2025/05]` **Internet of Agents: Fundamentals, Applications, and Challenges**. *Yuntao Wang et al.* ![IEEE TCCN 2025](https://img.shields.io/badge/IEEE_TCCN_2025-blue) [[Paper](https://arxiv.org/abs/2505.07176)]
- `[2025/05]` **A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)**. *Abul Ehtesham et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2505.02279)]
- `[2025/05]` **Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents**. *Christian Schroeder de Witt et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2505.02077)]
- `[2025/04]` **A Survey of AI Agent Protocols**. *Yingxuan Yang et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2504.16736)]
- `[2025/04]` **A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment**. *Kun Wang et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2504.15585)]
- `[2025/03]` **Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents**. *Shuo Ren et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.24047)]
- `[2025/03]` **Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions**. *Xinyi Hou et al.* ![ACM TOSEM](https://img.shields.io/badge/ACM_TOSEM-blue) [[Paper](https://arxiv.org/abs/2503.23278)] [[Code](https://github.com/security-pride/MCP_Landscape)] ![Stars](https://img.shields.io/github/stars/security-pride/MCP_Landscape?style=social)
- `[2025/03]` **Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey**. *Shengyue Guan et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.22458)]
- `[2025/03]` **Survey on Evaluation of LLM-based Agents**. *Asaf Yehudai et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.16416)]
- `[2025/03]` **A Survey on Trustworthy LLM Agents: Threats and Countermeasures**. *Miao Yu et al.* ![KDD 2025](https://img.shields.io/badge/KDD_2025-blue) [[Paper](https://arxiv.org/abs/2503.09648)]
- `[2025/03]` **Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions**. *Mourad Gridach et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2503.08979)]
- `[2025/02]` **Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems**. *Bingyu Yan et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2502.14321)]
- `[2025/02]` **Multi-Agent Risks from Advanced AI**. *Lewis Hammond et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2502.14143)]
- `[2025/02]` **A Survey of LLM-based Agents in Medicine: How far are we from Baymax?** *Wenxuan Wang et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2502.11211)]
- `[2025/02]` **Position: Towards a Responsible LLM-empowered Multi-Agent Systems**. *Jinwei Hu et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2502.01714)]
- `[2025/01]` **Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG**. *Aditi Singh et al.* ![arXiv 2025](https://img.shields.io/badge/arXiv_2025-lightgrey) [[Paper](https://arxiv.org/abs/2501.09136)]
- `[2024/12]` **From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents**. *Xinyi Mou et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2412.03563)] [[Code](https://github.com/FudanDISC/SocialAgent)] ![Stars](https://img.shields.io/github/stars/FudanDISC/SocialAgent?style=social)
- `[2024/11]` **Large Language Model-Brained GUI Agents: A Survey**. *Chaoyun Zhang et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2411.18279)]
- `[2024/11]` **Navigating the Risks: A Survey of Security, Privacy, and Ethics Threats in LLM-Based Agents**. *Yuyou Gan et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2411.09523)]
- `[2024/09]` **Agents in Software Engineering: Survey, Landscape, and Vision**. *Yanlin Wang et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2409.09030)]
- `[2024/09]` **Large Language Model-Based Agents for Software Engineering: A Survey**. *Junwei Liu et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2409.02977)]
- `[2024/07]` **The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies**. *Feng He et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2407.19354)]
- `[2024/04]` **A Survey on Large Language Model-Based Game Agents**. *Sihao Hu et al.* ![arXiv 2024](https://img.shields.io/badge/arXiv_2024-lightgrey) [[Paper](https://arxiv.org/abs/2404.02039)]
- `[2023/12]` **Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives**. *Chen Gao et al.* ![Humanities & Social Sciences Communications 2024](https://img.shields.io/badge/Humanities_%26_Social_Sciences_Communications_2024-blue) [[Paper](https://arxiv.org/abs/2312.11970)]

<p align="right">(<a href="#top">back to top</a>)</p>

## Frameworks & Infrastructure

> General-purpose platforms and frameworks for building LLM multi-agent systems.

### Multi-Agent Frameworks

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

## Architecture & Organization

> How agents are wired together — topology, roles, and automated system design.

### Communication Topology & Organization Structure

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Automated MAS Design & Agentic Workflow Optimization

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Agent Communication Protocols & Interoperability

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Memory & Context Sharing

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

## Collaboration & Reasoning

> Mechanisms through which multiple LLM agents reason, argue, and cooperate.

### Multi-Agent Debate & Collaborative Reasoning

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Role-Playing, Cooperation & Social Reasoning

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

## Training Multi-Agent LLMs

> Fine-tuning and reinforcement learning for systems of LLM agents.

### Multi-Agent Fine-Tuning & Reinforcement Learning

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

## Evaluation & Analysis

> Benchmarks, failure analysis, and scaling studies of LLM multi-agent systems.

### Benchmarks & Environments

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Failure Analysis, Attribution & Scaling

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

## Safety & Security

> Attacks, defenses, and robustness of LLM multi-agent systems.

### Safety, Security & Robustness

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

## Applications

> LLM multi-agent systems applied to real domains.

### Software Engineering & Coding

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Scientific Discovery & Research

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Social Simulation & Human Behavior

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Games, Embodied AI & Robotics

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Medicine & Healthcare

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Finance & Economics

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

### Other Domains

*Coming soon — PRs welcome!*

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- END GENERATED -->

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

<p align="center"><sub>Last updated: 2026-09-26 · Generated by <a href="scripts/build_readme.py">build_readme.py</a></sub></p>
