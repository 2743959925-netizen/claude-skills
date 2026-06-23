---
name: doi-to-zotero
description: 从公众号文章/文本/URL中提取DOI，通过CrossRef获取元数据，从Sci-Hub下载PDF，生成RIS文件并自动导入Zotero。所有文件存入D:\zotero-claude\YYYY-MM-DD\。当用户发送含DOI的文章、公众号链接、要求"导入Zotero"、"提取DOI"、"下载论文"、"把文章导入文献库"、"自动下载文献"时使用。
---

# doi-to-zotero — DOI 提取、PDF 下载与 Zotero 自动导入

## 触发条件

以下任一情况触发本 skill：

1. 用户发送含 **DOI** 的文本（URL 形式或裸 DOI），且说"导入 Zotero"、"提取 DOI"、"下载论文"、"加入文献库"等
2. 用户发送**文章 URL**（公众号链接、网页链接等），需要提取 DOI
3. 用户发送含 DOI 的文章，且上下文表明需要获取原文

## 工作流程

### Step 1: 获取文章内容

如果用户发了**链接**（公众号文章 URL、网页 URL 等），先用 `WebFetch` 工具抓取页面内容：

```
WebFetch url="用户发的链接" prompt="提取页面中的所有DOI和论文引用信息"
```

从抓取结果中找出 DOI。

如果用户直接发了**文本**，从中提取 DOI。

### Step 2: 运行脚本

```bash
python "C:\Users\27439\.claude\skills\doi-to-zotero\scripts\doi_to_zotero.py" \
  --text "文章内容（含DOI）" \
  --output-dir "D:\zotero-claude"
```

参数说明：

| 参数 | 作用 |
|------|------|
| `--text "..."` | 传入包含 DOI 的文本 |
| `--doi "10.xxx"` | 直接指定 DOI（可重复） |
| `--text-file path` | 从文件读取 |
| `--no-pdf` | 只生成 RIS，不下载 PDF |
| `--no-launch` | 不自动打开 Zotero |
| `--mailto` | CrossRef 礼貌池邮箱 |

### Step 3: 脚本行为

脚本按顺序执行：

1. 从文本提取所有 DOI → 去重
2. CrossRef 获取每篇论文的元数据（标题、作者、期刊、年份等）
3. 在 `D:\zotero-claude\YYYY-MM-DD\` 下创建当天日期文件夹
4. 从 Sci-Hub 下载每篇论文的 PDF（8 个域名自动切换）
5. 生成 RIS 文件（含完整元数据）
6. 自动打开 Zotero 导入 RIS

### Step 4: 解析结果

脚本输出 JSON，Claude 解析后回复用户。

### Step 5: 回复格式

```
✅ 已找到 2 篇论文

1. Solid-state batteries: a mechanistic perspective
   Nature, 2024 | 10.1038/s41586-024-08000-1
   作者: Smith J, Lee K, Wang M 等

2. Advanced solid electrolytes for all-solid-state batteries
   Advanced Materials, 2024 | 10.1002/adma.202401234
   作者: Zhang Y, Park H 等

📂 保存位置: D:\zotero-claude\2026-05-09\
📄 RIS: papers-143022.ris
📥 PDF: 2/2 下载成功，已关联到 Zotero 条目
   - Solid-state batteries.pdf → L1 标签已写入 RIS
   - Advanced solid electrolytes.pdf → L1 标签已写入 RIS
📚 Zotero 导入已触发（请在电脑前确认导入弹窗）
   Zotero 导入后将自动关联 PDF 附件
❌ 0 个错误
```

有 PDF 下载失败时：
```
⚠️ 1 篇 PDF 下载失败（Sci-Hub 暂不可用），RIS 元数据仍已生成。
建议稍候重试或手动去 Zotero 里用 DOI 补下 PDF。
```

## 文件结构

```
D:\zotero-claude\
├── 2026-05-09\
│   ├── papers-143022.ris
│   ├── Solid-state batteries a mechanistic perspective.pdf
│   └── Advanced solid electrolytes for all-solid-state batteries.pdf
├── 2026-05-08\
│   └── ...
└── ...
```

## 注意事项

- 输出根目录固定为 `D:\zotero-claude`，按日期自动分文件夹
- Sci-Hub 有 8 个备用域名，逐一轮询直到成功
- PDF 文件名取自论文标题
- CrossRef 每次请求间隔 0.3 秒
- Zotero 导入时需在电脑前点一次"完成"
- Sci-PDF 插件会在后台继续尝试下载失败的 PDF
