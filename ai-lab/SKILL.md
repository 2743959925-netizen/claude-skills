---
name: ai-lab
description: "AI实验台(v1.1 吸收AIDE/GPU优化)——向量数据库+模型推理+Jupyter交互+自动ML实验。覆盖chroma/faiss/qdrant向量检索、huggingface模型管理、llama-cpp本地推理、jupyter内核、结构化输出、自动化ML实验循环。触发: 向量数据库/本地跑模型/HuggingFace/Jupyter/embedding/自动调参/ML实验。"
metadata:
  version: "1.1.0"
  mega: true
  subskills:
    vector: [chroma, faiss, qdrant]
    models: [huggingface-hub, llama-cpp, instructor]
    interactive: [jupyter-live-kernel]
    auto_experiment: [aide-ml-experiment]
  absorbed_from:
    - AIDE (WecoAI): agentic tree search for ML code optimization
    - optimize-for-gpu (scientific-agent-skills): GPU optimization patterns
    - pytorch-lightning (scientific-agent-skills): structured ML training
---

# 🤖 AI 实验台 (ai-lab) v1.1

向量检索 + 模型推理 + Jupyter + 自动 ML 实验。跑模型/做 embedding/调参时用。

## 意图路由表

### 🗂️ 向量数据库

| 你说... | 路由到 |
|---------|--------|
| "用Chroma向量检索" | `chroma` |
| "FAISS检索" / "高效向量搜索" | `faiss` |
| "Qdrant向量库" | `qdrant` |

> 注意：`pinecone` 云端付费，🔴 不用，未纳入。

### 🧠 模型相关

| 你说... | 路由到 |
|---------|--------|
| "从HuggingFace下个模型" / "HF模型" | `huggingface-hub` |
| "本地跑LLM" / "llama.cpp推理" | `llama-cpp` |
| "结构化JSON输出" / "LLM输出格式化" | `instructor` |

> 注意：`vllm`、`flash-attention`、`grpo-rl-training`、`stable-diffusion`、`honcho`——研究生用不上，未纳入。

### 💻 交互环境

| 你说... | 路由到 |
|---------|--------|
| "跑Python数据分析" / "Jupyter" | `jupyter-live-kernel` |

### 🔬 自动 ML 实验（NEW v1.1）

| 你说... | 路由到 |
|---------|--------|
| "自动调参" / "自动优化模型" | `aide-ml-experiment`（AIDE 树搜索模式） |
| "GPU优化" / "CUDA加速" | 吸收 optimize-for-gpu 模式 |
| "PyTorch Lightning训练" | 吸收 pytorch-lightning 模式 |

## 执行规则

1. 向量库选型：本地小规模 → `chroma`；高效检索 → `faiss`；生产级 → `qdrant`
2. 模型下载优先用 HuggingFace 镜像（国内网络）
3. 自动 ML 实验：先小规模试跑，再扩展（AIDE 模式）
4. 研究生实际常用：`jupyter-live-kernel` > `huggingface-hub` > 其他
