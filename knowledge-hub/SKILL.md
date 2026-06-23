---
name: knowledge-hub
description: "知识中枢——Wiki管理+笔记存档+可视化+文件规划。覆盖wiki全流程(摄取/检索/查健康)、对话存档(save)、自主研究(autoresearch)、深度思考(think)、Obsidian增强、Canvas白板、文件规划。触发: wiki/存档/ingest/查知识/lint/canvas/规划任务。"
metadata:
  version: "1.0.0"
  mega: true
  subskills:
    wiki: [wiki, wiki-ingest, wiki-query, wiki-lint, wiki-mode, wiki-retrieve, wiki-cli, wiki-fold]
    notes: [save, autoresearch, think, obsidian-bases, obsidian-markdown]
    visual: [canvas, excalidraw, defuddle]
    planning: [planning-with-files-zh]
---

# 🧠 知识中枢 (knowledge-hub)

Wiki 体系 + 笔记存档 + 可视化 + 任务规划，一站式知识管理。

## 意图路由表

### 📚 Wiki 体系

| 你说... | 路由到 |
|---------|--------|
| "/wiki" / "检查wiki状态" | `wiki` |
| "ingest [文件/URL]" / "把这篇摄入wiki" | `wiki-ingest` |
| "wiki里有没有XXX" / "查一下XXX" | `wiki-query` |
| "lint wiki" / "检查wiki健康" | `wiki-lint` |
| "切换wiki模式" / "wiki用Zettelkasten" | `wiki-mode` |
| 高级混合检索 | `wiki-retrieve` |
| 创建新wiki结构 | `wiki-fold` |
| (Obsidian CLI底层传输) | `wiki-cli` ← 自动 |

### 📝 笔记与存档

| 你说... | 路由到 |
|---------|--------|
| "/save" / "存档这次对话" | `save` |
| "/autoresearch [话题]" | `autoresearch` |
| "/think" / "深入思考XXX" | `think` |
| "Obsidian数据库" / "Dataview" | `obsidian-bases` |
| "Obsidian Markdown增强" | `obsidian-markdown` ← 自动 |

### 🗺️ 可视化

| 你说... | 路由到 |
|---------|--------|
| "/canvas" / "画白板" / "可视化" | `canvas` |
| "/canvas add image" / "手绘" | `excalidraw` |
| "提取网页正文" | `defuddle` |

### 📋 文件规划

| 你说... | 路由到 |
|---------|--------|
| 复杂任务自动规划 | `planning-with-files-zh` ← 复杂任务自动触发 |
| "用文件规划法做XXX" | `planning-with-files-zh` |

## 执行规则

1. wiki-* 系列按标准流程串行（ingest → lint → query）
2. save 操作后提示存档位置
3. 复杂任务自动触发 planning-with-files-zh
