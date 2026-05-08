# 給教師 — 專業分支

> **繁體中文** | [简体中文](./for-teacher.zh-CN.md) | [English](./for-teacher.en.md)

> [← 回主路線 README](../README.md) · 走完 **Track A 的 A3** 或 **Track B 的 Stage 7** 後從這裡接續。把 agentic AI 應用到教學流程上。

## 使用情境

- 教案生成
- Quiz / 評分量表（rubric）建立
- 投影片準備
- 學生回饋整理
- 課程地圖

## 精選 Projects

### 教學流程 Skills

（大多數還沒有做成 skill marketplace。這個分支最有社群貢獻空間——見 CONTRIBUTING.md。）

### 可用的基礎元件

#### [obra/superpowers](https://github.com/obra/superpowers) ⭐⭐⭐⭐
通用的寫作 / 腦力激盪 skill。可改用在備課上。

#### [Claude Code](https://github.com/anthropics/claude-code)（搭配自訂 CLAUDE.md）⭐⭐⭐⭐⭐
★ 120k+ — 教師很適合先從這裡開始。低門檻先用 Claude.ai（網頁版）試水溫；如果是會重複的流程，再升級到 Claude Code。

### 教學課程素材（給教師備課用）

#### [huggingface/agents-course](https://github.com/huggingface/agents-course) ⭐⭐⭐⭐

| 欄位 | 內容 |
|---|---|
| Stars | ★ 28k+ |
| License | Apache-2.0 |

**教什麼**：Hugging Face 官方的 agent 課程——notebook、練習、結業認證。是一份**現成的「AI agent 教學」素材**。

**適合誰**：要在學校 / 工作坊開「AI agent 入門」課程的老師，可以直接拿來當教材或改編。

**備註**：注意這是「教 AI agent 怎麼建」的教材，不是「老師用 AI 教書」的工具。

---

#### [datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) ⭐⭐⭐⭐（中文）

| 欄位 | 內容 |
|---|---|
| 語言 | 中文（zh-CN） |
| Stars | ★ 13k+ |
| License | NOASSERTION |

**教什麼**：Datawhale 出品的中文 LLM 應用開發課程——含 RAG、agent、章節練習。中文教師備課的現成模板。

**適合誰**：中文教師要找現成可改的 LLM 教材底稿、再針對自己學生程度調整。

**備註**：跟 hf agents-course 一樣，是「教學生建 LLM 應用」的教材，不是「教師端的 AI 助教」。

---

### Prompt 素材庫

#### [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) ⭐⭐⭐⭐

| 欄位 | 內容 |
|---|---|
| Stars | ★ 161k+ |
| License | NOASSERTION（CC0 / public domain 風格，但未提供 SPDX） |

**教什麼**：社群維護的 prompt 大全——「act as X」型樣板涵蓋幾百種角色（老師、面試官、stand-up comedian、辯論者⋯）。教師可以拿來當「prompt 寫法範例」教給學生，或直接借用其中合適的當作課堂示範。

**適合誰**：要教學生「prompt engineering」的老師，找現成例子比較不同寫法的差異。

**備註**：品質不一致——當作素材庫挑選用，不是「全部直接拿去教」。

---

### 閱讀材料

#### [The Effortless Academic — Beginner Guides](https://effortlessacademic.com/claude-code-and-cowork-for-academics-beginner-guide-part-1/)
寫給學術工作者導入 Claude Code 的多篇指南，教師也適用。

## 可以建的流程

這些是模板——配合你的學科自行調整：

- **教案生成器**：用課綱 + 主題提示 → 大綱 → 投影片 → 評量
- **Rubric 建立**：學生作業樣本 + 學習目標 → rubric 草稿
- **個別化回饋**：學生作業 + rubric → 個別化文字回饋（要人工把關）

### 3 個可直接複製的 prompt 範本

**1. 教案大綱生成**（複製到 Claude.ai 即可用）：
```
你是一位 [學科] 老師。我要給 [年級] 學生上一堂 [時長] 分鐘的課，主題是「[主題]」。
學生先備知識：[簡述]。請產出：
1. 學習目標（3-4 條，用 Bloom's taxonomy 動詞）
2. 課程大綱（含時間分配）
3. 1 個課堂活動 / 討論題
4. 1 個課後評量題
不要產生超出我給的主題範圍的內容。
```

**2. Rubric 草稿生成**：
```
我有一份 [作業類型] 作業，學生年級 [年級]，主題 [主題]。
學習目標：[列 2-3 條]。
請產出一份 4 級 rubric（卓越 / 熟練 / 發展中 / 待改進），
每級在「內容深度」「組織結構」「論證 / 計算」「表達清晰度」4 個面向各給一段描述。
描述要具體可觀察，不用「品質好」這種模糊詞。
```

**3. 學生回饋整理**：
```
以下是 [N] 份學生作業片段：
[貼上文本]

請：
1. 摘要這批作業共同的 3 個強項
2. 摘要 3 個共同弱點
3. 針對最常見弱點，建議 1-2 個下次上課該加強的環節
不要做個別化評語——我會自己針對個人寫。
```

## 隱私 + 倫理（重要）

教師端用 LLM 跟一般 user 不同，**牽涉學生資料**——以下是 hard rule：

- **不要把學生個資丟進公開 LLM**（姓名、學號、聯絡方式、成績）。需要的話先匿名化（用「學生 A / B / C」）
- **AI 輔助 ≠ AI 評分**：用 LLM 草擬回饋 / rubric 沒問題，但**最終評分一定要人工把關**——LLM 對複雜思考的評估還不可靠
- **告知學生**：如果課堂材料是 AI 輔助生成，建議向學生揭露（比照論文揭露 AI 工具使用）。教學誠信很重要
- **檢查事實**：LLM 會編造引用、學者名字、研究數據。專業領域內容**必須核對**才能上課
- **學生作品的著作權**：不要把學生作品用 LLM 大量分析後上傳到第三方 service，可能踩 FERPA / GDPR / 個資法

如果你的學校 / 機構有 AI 使用政策，**那份比這份優先**。

## 給教師的層級建議

大多數教師應該停在 **Tier 0（瀏覽器聊天）**或 **Tier 1（Claude Desktop）**：

- **Tier 0**：Claude.ai 網頁版聊天——複製貼上 prompt，免安裝
  - 適合：偶爾備課、單次任務、出題、寫信
  - 例子：複製上面的「教案大綱生成」prompt，填入主題就跑
- **Tier 1**：Claude Desktop / [NotebookLM](https://notebooklm.google.com/)——可上傳檔案、保留對話歷史
  - 適合：批改 / 整理一整學期資料、做課程地圖、整批匯入課本 PDF 後問問題
  - 例子：上傳整門課的 reading list PDF 到 NotebookLM，學期中可以隨時 query
- **Tier 2+ (CLI / SDK)**：只有當你開始**自動化重複流程**才需要
  - 例子：每週固定收 30 份作業 → 自動生成回饋初稿
  - 不熟程式的老師可以**找學校的 IT 同事 / 學生 RA 幫忙**設定，自己只用結果

> 升級到 Tier 2+ 就建議走 [Track A — CLI Power User](../tracks/cli/A1-cli-intro.md)。

## 也適用其他分支

很多老師同時是研究員 / 知識工作者，這幾個分支重疊：

- **也做研究**（找文獻、寫 paper、整理 references）→ [研究員分支](./for-researcher.md)
- **要寫報告 / 整理會議記錄 / 跨工具整合**（Notion、Excel、Email）→ [知識工作者分支](./for-knowledge-worker.md)
- **要把 AI 接到 Notion / Obsidian / 飛書** 等日常工具 → [`resources/mcp-skills-catalog.md`](../resources/mcp-skills-catalog.md)

## 社群備註

這個分支目前是精選內容最少的一塊。特別歡迎以下貢獻：

- 教案生成 skill
- 學科專屬的 prompt library（國文老師的 prompts、數學老師的 prompts、英文老師的 prompts ⋯）
- 教師專屬的 MCP server（成績冊整合、LMS 串接如 Canvas / Moodle / Google Classroom）
- **某學科 + 某年級的完整 case study**（例如「我用 AI 帶國中數學一個學期，這是我的 workflow」）

請見 [CONTRIBUTING.md](../CONTRIBUTING.md)。
