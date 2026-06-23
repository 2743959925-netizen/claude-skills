# 🛠️ Claude Code Skills

> 汉堡包的超能力工具箱 — 5 个 Mega-Skill 调度台 + 96 个子 skill  
> 日常直接用中文说需求，调度台自动路由，不需要记子 skill 名

## 🧩 五大调度台（Mega-Skills）

| Mega-Skill | 用途 | 子 skill 数 |
|-----------|------|------------|
| [research-lab](./research-lab/) 🔬⭐ | 论文检索→审稿→写作→PPT→实验分析 | 56 |
| [knowledge-hub](./knowledge-hub/) 📝⭐ | Wiki + 笔记 + Canvas + 文件规划 | 19 |
| [info-scout](./info-scout/) 🔍 | 17+ 平台搜索 + 热点 + 博客监控 | 5 |
| [dev-toolkit](./dev-toolkit/) 🛠️ | GitHub + 调试 + Docker + 代码质量 | 40 |
| [ai-lab](./ai-lab/) 🤖 | 向量库 + 模型推理 + Jupyter | 7 |

## 📂 目录结构

```
claude-skills/
├── research-lab/          # 🔬 科研全流程
│   ├── paper-search/      # 论文检索 (知网/GS/arXiv/DOI)
│   ├── paper-reading/     # 论文阅读与审稿
│   ├── paper-writing/     # 论文写作与润色
│   ├── presentation/      # PPT 与可视化
│   ├── idea/              # Idea 评估与打磨
│   ├── experiment/        # 实验数据分析
│   └── extra/             # 面试/写作扩展
├── knowledge-hub/         # 📝 知识管理
│   ├── wiki/              # Wiki 引擎
│   ├── notes/             # 笔记与存档
│   ├── visual/            # Canvas/Excalidraw
│   └── planning/          # 文件规划法
├── info-scout/            # 🔍 信息侦察
│   └── modules/           # 搜索/热点/博客/skill发现
├── dev-toolkit/           # 🛠️ 开发工具箱
│   ├── github/            # PR/Issues/Code Review
│   ├── process/           # TDD/调试/简化/增量开发
│   ├── lifecycle/         # CI/CD/发布/迁移
│   ├── quality/           # API/文档/安全/性能
│   └── infra/             # Docker/磁盘/格式
├── ai-lab/                # 🤖 AI 实验台
│   ├── vector/            # Chroma/FAISS/Qdrant
│   ├── models/            # HF/Llama/结构化输出
│   └── interactive/       # Jupyter
└── frozen-zone/           # ⚙️ 不动区 (底层/不常用)
    ├── hermes-* ×9        # AI 记忆与路由
    ├── claude-to-im       # IM 桥接
    └── ...                # Web3/区块链等
```

## 🚀 使用方式

在 Claude Code 中直接说需求即可：

```
"审稿这篇论文"    → research-lab → academic-paper-reviewer
"做组会PPT"       → research-lab → group-meeting-pptx
"保存这个到wiki"  → knowledge-hub → save
"Docker部署"      → dev-toolkit → docker-management
"搜小红书XXX"     → info-scout → agent-reach
"FAISS向量检索"   → ai-lab → faiss
```

## 📦 安装

```bash
# 克隆到 Claude Code skills 目录
git clone https://github.com/2743959925-netizen/claude-skills.git ~/.claude/skills-github
```

## 📋 维护

- 索引文件: [_分类索引.md](./_分类索引.md)
- 汉堡包的知识库: 参见 `CLAUDE.md`
- 安装新 skill: 自动更新索引
