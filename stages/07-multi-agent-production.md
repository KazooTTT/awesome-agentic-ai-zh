# Stage 7 — Multi-Agent · Production

> **繁體中文** | [简体中文](./07-multi-agent-production.zh-Hans.md) | [English](./07-multi-agent-production.en.md)

⏱ **時間估算**：2-4 週（約 15-30 小時）

> 💡 用語密度高（multi-agent / handoff / eval / observability / guardrails⋯）→ 翻 [`resources/glossary.md` §4 + §6](../resources/glossary.md#4-multi-agent)。

> 📋 **本章組成**：〔Multi-Agent · Production 是什麼（先定位）+ Discipline lineage〕→ 學習目標 → 進入條件 → 必修閱讀 → Harness Engineering（8 個核心元件）→ 動手練習 → 常用工具推薦 → 精選 Projects → 自我檢查  
> 🔑 **關鍵名詞**：見 [`resources/glossary.md` §4 + §6](../resources/glossary.md#4-multi-agent)（multi-agent / orchestration / handoff / eval / observability / harness）

最後一個階段。你正從「我會做 agent」走向「我能在 production 跑起來，多個 agent 協作、有 eval、有 observability、會 deploy」。

## 🎯 Multi-Agent · Production 是什麼（先定位）

**Multi-Agent · Production = 多 agent 協作 + 把 agent 從 prototype 推到 production 的工程學科**。本 stage 跟前面 stage 的分工：

- **Stage 4** = 單 agent framework 怎麼挑、ReAct / Plan-Execute 等 pattern
- **本 stage** = **多 agent 協作** + **harness engineering**（production runtime 工程）+ **deploy / observability / eval**

**Discipline lineage**（你現在在第 3 層 = 最上層）：

| 層 | Discipline | 解決什麼 | 在哪 stage |
|---|---|---|---|
| 1 | **Prompt Engineering** | 單次 LLM call 怎麼問才準 | [Stage 2](02-prompt-engineering.md) |
| 2 | **Context Engineering** | 跨多次 call 怎麼動態組 prompt | [Stage 6](06-memory-rag.md) |
| **3** | **Harness Engineering**<br>（**本 stage**） | **把多個 LLM call 包成 production runtime** | **本 stage** |

**本 stage 3 個 problem domain**：

1. **Multi-agent 協作** — debate / planner-executor / peer review / handoff / supervisor-worker pattern
2. **Harness Engineering** — agent loop / tool registry / context manager / safety / retry / telemetry / eval / cost（8 個 component、下面詳述）
3. **Production** — eval harness / observability / cost & latency 優化 / deploy

**跟 Stage 5 的分工**（避免混淆）：

| 跟誰比 | 那邊講什麼 | 本 stage 講什麼 |
|---|---|---|
| **Stage 5.5 Subagents** | Claude Code 原生 subagent 機制（markdown-based、不寫程式）| 通用 multi-agent framework（autogen / crewAI / langgraph、跨 vendor）|
| **Stage 5.6 Claude Code source** | Claude Code source 解剖（reference harness case study）| Harness engineering 通則（discipline-level、不綁特定 vendor）|

## 📌 學習目標

- 設計 multi-agent orchestration 模式（debate、planner-executor、peer review）
- 為 agent 架一套 evaluation harness
- 加上 observability（tracing、logging、cost tracking）
- 用 Anthropic SDK / OpenAI SDK 做 production deploy（進階功能：streaming、prompt caching、batching）
- 把 agent deploy 到 production（Docker、serverless、monitoring）

## 🚪 進入條件

你應該已經：
- 完成 Stage 4（用過至少一個 agent framework 跑 multi-agent demo）
- 完成 Stage 5（懂 MCP / Skills / Plugins / Subagents 各自角色，並用 §5.6 解剖過 harness 內部）
- 完成 Stage 6（會基本 RAG，能講出 memory pattern 差異）
- 對 Docker / git / CI 基礎熟悉（production deploy 會用到）

沒到的話 → 補完前面幾個 stage。本 stage 是「組合所有前面學到的東西 → 跑 production」，缺一塊都會卡。

## 📚 必修閱讀

1. [**Anthropic — Building Effective Agents**](https://www.anthropic.com/engineering/building-effective-agents) — 用 production 的角度再讀一次
2. [**Anthropic — Prompt Caching**](https://www.anthropic.com/news/prompt-caching) — 90% 成本下降的技巧
3. [**Anthropic — Message Batches API**](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing) — 非同步 batch job
4. **任一 eval framework 的文件** — promptfoo 或 LangSmith 或 weave
5. [**ai-boost/awesome-harness-engineering**](https://github.com/ai-boost/awesome-harness-engineering)（★ 780+）— agent harness 的工具 / pattern / eval / memory / MCP / observability 全集合
6. [**ZhangHanDong/harness-engineering-from-cc-to-ai-coding**](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding)（★ 1.3k+）— 從 Claude Code 原始碼學 harness 設計（中文）

## 🏗 Harness Engineering — production agent runtime 的工程學 ⭐ 本 stage 核心概念

### Discipline 定位：prompt → context → harness 三層

把 LLM 用成 production agent 系統、有 3 層**工程學科**（discipline）。每一層 cover 不同問題、後一層假設前一層已經沒問題：

| Discipline | 解決什麼問題 | 主要技巧 | 在哪學 |
|---|---|---|---|
| **1. Prompt Engineering** | 單次 LLM call 怎麼問才會準 | system prompt / few-shot / CoT / structured output | **[Stage 2](02-prompt-engineering.md)** |
| **2. Context Engineering** | 跨多次 call 怎麼動態組裝 prompt | RAG retrieval / memory / context window 管理 / tool description 排序 | **[Stage 6](06-memory-rag.md)** + Stage 2 §進階 |
| **3. Harness Engineering**<br>（**本節**） | 把多個 LLM call 包成 production agent runtime | agent loop / retry / safety / telemetry / observability / cost control | **本 stage** |

→ **2025 後段「harness engineering」才正式成為業界共識詞**（Anthropic / Cursor / Cognition 等 AI coding tool 團隊用得最多）——因為前兩層已經被 prompt eng / context eng 解決得差不多了、production agent 的剩餘複雜度都在 runtime 工程。

### Harness 的 7 個核心元件

**Harness = 把 LLM agent 包成 production 系統的「工具帶」**。一個 production agent runtime 包含這 7 個元件（前 6 個是 runtime 內建、第 7 個 eval 是外掛工具但也算 harness 的一部分）：

| 元件 | 做什麼 | 對應本 stage 練習 |
|---|---|---|
| **Agent loop** | 「LLM → tool → result → LLM」迴圈、穩定處理多輪 | 練習 1 multi-agent 辯論 |
| **Tool registry** | 動態 tool dispatch、permission gate、sandboxing | （在每個 framework / SDK 都有） |
| **Context manager** | message history 管理、context window 控制、auto-compact | Stage 6 + 本 stage 練習 4 SDK |
| **Safety layer** | permission prompts、sandboxed exec、destructive op 攔截 | （Claude Code 內建、SDK 可自訂） |
| **Retry / recovery** | tool fail 怎麼處理（exception vs LLM 自己看 error 反思） | 練習 4 SDK 進階 |
| **Telemetry / Observability** | metrics、logging、token counting、trace export | **練習 3 Observability** |
| **Eval harness** | regression test、quality gate、A/B test | **練習 2 Eval** |

**Framework vs Harness 關鍵差別**：
- **Framework**（[Stage 4](04-agent-frameworks.md)）規範 **API** — 你呼叫的介面長什麼樣
- **Harness**（本節）規範 **runtime** — 怎麼跑、怎麼 recovery、怎麼觀測

### Reference 實作

想看 production-grade harness 長什麼樣？兩個 reference：

- **Claude Code 整個 runtime** — 是 reference harness 實作。**讀 source 練習見 [Stage 5.6](05-claude-code-ecosystem.md#56--claude-code-source-解剖reference-harness-implementation-track-b-必看)**（clone `claude-agent-sdk-python` 解剖 main loop + 上表前 6 個 runtime 元件位置；第 7 個 Eval harness 是外掛、見本 stage §練習 2 Eval）
- **`anthropics/claude-agent-sdk-python`** source — 上面練習用的具體 repo

→ 本 stage 剩下的 5 個練習（multi-agent / eval / observability / SDK / deploy）每個都是 harness 的一個面向。學完整 stage = 拼出完整的 harness engineering mental model。

## 🛠 動手練習（基礎 illustrative 練習）

### 練習 1：Multi-Agent 辯論
兩個 agent 辯論一個題目（例如「該用 Python 還是 Rust 寫 backend」），第三個 agent 當裁判。觀察辯論收斂或分歧的 pattern。

### 練習 2：Eval
替你前面的 agent 寫一份 eval，跑 N 次量成功率。把「我用眼睛看一下」的習慣換掉。

### 練習 3：Observability
把 LangSmith、Helicone、或 weave 接上一個 agent，看完整 trace。理解「沒 observability 的 agent debug = 黑盒」。

### 練習 4：SDK 進階
在同一次呼叫裡用 streaming + prompt caching + tool use。看成本怎麼降下來。

### 練習 5：Deploy
把一個 agent 包進 Docker，deploy 到雲端（任何 provider 都行）。學會把 prototype 變成可以給別人跑的東西。

## 🎯 常用 Multi-Agent / Production 工具推薦（按用途分類）

不知道從哪挑工具？下面是 2025-2026 業界常用搭配——**挑入口看「場景」、想深入點連結看 repo**：

| 場景 | 推薦工具 | 為什麼 |
|---|---|---|
| **第一次寫 multi-agent**（最快上手）| [crewAI](https://github.com/crewAIInc/crewAI) | role-based、幾行 code 跑起來、production pattern 直接 |
| **想要 group debate / brainstorm pattern** | [AutoGen](https://github.com/microsoft/autogen) | GroupChat 自由辯論、Microsoft 出品 |
| **production 要 audit trail / checkpoint / human-in-loop** | [LangGraph](https://github.com/langchain-ai/langgraph) | state machine、控制最完整 |
| **eval 標準化**（CI / regression 必裝）| [promptfoo](https://github.com/promptfoo/promptfoo) ⭐ | YAML config、跨模型比較、★ 20k+ |
| **eval + observability 同平台** | [langfuse](https://github.com/langfuse/langfuse) ⭐ | OSS、tracing + eval + prompt mgmt、★ 26k+ |
| **不改程式、快速 instrumentation** | [Helicone](https://github.com/Helicone/helicone) | proxy 中介、不綁 framework |
| **全 stack 在 LangChain** | [LangSmith](https://www.langchain.com/langsmith)（商業）| LangChain 官方 observability |
| **打造 Claude agent**（programmatic）| [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) ⭐ | Anthropic 官方 agent SDK、跟 Claude Code 同 runtime |
| **Deploy agent 成 API service** | [BentoML](https://github.com/bentoml/BentoML) | 最完整、Docker + serving |
| **自架開源 LLM**（取代付費 API）| [vLLM](https://github.com/vllm-project/vllm) | 高吞吐量、★ 79k+ |
| **Fine-tune 開源 LLM** | [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 100+ 模型統一 SFT/DPO/PPO/GRPO、Web UI 零 code、中文社群最廣、★ 70k+ |

**建議入手順序**：
1. 第一個 multi-agent：**crewAI**（role-based、最簡單）
2. 加 eval：**promptfoo**（YAML、CI 整合）
3. 加 observability：**langfuse**（OSS、完整）
4. Production 升級：換 **LangGraph**（control 強）+ **BentoML**（deploy）
5. 進階：自架 LLM 接 **vLLM**、fine-tune 用 **LLaMA-Factory**

## 🎯 精選 Projects（範本 / SDK / 工具 collection）

按用途分類、22 個項目一張表搞定。**挑入口看「適合誰」、想深入點連結看 repo**。

| 分類 | Project | ⭐ | 適合誰 | 為什麼推薦 / 備註 |
|---|---|---|---|---|
| **Multi-Agent Orchestration** | [microsoft/autogen](https://github.com/microsoft/autogen) | ⭐⭐⭐⭐⭐ | 想要 GroupChat 自由 debate pattern | Stage 4 介紹過、production 場景再回頭看 multi-agent 辯論 / brainstorming 模式 |
| | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | ⭐⭐⭐⭐⭐ | 想要 role-based 流水線 | 角色式 multi-agent（research → writer → reviewer），最簡單 production pattern |
| | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | ⭐⭐⭐⭐⭐ | 需要 audit trail / checkpoint / human-in-the-loop | state machine 路線、production 控制最強 |
| **Eval Frameworks** | [promptfoo](https://github.com/promptfoo/promptfoo) ⭐ | ⭐⭐⭐⭐⭐ | 把 eval 流程標準化、CI 整合 | YAML config、跨模型比較。★ 20k+、MIT |
| | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | ⭐⭐⭐⭐ | 學術 benchmark 主張（MMLU / HellaSwag / GSM8K）| 學術等級。★ 12k+、MIT |
| | [openai/evals](https://github.com/openai/evals) | ⭐⭐⭐⭐ | OpenAI 專屬 eval / 想回饋上游 | ★ 18k+ |
| **Observability** | [langfuse](https://github.com/langfuse/langfuse) ⭐ | ⭐⭐⭐⭐⭐ | 自架 production observability | OSS LangSmith 替代、traces + sessions + evals + prompt mgmt。★ 26k+、MIT |
| | [LangSmith](https://www.langchain.com/langsmith)（商業）| ⭐⭐⭐⭐ | 全 stack 在 LangChain / LangGraph 上 | LangChain 官方、只有 hosted 版 |
| | [Helicone](https://github.com/Helicone/helicone) | ⭐⭐⭐⭐ | 不想改程式、快速上 instrumentation | proxy 中介、順便拿到 logging + caching。★ 5k+、Apache 2.0 |
| | [weave (W&B)](https://github.com/wandb/weave) | ⭐⭐⭐⭐ | 團隊已在用 W&B 做 ML 實驗追蹤 | W&B tracing + eval、跟 wandb 整合 |
| **Anthropic SDK 進階** | [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) | ⭐⭐⭐⭐⭐ | 直接基於 Claude API 做應用 | 官方 Python SDK：streaming / async / tool use / prompt caching / batches / files |
| | [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript) | ⭐⭐⭐⭐ | TypeScript / Node / web app | Python SDK 的 TS 版 |
| | [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) ⭐ | ⭐⭐⭐⭐⭐ | 打造 Claude-based agent 而非只 API | 內建 tool use loop / file access / sandbox / subagent 編排；跟 Claude Code 同 runtime、想看內部運作直接讀 source。★ 6k+、MIT |
| | [claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript) | ⭐⭐⭐⭐ | Node / web app 環境 Claude agent | Claude Agent SDK TS 版。★ 1.4k+ |
| | [Anthropic Cookbook（進階）](https://github.com/anthropics/anthropic-cookbook) | ⭐⭐⭐⭐ | 想看官方進階 SDK pattern | 特別是 `prompt_caching.ipynb` / `tool_use/` / `multimodal/` 三個 notebook |
| **Deployment** | [BentoML](https://github.com/bentoml/BentoML) | ⭐⭐⭐⭐ | 把 agent 包成 production API service | Docker + serving framework。★ 8k+、Apache 2.0 |
| | [LangServe](https://github.com/langchain-ai/langserve) | ⭐⭐⭐⭐ | LangChain agent 快速 deploy | 底層 FastAPI |
| | [vLLM](https://github.com/vllm-project/vllm) | ⭐⭐⭐⭐ | 自架開源 LLM 取代付費 API | 高吞吐量 LLM serving、Llama / Qwen 等。★ 79k+、Apache 2.0 |
| **中文 deploy / fine-tune** | [datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) | ⭐⭐⭐⭐ | 中文團隊要自架開源 LLM | training-to-deployment 完整中文指南、Qwen / Llama / GLM / 多模態。★ 30k+、Apache 2.0 |
| | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | ⭐⭐⭐⭐⭐ | 要 fine-tune 開源 LLM（不只 prompt eng）| 100+ 模型統一 SFT/DPO/PPO/GRPO、Web UI 零 code、中文社群最廣。★ 70k+、Apache 2.0 |
| **Multi-Agent 案例研究** | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | ⭐⭐⭐⭐⭐ | 想看角色分工 + artifact 交接 pattern | SOP-based PM / Architect / Engineer multi-agent team、PRD → 設計 → code 一路產出。★ 67k+、MIT |
| | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | ⭐⭐⭐⭐ | 想看 agent debate / peer-review pattern | 對話式軟體開發、agents 在 design / code / test 互相辯論。★ 33k+、Apache 2.0、有 zh README |
| | [princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent) | ⭐⭐⭐⭐ | 理解為什麼 tool 設計 > prompt tuning | Agent-Computer Interface (ACI) 設計思路、Princeton paper-backed、SWE-Bench 領先方法。★ 19k+、MIT |

> 🌳 **Claude 原生 subagent 機制**（不用 framework 也能 multi-agent）見 [Stage 5.5](05-claude-code-ecosystem.md#55--subagentsclaude-code-原生-multi-agent-機制)。本 stage 重 framework / production；Stage 5.5 重 markdown-based subagent 編排。

## ✅ Stage 7 之後的自我檢查

你能不能：
- [ ] 設計一個 multi-agent 系統，協作協定講得清楚
- [ ] 在 CI 跑自動 eval pipeline
- [ ] 把 observability（tracing）接到 production agent
- [ ] 在真實 workload 上量測 prompt caching 前後的成本差異
- [ ] 把 agent deploy 到雲端（任何 provider）

如果都可以 → 你已經跑完主路線。挑一個[特化分支](../README.md#️-7-階段學習地圖)，或回過頭來貢獻這份 repo。

## 💡 接下來

你已經有基礎能力了。接下來 6-12 個月應該專注在：
1. **挑一個 production 系統** 從 prototype 推到 production
2. **回饋上游**（LangGraph、AutoGen、MCP servers、Anthropic cookbook）
3. **讀論文**——agent 研究進展很快
4. **做出看得到的東西**——開源一個真的工具，不要再寫教學了
