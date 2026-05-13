> [繁體中文](./README.md) | [简体中文](./README.zh-Hans.md) | **English**

# `examples/` — Runnable hands-on exercises

> [← Back to main path README](../README.en.md)

Every stage in the learning roadmap has a "Hands-on Exercises" section that tells you *what* to do. This folder adds the **actual runnable starter code** — copy → install deps → `python starter.py` → see expected output.

## Directory layout

```
examples/
├── stage-3/                     # Tool Use & Agent intro
│   ├── 03-react-from-scratch/   # Exercise 3: ReAct from scratch
│   │   ├── starter.py           # Main program (~70 LOC runnable)
│   │   ├── test.py              # Self-check (pure assert, no pytest)
│   │   ├── README.md            # 200-400-word walkthrough (+.zh-Hans.md +.en.md)
│   │   └── requirements.txt     # Pinned deps
│   └── ...
├── stage-1/
└── ...
```

Short exercises (≤30 LOC) stay inline as `<details>` blocks in the stage doc — no folder. Longer ones (>30 LOC) get their own folder so stage docs don't get bloated by code blocks.

## How to run any example

```bash
cd examples/stage-3/03-react-from-scratch
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...   # Each example header lists the key it needs
python starter.py                     # Hits the real API to see output (~$0.001 in credits)
python test.py                        # Runs validation (mock-based, free)
```

## Design rules

| Dimension | Rule |
|---|---|
| Program length | starter ≤80 LOC, split if longer |
| Dependencies | stdlib + ≤2 pip packages, pinned versions |
| Tests | Plain `assert`, no pytest; reader runs `python test.py` to see ✅ |
| Comments | Chinese (zh-TW primary), English variable / function names |
| Self-check | Every starter.py ends with a `# === Self-check ===` block |
| Environment vars | Header comment must list required keys |
| Free-tier friendly | Use the cheapest model (claude-haiku / Ollama); note how to switch to Sonnet |
| **Windows encoding** | **Every .py must reconfigure stdout to UTF-8** (see below) |

### Windows cp950 encoding fix (mandatory in every starter.py / test.py)

Windows consoles default to cp950 (Big5) and can't print emoji or non-Big5 Chinese. Add this right after imports in every `.py`:

```python
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
```

Without it, Windows readers running in PowerShell / cmd hit `UnicodeEncodeError: 'cp950' codec can't encode character '✅'`.

## Three paths — **default is Ollama (cost-driven)**

> 💰 **Why default to Ollama?** Running 1000 practice iterations on Sonnet costs ~$4; on haiku ~$0.25; on local Ollama $0. **API cost should not block learning.** Reserve cloud LLMs for "want to see high-quality answers / production deployment".

Every exercise ships with all three paths:

### Path A (**default, recommended**) — local Ollama
- Default `starter.py` / first inline `<details>` block uses a local model
- Requires [Ollama](https://ollama.com); pull a model based on the stage:
  - **Stage 1 + 2** (plain chat / prompt eng): `ollama pull gemma3:4b` (3.3 GB; CPU-friendly)
  - **Stage 3+** (tool use / agent): `ollama pull qwen2.5:3b` (1.9 GB; reliable tool-use support)
- $0, offline, fine for privacy-sensitive data
- SDK uses the `openai` package (OpenAI-compatible API) with `base_url="http://localhost:11434/v1"`
- Best for: all readers (this is the default recommendation)

### Path B (optional) — Anthropic API (when you want cloud quality)
- Companion `starter_anthropic.py` (folder) or the second inline `<details>` block
- Requires `ANTHROPIC_API_KEY`; ~$0.001 per run (haiku) / ~$0.004 (sonnet)
- Higher answer quality and lower latency than local 3-4B Ollama models
- Best for: production-quality demands, long-context work, the Stage 7 production tier

### Path C (verify logic, no API call)
- Every `test.py` uses `unittest.mock`; `python test.py` validates code logic without spending
- Complements A / B — mock first, then real call

### Trade-offs

| Dimension | A Ollama (default) | B Anthropic | C Mock |
|---|---|---|---|
| Cost per call | $0 | ~$0.001-0.004 | $0 |
| Requires | Ollama install | API key | nothing |
| Answer quality | medium (3-4B model) | high | canned, unrepresentative |
| Speed | 5-30 s/call (no GPU) | ~1-3 s/call | <0.1 s |
| Offline | ✅ | ❌ | ✅ |
| Privacy-sensitive data | ✅ | ❌ | ✅ |
| Stage 3+ tool use | ✅ (qwen2.5 / llama3.2) | ✅ | ✅ |
| Best for | **default, no budget pressure** | production upgrade | logic verification |

→ **Recommended flow**: C first (validate logic, no cost), then A (see real model behaviour locally), then B at the Stage 7 production stage if cloud quality is needed.

## Index by stage

| Stage | Exercises | Example location |
|---|---|---|
| 1 LLM basics | 6 | inline 4 + folder 2 (`examples/stage-1/`) |
| 2 Prompt engineering | 4 | all inline |
| **3 Tool use** | **6** | inline 1 + folder 5 (`examples/stage-3/`) |
| 4 Frameworks | 5 | all folder (`examples/stage-4/`) |
| 5 Claude Code ecosystem | 11 | inline 6 + folder 5 (`examples/stage-5/`) |
| 6 Memory/RAG | 5 | all folder (`examples/stage-6/`) |
| 7 Multi-agent | 5 | inline 1 + folder 4 (`examples/stage-7/`) |
| Track A1-A3 | 12 | all inline + 2 small folders (CLI-9 / CLI-10) |

→ T1 scope: **Stage 3 全 6 exercises only** (remaining stages roll out per plan tiers).

## Contributing / reporting issues

If something doesn't run, output doesn't match expectations, or you want to add a new example:
- File an issue tagged `examples`
- Or open a PR following the "Design rules" table above

## Why this split (instead of stuffing everything into stage docs)

1. **Stage docs stay readable** — roadmap readers don't always want code, they want concepts; long code blocks break that
2. **Examples evolve independently** — SDK bumps, model rename, example needs its own commit without polluting the roadmap's git log
3. **Readers can clone one example** — `svn export` or `git clone --filter=tree:0` grabs a single folder
4. **Future CI** — example failures shouldn't block mdbook deploy; this split lets CI run examples conditionally
