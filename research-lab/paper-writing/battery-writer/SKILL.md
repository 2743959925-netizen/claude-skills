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
