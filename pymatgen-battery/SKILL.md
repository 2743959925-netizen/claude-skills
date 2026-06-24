---
name: pymatgen-battery
description: "电池材料计算——基于pymatgen的晶体结构分析、相图计算、Materials Project查询、格式转换。覆盖硫化物电解质(LGPS/argyrodite)、正极材料(NCM/LFP)、界面结构、离子扩散、能带/DOS分析。触发: 晶体结构/CIF/POSCAR/相图/Materials Project/能带/态密度/硫化物电解质结构/扩散通道。"
metadata:
  version: "1.0.0"
  source: adapted from K-Dense-AI/scientific-agent-skills/pymatgen
  requires: [pymatgen, mp-api]
  optional_env: ["MP_API_KEY"]
---

# 🔋 pymatgen-battery - 电池材料计算

基于 pymatgen (Python Materials Genomics) 的电池材料计算分析。从晶体结构到电化学性质。

## 适用场景

- 分析硫化物固态电解质（argyrodite Li₆PS₅Cl、LGPS 等）晶体结构
- 计算正极材料（NCM、LFP、LiCoO₂）的锂离子扩散通道
- 查询 Materials Project 数据库获取已有计算数据
- 计算相图、热力学稳定性、电化学稳定窗口
- 分析电子结构（能带、态密度 DOS）
- 构建表面/界面模型
- 格式转换：CIF ↔ POSCAR ↔ XYZ ↔ VASP

## 快速安装

```bash
# 核心库
pip install pymatgen

# Materials Project API（查询数据库用）
pip install mp-api

# 可选扩展
pip install pymatgen[analysis]  # 分析工具
pip install pymatgen[vis]       # 可视化
```

### Materials Project API Key

```bash
export MP_API_KEY="your_key_here"
# 或从 https://materialsproject.org/api 获取
```

> 不设置 API key 也可做本地结构分析，只是不能查询 MP 数据库。

## 常见用法

### 1. 读取/分析晶体结构

```python
from pymatgen.core import Structure

# 读取 CIF 或 POSCAR
struct = Structure.from_file("argyrodite.cif")

# 基本信息
print(f"化学式: {struct.composition.reduced_formula}")
print(f"空间群: {struct.get_space_group_info()}")
print(f"密度: {struct.density:.2f} g/cm³")
print(f"晶格参数: a={struct.lattice.a:.3f}, b={struct.lattice.b:.3f}, c={struct.lattice.c:.3f}")
```

### 2. 硫化物电解质结构分析

```python
from pymatgen.core import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer

# 分析 Li⁺ 扩散通道
# 读取 argyrodite Li₆PS₅Cl 结构
struct = Structure.from_file("Li6PS5Cl.cif")

# 查看 Li 位点占位
li_sites = [site for site in struct if site.species_string == "Li"]
print(f"Li 位点数: {len(li_sites)}")

# 计算 Li-Li 距离分布（评估扩散通道）
from pymatgen.analysis.local_env import CrystalNN
cnn = CrystalNN()
for i, site in enumerate(li_sites[:5]):
    neighbors = cnn.get_nn_info(struct, i)
    print(f"Li[{i}]: {len(neighbors)} 近邻")
```

### 3. 查询 Materials Project

```python
from mp_api.client import MPRester

with MPRester() as mpr:
    # 搜硫化物电解质
    docs = mpr.summary.search(
        chemsys="Li-P-S-Cl",
        fields=["material_id", "formula_pretty", "band_gap", "formation_energy_per_atom"]
    )
    for doc in docs[:5]:
        print(f"{doc.material_id}: {doc.formula_pretty}, gap={doc.band_gap:.2f} eV")

    # 按 material_id 获取结构
    struct = mpr.get_structure_by_material_id("mp-xxx")
```

### 4. 相图计算

```python
from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter

with MPRester() as mpr:
    # 获取 Li-P-S 三元系所有相
    entries = mpr.get_entries_in_chemsys(["Li", "P", "S"])
    pd = PhaseDiagram(entries)

    # 计算 Li₆PS₅Cl 的分解能（energy above hull）
    for entry in entries:
        if "Li6PS5Cl" in entry.composition.reduced_formula:
            decomp = pd.get_decomp_and_e_above_hull(entry)
            print(f"分解能: {decomp[1]:.3f} eV/atom")
```

### 5. 格式转换

```python
from pymatgen.core import Structure

# CIF → POSCAR
struct = Structure.from_file("battery.cif")
struct.to(filename="battery.vasp", fmt="poscar")

# POSCAR → CIF
struct2 = Structure.from_file("POSCAR")
struct2.to(filename="output.cif", fmt="cif")

# 批量转换
import glob
for cif_file in glob.glob("*.cif"):
    struct = Structure.from_file(cif_file)
    struct.to(filename=cif_file.replace(".cif", ".vasp"), fmt="poscar")
```

### 6. 能带和态密度

```python
from pymatgen.electronic_structure.plotter import DosPlotter, BSPlotter

# 读取 VASP 计算输出
from pymatgen.io.vasp import Vasprun
vasprun = Vasprun("vasprun.xml")
dos = vasprun.complete_dos
band = vasprun.get_band_structure()

# 画 DOS
plotter = DosPlotter()
plotter.add_dos("Total", dos)
plotter.save("dos.png")

# 画能带
bs_plotter = BSPlotter(bs=band)
bs_plotter.save("band.png")
```

### 7. 表面/界面构建

```python
from pymatgen.core.surface import SlabGenerator, generate_all_slabs

# 从体相切表面
struct = Structure.from_file("electrode.cif")
slab_gen = SlabGenerator(
    struct, miller_index=[1,0,0],
    min_slab_size=10, min_vacuum_size=15
)
slabs = slab_gen.get_slabs()
print(f"生成 {len(slabs)} 个 slab 模型")
```

## 执行规则

1. **优先用 Materials Project**：已有计算数据直接查询，不做重复计算
2. **格式转换优先**：CIF↔POSCAR 用 pymatgen，不要手写
3. **无 API key 降级**：用本地结构分析功能，不查 MP
4. **大计算提示**：DFT 级别的计算提示用户需要 HPC 资源
5. **可视化用 matplotlib**：结构可视化建议用 VESTA 或 pymatgen 内置 plot

## 参考

- pymatgen 文档: https://pymatgen.org
- Materials Project: https://materialsproject.org
- 原始 skill 来源: K-Dense-AI/scientific-agent-skills/pymatgen
