---
name: battery-figure
description: Use when the user asks to draw battery research figures: GCD charge/discharge curves, CV, EIS Nyquist, dQ/dV, rate performance, cycling stability+CE, LSV, Ragone plots, symmetric cell voltage-time, mechanism schematics, CCD. Triggers on: 电池画图, 电池图, 电池figure, 电池plot, 电化学图, 充放电曲线, EIS图, CV图.
---

# battery-figure

## Overview

Battery-specific scientific figure creation with 11 pre-built templates. Each template includes: Figure Contract, Python code skeleton, annotation standards, and common pitfalls. Follows nature-figure typography standards adapted for battery conventions. Built on AM/AFM/JACS/Angew-level plotting quality.

## Figure Contract (Mandatory First)

Define these five elements before any plotting code:

1. **Core conclusion**: What does this figure prove? (one sentence)
2. **Evidence chain**: What does each panel prove?
3. **Figure archetype**: Which battery figure type?
4. **Journal export spec**: TIFF 600 DPI, SVG fonttype:none
5. **Color scheme**: One palette through the paper

## 11 Battery Figure Templates

### 1. GCD — Galvanostatic Charge/Discharge

**Key annotations**: First-cycle CE number on plot, voltage plateau position (dashed line), polarization ΔV. Different cycle numbers: different line styles. Multi-sample: label each.

```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(4, 3))
ax.plot(cap_p, vol_p, '--', color='#808080', label='Pristine')
ax.plot(cap_m, vol_m, '-',  color='#2166AC', label='Modified')
ax.set_xlabel('Specific Capacity (mAh g$^{-1}$)', fontsize=7)
ax.set_ylabel('Voltage (V vs. Li$^+$/Li)', fontsize=7)
ax.tick_params(labelsize=7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.annotate('ICE = 93%', xy=(x, y), fontsize=7)
fig.tight_layout(); fig.savefig('gcd.tiff', dpi=600)
```

**Pitfalls**: Don't plot 50 cycles on one panel. Pick 1st, 10th, 50th, 100th. Y-axis consistent across samples.

### 2. dQ/dV — Differential Capacity

**Key annotations**: H1-M-H2-H3 phase transition peak labels, peak shift ΔV in mV. Color gradient: light = early cycle, dark = late.

**Pitfalls**: Smoothing parameter must be consistent. Y-axis range identical for comparison.

### 3. EIS — Nyquist Plot

**Key annotations**: Rs (high-freq intercept), Rct (semicircle diameter), equivalent circuit inset, frequency arrow.

**Critical rule**: `ax.set_aspect('equal')` — XY must be equal scale. Flattened semicircle = rookie mistake.

### 4. CV — Cyclic Voltammetry

**Display**: Multi-cycle overlay (4-5 cycles, light→dark) OR multi-scan-rate + i_p vs v^(1/2) inset.

**Key annotations**: O_x/R_x peak voltages, ΔE_p, i_pa/i_pc, scan rate, scan direction arrow.

**Pitfalls**: Use current density (mA cm⁻²), not raw current. Y-axis symmetric around zero. Distinguish CV (cyclic) from LSV (single sweep).

### 5. LSV — Linear Sweep Voltammetry

**Two modes**: Oxidation sweep (OCP→high V) for anodic limit; Reduction sweep (OCP→low V) for cathodic limit.

**Format**: log|j| vs V, onset by tangent intersection (0.05 mA cm⁻² threshold).

**Pitfalls**: State onset criterion explicitly. Stability window often overstated. SSE vs liquid: different electrode configurations.

### 6. Rate Performance

**Format**: Stepped X-axis, C-rate segments. Two modes: X=cycle number (default) or X=C-rate log scale.

**Key annotations**: Average capacity per rate, recovery %, CE across rates, 1C definition in caption.

**Pitfalls**: Loading (mg cm⁻²) MUST be stated. Use cycle 3-5 values, not cycle 1. Loading and 1C definition must match when comparing.

### 7. Cycling Stability + Coulombic Efficiency

**Two variants**:

**7a. Full dual-Y (capacity + CE)** — when you have both capacity and CE data:
- Left Y: discharge capacity (mAh g⁻¹). Right Y: CE (%).
- CE Y range: **95-100%** (or 90-100% if needed). Never 0-100% — it compresses CE differences to invisibility.

**7b. CE-only** — when you only have CE vs cycle number:
- Single Y-axis: CE (%). Range decision:
  - If CE stays >85% throughout: zoom to 80-100% or 90-100%
  - If CE varies widely (formation + stable + death): use full range but label phases clearly
- Add phase annotations: formation zone (shaded grey), stable zone (shaded green + avg CE line in red `#B2182B`), death zone (shaded red)

**Key annotations**: Initial/final CE (or capacity if dual-Y), CE_avg over stable cycles, cycle count of stable region. Per Adams 2017: always state which cycles were used for averaging and which were excluded.

**Phase annotation pattern** (for full life-cycle CE data):
```python
# Formation
ax.axvspan(1, formation_end, alpha=0.07, color='#808080')
# Stable — green shade + red avg line
ax.axvspan(stable_start, stable_end, alpha=0.05, color='#2E8B57')
ax.axhline(y=ce_avg, xmin=stable_start/total, xmax=stable_end/total,
           color='#B2182B', linewidth=1.2, linestyle='--')
# Death
ax.axvspan(death_start, death_end, alpha=0.09, color='#B2182B')
```

**Pitfalls**: Don't use 95-100% range when data includes formation/death — the plot becomes unreadable. Always state loading (mg cm⁻²) and current density (C-rate or mA g⁻¹) in caption.

### 8. Symmetric Cell Voltage-Time

**Format**: Galvanostatic square wave, voltage vs time.

**Key annotations**: Current density (mA cm⁻²), areal capacity (mAh cm⁻²), overpotential evolution, short circuit time, local zoom insets.

### 9. Ragone Plot

**Format**: Log-log. X: power density (W kg⁻¹), Y: energy density (Wh kg⁻¹).

**Key annotations**: This work (large star), literature (grey circles), application regions, level: cell/pack/material.

**Pitfalls**: Always state the level. Don't mix levels on one plot.

### 10. Mechanism / Structure Schematic

**Format**: Labeled components, process arrows, proportional relationships. Information density > decoration.

**Tool**: PPT shapes, matplotlib.patches, or python-pptx native shapes.

### 11. CCD — Critical Current Density

**Format**: Stepped current density vs time, with voltage profile.

**Key annotations**: CCD value (mA cm⁻²) at voltage drop, areal capacity per step, polarization trend before short.

## Battery Color Conventions

| Use | Color | Hex |
|---|---|---|
| Control / pristine | Grey | `#808080` |
| Experimental / this work | Blue `#2166AC` or Red `#B2182B` | Pick one through paper |
| Charge | Red | `#B2182B` |
| Discharge | Blue | `#2166AC` |
| Oxidation peak | Solid line | Same as charge |
| Reduction peak | Dashed line | Same as discharge |
| CE right axis | Light green or light blue | Distinct from capacity |
| Literature points | Grey circles | `#808080` |

## Typography and Export

- Font: Arial or Helvetica
- Axis labels: 7 pt, panel markers: 9 pt bold, top-left
- Export: TIFF 600 DPI; SVG `svg.fonttype: 'none'`; PDF `pdf.fonttype: 42`
- No top/right spines
- Scale bars mandatory on SEM/TEM
- Error bars: ≥3 experiments, labeled ±SD
- One hero panel dominates, avoid equal 2×2 grids

## Quick Self-Check

- [ ] Active material loading (mg cm⁻²) stated
- [ ] Current density labeled (mA g⁻¹, mA cm⁻², or C-rate with 1C definition)
- [ ] SEM/TEM: scale bar visible
- [ ] EIS: X/Y equal scale
- [ ] Cycling+CE: CE Y-axis 95-100%
- [ ] Error bars with n stated
- [ ] Colorblind-friendly (no red/green-only distinction)
- [ ] No top/right spines
- [ ] Font ≥ 7 pt at export
