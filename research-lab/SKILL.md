---
name: research-lab
description: "科研全流程智能调度台(v2.0 吸收外部skill生态)。覆盖论文检索(知网/GS/arXiv/BGPT)→阅读审稿→写作润色→PPT汇报→实验分析→电池材料计算→idea评估→实验设计→科学可视化。说人话即可，自动识别意图路由到对应子skill。触发: 搜论文/下载论文/审稿/写引言/润色/做PPT/评估idea/分析数据/文献综述/电池/电化学/晶体结构/相图/Materials Project/实验设计。"
metadata:
  version: "2.0.0"
  mega: true
  subskills:
    paper_search: [cnki-search, cnki-advanced-search, cnki-download, cnki-export, cnki-paper-detail, cnki-journal-index, cnki-journal-search, cnki-journal-toc, cnki-navigate-pages, cnki-parse-results, gs-search, gs-advanced-search, gs-cited-by, gs-export, gs-fulltext, gs-navigate-pages, arxiv, doi-to-zotero, battery-search]
    paper_reading: [academic-paper, academic-paper-reviewer, pre-submission-reviewer, research-summary, literature-review-writing, academic-pipeline]
    paper_writing: [research-paper-writing, battery-writer, nature-polishing, nature-citation, nature-data, intro-drafter, tech-paper-template, benchmark-paper-template]
    presentation: [group-meeting-pptx, nature-paper2ppt, battery-paper2ppt, nature-figure, battery-figure, figure-designer, manim-video, scientific-schematics]
    idea: [idea-evaluator, idea-refine, vibe-research-workflow, deep-research, hypothesis-generation]
    experiment: [hv-analysis, battery-analysis, youtube-content, whisper, experimental-design, exploratory-data-analysis, statistical-analysis]
    battery_materials: [pymatgen-battery]
    extra: [interview-me, khazix-writer]
  absorbed_from:
    - scientific-agent-skills (K-Dense-AI): pymatgen, experimental-design, scientific-visualization, statistical-analysis, literature-review, peer-review
    - AI-Research-SKILLs (Orchestra-Research): hypothesis-generation, exploratory-data-analysis
    - Awesome-Auto-Research-Tools: BGPT paper search patterns, PaperQA2 RAG patterns, PaperBanana auto-illustration, STORM deep research synthesis
---

# 🔬 科研工作台 (research-lab) v2.0

吸收外部 skill 生态后的升级版。你不需要记住任何子 skill 的名字，直接说人话，自动路由。

## 意图路由表

### 📥 论文检索与下载

| 你说... | 路由到 |
|---------|--------|
| "搜知网/CNKI XXX" | `cnki-search` |
| "知网高级搜索XXX" | `cnki-advanced-search` |
| "下载这篇知网论文" | `cnki-download` |
| "导出引用/题录" | `cnki-export` |
| "看这篇知网论文详情" | `cnki-paper-detail` |
| "XXX期刊目录" | `cnki-journal-index/search/toc` |
| "Google Scholar搜XXX" | `gs-search` |
| "Scholar高级搜索" | `gs-advanced-search` |
| "这篇被谁引用了" | `gs-cited-by` |
| "导出Scholar结果" | `gs-export` |
| "找这篇全文" | `gs-fulltext` |
| "arXiv搜XXX" | `arxiv` |
| "DOI加到Zotero" | `doi-to-zotero` |
| "搜一下XXX论文" (未指定平台) | `battery-search` (电池类) / `gs-search` + `cnki-search` |
| "结构化搜XXX实验数据" / "提取论文方法/样本量" | BGPT 风格结构化搜索 → WebSearch + 字段提取 |

### 📖 论文阅读与审稿

| 你说... | 路由到 |
|---------|--------|
| "分析/总结这篇论文" | `research-summary` |
| "审稿这篇论文" | `academic-paper-reviewer` ← **默认审稿模式（四问+三idea）** |
| "投稿前帮我审一下" | `pre-submission-reviewer` |
| "写XXX文献综述" | `literature-review-writing` |
| "批量处理论文" | `academic-pipeline` |
| "写学术论文" | `academic-paper` |
| "这篇论文方法论有什么漏洞" | `academic-paper-reviewer` + scientific-critical-thinking 框架 |
| "对比几篇论文的方法" | `literature-review-writing` + 方法论对比矩阵 |

### ✍️ 论文写作

| 你说... | 路由到 |
|---------|--------|
| "润色这段英文" | `nature-polishing` |
| "Nature引用格式" | `nature-citation` |
| "Nature图规范" | `nature-data` |
| "写引言草稿" | `intro-drafter` |
| "评估这个idea" | `idea-evaluator` |
| "论文模板" | `tech-paper-template` / `benchmark-paper-template` |
| "写论文XXX部分" | `research-paper-writing` |
| "电池论文写作/润色" | `battery-writer` |
| "投稿模板/期刊格式" | `tech-paper-template` + venue-templates 风格 |

### 🎬 演示与汇报

| 你说... | 路由到 |
|---------|--------|
| "组会PPT" | `group-meeting-pptx` |
| "论文做成PPT" | `nature-paper2ppt` / `battery-paper2ppt`(电池方向) |
| "Nature风格图" | `nature-figure` |
| "电池配图" | `battery-figure` |
| "图怎么改进" | `figure-designer` |
| "动画演示XXX原理" | `manim-video` |
| "画个科学示意图/机理图/TOC" | `scientific-schematics` (吸收 PaperBanana 多 Agent 配图) |
| "数据可视化/科研配色" | `figure-designer` + scientific-visualization 框架 |

### 🧪 科研辅助与实验

| 你说... | 路由到 |
|---------|--------|
| "分析研究方向/博导视角" | `vibe-research-workflow` |
| "深入研究XXX" | `deep-research` (吸收 STORM Wiki 风格长文生成) |
| "电化学数据分析/CV/EIS/充放电" | `hv-analysis` |
| "电池数据分析" | `battery-analysis` |
| "录音转文字" | `whisper` |
| "提取YouTube视频内容" | `youtube-content` |
| "优化/打磨这个idea" | `idea-refine` |
| "模拟面试" / "面试准备" | `interview-me` |
| "Khazix风格写作" | `khazix-writer` |
| "实验怎么设计/对照组" | `experimental-design` (吸收 scientific-agent-skills) |
| "数据探索/EDA" | `exploratory-data-analysis` |
| "统计分析/显著性/误差棒" | `statistical-analysis` |
| "提出假设/猜想" | `hypothesis-generation` |

### 🔋 电池材料计算（NEW v2.0）

| 你说... | 路由到 |
|---------|--------|
| "分析晶体结构/CIF/POSCAR" | `pymatgen-battery` |
| "画相图/热力学稳定性" | `pymatgen-battery` |
| "查Materials Project数据" | `pymatgen-battery` |
| "算能带/态密度DOS" | `pymatgen-battery` |
| "做表面/界面/扩散分析" | `pymatgen-battery` |
| "格式转换 CIF↔POSCAR↔XYZ" | `pymatgen-battery` |
| "硫化物电解质结构分析" | `pymatgen-battery` |

## 执行规则

1. **单意图直接路由** → 调用对应子 skill
2. **多意图串行** → 如"搜这篇然后审稿" → 先搜后审
3. **意图不明反问** → 简短确认
4. **子 skill 不可用降级** → WebSearch/WebFetch 替代
5. **始终遵循 CLAUDE.md** → 审稿四问框架；中文回复
6. **电池相关语境** → 优先用 battery-* 系列 skill
7. **材料计算类** → 先检查 pymatgen 是否可安装，降级为 WebFetch Materials Project

## 快捷指令

- `/lab search [关键词]` = 论文搜索
- `/lab review` = 审稿模式
- `/lab polish` = Nature 润色
- `/lab ppt` = 组会 PPT
- `/lab idea` = 评估 idea
- `/lab mat [材料名/结构]` = pymatgen 材料计算（NEW）
- `/lab design [实验主题]` = 实验设计（NEW）
