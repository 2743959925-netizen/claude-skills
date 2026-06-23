---
name: info-scout
description: "信息侦察——跨平台搜索+热点追踪+博客监控+skill发现。覆盖agent-reach(17+平台)、duckduckgo搜索、AI热点、RSS监控、新skill发现。触发: 搜一下/搜索XXX平台有没有/最近AI有什么热点/监控这个博客/有没有XXX的skill。"
metadata:
  version: "1.0.0"
  mega: true
  subskills: [agent-reach, duckduckgo-search, aihot, blogwatcher, find-skill]
---

# 🔍 信息侦察 (info-scout)

跨平台搜索 + 信息获取 + 订阅监控。不用记子 skill 名。

## 意图路由表

| 你说... | 路由到 | 说明 |
|---------|--------|------|
| "帮我在XXX上搜YYY" / "搜一下小红书/Twitter/B站..." | `agent-reach` | 覆盖 17+ 平台 |
| "搜索XXX" (通用网页搜索) | `duckduckgo-search` | 免费，无 API key |
| "AI最近有什么热点" | `aihot` | AI 领域热点追踪 |
| "监控这个博客" / "RSS订阅XXX" | `blogwatcher` | 博客更新监控 |
| "有没有XXX的skill" / "找skill" | `find-skill` | Skill 市场搜索 |

## 优先级规则

1. 明确指定平台 → 用 `agent-reach`
2. 通用搜索 → 优先 `duckduckgo-search`（免费无限制），再 fallback `WebSearch`
3. 找新 skill → 用 `find-skill`
