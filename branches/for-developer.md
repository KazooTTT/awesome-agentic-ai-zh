# 開發者延伸路線（For Developers）

> **繁體中文** | [简体中文](./for-developer.zh-Hans.md) | [English](./for-developer.en.md)

[← 回主路線](../README.md)

<!-- freshness: canonical=branches/for-developer.md; verified_on=2026-08-29; scope=coding-agents,tool-identity,permissions,sandboxing,project-status; max_age_days=90 -->

<a id="使用情境開發場景-ai-怎麼幫"></a>

## 📌 這條路幫你做什麼

AI 程式助手像一位會讀檔案、改程式和跑指令的助手。它可以做事，也可能做錯事。這條路先教你把任務縮小、看懂改動，再決定要不要留下。

建議路線：`A1 → A2 → Stage 5 核心 5.1–5.4 → A3`（[A1](../tracks/cli/A1-cli-intro.md)、[A2](../tracks/cli/A2-cli-workflow.md)、[Stage 5](../stages/05-claude-code-ecosystem.md)、[A3](../tracks/cli/A3-cli-production.md)）；Stage 8 建議但不擋本頁。Track B 可先讀 [Stage 7](../stages/07-multi-agent-production.md)。

## 🎯 學習目標

完成這一頁後，你可以：

1. 分清工具的核心身分，以及它在哪些操作介面（surface）出現。
2. 先限制檔案、指令與網路權限，再讓 agent 動手。
3. 用 diff、test、人工 review 與 rollback 管理一次小改。
4. 分開檢查程式品質、agent 行為與 production 觀測資料。

<a id="coding-agents"></a>
## 🧩 八個核心詞

- **IDE（Integrated Development Environment）**：寫程式、看檔案與執行工具的工作桌，例如一個程式編輯器。它是一種操作介面（surface），不等於 agent 的核心身分。
- **Coding Agent（程式代理）**：能讀 code、使用工具、修改檔案並依結果繼續工作的軟體。它可能出現在 CLI、IDE、desktop 或 cloud。
- **Provider／Router（供應商／路由器）**：Provider 提供模型服務；Router 把請求轉送到一個或多個 provider。Router 不是模型，也不替你管理 repo 權限。
- **Model／Runtime（模型／執行環境）**：Model 產生下一步內容；Runtime 負責讓模型在某個地方執行或被呼叫。本機 runtime 不等於 coding agent。
- **Sandbox（沙箱）**：把程式關在有限範圍裡，像只讓小孩在安全遊戲區活動。它降低風險，但不是百分之百保證。
- **Approval（人工批准）**：高風險動作前由人明確說可以。test 通過不代表 agent 自動取得 push、merge 或 deploy 權限。
- **Diff／Rollback（差異／回復）**：Diff 告訴你改了什麼；Rollback 把不想要的改動安全退回。兩個要一起設計。
- **Eval／Observability（評測／可觀察性）**：Eval 用固定案例測品質；Observability 保存執行中的 trace、log、成本與錯誤，幫你知道系統發生什麼事。

### 工具名稱不要混在一起

| 名稱 | 核心身分 | 白話說法 |
|---|---|---|
| OpenCode | Coding agent／harness | 會在程式專案裡讀、改、測 |
| Pi | Coding agent／harness | 從小核心加 extensions、skills 或 RPC |
| OpenRouter | API Router | 把模型請求送到 provider；不會替你改 repo |
| Ollama | Local model runtime | 在本機提供模型執行與 API；本身不是 coding agent |

**Surface（操作介面）**就是你從哪裡使用工具。「工具是什麼」和「從哪裡操作」是兩件事。Cursor、Cline、Continue 都有 coding-agent 能力，也各自提供不只一種 surface；不能只看畫面像 IDE，就把它們縮成 IDE-only 工具。

<a id="code-review"></a>
## 🛠 第一個練習：完成一次可回復的小改

請在可丟棄的 demo repo 或新 branch 操作。直接把下面這段貼給 coding agent：

```text
先做 read-only plan，不要修改任何檔案。

任務：找出 README.md 裡一個可以說得更清楚、但不改變技術意思的句子。
請先回報：
1. 你要改哪一句。
2. 為什麼這是小範圍改動。
3. 我應該執行哪個 test 或文件檢查。
4. rollback 方法。

在我明確人工批准前，不要寫檔。批准後只准修改 README.md。
完成後顯示 git diff -- README.md，並回報 test 結果。
不要 push、merge 或 deploy。
```

收到 plan 後，由 human／人工讀完再批准。修改完成後自己執行：

```powershell
git diff -- README.md
# 接著執行這個 repo 的文件 test 或最小相關 test
```

如果改動不是你要的，先確認 `README.md` 沒有別人的未保存工作，再只 rollback 這個練習產生的改動。不要用會清掉整個工作區的指令。

<a id="推薦工具"></a>
<a id="tier-升級路徑"></a>
## 📚 先選一個入口

| 你現在想做的事 | 先用什麼 | 為什麼 | 推薦度 |
|---|---|---|---|
| 使用有完整 permission 與 sandbox 文件的 agent | [Claude Code](https://code.claude.com/docs/en/overview) | 方便學 plan、權限、diff 與多種操作介面 | ⭐⭐⭐⭐⭐ |
| 使用開源、可換 provider 的 coding agent | [OpenCode](https://github.com/anomalyco/opencode) | 能把 agent、provider 與 Router 分開理解 | ⭐⭐⭐⭐⭐ |
| 從 IDE 開始，但仍保留逐步批准 | [Cline](https://github.com/cline/cline) | IDE、CLI 與 SDK 都有入口，適合比較 surface | ⭐⭐⭐⭐⭐ |

不要只問「哪個最強」。先問它能看到哪些檔案、能跑哪些命令、是否能連網、誰批准高風險動作，以及失敗時怎麼回復。

<a id="也適用其他分支"></a>
## ✅ 完成檢查與下一站

- [ ] 我能說出 coding agent、Router 與 local runtime 的差別。
- [ ] agent 先給 read-only plan，得到人工批准後才改一個檔案。
- [ ] 我讀過完整 diff，也真的執行了對應 test。
- [ ] 我知道如何只回復這次改動，而且 agent 沒有 push、merge 或 deploy。

下一站：要設計 Skills／MCP，走 [Stage 5](../stages/05-claude-code-ecosystem.md)；要做 eval、observability 與 production gate，走 [Stage 7](../stages/07-multi-agent-production.md)；要比較 CLI agents，打開 [CLI agent 指南](../resources/cli-agents-guide.md)。

<details markdown="1">
<summary>⏱ 展開：時間、環境、費用與 secret 邊界</summary>

第一個練習約需 20–40 分鐘。使用可丟棄 repo 或新 branch，先確認 `git status`，不要把同事或 Claude 正在修改的檔案交給另一個 agent 覆蓋。

- API key 放環境變數或工具支援的 secret store，不貼進 prompt、README 或 commit。
- 先關閉不需要的網路、外部目錄與 shell 權限。
- 費用依 model、provider、輸入量與重試次數變動；教材不保存固定「每次多少錢」的猜測。
- Sandbox 只能減少爆炸半徑；外部服務、credential 與人為批准仍要分開保護。

</details>

<details markdown="1">
<summary>📖 展開：建議閱讀順序</summary>

1. [Claude Code overview](https://code.claude.com/docs/en/overview)：先看一個 coding agent 有哪些 surface。
2. [Claude Code permissions](https://code.claude.com/docs/en/permissions)：再看 allow、ask 與 deny。
3. [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)：理解檔案與網路隔離。
4. [Aider Git integration](https://aider.chat/docs/git.html)：了解 auto-commit、diff、undo 與 hook 邊界。
5. [OpenCode V2 docs](https://opencode.ai/v2/docs) 與 [Pi docs](https://pi.dev/docs/latest)：比較可換 provider 的 coding harness。
6. [OpenRouter routing](https://openrouter.ai/docs/guides/routing/provider-selection) 與 [Ollama docs](https://docs.ollama.com/)：確認 Router 與 local runtime 不是 agent。

</details>

<a id="精選-projects"></a>
<a id="社群備註"></a>
<details markdown="1">
<summary>⭐ 展開：完整開發工具與專案表</summary>

<small>工具身分、surface、授權與 repository 狀態於 2026-08-29 UTC 依官方文件與 GitHub API 查核。推薦度是本學習地圖的編輯評分，不是 GitHub stars 或效能排名。</small>

<table>
<thead><tr><th scope="col">分類</th><th scope="col">官方工具／專案</th><th scope="col">核心身分</th><th scope="col">主要 surface</th><th scope="col">適合做什麼</th><th scope="col">權限／限制與狀態</th><th scope="col">推薦度</th></tr></thead>
<tbody>
<tr><th scope="rowgroup" rowspan="9">Agent／harness</th><td><a href="https://code.claude.com/docs/en/overview">Claude Code</a></td><td>coding agent</td><td>CLI／IDE／desktop／cloud</td><td>學 permission、sandbox、project rules 與完整 agent workflow</td><td>商業產品；保留 permission prompt，先從小 repo 開始</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></td><td>coding agent／harness</td><td>terminal／desktop</td><td>切換 provider 或相容 endpoint</td><td>活躍；MIT；V2 專案規則使用 <code>AGENTS.md</code></td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/earendil-works/pi">earendil-works/pi</a></td><td>coding agent／harness</td><td>terminal／SDK／RPC</td><td>從小核心加 extensions、skills 與自訂流程</td><td>活躍；MIT；沒有內建 sandbox，要自己隔離</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/Aider-AI/aider">Aider-AI/aider</a></td><td>coding agent／pair programmer</td><td>CLI</td><td>用 git diff、commit 與 undo 管理小改</td><td>活躍；Apache-2.0；預設 auto-commit 不等於可跳過 hook</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/aaif-goose/goose">aaif-goose/goose</a></td><td>coding／general agent</td><td>CLI／desktop／API</td><td>連接 providers、MCP 與 extensions</td><td>活躍；Apache-2.0；先用低權限 extension</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://cursor.com/docs">Cursor</a></td><td>coding agent + AI editor</td><td>IDE／CLI／cloud／SDK</td><td>從編輯器到背景 agent 的多 surface workflow</td><td>商業產品；每個 surface 的權限與資料邊界分開看</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/cline/cline">cline/cline</a></td><td>coding agent</td><td>IDE／CLI／SDK</td><td>逐步批准工具、檔案與 browser 操作</td><td>活躍；Apache-2.0；不要把 IDE surface 當安全保證</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/continuedev/continue">continuedev/continue</a></td><td>coding agent</td><td>CLI／VS Code／JetBrains</td><td>閱讀既有開源 coding-agent 與 editor 整合</td><td>read-only、不再積極維護；Apache-2.0；官方 2.0.0 是最後版本</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/OpenHands/OpenHands">OpenHands/OpenHands</a></td><td>software-development agent platform</td><td>web／CLI／SDK／cloud</td><td>在 sandbox 中處理較完整的 issue</td><td>活躍；MIT；任務越大越需要 checkpoint 與人工 review</td><td>⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="2">工作流支援</th><td><a href="https://github.com/obra/superpowers">obra/superpowers</a></td><td>skills／workflow collection</td><td>agent plugin／skills</td><td>參考 planning、TDD、debug 與 review 流程</td><td>活躍；MIT；流程模板仍要配合自己的 repo gate</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/yamadashy/repomix">yamadashy/repomix</a></td><td>repo context packer</td><td>CLI／MCP</td><td>整理一次性的 codebase context 給 reviewer 或 agent</td><td>活躍；MIT；輸出前仍要排除 secrets 與不必要檔案</td><td>⭐⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="1">歷史</th><td><a href="https://github.com/RooCodeInc/Roo-Code">Roo Code</a></td><td>歷史 coding agent</td><td>VS Code extension</td><td>閱讀多 mode agent 的設計歷史</td><td>已封存；Apache-2.0；不當新專案現行首選</td><td>⭐⭐⭐</td></tr>
</tbody>
</table>

</details>

<a id="必練流程按使用頻率"></a>
<a id="3-個具體-workflow-recipe"></a>
<details markdown="1">
<summary>🧪 展開：從每日小改走到團隊 workflow</summary>

### 每日開發

`plan → 人工批准 → 小改 → diff → test → review → commit`。每一步都能停下來，才容易找出錯在哪裡。

### PR review

把 agent 的意見當另一位 reviewer 的候選 finding。要求它指出檔案、行為、重現方式與建議測試；沒有證據的「看起來可能有問題」不要直接當阻擋理由。

### CI

CI agent 使用唯讀 token、最小 repository 權限與固定輸入。不要讓來自 issue、PR 或網頁的文字直接變成可執行命令。發布、merge 與 secrets 一律保留額外批准。

### 批次重構

先建立基準測試，再按模組分批。每批都有 checkpoint、diff 與 rollback；不要因為 agent 能改很多檔案，就一次把整個 repo 交出去。

</details>

<a id="常見踩坑anti-patterns"></a>
<details markdown="1">
<summary>🧯 展開：常見錯誤、替代方案與 rollback</summary>

| 問題 | 改成什麼 |
|---|---|
| 看到 IDE 畫面就以為工具只能在 IDE 用 | 分開看核心身分與所有 surface |
| 把 OpenRouter、Ollama、OpenCode 當同一類 | OpenRouter 不是 model，Ollama 不是 coding agent；Router、runtime、coding agent 分開選 |
| agent 說 test 綠就直接接受 | 自己讀 diff、確認 test 覆蓋需求，再人工批准 |
| 用固定行數判斷安全 | 看變更範圍、可測性、可回復性與 diff 是否可讀 |
| Aider 自動 commit 就跳過 hook | 明確啟用專案需要的 verify／hook，再走正常 review gate |
| 多個 agent 同時改同一檔案 | 分清檔案 ownership、使用獨立 worktree，最後人工整合 |

Rollback 前先看 `git status` 和 diff，辨認哪些是這次 agent 的改動。只回復已確認的目標，不要用 broad reset 清掉別人的工作。

</details>
