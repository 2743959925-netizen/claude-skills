---
name: skill-usage-tracker
description: 统计和展示 skill 使用频率。自动通过 PostToolUse hook 累积计数，手动触发时输出 ASCII 柱状图。
---

# Skill Usage Tracker

追踪你使用各个 skill 的频率，终端 ASCII 柱状图可视化。

## 工作原理

- **自动计数**：PostToolUse hook 在每次 Skill 被调用后自动运行 `scripts/counter.js`，将计数 +1 写入 `data/usage.json`
- **手动查看**：对汉堡包说"看 skill 使用频率"或"skill 统计"，读取 `data/usage.json` 生成柱状图

## 文件结构

```
skill-usage-tracker/
  SKILL.md
  scripts/
    counter.js      ← hook 调用的计数器
  data/
    usage.json      ← {"skill-name": {"count": N, "lastUsed": "ISO8601"}}
```
