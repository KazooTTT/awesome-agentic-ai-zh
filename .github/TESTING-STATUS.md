# Testing Status — 誠實揭露

> 這份是給 maintainer / 第一個跑各個 build 的人看的。**誠實地說明哪些 code 真的跑過、哪些只是 syntax check、哪些完全沒測**。

最後更新：2026-07-17

---

## ✅ 真的跑過、有觀察輸出

| 項目 | 狀態 | 證據 |
|---|---|---|
| `scripts/refresh-stars.py` | ✅ Verified | 在 main 上跑過 N 次，0 drift / 0 not-found 都有實際輸出 |
| `scripts/pr-link-audit.py` | ✅ Verified | unit tests 綠 + offline `--diff-file` smoke；live `gh api` 正確 flag 了 archived LangServe（★/license/pushed 都對證過） |
| `scripts/check-links.py --fast` | ✅ Verified | 跑過 120 GitHub URLs 全 OK |
| `gh api` repo 元資料抓取 | ✅ Verified | 152 個 entry 的 stars / license / pushed 都對證過至少一次 |
| Mermaid syntax | ✅ Verified | GitHub 上 render 看過正確（README hero） |
| CI banned-words / overclaim grep | ✅ Verified | 用相同 grep 邏輯本地跑過，0 violations |

---

## ⚠️ 只做了 syntax check / 配置 validation，沒實際 end-to-end 跑

| 項目 | 狀態 | 缺什麼 |
|---|---|---|
| `scripts/build-pdf.sh` | ⚠️ Bash syntax OK | **沒實際跑過** pandoc + xelatex；沒驗證輸出的 PDF 真的能開、CJK 字型真的可用 |
| `scripts/build-mdbook.sh` | ⚠️ Bash syntax OK | 跑過一次但 mdbook-mermaid 失敗（已 fix 但沒重跑驗證） |
| `.github/workflows/lint.yml` | ⚠️ YAML valid | **沒在真 PR 上觸發過**——不知道 Linux runner 上 grep 行為跟本地 git-bash 是否一致 |
| `.github/workflows/pr-link-audit.yml` | ⚠️ YAML valid · script 已測 | **Action 本體沒在真 PR 上觸發過**——fork-skip gate、sticky comment PATCH/POST、`base...head` SHA diff 解析都還沒在真 runner 上驗證（script 邏輯本身有 unit tests + offline smoke） |
| `.github/workflows/docs.yml` | ⚠️ YAML valid · 本機 mkdocs build 綠 | 統一 Pages workflow（mkdocs `/` + mdBook `/book/`，取代已刪除的 deploy-book.yml）。mdBook 子路徑 base-url 尚未在 CI 端到端驗證（首次 deploy 後需實測 `/book/` 資產） |
| `walkthroughs/build-first-agent-in-7-steps.md` 的 Python 範例（~350 行）| ⚠️ 結構合理 | **完全沒實際跑過**——根據對 Anthropic SDK / LangGraph / Chroma / promptfoo 的理解寫出來，但沒從頭到尾 execute 一次。可能有：API 介面變動、套件版本相依、import path 微差 |
| `book.toml` mdBook 設定 | ⚠️ TOML valid | 沒實際 build 過完整 site |

---

## ❌ 完全沒測（design / template，等實際使用才會發現問題）

| 項目 | 為什麼沒測 |
|---|---|
| `scripts/build-pdf.sh` 跑出來的 PDF 視覺品質 | 需要 pandoc + xelatex + Noto Sans CJK 全套，本地環境沒裝 |
| GitHub Pages 上的 mdBook hosted 版 | repo Settings 還沒切到 GitHub Actions source（user 手動步驟） |
| 第一個 PDF release | 需要先跑 build-pdf.sh，沒做 |
| `.github/launch-checklist.md` 內所有「啟用 Discussions / 提交到 awesome lists / 寫 launch posts」項目 | 全部還沒做 |

---

## 對社群貢獻者的建議

如果你是第一個真的要跑某個 build / workflow 的人：

1. **跑 `bash scripts/build-pdf.sh` 之前**：先按 `scripts/README.md` 把字型裝好；輸出 PDF 之後實際開來看 CJK / mermaid block 有沒有正常
2. **跑 `bash scripts/build-mdbook.sh` 之前**：先 `cargo install mdbook mdbook-mermaid` 並在 repo root 跑 `mdbook-mermaid install .`；推上去前先本地 `--serve` 看一下
3. **試 walkthrough 的 Python**：建議用一個全新環境（venv），照 Stage 0 的一次性 install 跑完，遇到任何 import / API 不符的，**請開 issue + PR**——因為這就是「第一手實測」價值最高的時刻
4. **觸發 CI lint workflow**：開個 throwaway PR 改 `stages/01-llm-basics.md`，故意加 `教程` 這個禁用詞，看 banned-words job 有沒有正常 fail。如果沒抓到，調整 grep 邏輯
5. **Deploy book 第一次**：repo Settings → Pages → Source: GitHub Actions，然後 push 一次 commit 讓 workflow 跑。看 Actions tab 看結果

---

## 為什麼 maintainer 沒全部 test

老實說：

- **Build 工具鏈成本**：pandoc + xelatex + Noto Sans CJK 一套裝下來要 1-2 GB + 1-2 小時。不在 launch-blocking 路徑上時不值得本地裝
- **AI walkthrough 的 LangGraph / Chroma 等套件**：版本日新月異；今天測完明天可能就過期。所以選擇用「**對著官方 API 文件寫，註明可能要對現在版本調整**」的策略
- **CI workflow**：在真 PR 上才會觸發；沒第一個外部 PR 之前是 false-positive 還是 fully working 都看不出來

這份 repo 是 **「ship-able skeleton」**——所有結構都對、所有 metadata 都驗證過、所有 prose 都過 review，但**第一次實際跑 build / deploy / walkthrough 還是會發現坑**。

第一個踩到坑的人請開 issue + PR——這正是社群協作的價值所在。

---

## 修這份 testing status

每次跑過某個項目後，把上面表格的 ⚠️ 改成 ✅ 並補「證據」欄。
真實「跑過 + 有 observable output」才算 ✅，「我覺得 OK」不算。
