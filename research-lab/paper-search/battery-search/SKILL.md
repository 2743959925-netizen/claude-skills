---
name: battery-search
description: Use when the user asks to search for battery literature, track new papers in a research direction, find what papers cite a given paper, or identify battery review articles. Triggers on: 电池文献, 电池检索, 电池搜论文, 电池新论文, 电池综述, battery literature search, battery paper tracking.
---

# battery-search

## Overview

Battery literature search strategy. Includes journal hierarchy, keyword search templates organized by the user's three research directions, literature tracking methods, and paper reading priority order.

## Battery Journal Hierarchy

### Top-tier
| Journal | Battery relevance |
|---|---|
| Nature Energy | Groundbreaking battery tech, policy |
| Nature Materials | Fundamental materials for batteries |
| Nature Nanotechnology | Nanoscale battery materials |
| Science | Fundamental breakthroughs |
| Joule | Battery technology, energy storage |
| Nature Communications | High-quality battery research |
| Science Advances | Broad battery research |

### Core battery journals
| Journal | Typical content |
|---|---|
| Advanced Materials (AM) | Materials innovation for batteries |
| Advanced Functional Materials (AFM) | Functional battery materials |
| Advanced Energy Materials (AEM) | Energy storage devices & systems |
| Angewandte Chemie Int. Ed. | Molecular/supramolecular battery approaches |
| JACS | Fundamental chemistry for batteries |
| ACS Energy Letters | Rapid-communication battery research |
| Energy & Environmental Science (EES) | High-impact energy research |
| Energy Storage Materials | Battery-focused: Li/Na/K/Zn, SSE |
| ACS Nano | Nanostructured battery materials |
| Nano Letters | Nanoscale battery science |
| Chemistry of Materials | Materials chemistry for batteries |

### Applications & electrochemistry
| Journal | Typical content |
|---|---|
| Chemical Engineering Journal (CEJ) | Applied battery engineering |
| Journal of Power Sources | Applied battery research |
| Electrochimica Acta | Fundamental electrochemistry |
| Journal of the Electrochemical Society | Electrochemistry fundamentals |
| ACS Applied Materials & Interfaces | Applied battery materials |

## Keyword Search Templates

### Direction 1: Anode-free lithium metal batteries
```
("anode-free" OR "anodeless" OR "zero-excess lithium" OR "zero anode")
AND ("lithium metal" OR "li metal")
AND ("deposition" OR "plating" OR "nucleation" OR "current collector" OR "host")
```

### Direction 2: Sulfide solid-state electrolytes
```
("sulfide" OR "argyrodite" OR "Li6PS5" OR "LPSCl" OR "thio-phosphate" OR "thiophosphate")
AND ("solid-state electrolyte" OR "solid electrolyte" OR "SSE")
AND ("ionic conductivity" OR "stability" OR "interface" OR "coating" OR "moisture")
```

### Direction 3: Polymer solid-state electrolytes
```
("PEO" OR "polyethylene oxide" OR "polymer electrolyte" OR "composite electrolyte")
AND ("solid-state" OR "all-solid-state")
AND ("ionic conductivity" OR "interface" OR "dendrite" OR "mechanical")
```

### Cross-cutting topics
```
# SEI / interphase
("SEI" OR "interphase" OR "interfacial") AND ("lithium metal" OR "solid-state")

# Dendrite suppression
("lithium dendrite" OR "filament" OR "short circuit") AND ("suppression" OR "inhibition")

# CE measurement
("coulombic efficiency" OR "CE") AND ("measurement" OR "accurate" OR "standardized")
```

## Literature Tracking

### "What's new in this direction?"
1. Google Scholar: keyword set, filtered to current year
2. Check latest issues of core journals (AM, AEM, ACS Energy Lett, Energy Storage Mater, Angew)
3. Report: title, journal, date, core claim (1 line), innovative angle

### "Who cited this paper?"
- Google Scholar "cited by" or Semantic Scholar API
- Group citing papers: supports / contradicts / extends to new system / incremental

### "Reviews on this topic?"
- Search: "(topic) AND (review OR perspective OR roadmap OR outlook)"
- Filter to last 3 years, high-impact journals
- Summarize each review's framework and angle

## Paper Reading Priority

When encountering a new battery paper, extract in this order:

1. **Title + Journal + Year** → sets quality expectations
2. **Abstract** → core claim and key numbers
3. **Figure 1** (usually schematic) → what did they design
4. **Cycling + CE figure** → the "lifeline": what performance level
5. **TOC / graphical abstract** → one-picture summary
6. **Comparison table** → how it stacks against literature
7. **Methods section** → electrolyte amount? pressure? loading? (where the devil hides)
8. **Supporting Information figures** → real validation often buried here

Then decide: deep-read, skim, or file for later.

## Comparison Data Hunting

When preparing a manuscript and you need benchmark data to compare against:

**Step 1** — Define comparison criteria that must match:
- Same active material (e.g., NMC811, not just "NMC")
- Same electrolyte type (e.g., sulfide SSE, not "solid-state")
- Same areal capacity range (e.g., 2-4 mAh cm⁻²)
- Same voltage range
- Same temperature and pressure

**Step 2** — Search specifically for comparison tables:
```
(topic) AND ("Table" OR "comparison" OR "compared with" OR "benchmark")
```
In Google Scholar, filter to last 2-3 years, top journals.

**Step 3** — Extract comparison data to a structured table:
| Ref | Material | Loading | CE | Cycles | Retention | Test condition |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

**Step 4** — Flag unfair comparisons in your own paper BEFORE the reviewer does:
- If your loading is 1 mg cm⁻² and the benchmark is 5 mg cm⁻², state this limitation
- If your test temperature is 60°C and the benchmark is 25°C, state this
- Never cherry-pick the worst literature value — pick the best to compare against

**Common comparison traps in battery papers**:
- Comparing your 0.1C cycling against someone's 1C cycling without noting the rate difference
- Comparing against a paper from 2015 when the field has improved significantly since
- Using "commercial electrolyte" as baseline without specifying composition
