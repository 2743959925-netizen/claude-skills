---
name: battery-writer
description: Use when the user asks to write or polish battery paper sections (Abstract, Introduction, Results & Discussion), needs battery-specific terminology guidance, or wants to check for overclaiming before submission. Triggers on: 电池论文写作, 电池润色, 电池写作, 电池Abstract, 电池Introduction, battery writing, battery polishing.
---

# battery-writer

## Overview

Battery paper writing templates and self-checks. Built from the user's actual paper corpus (Fadillah 2025 AM, Li 2025 Angew, Oh 2026 Angew). Covers Abstract, Introduction, Results structure, battery terminology, and an overclaiming checklist.

## Abstract Template

Battery papers in AM/AFM/JACS/Angew follow this pattern:

```
[1-2 sentences: Big picture / motivation]
[1 sentence: Specific problem / bottleneck — be mechanistic, not vague]
[1 sentence: This work's approach — "Here, we report/present/demonstrate..."]
[2-3 sentences: Key quantitative results with numbers, not adjectives]
[1 sentence: Significance / broader impact]
```

**Example pattern** (from Fadillah 2025 AM):
> Solid-state electrolytes enable next-generation batteries due to their intrinsic safety. However, sulfide-based systems suffer from limited electrochemical stability and high moisture sensitivity. Here, we report the molecular surface engineering of Li argyrodite SSE using [material] in a single-step coating strategy. The coated electrolyte maintains ionic conductivity (>X mS cm⁻¹) and retains >Y% after Z h dry room exposure. In full cells, it delivers X mAh g⁻¹ at Y C with >Z% CE. These results demonstrate [material] as a scalable interfacial modifier for sulfide-based solid-state batteries.

**Do NOT**:
- Start with "Lithium-ion batteries have attracted extensive attention..." (overused)
- Use "excellent", "remarkable", "outstanding" without adjacent numbers
- Claim "superior performance" without stating what it's superior to and by how much

## Introduction Logic Chain (5 paragraphs)

**P1. Grand context (1-2 sentences)**:
"Electrification of transport / Grid storage demands batteries with higher energy density."

**P2. Specific system & its promise (2-3 sentences)**:
"All-solid-state batteries using sulfide electrolytes offer [specific advantage]."
Cite key advances (argyrodite conductivity records, etc.)

**P3. The bottleneck — what's actually stopping it (3-4 sentences)**:
"However, [specific problem] limits practical application because [mechanism — e.g., P-S bond instability leads to hydrolysis/oxidation]."
This is the most important paragraph. Be specific about mechanism, not vague about "challenges remain."

**P4. Existing solutions and their limitations (2-3 sentences)**:
"Approaches such as [A], [B], and [C] have been explored, but [specific limitation — cracks, sacrifices conductivity, only addresses one interface]."
Never say "no solution exists." Say "existing strategies face trade-offs between X and Y."

**P5. This work's approach + preview (2-3 sentences)**:
"Here, we [design/synthesize/report] [material/system] that [mechanism of action]. This strategy achieves [key metric 1] and [key metric 2], demonstrating [broader significance]."

## Results & Discussion Structure

**Pattern A — Characterization cascade** (materials papers):
1. Synthesis & structural characterization (XRD, Raman, SEM/TEM)
2. Surface/interfacial chemistry (XPS, FTIR, DFT)
3. Electrochemical stability (EIS, LSV, CCD)
4. Interfacial performance (symmetric cell, XPS post-mortem)
5. Full-cell performance (rate, cycling, dQ/dV)
6. Post-cycling analysis (SEM, XPS, EIS of cycled cells)

**Pattern B — Function-property cascade** (mechanism papers):
1. Design principle
2. Proof of concept (simplified system)
3. In-depth mechanism study
4. Translation to practical system
5. Generality demonstration

**Writing rules per subsection**:
- Lead with 1 sentence: what was done and why
- Data → interpret → connect to next experiment
- Each paragraph ends with a transition
- Never list characterization — explain WHY this characterization was chosen

## Battery Terminology

Keep English in manuscript text. Chinese gloss for oral use only.

| English | Chinese gloss | Usage rule |
|---|---|---|
| SEI (solid electrolyte interphase) | 固体电解质界面相 | Always SEI in text |
| CE (Coulombic efficiency) | 库仑效率 | CE sufficient |
| CCD (critical current density) | 临界电流密度 | CCD |
| GCD (galvanostatic charge/discharge) | 恒流充放电 | GCD |
| CV (cyclic voltammetry) | 循环伏安 | CV |
| EIS (electrochemical impedance spectroscopy) | 电化学阻抗谱 | EIS |
| ASSB (all-solid-state battery) | 全固态电池 | ASSB |
| SSE (solid-state electrolyte) | 固态电解质 | SSE |
| AFLMB (anode-free Li metal battery) | 无负极锂电池 | AFLMB |
| N/P ratio | N/P比 | Keep English |
| Areal capacity | 面容 | mAh cm⁻² |
| Mass loading | 活性物质载量 | mg cm⁻² |
| Rate capability | 倍率性能 | — |

## Figure Caption Writing

Battery figure captions follow a strict pattern. Each caption should answer: what was measured, under what conditions, and what key result emerged.

**Template**:
```
Figure X. [1-sentence result statement]. a) [Panel a description + key observation].
b) [Panel b description + key quantitative result]. c) [Panel c description + interpretation].
```

**Example** (from Fadillah 2025 AM):
> Figure 2. a) Li-ion conductivity of pristine and modified LPSClBr before and after dry room exposure. b) Critical current density of Li symmetrical cells with a constant capacity of 1.0 mAh cm⁻². c) Symmetrical cell performance at 1.0 mA cm⁻², 1.0 mAh cm⁻².

**Rules**:
- State the measurement condition in the caption (current density, temperature, areal capacity, voltage range)
- If a panel shows a comparison, state what was compared and which is better
- Never use "as shown in Figure X" in the main text — just state the result and cite the figure
- Abbreviations defined at first use in the paper, not re-defined per caption

## Overclaiming Self-Check (10 items)

Before finalizing any battery manuscript:

1. **"High capacity"** → Is mass loading stated? Current density stated?
2. **"Stable cycling"** → How many cycles? What rate? What retention %?
3. **"High CE"** → Which method? (Reservoir? Aurbach? Single cycle?) Per Adams 2017, method matters.
4. **"Suppresses dendrites"** → Direct SEM evidence at multiple locations? Or inferred from voltage?
5. **"Practical conditions"** → Temperature? Stack pressure? Areal capacity >3 mAh cm⁻²? Lean electrolyte?
6. **"Outperforms literature"** → Specific comparison table with identical test conditions?
7. **Electrochemical stability window** → Onset criterion stated? (current density threshold)
8. **Energy density claim** → Cell-level or material-level? All components included?
9. **"Air-stable"** → What RH? What exposure time? What metric (conductivity? H₂S generation?)?
10. **Comparison to literature** → Same loading? Same voltage range? Same electrolyte amount?

## Reviewer Response Template

When addressing reviewer comments, follow this structured pattern:

### Response Format

```
Reviewer #X, Comment #Y:

[Reviewer's original comment in italics]

Response:
We thank the Reviewer for this insightful comment. [1-sentence acknowledgment]

[Action taken]:
- [Specific change 1 — cite new figure/table number]
- [Specific change 2 — cite line number in revised manuscript]

[Evidence]:
[New data, new analysis, or reasoning — with specific numerical values]
```

### Battery-Specific Response Patterns

| Reviewer says | Your response should include |
|--------------|------------------------------|
| "Is the CE measurement reliable?" | State measurement method (Adams Method 1/2/3), n cells tested, error bars, conditions |
| "The areal capacity is too low for practical relevance" | If loading < 3 mAh/cm²: acknowledge limitation, add high-loading data if available, state as "proof of concept" |
| "What is the electrolyte amount?" | State E/S ratio or electrolyte volume. If unknown, admit and note as limitation |
| "The comparison to literature is unfair" | Add comparison table with matched conditions (loading, voltage, temp, pressure) |
| "Missing control experiment" | Add the control. If impossible (time/equipment), explain why and note as limitation |
| "The mechanism is speculative" | Tone down claims: "suggests" → "indicates" ; add DFT/MD if possible ; clarify what's proven vs hypothesized |
| "XPS peaks are misinterpreted" | Re-check binding energy assignments against NIST XPS database or standard reference |
| "No error bars on electrochemical data" | Re-run statistics on ≥3 cells, add error bars to all key figures |

### Cover Letter Template

```
Dear Editor,

We submit our manuscript titled "[TITLE]" for consideration in [JOURNAL].

[P1: Why this topic matters now — 2 sentences]
Solid-state batteries using sulfide electrolytes have advanced rapidly, yet [specific bottleneck] remains unresolved because [mechanism].

[P2: What we did — 2 sentences]
Here, we report [approach] that [mechanism of action]. This strategy achieves [key metric 1] and [key metric 2] under [relevant conditions].

[P3: Why this journal — 1 sentence]
This work aligns with [JOURNAL]'s focus on [journal's scope area] and will interest readers in [specific communities].

[P4: Statements — bullet list]
- All authors have approved the manuscript
- This work is not under consideration elsewhere
- The authors declare no competing interests
- [Data availability statement]

Sincerely,
[Corresponding author]
```

## Nature Portfolio 投稿预检

吸收自 Nature-Paper-Skills (Boom5426)。投稿到 Nature 系列期刊前必查。

### 选刊决策树

按以下顺序决策：

1. **选读者和期刊家族**：
   - 论文的核心概念突破是否对专业外读者有广泛吸引力？→ **Nature**
   - 核心贡献是方法、检测平台、计算方法的使能能力？→ **Nature Methods**
   - 论文价值不仅是技术新颖性，更是生物技术/医学意义、转化潜力、工程深度？→ **Nature Biotechnology**

2. **选文章类型**：
   - `Article`：完整研究故事，多个相互关联的主张和实质性证据链
   - `Resource`：社区有用的数据集、平台、图谱、数据库——持久价值在于广泛复用
   - `Analysis`：综合性/对比性分析研究——核心贡献是分析洞察而非新实验方法
   - 短格式方法/报告：仅当故事更紧凑、自包含且期刊明确支持该格式时

3. **检查证据包是否匹配期刊承诺**：
   - Nature Methods fit check：明确的技术进步 / 对可用方法的验证和基准测试 / 足够的细节或协议访问以支持可重复性 / 展示通用实用性（不只是单一场景）/ 明确的生物学或生物医学应用
   - Nature Biotechnology fit check：对生物技术或医学的意义 / 为什么足够充实适合完整文章而非短报告 / 是否是真正的 Article 还是应该按 Resource 来写

4. **最后才优化框架和文笔**

### 投稿前预检清单

提交前检查以下项目：

1. **报告标准**：
   - 确认是否需要 Reporting Summary
   - 确保正文和 SI 已包含该 summary 所需的所有信息
2. **数据和代码可用性**：
   - 仓库名称、accession IDs、下载链接、访问限制已准备就绪
   - 不要等到接收后才搞清楚 data/code statement
3. **协议和可重复性**：
   - 对于方法论文，确保可用的协议路径明确：SI/协议仓库/公共方法记录
4. **图像完整性和原始数据**：
   - 确保可提供未处理的源图像和原始 blot/gel 材料
   - 移除任何可能被视为选择性增强的制图习惯
5. **AI 和归属**：
   - 披露生成式 AI 工具的使用（如期刊要求）
   - 不要把 AI 生成的图像或未声明的 AI 写作内容当作默认安全
6. **相关稿件和预印本披露**：
   - 披露预印本、重叠投稿、相关稿件和会议论文集历史

## 系统化审稿流程

吸收自 Nature-Paper-Skills 的 paper-reviewer。

### 审稿三阶段

**Stage 1：初始评估**
- 核心研究问题/假设是什么？
- 主要发现和结论是什么？
- 工作是否科学可靠且有意义？
- 是否适合目标期刊？
- 有无立即排除出版的重大缺陷？

输出：2-3句话的简要总结，捕捉手稿的本质和初步印象。

**Stage 2：逐节详细审查**

| 章节 | 检查要点 |
|------|---------|
| **标题和摘要** | 准确性？是否准确反映研究内容和结论？明确？标题是否具体、准确、信息丰富？完整性？ |
| **引言** | 背景充分且最新？研究问题是否有明确动机和论证？原创性和意义是否清晰？相关先前研究是否适当引用？ |
| **方法** | 可重复性：另一研究者能否根据描述复现该研究？方法是否适合回答研究问题？试剂、设备、参数是否充分描述？伦理审批和数据处理是否记录？ |
| **统计** | 统计方法是否适当、清晰描述和合理？样本量和效能计算？随机化和盲法？纳入/排除标准？统计检验和多重比较校正？ |
| **结果** | 展示是否逻辑清晰？图表是否适当、清楚、标签正确？统计结果是否正确报告（效应量、置信区间、p值）？是否客观呈现无过度解释？是否包括阴性结果？ |
| **讨论** | 结论是否有数据支撑？局限性是否承认和讨论？发现是否放在现有文献中适当定位？推测是否与数据支持的结论明确区分？ |
| **参考文献** | 关键相关论文是否引用？最新重要研究是否包含？对立观点是否适当引用？引用是否准确？有无过度自引？ |

**Stage 3：综合评估**
- 综合所有问题，形成整体判断
- 区分致命缺陷和可修问题
- 提供建设性反馈，而不仅仅是指出问题

### 常见问题识别

| 问题类型 | 具体表现 |
|---------|---------|
| **选择性报告** | 只展示有利结果，隐藏阴性或矛盾数据 |
| **统计不当** | 不合适的检验方法、缺少多重比较校正 |
| **缺少误差棒** | 无标准差/标准误/置信区间 |
| **过度拟合** | 训练集和测试集不独立 |
| **批次效应** | 未控制的批次/混杂变量 |
| **缺少对照** | 无对照组或验证实验 |
| **因果声称无因果证据** | 从相关性推断因果关系 |
| **机制声称无机制证据** | 声称分子/原子机制但没有直接证据 |
