---
name: group-meeting-pptx
description: Use when the user asks to make a group meeting PPT, journal club PPT, or presentation from a paper PDF. Triggers on: 做组会PPT, 组会汇报, 组会ppt, journal club, 做个ppt, 做个汇报ppt, 论文ppt, paper to ppt, 汇报ppt.
---

# Group Meeting PPTX Builder

Automate the full pipeline: paper PDF -> clean figures + text -> Nature-style Chinese PPTX.

## Workflow

### Step 1: Extract paper content

Run `extract_paper.py` to get text and clean embedded figures:

```bash
python <skill_dir>/extract_paper.py "<pdf_path>" "<output_dir>"
```

This produces:
- `<output_dir>/paper_text.txt` — full paper text
- `<output_dir>/figures/` — clean embedded figures (NOT page screenshots)
- `<output_dir>/figures/manifest.json` — figure metadata

**Critical:** This extracts the original figure images embedded in the PDF. Do NOT render full pages as screenshots — that includes journal headers, page numbers, and surrounding text.

### Step 2: Read and classify the paper

Read `paper_text.txt`. Identify:
- Paper type (discovery, methods, materials, clinical, review, etc.)
- Central claim and knowledge gap
- Key figures and what they show
- Main results with quantitative data

### Step 3: Design slides

Default: 12-14 slides for a 15-20 minute report.

Structure (adapt to paper type):
1. 标题页 (cover)
2. 研究背景 (bullets)
3. 知识缺口/技术瓶颈 (bullets)
4. 论文核心策略 (bullets)
5-7. 关键证据 (figure slides with original paper figures)
8. 机理/综合 (dual_panel or bullets)
9-10. 更多证据/验证 (figure or three_columns)
11. 实用化/应用 (dual_with_figure or figure)
12. 创新点 (innovations)
13. 局限性 (bullets)
14. 总结与讨论 (bullets)

**Slide type reference:**
- `cover`: title, subtitle, authors, journal, affiliation
- `bullets`: title + bullet list (font_size optional, default 16)
- `figure`: title + one full-width figure + source label
- `dual_panel`: title + two side-by-side panels with bullets + optional summary
- `three_columns`: title + three equal columns with bullets
- `dual_with_figure`: title + two panels above + one figure below
- `innovations`: title + numbered innovation cards

**Figure mapping:** Match extracted figures to slides by reading the paper and identifying which figure belongs where. The manifest.json shows dimensions and which page each figure came from.

**Title rule:** Use conclusion-style titles ("F-LPSCl 显著提升循环稳定性") not topic labels ("Figure 3").

### Step 4: Build slides.json

Create a JSON file with slide data. Example structure:

```json
[
  {"title": "表面氟化屏蔽策略...", "type": "cover", "subtitle": "...", "authors": "...", "journal": "...", "affil": "..."},
  {"title": "研究背景", "type": "bullets", "bullets": ["...", "..."], "footer": "组会汇报"},
  {"title": "表面氟化构建", "type": "figure", "figure": "page03_fig01.jpeg", "source": "Source: Fig. 1, Journal, Year", "footer": "组会汇报"},
  {"title": "机理小结", "type": "dual_panel", "left": {"header": "机制1", "bullets": ["..."]}, "right": {"header": "机制2", "bullets": ["..."]}, "summary": ["..."], "footer": "组会汇报"}
]
```

**Every figure slide MUST include a `source` field** with the paper's figure number and journal.

### Step 5: Build PPTX

```bash
python <skill_dir>/build_pptx.py "<slides.json>" "<figures_dir>" "<output.pptx>"
```

### Step 6: Verify

Reopen the PPTX with python-pptx and check:
- Correct slide count
- All figures embedded
- No missing images
- File size reasonable (<10 MB)

## Design Rules

- 16:9 widescreen, white background
- Color: deep blue (#1B3A5C) + accent blue (#3A7CA5)
- Font: Arial, clean hierarchy
- Each slide makes ONE point
- Figures are clean original images, not page screenshots
- Source labels on all figure slides
- Chinese titles, bullets, and captions
- Footer "组会汇报" on all slides except cover

## Figure Extraction (Critical)

The `extract_paper.py` script extracts original embedded images from the PDF. These are the author-submitted figure files — clean, no surrounding text. This is the key improvement over naive full-page rendering.

If a figure spans multiple pages or is vector graphics (no embedded raster), render the figure area at 300 DPI:

```python
clip = fitz.Rect(45, 65, page.rect.width - 45, page.rect.height - 25)
pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72), clip=clip)
```

## Output

- `<output_dir>/final_presentation_cn.pptx` — the deliverable
- `<output_dir>/qa_report.md` — short quality report
