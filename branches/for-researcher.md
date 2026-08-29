# 研究人員延伸路線（For Researchers）

> **繁體中文** | [简体中文](./for-researcher.zh-Hans.md) | [English](./for-researcher.en.md)

[← 回主路線](../README.md)

<!-- freshness: canonical=branches/for-researcher.md; verified_on=2026-08-29; scope=research-tools,citations,privacy,reproducibility,project-status; max_age_days=90 -->

<a id="使用情境研究階段-ai-怎麼幫"></a>

## 📌 這條路幫你做什麼

這一頁不是要讓 AI 替你當研究者。它要幫你做一件更簡單的事：**找到資料、看懂資料，再確認答案真的有資料支持。**

- 會用終端機或 Python：完成 [Track A 的 A3](../tracks/cli/A3-cli-production.md) 或 [Track B 的 Stage 7](../stages/07-multi-agent-production.md) 後再來。
- 不寫程式：也可以直接做下面的第一個練習。只需要瀏覽器和一篇公開 paper。

## 🎯 學習目標

完成這一頁後，你可以：

1. 分清「AI 說了什麼」和「原文真的寫了什麼」。
2. 逐條核對引用來源，而不是看到引用編號就相信答案。
3. 知道哪些資料可以上傳，哪些資料要先問機構或資料擁有者。
4. 保存足夠紀錄，讓自己或同事能重新做一次。

## 🧩 八個核心詞

- **Source（來源）**：你拿來查證的原始材料，例如 paper、資料集或研究紀錄。像答案後面的課本。
- **Claim（主張）**：一句可以被檢查的說法，例如「方法 A 在資料集 B 上比較好」。
- **Citation（引用）**：帶你回到來源位置的路標。它只說「去這裡看」，不保證那裡真的支持主張。
- **Source Verification（來源核對）**：打開原文，檢查作者寫的內容、範圍與限制是否和答案一致。
- **Literature RAG（文獻 RAG）**：先從你允許使用的文獻找片段，再把片段交給模型回答。像先翻書再作答。
- **Reproducibility（可重現性）**：別人拿到你的資料、步驟、版本與設定後，可以重新跑出可比較的結果。
- **Private Data（私人資料）**：不能任意公開或上傳的內容，例如受試者資料、病歷、未公開手稿與公司機密。
- **Human Review（人工審查）**：由人對 claim、citation、程式、表格與最後決定負責。AI 不能替你簽名或承擔責任。

<a id="文獻-rag--qa"></a>
## 🛠 第一個練習：核對一篇 paper 的三個答案

上傳前先確認 **授權或著作權** 與 **工具條款** 都允許。paper 公開可讀，不等於可以交給另一個服務。

使用公開 paper：[Attention Is All You Need](https://arxiv.org/abs/1706.03762)。把 paper 加進能顯示 citation 的工具，再直接複製下面這段：

```text
請只根據這篇 paper 回答下面三題。每個答案都要附 citation；找不到證據就寫「unsupported／未支持」，不要猜。

1. 這篇 paper 想解決什麼問題？
2. 作者提出的方法包含哪些主要部分？
3. 作者用哪些實驗支持結果，又說了哪些限制？

回答後，列出每個 citation 對應的 original text。不要把你的推測寫成作者的 claim。
```

接著做三個動作：

1. 點開每一個 citation。
2. 把答案和 original text 放在一起讀；數字、資料集與適用範圍都要相同。
3. 原文沒有支持的句子標成 **unsupported／未支持**，不要為了讓答案看起來完整而補一個不相干的引用。

<a id="層級建議"></a>
## 📚 先選一個入口

| 你現在想做的事 | 先用什麼 | 為什麼 | 推薦度 |
|---|---|---|---|
| 用瀏覽器問一篇 paper | [Gemini Notebook（原 NotebookLM）](https://notebooklm.google.com/) | 上傳來源後可從 citation 回到原文，最容易開始 | ⭐⭐⭐⭐⭐ |
| 整理自己的文獻庫 | [Zotero](https://www.zotero.org/) | 先把 PDF、作者、年份與筆記放好，再談 AI | ⭐⭐⭐⭐⭐ |
| 用 Python 做可重跑的文獻 RAG | [PaperQA2](https://github.com/Future-House/paper-qa) | 回答以科學文件和引用為中心，適合學程式化流程 | ⭐⭐⭐⭐⭐ |

Gemini Notebook 是 Google 在 2026-07-16 對 NotebookLM 使用的現行名稱；舊名稱只保留來幫你辨識。citation 是查證入口，不是「答案一定正確」的保證。

## ✅ 完成檢查與下一站

- [ ] 我核對了三個答案，不只看 citation 編號。
- [ ] 我至少找到一個「原文支持」或「未支持」的例子。
- [ ] 我沒有上傳未獲允許的私人資料。
- [ ] 我保存了來源、問題、工具名稱、日期與自己的判斷。

下一站：想做文獻 RAG，走 [Stage 6](../stages/06-memory-rag.md)；想讓多個 agent 分工，走 [Stage 7](../stages/07-multi-agent-production.md)；想把流程接到外部工具，再看 [MCP／Skills catalog](../resources/mcp-skills-catalog.md)。

<details markdown="1">
<summary>⏱ 展開：時間、帳號、費用與資料安全</summary>

第一個練習約需 20–40 分鐘。私人資料先停下來確認 IRB、機構政策、合約、資料擁有者同意與工具條款。

[Gemini Notebook 隱私說明](https://support.google.com/gemininotebook/answer/17004255)指出，一般內容不會直接拿來訓練基礎模型，除非使用者選擇提供 feedback；feedback 可能連同內容交由人員檢視。這不等於你的研究資料自動獲准上傳。病歷、受試者資料、未公開稿件與公司機密仍要遵守自己的治理規則。

付費功能、配額與機構帳號規則會改變。開始前看官方頁面，不在教材保存容易過期的固定價格。

</details>

<a id="必修閱讀"></a>
<details markdown="1">
<summary>📖 展開：建議閱讀順序</summary>

1. [Gemini Notebook citation 說明](https://support.google.com/gemininotebook/answer/16179559)：學會從回答回到原文。
2. [Gemini Notebook 更名公告](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)：確認現行名稱與產品定位。
3. [Zotero 文件](https://www.zotero.org/support/)：先把來源管理好。
4. [PaperQA2 README](https://github.com/Future-House/paper-qa)：再看程式化 literature RAG。
5. [AI Scientist v2 LICENSE](https://github.com/SakanaAI/AI-Scientist-v2/blob/main/LICENSE)：進階研究自動化前先讀使用邊界。

</details>

<a id="精選-projects"></a>
<a id="大綱與寫作"></a>
<a id="文獻管理整合"></a>
<details markdown="1">
<summary>⭐ 展開：完整研究工具與專案表</summary>

<small>工具名稱、授權與 repository 狀態於 2026-08-29 UTC 依官方頁面與 GitHub API 查核。推薦度是本學習地圖的編輯評分，不是 GitHub stars 或排行榜。</small>

<table>
<thead><tr><th scope="col">分類</th><th scope="col">官方工具／專案</th><th scope="col">適合做什麼</th><th scope="col">狀態／授權</th><th scope="col">先知道的限制</th><th scope="col">推薦度</th></tr></thead>
<tbody>
<tr><th scope="rowgroup" rowspan="3">開始與整理</th><td><a href="https://notebooklm.google.com/">Gemini Notebook（原 NotebookLM）</a></td><td>用來源做問答並回到 citation</td><td>正式可用；雲端服務</td><td>引用仍要逐條核對；私人資料先看政策</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://www.zotero.org/">Zotero</a></td><td>管理 PDF、metadata、筆記與引用</td><td>正式可用；桌面／Web</td><td>它先解決來源管理，不會替你判斷研究品質</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/Future-House/paper-qa">Future-House/paper-qa</a></td><td>用 Python 建立 citation-grounded literature RAG</td><td>活躍；Apache-2.0</td><td>需要設定模型與文獻來源，品質仍要自己評測</td><td>⭐⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="4">探索與寫作</th><td><a href="https://github.com/assafelovic/gpt-researcher">assafelovic/gpt-researcher</a></td><td>多來源搜尋與 research brief</td><td>活躍；Apache-2.0</td><td>適合找候選來源，不是引用正確性的最後裁判</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/stanford-oval/storm">stanford-oval/storm</a></td><td>先整理多個觀點，再寫大綱與長文</td><td>可用；MIT；更新較慢</td><td>使用前先確認依賴與資料來源仍相容</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/kaixindelele/ChatPaper">kaixindelele/ChatPaper</a></td><td>中文 paper 摘要、翻譯與寫作輔助</td><td>可用；自訂條款</td><td>不是標準 SPDX 授權；商業或散布前先讀條款</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/MuiseDestiny/zotero-gpt">MuiseDestiny/zotero-gpt</a></td><td>在 Zotero 閱讀時和文獻互動</td><td>可用；AGPL-3.0</td><td>外掛與模型設定要另外維護</td><td>⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="2">研究自動化</th><td><a href="https://github.com/flonat/flonat-research">flonat/flonat-research</a></td><td>參考研究用 skills、agents、hooks 與 LaTeX 流程</td><td>活躍；MIT</td><td>是基礎建設範例，不是每個領域都可直接套用</td><td>⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/SakanaAI/AI-Scientist-v2">SakanaAI/AI-Scientist-v2</a></td><td>研究端到端 multi-agent 實驗架構</td><td>研究參考；自訂 source-code license</td><td>不是作者替代品，也不是可直接投稿的保證</td><td>⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="1">歷史</th><td><a href="https://github.com/langchain-ai/open_deep_research">langchain-ai/open_deep_research</a></td><td>閱讀早期 deep-research agent 架構</td><td>已封存；MIT</td><td>只作歷史參考；新專案請改用仍在維護的工具</td><td>⭐⭐⭐⭐⭐</td></tr>
</tbody>
</table>

</details>

<a id="研究流程-marketplace"></a>
<a id="multi-llm-研究組合本-repo-維護者的研究-setup"></a>
<a id="multi-agent-for-research"></a>
<a id="必練流程按使用頻率"></a>
<details markdown="1">
<summary>🧪 展開：把單篇練習變成可重跑研究流程</summary>

### 文獻 inbox

1. 先保存 DOI、URL、作者、年份與取得日期。
2. 讓工具產生摘要，但把每個 claim 連回原文。
3. 人工決定「閱讀、排除、待確認」，並記下理由。

### 跨 paper synthesis

先問每篇 paper 各自說什麼，再比較它們在哪裡同意、衝突或使用不同條件。不要先要求模型寫一個看起來完整的故事，才回頭找引用。

### 程式與實驗

保存資料版本、environment、seed、prompt、模型／工具版本、輸出與人工修改。能重新執行不代表結論正確，但沒有這些紀錄，錯誤通常更難找到。

### 投稿前

逐一核對 claim、citation、表格、圖、程式與期刊規範。AI 可以提供第二雙眼睛；作者仍要做最後判斷並依期刊政策揭露使用方式。

</details>

<details markdown="1">
<summary>🧯 展開：常見錯誤、替代方案與排錯</summary>

| 問題 | 先怎麼做 |
|---|---|
| citation 點開後沒有支持答案 | 把句子標成未支持；縮小問題；不要換一個看似相關的引用硬補 |
| 工具讀不到掃描 PDF | 先做 OCR，再抽查頁碼與公式有沒有壞掉 |
| 多篇 paper 的結論被混在一起 | 要求每個 claim 都列 paper 名稱、頁碼或段落，再做 synthesis |
| 資料不能上傳雲端 | 使用機構核准環境；必要時看 [Stage 6](../stages/06-memory-rag.md) 的本機 RAG 路線 |
| 自動化太複雜 | 回到「一篇 paper、三個問題、逐條核對」，確認小流程可靠後再加工具 |

沒有任何工具可以代替 IRB、資料治理、作者責任或領域專家的判斷。

</details>
