---
name: dev-toolkit
description: "开发工具箱——GitHub工作流+软件工程全流程+调试测试+基础设施。覆盖代码审查、PR管理、代码质量、调试、测试、CI/CD、性能优化、安全加固、Docker、磁盘分析等。触发: PR审查/GitHub/调试/测试/Docker/磁盘空间/部署/重构/代码质量。"
metadata:
  version: "1.0.0"
  mega: true
  subskills:
    github: [github-code-review, github-issues, github-pr-workflow]
    process: [code-review-and-quality, code-simplification, debugging-and-error-recovery, systematic-debugging, test-driven-development, subagent-driven-development, doubt-driven-development, source-driven-development, spec-driven-development, incremental-implementation]
    lifecycle: [ci-cd-and-automation, shipping-and-launch, deprecation-and-migration, git-workflow-and-versioning]
    quality: [api-and-interface-design, documentation-and-adrs, security-and-hardening, performance-optimization, observability-and-instrumentation, context-engineering, planning-and-task-breakdown, frontend-ui-engineering, browser-testing-with-devtools]
    infra: [docker-management, storage-analyzer, neat-freak]
    extra: [ui-ux-pro-max]
---

# 🛠️ 开发工具箱 (dev-toolkit)

GitHub + 软件工程全流程 + 基础设施。你研究生偶尔写代码/跑实验时用。

## 意图路由表

### 🔗 GitHub 工作流

| 你说... | 路由到 |
|---------|--------|
| "审查这个PR" / "review代码" | `github-code-review` |
| "GitHub Issues XXX" | `github-issues` |
| "创建PR" / "PR工作流" | `github-pr-workflow` |

### 🔧 软件工程流程

| 你说... | 路由到 |
|---------|--------|
| "检查代码质量" / "代码review" | `code-review-and-quality` |
| "简化这段代码" | `code-simplification` |
| "调试XXX" / "这个bug" | `debugging-and-error-recovery` |
| 系统化调试 | `systematic-debugging` |
| "写测试" / "TDD" | `test-driven-development` |
| "用子代理开发" | `subagent-driven-development` |
| "疑问驱动开发" | `doubt-driven-development` |
| "源码驱动开发" | `source-driven-development` |
| "spec驱动开发" | `spec-driven-development` |
| "增量实现" | `incremental-implementation` |

### 🚀 软件生命周期

| 你说... | 路由到 |
|---------|--------|
| "CI/CD" / "自动化部署" | `ci-cd-and-automation` |
| "发布" / "上线" / "shipping" | `shipping-and-launch` |
| "迁移" / "废弃旧接口" | `deprecation-and-migration` |
| "Git工作流" / "分支策略" | `git-workflow-and-versioning` |

### ✅ 代码质量与安全

| 你说... | 路由到 |
|---------|--------|
| "设计API" / "接口设计" | `api-and-interface-design` |
| "写文档" / "ADR" | `documentation-and-adrs` |
| "安全检查" / "加固" | `security-and-hardening` |
| "性能优化" | `performance-optimization` |
| "可观测性" / "监控" | `observability-and-instrumentation` |
| "上下文工程" / "prompt engineering" | `context-engineering` |
| "任务拆解" / "planning" | `planning-and-task-breakdown` |
| "前端UI" / "界面设计" | `frontend-ui-engineering` |
| "浏览器测试" | `browser-testing-with-devtools` |
| "UI/UX设计" | `ui-ux-pro-max` |

### 🏗️ 基础设施

| 你说... | 路由到 |
|---------|--------|
| "Docker XXX" | `docker-management` |
| "磁盘空间" / "什么东西占空间" | `storage-analyzer` |
| "整理代码格式" | `neat-freak` |

## 跳过不纳入的

以下 🔴 用不上的 skill **不在本调度台内**：
- `webapp-testing`、`native-mcp`、`mcporter`、`oss-forensics`、`sherlock`
- `atlas-contract`、`atlas-ledger`、`base-blockchain`、`solana`、`polymarket`
- `google-workspace`、`linear`、`khazix-writer`、`one-password`、`interview-me`

## 执行规则

1. 代码类需求优先用 process 组 skill
2. 部署/发布类需求用 lifecycle 组
3. 研究生基本只用 GitHub + docker + storage-analyzer，其余按需触发
