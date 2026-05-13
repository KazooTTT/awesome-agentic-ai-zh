> **繁體中文** | [简体中文](./README.zh-Hans.md) | [English](./README.en.md)

# `examples/` — 動手練習可跑範例

> [← 回主路線 README](../README.md)

學習地圖每個 stage 都有「動手練習」section、講「該做什麼」。這個資料夾補上**真的可以跑的範例 code**——複製 → 裝依賴 → `python starter.py` 看到預期輸出。

## 目錄結構

```
examples/
├── stage-3/                     # Tool Use & Agent 入門
│   ├── 03-react-from-scratch/   # 練習 3：從零實作 ReAct
│   │   ├── starter.py           # 主程式（~70 行可跑）
│   │   ├── test.py              # 自我驗證（pure assert、無 pytest）
│   │   ├── README.md            # 200-400 字走查（+.zh-Hans.md +.en.md）
│   │   └── requirements.txt     # 依賴釘版本
│   └── ...
├── stage-1/
└── ...
```

短的練習（≤30 LOC）直接以 `<details>` 收摺塞在 stage 檔內、不開資料夾。長的（>30 LOC）才開資料夾——避免 stage 檔被 code block 撐爆。

## 怎麼跑任一個範例

```bash
cd examples/stage-3/03-react-from-scratch
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...   # 各範例頂端會說它要哪個 key
python starter.py                     # 跑真的 API 看輸出（會花一點點錢、約 $0.001）
python test.py                        # 跑驗證（用 mock、不花錢）
```

## 設計原則

| 維度 | 規則 |
|---|---|
| 程式長度 | starter ≤80 LOC、超過拆檔 |
| 依賴 | stdlib + 最多 2 個 pip 套件、釘版本 |
| 測試 | 純 `assert`、不用 pytest、reader 跑 `python test.py` 看 ✅ |
| 註解 | 中文（zh-TW 為主）、變數 / 函式名英文 |
| 自我驗證 | 每個 starter.py 結尾必有 `# === 自我驗證 ===` 區塊 |
| 環境變數 | 頂端註解寫清楚需要哪些 key |
| Free-tier 友善 | 用最便宜 model（claude-haiku / Ollama）、註解寫怎麼換 Sonnet |
| **Windows 編碼** | **每個 .py 頂端必須有 UTF-8 reconfigure**（見下） |

### Windows cp950 編碼 fix（每個 starter.py / test.py 必加）

Windows 預設 console 是 cp950（Big5）、印不出 emoji 跟非 Big5 中文。每個 `.py` 檔頂端 import 區後立刻加：

```python
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
```

否則 Windows reader 在 PowerShell / cmd 跑會炸 `UnicodeEncodeError: 'cp950' codec can't encode character '✅'`。

## 三條路徑 — **默認用 Ollama（成本考量）**

> 💰 **為什麼默認 Ollama？** 練習場景跑 1000 次跑滿 Sonnet ~$4、跑 haiku ~$0.25、跑本機 Ollama $0。**學習階段不該被 API 成本卡住**。Cloud LLM 留給「想看高品質答案 / production deployment」時用。

每個練習都同時提供 3 條路徑：

### Path A（**默認、推薦**）— Ollama 本機
- 預設 `starter.py` / 第一個 inline `<details>` 用本機 LLM
- 需 [Ollama](https://ollama.com)、按 stage pull 對應 model：
  - **Stage 1 + 2**（純 chat / prompt eng）：`ollama pull gemma3:4b`（3.3 GB、CPU 跑也通）
  - **Stage 3+**（tool use / agent）：`ollama pull qwen2.5:3b`（1.9 GB、tool-use 支援穩定）
- 全程 $0、offline、隱私敏感資料 OK
- SDK 用 `openai` package（OpenAI-compatible API）、`base_url="http://localhost:11434/v1"`
- 適合：所有讀者（默認推這條）

### Path B（選擇性）— Anthropic API（想看 cloud 高品質時）
- 對照 `starter_anthropic.py`（folder）或第二個 inline `<details>` 區塊
- 需 `ANTHROPIC_API_KEY`、跑一輪約 $0.001（haiku）/ $0.004（sonnet）
- 答案品質 / latency 都比本機 Ollama 強
- 適合：production 要求高品質、需要 long-context、Stage 7 production tier

### Path C（驗邏輯、不打 API）
- 所有 `test.py` 都用 `unittest.mock`、`python test.py` 看程式邏輯有沒有寫對
- 跟 Path A / B 互補：先 mock 驗邏輯、再 real call 確認

### 三條路的 Trade-off

| 維度 | A Ollama（默認）| B Anthropic | C Mock |
|---|---|---|---|
| Cost / call | $0 | ~$0.001-0.004 | $0 |
| 需要 | Ollama install | API key | 無 |
| 答案品質 | 中（3-4B model） | 高 | 預設、看不出真實品質 |
| 速度 | 5-30s/call（無 GPU） | ~1-3s/call | <0.1s |
| Offline | ✅ | ❌ | ✅ |
| 隱私敏感資料 | ✅ | ❌ | ✅ |
| Stage 3+ tool use | ✅（qwen2.5 / llama3.2） | ✅ | ✅ |
| 適合 | **默認、無預算壓力** | production 升級 | 程式邏輯驗證 |

→ **建議流程**：先 C 驗邏輯（不花錢）、再 A 本機跑看實際 model 行為、production 階段（Stage 7）再升 B 看 cloud 品質。

### 怎麼從 Ollama 換到 Anthropic？

每個練習都有 `<details>` Path B 區塊或 `starter_anthropic.py`、改 3 行：

```python
# 從這個（Path A 默認）：
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
r = client.chat.completions.create(model="gemma3:4b", ...)

# 換成這個（Path B、若有 ANTHROPIC_API_KEY）：
import anthropic
client = anthropic.Anthropic()
r = client.messages.create(model="claude-haiku-4-5", ...)
```

主要差異：messages create 方法名、response shape（`choices[0].message.content` vs `content[0].text`）、tool spec wrap（OpenAI 多一層 `{"type": "function", "function": {...}}`）。詳細對照表見 [`resources/cli-agents-guide.md`](../resources/cli-agents-guide.md)。

## 對應 stage 索引

| Stage | 練習 | 範例位置 |
|---|---|---|
| 1 LLM 基礎 | 6 個 | inline 4 + folder 2（`examples/stage-1/`） |
| 2 Prompt eng | 4 個 | 全 inline |
| **3 Tool use** | **6 個** | inline 1 + folder 5（`examples/stage-3/`） |
| 4 Frameworks | 5 個 | 全 folder（`examples/stage-4/`） |
| 5 Claude Code 生態 | 11 個 | inline 6 + folder 5（`examples/stage-5/`） |
| 6 Memory/RAG | 5 個 | 全 folder（`examples/stage-6/`） |
| 7 Multi-agent | 5 個 | inline 1 + folder 4（`examples/stage-7/`） |
| Track A1-A3 | 12 個 | 全 inline、外加 2 個小 folder（CLI-9 / CLI-10） |

→ T1 完成範圍：**只有 Stage 3 全部 6 個**（剩餘 stage 按 plan 分批推進）。

## 貢獻 / 報錯

跑不過、結果跟預期輸出對不上、或想補一個新練習：
- 開 issue 標 `examples` label
- 或直接 PR、follow 本資料夾「設計原則」表格的規則

## 為什麼這樣分（不直接全塞 stage 檔）

1. **Stage 檔保持 readable**：學習地圖讀者不一定要看 code、只想理解 concept；長 code block 干擾閱讀流
2. **範例可獨立演進**：API SDK 升版、model name 改、範例需要單獨 commit、不污染學習地圖 git log
3. **Reader 可以 clone 單一 example**：`svn export` 或 `git clone --filter=tree:0` 只抓一個資料夾
4. **未來 CI**：example 失敗不應 block mdbook deploy；分開可讓 CI 有條件性檢查
