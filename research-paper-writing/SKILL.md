---
name: research-paper-writing
description: Academic paper writing workflow — literature review, LaTeX setup, structure, citations, and conference submissions.
version: 1.0.0
author: hermes-CCC (ported from Hermes Agent by NousResearch)
license: MIT
metadata:
  hermes:
    tags: [Research, Academic, Writing, LaTeX, Papers, Citations, Conference]
    related_skills: [arxiv]
---

# Research Paper Writing

End-to-end workflow for writing and submitting academic papers.

---

## Paper Structure

```
1. Title & Authors
2. Abstract         ← write last, 150-250 words
3. Introduction     ← problem, gap, contributions, roadmap
4. Related Work     ← what exists, why insufficient
5. Methodology      ← your approach, architecture, algorithm
6. Experiments      ← setup, baselines, metrics
7. Results          ← tables, figures, analysis
8. Discussion       ← limitations, broader impact
9. Conclusion       ← summary, future work
10. References
Appendix (optional)
```

---

## Abstract Formula

```
[PROBLEM] Prior work has struggled with X.
[GAP] Existing approaches fail because Y.
[SOLUTION] We propose Z, which does A and B.
[RESULTS] On benchmark C, we achieve D% improvement.
[IMPACT] This enables E.
```

---

## LaTeX Setup

```bash
# Ubuntu/Debian
sudo apt install texlive-full

# macOS
brew install --cask mactex

# Windows
# Install MiKTeX from miktex.org

# Verify
pdflatex --version
bibtex --version
```

### Compile

```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex   # run 3x for refs to resolve

# Or with latexmk (auto-detects what to run)
latexmk -pdf paper.tex
latexmk -pdf -pvc paper.tex  # continuous preview
```

---

## Minimal LaTeX Paper

```latex
\documentclass{article}
\usepackage{amsmath, amssymb, graphicx, booktabs, hyperref}
\usepackage[margin=1in]{geometry}
\usepackage[numbers]{natbib}

\title{Your Paper Title}
\author{Author One \and Author Two}
\date{}

\begin{document}
\maketitle

\begin{abstract}
Your abstract here.
\end{abstract}

\section{Introduction}
\label{sec:intro}

\section{Related Work}
Prior work \citep{vaswani2017attention} showed...

\section{Method}
\label{sec:method}

\section{Experiments}

\begin{table}[t]
\centering
\caption{Main results}
\begin{tabular}{lcc}
\toprule
Method & Metric A & Metric B \\
\midrule
Baseline & 70.1 & 65.3 \\
Ours & \textbf{74.8} & \textbf{70.2} \\
\bottomrule
\end{tabular}
\end{table}

\section{Conclusion}

\bibliography{references}
\bibliographystyle{plainnat}
\end{document}
```

---

## References (.bib file)

```bibtex
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and others},
  journal={NeurIPS},
  year={2017}
}

@inproceedings{devlin2019bert,
  title={{BERT}: Pre-training of deep bidirectional transformers},
  author={Devlin, Jacob and others},
  booktitle={NAACL},
  year={2019}
}
```

Get BibTeX from:
- Google Scholar → Cite → BibTeX
- arXiv → Export BibTeX (bottom of abstract page)
- Semantic Scholar

---

## Literature Review via arXiv

```bash
# Use /arxiv skill to find papers
# Example searches:
# /arxiv search "GRPO reinforcement learning language model"
# /arxiv search "retrieval augmented generation survey"
# /arxiv get 2401.00001
```

---

## Figures

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(4, 3))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label="Our Method")
ax.plot(x, np.cos(x), "--", label="Baseline")
ax.set_xlabel("Epoch")
ax.set_ylabel("Accuracy")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("figure1.pdf", bbox_inches="tight", dpi=300)
```

Include in LaTeX:
```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.8\linewidth]{figure1.pdf}
\caption{Comparison of our method vs baseline.}
\label{fig:main}
\end{figure}
```

---

## Conference Templates

| Conference | Deadline | Template |
|-----------|---------|---------|
| NeurIPS | May | neurips.cc |
| ICLR | Oct | iclr.cc |
| ICML | Jan | icml.cc |
| ACL | Feb | acl-org.github.io |
| AAAI | Aug | aaai.org |

Download official template from the conference website — never use unofficial ones.

---

## Overleaf (Collaborative)

1. Upload all `.tex`, `.bib`, `.pdf` files to Overleaf
2. Share link with co-authors
3. Enable Track Changes for reviews
4. Download final PDF when ready

---

## Common Mistakes

- **Vague claims**: "significantly better" → give exact numbers
- **Missing baselines**: always compare against SOTA
- **No ablation**: show which parts of your method matter
- **Figure too small**: aim for readable at 100% zoom
- **Passive voice overuse**: "we propose" not "it is proposed"
- **Missing limitations**: reviewers will point them out; address proactively

---

## 门控写作工作流 (Gated Writing Pipeline)

吸收自 latex-paper-skills (yunshenwuchuxun)。门控管线确保每一步都有合同约束，不跳步。

### Issues CSV 合同机制

论文写作分解为独立的 issue 单元，每个 issue 有明确的状态和接收标准：

```
issue_id,section,description,owner,status,acceptance_criteria,evidence_required
IS-01,Abstract,"Write abstract per 5-sentence formula",author,pending,"150-250 words, all key numbers present, no adjectives without adjacent numbers",N
IS-02,Introduction-P1,"Grand context paragraph",author,pending,"1-2 sentences, specific application/demand context",N
IS-03,Introduction-P2,"Specific system & promise",author,pending,"2-3 sentences, cite key advances",Y
...
```

**状态流转**：`pending` → `writing` → `draft` → `verify` → `done`

### 门控节点

写作必须在以下门控全部通过后才能开始正文：

```
GATE 1: Plan approved
  ├─ 论文大纲已确认
  ├─ 贡献声明已对齐
  └─ 目标期刊已确定
      ↓
GATE 2: Issues CSV exists
  ├─ 所有写作单元已分解为 issue
  ├─ 每个 issue 有明确的接收标准
  └─ 证据要求已标注
      ↓
GATE 3: Per-issue writing
  ├─ 按 issue 顺序逐条写作
  ├─ 每条完成即更新状态为 draft
  └─ 绝不跳 issue
      ↓
GATE 4: Citation verified
  ├─ 每条 \cite{} 经 WebSearch 确认存在
  ├─ 确认引用内容与声称一致
  └─ 引用年份、作者、期刊正确
      ↓
GATE 5: QA passed
  ├─ 完整性检查（所有 issue done）
  ├─ 一致性检查（前后术语统一）
  ├─ 格式检查（期刊模板要求）
  └─ Overclaiming self-check (battery-writer 10项)
      ↓
GATE 6: Compile
  ├─ pdflatex → bibtex → pdflatex × 2
  └─ 无编译错误
```

### 关键规则

1. **禁止在计划批准前写正文**：`main.tex` 在计划批准和 issues CSV 存在前保持为骨架
2. **Issues CSV 是合同**：按 issue 更新状态；仅在接受标准满足时标记 DONE
3. **绝不伪造引用、结果或意义声明**
4. **实验数据回填模式**：如有 planned/placeholder 标记的实验结果，用 `results-backfill` 模式升级为 verified 声明

---

## 引文验证规则

吸收自 latex-paper-skills。每一条引用在进入 `ref.bib` 前必须验证。

### 验证内容

| 检查项 | 工具 |
|--------|------|
| 论文是否存在 | WebSearch "[第一作者] [年份] [标题关键词]" |
| 出版社/期刊是否正确 | WebSearch + Semantic Scholar |
| 年份是否匹配 | 对比搜索结果 |
| 引用内容是否与声称一致 | WebFetch 摘要/引言页 |
| BibTeX 条目完整性 | 检查 author, title, journal, year 字段非空 |

### 引用质量评分

| 分数 | 标准 |
|------|------|
| A | 同行评议期刊/顶会，引用内容与声称完全一致 |
| B | 同行评议，引用内容基本一致 |
| C | 预印本/非同行评议源 |
| F | 无法验证存在 → 禁止引用 |

### 批量验证流程

1. 提取所有 `\cite{}` key → 映射到 `ref.bib` 条目
2. 逐条运行 WebSearch 验证存在性和内容
3. 标记状态：verified / needs-correction / blocked
4. blocked 的引用：删除或替换为可验证来源
