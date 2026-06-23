---
name: literature-review-writing
description: 科技论文写作 —— 一套面向科技论文（尤其是综述 Survey）自动化写作的子技能体系。涵盖文献调研、结构逻辑、实验设计、图表制作与同行审议五大模块，配套工作流路由、质量门禁与分数递进路径。发布者：陈德里开源（量子位）。
---

# 科技论文写作（Literature Review Writing）

一套面向科技论文（尤其是综述 Survey）自动化写作的子技能体系，涵盖五大模块，配套工作流路由、质量门禁与分数递进路径。

## 五个子技能

| # | 子技能 | 说明 |
|---|--------|------|
| 01 | 文献调研 (Literature Survey) | 四阶段流水线：Recall → Score (LQS) → Classify (A/B/C/D) → Upgrade (arxiv→accepted) |
| 02 | 结构逻辑 (Structure & Logic) | 论文结构的逻辑搭建与论证链条设计 |
| 03 | 实验 (Experiments) | 实验方案设计与结果分析 |
| 04 | 设计 (Design) | 论文可视化设计、排版与图表风格 |
| 05 | 图表制作与同行审议 (Figures & Peer Review) | 图表生成与模拟审稿反馈 |

---

## 01 文献调研 (Literature Survey)

### 四阶段流水线

```
Recall → Score (LQS) → Classify (A/B/C/D) → Upgrade (arxiv → accepted)
```

### 输入

- **topic**: 研究主题关键词
- **taxonomy keywords**: 分类体系关键词

### 输出

- **references.bib**: 文献引用数据库
- **citation_plan.jsonl**: 引用计划（含分类、评分、升级建议）

### Stage 1: 高召回检索 (High Recall Search)

通过搜索工具执行 20-30 条高召回检索：

```bash
search pV -0 "site:arxiv.org <keywords>"
```

**目标**: 最大化召回相关文献，避免遗漏关键论文。

### Stage 2: LQS 评分 (Literature Quality Score)

对检索到的每篇论文进行质量评分：
- 期刊/会议等级
- 引用量
- 方法新颖性
- 实验完整性
- 与 topic 的关联度

### Stage 3: 分类 (Classify)

将论文分为 A/B/C/D 四个等级：
- **A 级**: 必读核心文献（经典 + SOTA）
- **B 级**: 重要参考（方法对比、基线）
- **C 级**: 边缘相关（可浏览）
- **D 级**: 排除（质量低或不相关）

### Stage 4: 升级 (Upgrade)

跟踪 arxiv 预印本到正式发表的状态变化，自动更新 citation_plan。

---

## 工作流路由

根据论文类型自动选择子技能执行顺序：

- **Survey/综述**: 01 → 02 → 05 → 04
- **Research/研究论文**: 01 → 03 → 02 → 04 → 05
- **Position Paper**: 02 → 01 → 04 → 05

## 质量门禁

每个阶段完成后有质量检查点：
1. 文献覆盖率 > 80%
2. 逻辑链无断点
3. 实验可复现
4. 图表自明性
5. 同行审议通过

## 分数递进路径

以 LQS 综合评分为基础，递进式推进写作深度，确保论文质量随工作流逐步提升。
