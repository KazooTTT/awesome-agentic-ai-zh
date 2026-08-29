# Stage 7 Agent Production Engineering 章名與順序計畫

## 目的

讓讀者分清三件事：**Agent Framework** 是工具箱、**Workflow Graph** 是工作地圖、**Graph Engineering** 是設計與維護工作地圖的工程工作；同時讓 Stage 7 的章名能涵蓋 Harness、Loop、Graph、Multi-Agent、Eval、Observability 與 Guardrail。

## 決定

- Stage 3 保留「工具使用與第一個 Agent Loop」。
- Stage 4 保留「Agent Frameworks & Workflow Graphs」，不直接改叫 Graph Engineering。
- Stage 7 使用上位名稱：
  - zh-TW：`Stage 7 — Agent Production Engineering：Harness、Loop 與 Graph`
  - en：`Stage 7 — Agent Production Engineering: Harness, Loops & Graphs`
  - zh-Hans：`Stage 7 — Agent Production Engineering：Harness、Loop 与 Graph`
- 五層 `Prompt → Context → Harness → Loop → Graph` 表示控制範圍由小到大，不是章節編號。
- 課程維持「先做出來、再看見結構、最後做穩」：Stage 2 Prompt／Context 初識 → Stage 3 Agent Loop → Stage 4 Framework／Workflow Graph → Stage 5 Harness 實例 → Stage 6 Context 深化 → Stage 7 Production 整合。

## 圖像決定

2026-08-29 重新檢查最新 `origin/main` 的三語 `agent-engineering-5layer` 圖後，確認它們已經：

- 移除「官方採用／非官方名稱」badge。
- 保留 `Prompt → Context → Harness → Loop → Graph`。
- 明寫「控制範圍往上變大，不是章節順序」。
- 把 Graph Engineering 配對 Workflow Graph，把 Loop Engineering 配對 Bounded Agent Loops。

因此本層不重畫、不改圖片 bytes；避免為了產生新圖而降低文字正確性或破壞已通過的三語圖像契約。

## 修改邊界

- 更新 Stage 7 三語 H1、五層段落自稱、README／index／PROGRESS／ROADMAP／MkDocs／mdBook、Stage 6 出口、Stage 7 examples 返回名稱、DESIGN、TESTING_PLAN、CHANGELOG 與 regression。
- 保留 Stage 7 的九個核心詞、五份必修閱讀、20 筆五星資源、五題練習、六個預設關閉選單及所有既有 anchor。
- 不改檔名、Stage 編號、模型事實、價格、freshness 日期、範例程式或圖檔。
- PR 開出後保持未合併；未經使用者明確同意，不 merge、retarget、刪 branch／worktree 或 prune。

## 驗收

- 三語完整 H1 與所有直接路由一致，compact 首頁卡仍保留附近的 Multi-Agent／production 說明。
- repo 非歷史 Markdown 不再出現舊 Stage 7 完整章名。
- 圖中五層順序與正文一致，但正文另列課程學習順序。
- strict anchors、anchor slug parity、mirror parity、locale links、Hans、image locale、freshness、reader UX、全量 scripts tests 與三語 MkDocs build 通過。
- 最終 staged diff 經獨立 `code-reviewer` APPROVE；任何 byte 修改都讓舊 ACK 失效。
