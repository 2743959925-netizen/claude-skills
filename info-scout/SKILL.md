---
name: info-scout
description: "信息侦察(v1.1 吸收STORM/PaperQA2)——跨平台搜索+热点追踪+博客监控+skill发现+深度调研合成。覆盖agent-reach(17+平台)、duckduckgo搜索、AI热点、RSS监控、新skill发现、STORM风格长文调研。触发: 搜一下/搜索XXX平台有没有/最近AI有什么热点/监控这个博客/有没有XXX的skill/深度调研/写调研报告。"
metadata:
  version: "1.1.0"
  mega: true
  subskills: [agent-reach, duckduckgo-search, aihot, blogwatcher, find-skill]
  absorbed_from:
    - STORM (Stanford): Wikipedia-like long-form article generation with citations
    - GPT Researcher: multi-agent deep web research
    - PaperQA2 (Future-House): high-accuracy RAG for scientific documents
    - local-deep-research: local-first research agent
    - DeerFlow (ByteDance): super-agent orchestration
---

# 🔍 信息侦察 (info-scout) v1.1

跨平台搜索 + 信息获取 + 深度调研 + 订阅监控。不用记子 skill 名。

## 意图路由表

| 你说... | 路由到 | 说明 |
|---------|--------|------|
| "帮我在XXX上搜YYY" / "搜一下小红书/Twitter/B站..." | `agent-reach` | 覆盖 17+ 平台 |
| "搜索XXX" (通用网页搜索) | `duckduckgo-search` | 免费，无 API key |
| "AI最近有什么热点" | `aihot` | AI 领域热点追踪 |
| "监控这个博客" / "RSS订阅XXX" | `blogwatcher` | 博客更新监控 |
| "有没有XXX的skill" / "找skill" | `find-skill` | Skill 市场搜索 |
| "深度调研XXX" / "写篇XXX综述" | STORM 风格长文生成 → `duckduckgo-search` + 多轮检索合成 | 自动生成带引用的 Wiki 式长文 |
| "这篇论文讲了什么数据" / "提取实验细节" | PaperQA2 风格 RAG → `WebSearch` + 结构化提取 | 高精度文献问答 |
| "本地调研XXX" | local-deep-research 风格 → `duckduckgo-search` + FAISS | 搜索→存储→合成 |
| "多线程查XXX" | DeerFlow 风格多 Agent → `agent-reach` + `duckduckgo-search` | 并行搜索聚合 |

## 优先级规则

1. 明确指定平台 → 用 `agent-reach`
2. 通用搜索 → 优先 `duckduckgo-search`（免费无限制），再 fallback `WebSearch`
3. 找新 skill → 用 `find-skill`
4. 深度调研/综述类 → 自动组合多轮搜索 + 合成 + 引用
