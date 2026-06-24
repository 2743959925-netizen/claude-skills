---
name: battery-analysis
description: Use when the user asks to analyze battery experimental data: calculate capacities from GCD, perform dQ/dV analysis, fit EIS spectra, compute GITT diffusion coefficients, or measure Coulombic efficiency precisely. Triggers on: 电池数据分析, 电池EIS拟合, 电池GITT, 电池dQdV, 电池库仑效率, battery data analysis, EIS fitting, CE measurement.
---

# battery-analysis

## Overview

Battery-specific experimental data analysis. Methods sourced from actual papers in the user's corpus (Adams 2017 AEM, Fadillah 2025 AM, Oh 2026 Angew). Covers GCD processing, dQ/dV analysis, EIS fitting, GITT, and precise CE measurement.

## GCD Data Processing

### Capacity calculation
- Specific capacity (mAh g⁻¹) = I (mA) × t (h) / m_active (g)
- Areal capacity (mAh cm⁻²) = I (mA) × t (h) / A_electrode (cm²)

### First-cycle Coulombic efficiency (ICE)
- ICE = Q_discharge / Q_charge × 100%
- Anode-free cells: ICE typically 80-95%. Below 80% = severe side reactions.
- Li metal with excess Li: ICE can appear >100% (Li reservoir effect). Note explicitly.

### Voltage plateau identification (NMC811)
- GCD plateau = region where dV/dQ ≈ 0
- NMC811: H1-M ~3.6-3.7 V, M-H2 ~3.75 V, H2-H3 ~4.0 V, H3 final ~4.2 V

### Extract from raw GCD files
| Parameter | Formula | Unit |
|---|---|---|
| Specific discharge capacity | I × t_discharge / m_active | mAh g⁻¹ |
| ICE | Q_discharge / Q_charge × 100% | % |
| Average discharge voltage | ∫V dQ / Q_total | V |
| Energy density (material) | Capacity × avg. voltage | Wh kg⁻¹ |
| Polarization ΔV | V_charge_avg − V_discharge_avg at 50% SOC | mV |

## dQ/dV Analysis

**Purpose**: Deconvolve capacity contributions, track phase transition degradation.

**Processing steps**:
1. Smooth raw GCD data: Savitzky-Golay filter, window 10-20 points, polynomial order 2-3
2. dQ/dV = ΔQ/ΔV per voltage increment (ΔV = 1-5 mV)
3. Plot dQ/dV vs V

**NMC811 peak assignment**:
| Peak | Voltage | Phase transition |
|---|---|---|
| H1 oxidation | ~3.65 V | H1 → M (hexagonal → monoclinic) |
| M oxidation | ~3.75 V | M → H2 |
| H2 oxidation | ~4.0 V | H2 → H3 |
| H3 oxidation | ~4.2 V | Final delithiation |

**Degradation signatures** (from Fadillah 2025 AM):
- Peak intensity decay → active material or Li inventory loss
- Peak shift to higher V (oxidation) → increased polarization. **>50 mV shift over 100 cycles = significant cathode-electrolyte degradation** (Fadillah tracked 0.16 V H1-M shift over 50 cycles)
- Peak broadening → heterogeneous reaction kinetics
- New peaks → new phase or side reactions

## EIS Fitting

### Standard equivalent circuit
```
R_bulk — (R_SEI // CPE_SEI) — (R_ct // CPE_dl) — W_diffusion
```

- R_bulk: bulk electrolyte resistance (high-freq intercept)
- R_SEI: SEI resistance (first semicircle)
- CPE_SEI: constant phase element for SEI
- R_ct: charge transfer resistance (second semicircle)
- CPE_dl: double layer capacitance
- W: Warburg diffusion (low-freq tail)

### Fitting workflow
1. Plot Nyquist (Z' vs -Z'') + Bode (log|Z| vs log f, phase vs log f)
2. Identify number of semicircles → determines circuit topology
3. Initial guesses: Rs ≈ high-freq intercept, R_SEI ≈ first semicircle diameter, R_ct ≈ second semicircle diameter
4. Fit with `scipy.optimize.curve_fit`
5. Report: χ² goodness-of-fit, error % per parameter, fitted circuit diagram

### Battery-specific EIS pitfalls
- **Sulfide SSEs**: grain boundary response can appear as mid-frequency semicircle distinct from SEI
- **Polymer SSEs**: often one merged semicircle (R_SEI + R_ct indistinguishable) + Warburg tail
- **High-frequency inductive loop**: cable/contact artifact, not a physical process — do not fit
- Fitting >3 semicircles → usually overfitting noise

### Python fitting skeleton
```python
import numpy as np
from scipy.optimize import curve_fit

def z_cpe(omega, Q, n):
    return 1 / (Q * (1j * omega)**n)

def eis_model(omega, R_bulk, R_sei, Q_sei, n_sei, R_ct, Q_dl, n_dl, W):
    Z_sei = R_sei * z_cpe(omega, Q_sei, n_sei) / (R_sei + z_cpe(omega, Q_sei, n_sei))
    Z_ct  = R_ct * z_cpe(omega, Q_dl, n_dl) / (R_ct + z_cpe(omega, Q_dl, n_dl))
    Z_w = W / np.sqrt(1j * omega)
    return R_bulk + Z_sei + Z_ct + Z_w

# Stack real and imaginary parts for fitting
def model_stack(omega, *params):
    Z = eis_model(omega, *params)
    return np.concatenate([Z.real, Z.imag])

data_stack = np.concatenate([Z_re_data, Z_im_data])
p0 = [10, 50, 1e-6, 0.8, 100, 1e-5, 0.8, 50]
popt, pcov = curve_fit(model_stack, omega, data_stack, p0=p0)
```

## GITT — Diffusion Coefficient

**Equation** (thin-film approximation):
```
D_Li = (4/πτ) × (m_B × V_M / M_B × S)² × (ΔE_s / ΔE_τ)²
```
Where τ = pulse duration, m_B = active mass, V_M = molar volume, M_B = molar mass, S = contact area, ΔE_s = steady-state voltage change, ΔE_τ = transient voltage change.

**NMC typical D_Li**: 10⁻¹⁰ to 10⁻⁸ cm² s⁻¹. Drops sharply near full delithiation (>4.3V). This is expected, not anomalous.

**Pitfalls**: Thin-film approximation invalid for thick electrodes. Contact area S often unknown — use geometric area as lower bound.

## Coulombic Efficiency — Precise Measurement

Based on Adams et al. (2017, Adv. Energy Mater.). **This is the standardized reference for CE measurement.**

### Phased CE Analysis (Full Life Cycle)

When analyzing CE data across the full battery life, always identify these phases:

| Phase | Signature | What to do |
|---|---|---|
| **Formation** | CE starts low, rises rapidly (e.g., 8%→85% over ~10 cycles) | Exclude from CE_avg. Count cycles to stabilization. Note ICE (initial CE). |
| **Stabilization** | CE continues rising, approaching plateau | Exclude from CE_avg. Short formation implies good electrolyte; long formation implies persistent side reactions. |
| **Stable plateau** | CE fluctuates within ±3% band | Compute CE_avg here. Report: N cycles used, mean ± std, max value. |
| **Anomaly / disruption** | Sudden CE drop (>10%) followed by slow recovery | Flag explicitly. Possible causes: test interruption, temperature change, micro-short circuit, electrolyte degradation event. Decide: exclude or include in avg with note. |
| **Death** | CE collapses, eventually reaching ~0% | Last cycle with CE > 50% marks end of useful life. Death before expected cycle life = rapid failure diagnosis needed. |

### Anomaly Decision Tree

When CE drops suddenly (e.g., 85% → 35%) then slowly recovers:
1. Check voltage profiles around the event — did voltage spike or drop? Short circuit?
2. Check if test was interrupted (power / temperature / rest period)
3. If external cause (equipment): note and exclude from CE_avg, but keep in plot
4. If internal cause (cell failure begins): include in CE_avg, this is real degradation
5. Always annotate the event in the plot — don't silently remove data

### Method 1 — Standard Li||Cu
- Deposit Q_P onto Cu substrate → strip to +1 V cutoff → measure Q_S
- CE = Q_S / Q_P per cycle
- CE_avg = (1/n) Σ(Q_S/Q_P) over n cycles
- First-cycle CE often low (95.7% in Adams). Stabilizes after ~25 cycles.
- **Pitfall**: Substrate effect inflates initial-cycle losses.

### Method 2 — Reservoir (Aurbach)
- Deposit reservoir Q_T (e.g., 4 mAh cm⁻²) onto Cu
- Cycle smaller Q_C (e.g., 0.5 mAh cm⁻²) for n cycles
- Final exhaustive strip to +1 V → measure Q_S
- CE_avg = (n×Q_C + Q_S) / (n×Q_C + Q_T)
- Removes Cu substrate effect after first deposition.

### Method 3 — With Conditioning (Recommended)
- Pre-conditioning cycle: deposit 4 mAh cm⁻², strip to +1 V (eliminates substrate effects)
- Then Method 2: deposit Q_T, cycle Q_C for n cycles, final strip Q_S
- CE_avg = (n×Q_C + Q_S) / (n×Q_C + Q_T), conditioning cycle excluded
- Adams: CE improved from 99.2% (Method 2) to **99.4%** (Method 3) for 4m LiFSI/DME

### Key findings from Adams 2017
- **Higher cycling capacity → faster stabilization → higher average CE**
- At 6 mAh cm⁻²: CE increased from 99.0% to 99.5% vs lower capacity
- **Li||Li symmetric cells are unreliable** for CE: Q_T hard to quantify, short circuits hard to detect, polarization increase ≠ Li depletion only
- Li deposition thickness: 1 mAh cm⁻² = 0.259 mg cm⁻² = 4.82 µm (theoretical, no porosity). Actual thickness ~2× due to voids.

### CE interpretation
| CE value | Implication |
|---|---|
| >99.9% | Excellent — viable for >1000 cycles |
| 99.5-99.9% | Good — viable for 200-500 cycles |
| 99.0-99.5% | Fair — viable for ~100 cycles |
| <99.0% | Poor — rapid capacity fade |

**Data source**: CE data comes in two forms:
1. **Raw Qp/Qs data** → compute CE = Qs/Qp per cycle, then CE_avg per Method 1-3
2. **Pre-computed CE% vs cycle** (e.g., from battery tester export) → skip Q calculations, directly apply phased analysis above

**Plotting**: After analysis, use `battery-figure` template #7 (CE-only variant) for the final figure. Pass phase boundaries and CE_avg to the plotting code.

## Battery Tester Raw Data Parsing

### Supported formats

| Tester | File format | Encoding | Key columns |
|--------|-----------|----------|-------------|
| LAND (蓝电) | `.xls` / `.xlsx` | GBK | 工步, 时间, 电压(V), 电流(mA), 容量(mAh), 比容量(mAh/g) |
| Neware (新威) | `.nda` / `.xlsx` / `.csv` | UTF-8 | Step, Time, Voltage, Current, Capacity, Spec. Capacity |
| Arbin | `.res` / `.csv` | ASCII | Cycle, Step, Time, Voltage, Current, Charge_Cap, Discharge_Cap |
| Bio-Logic | `.mpt` / `.mpr` | ASCII | mode, time/s, Ewe/V, I/mA, Q/mA.h, cycle number |

### LAND xlsx parser

```python
import pandas as pd

def parse_land(filepath):
    """Parse LAND battery tester xlsx output."""
    df = pd.read_excel(filepath, header=None, encoding='gbk')

    # Find header row (LAND uses a specific marker)
    header_row = None
    for i, row in df.iterrows():
        if '工步' in str(row.values) or 'Step' in str(row.values):
            header_row = i
            break

    if header_row is None:
        raise ValueError("Cannot find header row in LAND file")

    # Set header and clean
    df.columns = df.iloc[header_row]
    df = df.iloc[header_row+1:].reset_index(drop=True)

    # Standardize column names
    col_map = {
        '工步': 'step', '时间': 'time', '电压(V)': 'voltage',
        '电压': 'voltage', '电流(mA)': 'current_ma',
        '电流': 'current_ma', '容量(mAh)': 'capacity',
        '比容量(mAh/g)': 'specific_capacity',
        '充放电容量(mAh)': 'capacity',
    }
    df.rename(columns={k: v for k, v in col_map.items() if k in df.columns}, inplace=True)
    return df.astype(float, errors='ignore')
```

### Neware xlsx/csv parser

```python
def parse_neware(filepath):
    """Parse Neware battery tester output."""
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath, encoding='utf-8', skiprows=2)
    else:
        df = pd.read_excel(filepath, skiprows=2)

    col_map = {
        'Cycle': 'cycle', 'Step': 'step', 'Time': 'time',
        'Voltage(V)': 'voltage', 'Current(mA)': 'current_ma',
        'Capacity(mAh)': 'capacity', 'Spec. Cap.(mAh/g)': 'specific_capacity',
        'Energy(Wh)': 'energy',
    }
    df.rename(columns={k: v for k, v in col_map.items() if k in df.columns}, inplace=True)
    return df.astype(float, errors='ignore')
```

### Batch processing — GCD extraction from cycle data

```python
def extract_gcd_cycles(df, charge_steps=[1], discharge_steps=[2]):
    """Extract GCD data into per-cycle charge/discharge DataFrames."""
    cycles = {}
    for cyc in df['cycle'].unique():
        cyc_data = df[df['cycle'] == cyc]
        charge = cyc_data[cyc_data['step'].isin(charge_steps)]
        discharge = cyc_data[cyc_data['step'].isin(discharge_steps)]

        if len(charge) > 0 and len(discharge) > 0:
            cycles[cyc] = {
                'charge_capacity': charge['capacity'].max() - charge['capacity'].min(),
                'discharge_capacity': discharge['capacity'].max() - discharge['capacity'].min(),
                'ce': ((discharge['capacity'].max() - discharge['capacity'].min()) /
                       (charge['capacity'].max() - charge['capacity'].min()) * 100),
                'charge_data': charge,
                'discharge_data': discharge,
            }
    return cycles

# Usage: extract all cycle data, compute CE per cycle
cycles = extract_gcd_cycles(df)
ce_values = {c: d['ce'] for c, d in cycles.items()}
print(f"ICE = {ce_values[1]:.1f}%")
print(f"Avg CE (cycles 5-50) = {np.mean([ce_values[c] for c in range(5, 51)]):.2f}%")
```

### Auto-detect tester type from file

```python
def auto_parse(filepath):
    """Auto-detect battery tester type and parse accordingly."""
    import magic  # python-magic for MIME detection

    ext = filepath.lower().split('.')[-1]
    if ext in ('xls', 'xlsx'):
        # Try LAND first (GBK-encoded, 工步 marker)
        try:
            df = pd.read_excel(filepath, header=None, encoding='gbk')
            if any('工步' in str(v) for v in df.iloc[:5].values.flatten()):
                return parse_land(filepath)
        except: pass
        # Fallback to Neware
        try:
            return parse_neware(filepath)
        except: pass
    elif ext == 'csv':
        # Try Neware then Arbin
        try: return parse_neware(filepath)
        except: pass
    elif ext == 'mpt':
        return parse_biologic(filepath)

    raise ValueError(f"Cannot auto-detect tester type for: {filepath}")
```

## Data Processing Unit Conversions

| Parameter | Common units | Key conversion |
|---|---|---|
| Current density | mA cm⁻², A g⁻¹, C-rate | 1C = theoretical capacity (mAh g⁻¹) in 1h |
| Specific capacity | mAh g⁻¹ | 1 mAh = 3.6 C |
| Energy density | Wh kg⁻¹, Wh L⁻¹ | Wh = V × Ah |
| Power density | W kg⁻¹, W L⁻¹ | W = V × A |
| Ionic conductivity | S cm⁻¹ | σ = d / (R × A) |
| Diffusion coefficient | cm² s⁻¹ | — |
| Li thickness | µm | 1 mAh cm⁻² = 4.82 µm Li (theoretical) |
