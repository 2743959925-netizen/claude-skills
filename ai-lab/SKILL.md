---
name: ai-lab
description: "AI实验台——向量数据库+模型推理+Jupyter交互。覆盖chroma/faiss/qdrant向量检索、huggingface模型管理、llama-cpp本地推理、jupyter内核、结构化输出。触发: 向量数据库/本地跑模型/HuggingFace/Jupyter/embedding。"
metadata:
  version: "1.0.0"
  mega: true
  subskills:
    vector: [chroma, faiss, qdrant]
    models: [huggingface-hub, llama-cpp, instructor]
    interactive: [jupyter-live-kernel]
---

# 🤖 AI 实验台 (ai-lab)

向量检索 + 模型推理 + Jupyter。研究生偶尔跑模型/做 embedding 时用。

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

> 注意：`vllm`（高性能推理服务）、`flash-attention`（训练加速）、`grpo-rl-training`（强化学习训练）、`stable-diffusion`（图像生成）、`honcho`（用户记忆）—— 🔴 研究生基本用不上，未纳入。

### 💻 交互环境

| 你说... | 路由到 |
|---------|--------|
| "跑Python数据分析" / "Jupyter" | `jupyter-live-kernel` |

## 执行规则

1. 向量库选型：本地小规模 → `chroma`；高效检索 → `faiss`；生产级 → `qdrant`
2. 模型下载优先用 HuggingFace 镜像（国内网络）
3. 研究生实际常用：`jupyter-live-kernel` > `huggingface-hub` > 其他
