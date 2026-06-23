---
name: battery-paper2ppt
description: Use when the user asks to make a group-meeting PPT from a battery paper (solid-state batteries, Li metal batteries, anode-free batteries, sulfide/polymer electrolytes). Triggers on: 电池PPT, 电池组会, 电池论文做PPT, 电池journal club, battery PPT, battery presentation.
---

# battery-paper2ppt

## Overview

Transform battery research papers into Chinese group-meeting PPT presentations. Uses battery-specific paper classification (6 types) instead of generic scientific categories. Automatically recognizes battery-unique figures (GCD, CV, EIS, dQ/dV, rate, cycling+CE, CCD, symmetric cell, SEM, XPS). Built on AM/AFM/JACS/Angew-level paper conventions.

## Paper Classification

Classify the paper into one of six battery-specific types. Each maps to a narrative arc and slide structure.

| Type | Narrative Arc | Key Evidence Slides |
|---|---|---|
| A. Interface engineering / protective layer | Problem interface → material design → interfacial chemistry (Raman/FTIR/XPS/DFT) → electrochemical benefit (CCD/EIS/symmetric cell) → full-cell validation → mechanism summary | Coating schematic, spectroscopy comparison, CCD, symmetric cell voltage, cross-section SEM, cycling |
| B. Electrolyte modification | Intrinsic bottleneck (conductivity/window/interface) → design & synthesis → ion transport (EIS/GITT/LSV) → interface stability → full-cell performance | Molecular structure, Arrhenius plot, LSV, EIS Nyquist, symmetric cell, rate+cycling |
| C. Current collector / substrate design | Cu dead weight or nucleation barrier → lightweight/functional design → Li deposition morphology (SEM) → CE → energy density gain | Structure schematic, areal density comparison, SEM top+side view, CE comparison, energy density calc |
| D. Li deposition / nucleation control | Nucleation theory → substrate design → morphology evolution (SEM/Cryo-TEM) → CE + cycling → dead Li quantification | Nucleation overpotential, morphology evolution, CE boxplot, XPS depth profile, cycling comparison |
| E. Methodology / characterization standard | Existing inconsistency → proposed standard method → validation → broader significance | Method schematic, result comparison across methods, error analysis |
| F. Review / perspective | Field landscape → classification framework → per-theme deep dive → open questions → outlook | Field overview map, classification diagram, key data comparison table |

## Narrative Logic

Five arcs, selected by paper type:

- **claim-first**: One strong central claim. For papers with a single bold thesis.
- **question-to-evidence**: Mechanism and discovery. Phenomenon → unknown → hypothesis → design → evidence chain → model.
- **problem-to-solution**: Methods, tools, engineering. Bottleneck → proposed approach → workflow → validation → comparison.
- **workflow-to-validation**: Datasets, atlases, benchmarks. Why needed → design → pipeline → validation → insights.
- **evidence-map**: Reviews and perspectives. Why now → framework → themes → synthesis → future.

## Auto-Recognition of Battery Figures

When reading a paper PDF, recognize and interpret:

| Figure Type | Visual Signature | What to Extract |
|---|---|---|
| GCD | X: specific capacity / Y: voltage, plateaus | First-cycle CE, capacity, polarization, plateau position |
| CV | Enclosed curves, symmetric redox peaks | Peak positions, ΔE_p, i_pa/i_pc ratio, scan rate |
| EIS Nyquist | X: Z' / Y: -Z'', semicircle + line | Rs (intercept), Rct (semicircle), Warburg slope |
| dQ/dV | Differential peaks, H1-M-H2-H3 | Peak drift (mV), peak intensity decay |
| Rate performance | Stepped X-axis, C-rate segments | Capacity per rate, recovery rate |
| Cycling + CE | Dual Y: left capacity / right CE (%) | Capacity retention %, average CE |
| CCD | Stepped current, voltage profile | Short-circuit current density |
| Symmetric cell | Galvanostatic square wave | Overpotential, time to short, ASR |
| Cross-section SEM | Layered structure | Layer thickness, interface quality |
| XPS depth profile | Multi-element depth distribution | Interfacial composition gradient |

## Default PPT Structure

For interface engineering papers (Type A), 13 slides:

1. Title slide (paper title + journal + year + DOI)
2. Research background: why this matters
3. Knowledge gap: limitations of existing approaches
4. This work's strategy: material design & synthesis route
5. Interfacial chemistry evidence 1: spectroscopy
6. Interfacial chemistry evidence 2: XPS/DFT
7. Electrochemical stability: CCD / symmetric cell
8. Humidity / air stability (if applicable)
9. Full-cell performance: rate + cycling
10. Mechanism summary model
11. Innovation vs. literature comparison
12. Limitations & outlook
13. Summary: one core takeaway

Adapt for other paper types. Reviews expand evidence-map slides. Methodology papers expand validation slides.

## Battery PPT Style Rules

- Data figures: keep English axis labels, add Chinese title
- Every data slide: mark 2-3 key numerical values (e.g., "CE: 89% → 99.7%")
- Literature comparison: state specific numerical differences, never "outperforms prior work"
- Mechanism diagrams: prefer original figure crops over redrawing
- Chinese narration, preserve English abbreviations (CE, SEI, CCD, SSE, etc.)
- One claim per slide, hero figure dominates
- Slide titles: conclusion-style. "Li-OPA 涂层使 CCD 提升 3 倍至 2.4 mA cm⁻²" not "CCD 测试结果"

**SI figures are not optional**. Battery papers routinely bury the most convincing validation in Supporting Information — post-cycling SEM, XPS survey spectra, EIS fitting details, comparison to more baselines. Always scan SI for: (a) post-mortem analysis (SEM/XRD of cycled electrodes), (b) additional control experiments, (c) performance under varied conditions (temperature, pressure, loading), (d) reproducibility data across multiple cells.

**Methods slide**: For your own group's paper, include 1 methods slide with key experimental parameters that affect reproducibility — electrolyte amount, stack pressure, active material loading, voltage window, formation protocol. This is what other group members need to replicate your work. For other groups' papers, note missing parameters as discussion points.
