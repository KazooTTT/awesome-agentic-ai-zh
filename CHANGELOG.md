# Changelog

Last 14 days of substantive changes. Older history lives in `git log`.

Format: `YYYY-MM-DD · category · 1-line summary (commit-sha)`.

---

## 2026-07-16

- **content** · Track A (A2 CLI Workflow) gains **langchain-ai/openwiki** in Recommended Tools, next to repomix. First-party verified (github.com/langchain-ai/openwiki, MIT, 11.7k★, released 2026-07-01): an npm CLI (`openwiki --init`) that generates and auto-maintains a wiki of your codebase and wires a reference into `CLAUDE.md` / `AGENTS.md` so the coding agent reads it on demand; built on DeepAgents, traces to LangSmith. Added with a 💡 concept note naming the **agent-facing documentation** idea (structured codebase context the agent reads on demand, kept out of the prompt) and framing repomix (one-shot snapshot) vs OpenWiki (living wiki) as two angles on the same gap. Placed in Track A (not Track B): the learner value is operating a CLI agent better via context, not building an agent. Tri-locale; anchor / zh-Hans / switcher gates + code-reviewer pass.
- **content** · Glossary "Term not here? / 找不到的詞？" footer now points to **baihuaai.com（白话AI）** as a plainer-language companion (resolves #65, suggested by @linsipeng) — a free, ad-free Simplified-Chinese beginner glossary (term index + zero-basics zone) that explains AI terms in everyday words with analogies. Described only from first-party verification of the site; no unconfirmed term-coverage claims. Tri-locale; gates + code-reviewer pass.
- **content** · Four last-month breakout projects added after a first-party trending survey (GitHub Search API `created:>=2026-06-16` by stars; every fact re-verified from each repo's README + API before writing): **vercel/eve** → Stage 4 特殊路線 (filesystem-first TS agent framework — agent parts are conventional files: `instructions.md` / `tools/` / `skills/` / `channels/` / `schedules/`; `npx eve@latest init`, Apache-2.0, ★ 3.7k+, ⚠️ new 2026-06; category label extended to include filesystem-first, table now 17 projects); **cloudflare/security-audit-skill** → 5.3 recommended-skills table (official six-phase adversarial security-audit pipeline that seeded Cloudflare's vulnerability harness, MIT, ★ 2.5k+); **anthropics/launch-your-agent** → 5.3 recommended-skills table (official educational skill, idea → live Claude Managed Agent, honest ⚠️ it self-describes as an unmaintained reference implementation, Apache-2.0) — originally proposed for Stage 8, but the repo has no Managed-Agents context there, so it lives with the skills it actually is; **xai-org/grok-build** → cli-agents-guide comparison now 8 CLI agents (SpaceXAI's Rust TUI coding agent: codebase-aware edits, shell, web search, headless CI mode, ACP editor embedding; browser sign-in auth, Apache-2.0, ★ 10k+, ⚠️ flagged very-new — open-sourced 2026-07-14). Declined this round: the Tier-2 niche candidates (open-connector / openscience / shepherd / llm-space) and the offensive-security (AGPL red-teaming), no-license, and ToS-gray candidates. code-reviewer REQUEST CHANGES then caught stale "7 CLI agents" count/roster survivors, and a widened follow-up self-scan caught 8 more lines the review missed — **~28 survivor lines across 20 more files in total** (README ×3, resources/README ×3, for-developer ×3, for-everyday-users ×3 — incl. a pre-Hermes "six" in the en mirror, cookbook ×3 ×2 spots, A1-cli-intro's own duplicated roster ×3, agent-paradigms ×3, setup-guide ×3, docs/TESTING_PLAN) — all swept to 8, Grok Build added to every enumerated roster (the A1 entries carry the same very-new / not-your-first-CLI caveat; the cookbook "BYO-LLM CLIs" subset lists were deliberately NOT extended since Grok Build has no verified BYO support). Also per review: zh "hunting" mistranslation 攻擊/攻击 → 漏洞搜獵/漏洞搜猎, provider label pinned to "SpaceXAI（xAI，官方）", auth cell tightened to the README's literal claim, star-counts dropped from the 5.3 rows for table consistency ("educational" kept — it is the README's own verbatim self-description). Tri-locale; anchor / zh-Hans / switcher / stage-template gates + code-reviewer pass.

## 2026-07-13

- **content** · **Claude Fable 5 is back** — swept the repo's now-false "suspended / unavailable / use Opus 4.8" caveats. First-party verified (anthropic.com/news/redeploying-fable-5, 2026-06-30): the US export controls were lifted 2026-06-30 and Fable 5 was redeployed globally on 2026-07-01 (Claude Platform / Claude Code / Cowork; API rollout in progress; redeployed with a new safety classifier that blocks the flagged jailbreak and reroutes to Opus 4.8). Mythos 5 restored only for approved US organizations. Updated ~44 mentions across Stage 1 / 6 / 7 / 7.5 / 8, the glossary, examples/README, and the repo CLAUDE.md (tri-locale): suspension caveats → "restored 2026-07-01"; and since Fable 5 (Mythos-class, above Opus) is on top again, the now-false "Opus 4.8 is the current top usable Claude tier" claims were corrected to "Opus-class flagship" (kept only as a past-tense note where it records that Opus was the top usable tier *while Fable was suspended*). Also filled in Fable 5's now-known 1M context in the model pickers. Example pricing code AST-parses clean. Tri-locale; anchor / zh-Hans / switcher gates + code-reviewer pass.

## 2026-07-12

- **content** · Stage 2 Exercise 2 (Few-Shot) now makes a **fair** zero-shot vs few-shot comparison (resolves #62, reported by @WMichstaBe). The zero-shot baseline had no task instruction (just `input: {text}\noutput:`), which conflated "telling the model the task" with "showing examples" — small models often read it as text continuation and scored ~0, overstating the few-shot gain. Both conditions now share the same `TASK` instruction and few-shot only *adds* examples, so the experiment isolates the effect of the examples. The fragile `assert c3 >= c0` (few-shot isn't guaranteed to beat zero-shot) was replaced with a completeness check plus an honest "net gain may be 0 or even negative" printout; the observation prose was reframed to few-shot's real value (pinning output format + judgment on ambiguous cases). Path A + Path B, tri-locale; example code AST-parses clean; gates + code-reviewer pass.

## 2026-07-09

- **content** · Stage 7.5 gains a plain-language **"分工 / Division of labor"** subsection (tri-locale), sourced first-party from Anthropic's *Agentic coding and persistent returns to expertise* (2026-06-16) + the *2026 Agentic Coding Trends Report*: you decide **what** to build, the agent decides **how** (~70% of planning decisions are the human's; ~80% of execution is left to the agent). Ties into the stage's "work boundary" axis, the returns-to-expertise framing, and the human → agent-team extension (Stage 7). Written analogy-first (home-renovation) for non-engineers; every cited number is first-party-verified — the trends-report "delegation gap" figures were NOT first-party-confirmable, so deliberately omitted. Tri-locale; anchor / zh-Hans / switcher gates + code-reviewer pass.
- **site** · Removed the README **Star History** section. The star-history.com embedded chart no longer renders (GitHub restricted star-timeline data access in 2026; the anonymous `api.star-history.com/svg` embed now 503s for every repo, verified incl. `facebook/react`). Since the README header already carries a live stars badge, the section was redundant once the trend chart was gone, so it was dropped rather than kept as a duplicate badge. Tri-locale; gates + code-reviewer pass.
- **content** · **GPT-5.6 (Sol / Terra / Luna)** shipped and is no longer preview — rolled through Stage 1 (model table + legend), glossary (Context-Window + Frontier-Model), and Stage 6 (reasoning-table intro + GPT-5.5 row). All first-party verified against OpenAI's API model docs: **Sol** `gpt-5.6-sol` ($5/$30 per MTok), **Terra** `gpt-5.6-terra` ($2.50/$15), **Luna** `gpt-5.6-luna` ($1/$6); all three **1.05M context**, 128K max output, available in ChatGPT + Codex + API. **Fixes a real error**: the GPT row's Context read `~400k` (that was GPT-5.5's) — GPT-5.6 is 1.05M. The `(preview)` marker plus its now-unused legend clause were dropped per the table's maintenance convention (status resolved → delete the legend line); Stage 1 header month 2026-06 → 2026-07; the glossary frontier entry gains a 2026-07 cluster. Preview-vs-GA was checked carefully: the 2026-06-26 *preview* system card described the pre-launch limited-preview phase, whereas the API docs now list all three under "Frontier models" with pricing and **no** preview/limited badge (that page does badge "Deprecated" elsewhere, so the absence is meaningful). Tri-locale; anchor / zh-Hans / switcher / stage-template gates + code-reviewer pass.

## 2026-07-01

- **content** · Claude **Sonnet 5** (released 2026-06-30) rolled through the repo, all first-party verified (platform.claude.com model docs + anthropic.com/news/claude-sonnet-5): `claude-sonnet-4-6` → `claude-sonnet-5` and `Sonnet 4.6` → `Sonnet 5` everywhere they name the current default Sonnet — Stage 1 model table + reading list + pricing example, glossary Context-Window / Computer-Use / Frontier-Model entries, Stage 8 Computer-Use row, setup-guide + examples/README model-picker, all walkthrough + stage-3/4 example CLI commands, the `branches/for-developer` Aider example (its two-generations-old `claude-sonnet-4-20250514` snapshot also bumped to `claude-sonnet-5`), the repo CLAUDE.md picker, and the `freshness-models.yml` whitelist (47 content files, 43 model-ID swaps). Verified specs carried, none invented: **1M context** (same as Opus 4.8), **$3/$15** standard ($2/$10 intro through 2026-08-31), "best speed×intelligence" positioning; Sonnet 5 supersedes Sonnet 4.6 (now Legacy). Historical `Sonnet 4.5` references (Stage 6 predecessor list, Stage 7 GAIA leaderboard) deliberately left intact. Tri-locale; anchor / zh-Hans / switcher gates + code-reviewer pass.
- **content** · Stage 2 (Prompt Engineering) + glossary now spell out **zero-shot / one-shot / few-shot** in plain language — terms Exercise 2 leaned on but never defined. The glossary entry `Few-shot / Zero-shot` → `Zero-shot / One-shot / Few-shot` gains the previously-missing **one-shot** (exactly 1 example) plus a one-line framing (the three differ only in how many examples you show the LLM); Stage 2 Exercise 2 gets a 3-bullet inline explainer tying the `3-shot` its code uses back to "few-shot". Also corrected a stray Traditional `分類` → `分类` in the zh-Hans exercise line. Tri-locale; anchor / zh-Hans / switcher gates + code-reviewer pass.

## 2026-06-30

- **content** · Staleness audit Batch 1 (from the 2026-06-29 multi-agent repo audit): removed the phantom "Claude Mythos Preview" attribution on the Stage 7 WebArena benchmark row (→ "領先 model 未公布" — Mythos/Fable benchmarks were never published and access is suspended, so the cell contradicted the table's own caption); glossary Context-Window entry gains Grok 4.3 1M + Mistral Medium 3.5 256k for parity with the Frontier Model entry; cookbook "Claude 4.5+" → "Claude 4.8+"; A2A glossary entry refreshed to v1.0 (Linux Foundation governance, 150+ orgs, signed Agent Cards). All first-party verified. Tri-locale; gates pass.
- **content** · Staleness audit Batch 2 (model-ID / recommendation refresh, all first-party verified): Stage 6 Path-2 reasoning list + observation line, Stage 8 example comment, and setup-guide updated Gemini 3.1 Pro → 3.5 Flash and added xAI Grok 4.3 (GA) to the strongest-reasoning options; GPT-5.5 deliberately kept in runnable example code since GPT-5.6 is still limited preview (not GA); setup-guide free-tier corrected to "GPT-5.5 Instant (rate-limited)"; Stage 4 OpenAI Agents SDK "April 2026 update" reframed to past-tense (the built-in-sandbox / 7-provider claim verified accurate), AG2 v0.2-vs-v0.4 note softened. Tri-locale; gates pass.
- **layout** · Stage 1 model tables de-crammed: time-sensitive status/caveat text (Fable 5 suspension, license clauses, release dates, Arena rank) moved out of the data cells into one plain-language legend line per table; genuinely-old entries retired (GPT-5 / o-series, Gemini 3.1 Pro). Added an HTML-comment maintenance convention so the tables self-clean as models churn (new flagship = swap not append; resolved status = delete the legend line). Worst flagship cell dropped ~75 → ~33 chars. Tri-locale; plain-language; gates + code-reviewer (APPROVE) pass.
- **layout** · Stage 2 Curated-Projects table de-crammed (same pattern): the two worst cells (dspy / NirDiamant, ~150-182 → ~38-74 units) trimmed to a short reason + ★ / license; framework-not-tutorial + NOASSERTION caveats moved to one legend line. Tri-locale; gates pass.
- **layout** · Stage 1 Chinese-frontier table (the 7-provider / 7-col one, widest in the stage) split along the API-vs-open-weights line into two 6-col tables (① API-only: DeepSeek / Kimi / Hunyuan / MiniMax · ② open weights: Qwen / GLM / Yi); the License column folded into one plain legend per group. All 7 providers + license nuance preserved. Tri-locale; gates + column-count scan pass.
- **site** · MkDocs-Material UI upgrade (verified with a local `mkdocs build`, clean across all 3 locales): code-copy buttons, instant/SPA-style navigation + progress, navigation.sections, search.share, content tabs/tooltips/annotate; `:material-*:` icon support; new `docs/stylesheets/extra.css` (indigo brand color, grid-card hover, tighter rounded tables). A custom card landing page is a planned follow-up (blocked on the README-vs-index i18n conflict).
- **site** · Nav cleanup: the top nav was bilingual + inconsistent ("首頁 / Home", "Audience branches"…); switched to single-language source labels + i18n `nav_translations` so each locale shows only its own language (繁中 首頁 / en Home / 简中 首页), and dropped `navigation.sections` (over-expanded the sidebar). Verified with a local build, all 3 locales.
- **site** · Custom card landing page shipped (resolves the earlier README-vs-index blocker): `index.md` / `.en.md` / `.zh-Hans.md` is now the trilingual home — hero + stat cards + track/stage grid-cards. The README moved to an `/about/` page (staged as `about.md` so it no longer collides with `index` for the home slot), and `mkdocs_hooks.py` rewrites in-content `README.md` links to `about` at build time so they keep resolving (examples/README untouched). Verified locally: clean build, all 3 locale homes = landing, anchor / zh-Hans / switcher gates pass.
- **content** · Staleness audit Batch 3 (new harness-engineering frames + adds, all first-party sourced): Stage 7 gains a "feedback loops, not a more perfect prompt" subsection — the 4 feedback timings (tool returns / mid-run steering / end-of-turn acceptance / outer loop), anchored on Anthropic's planner→generator→evaluator harness post; Stage 7.5 gains "Harnesses expire: Model-Harness-Fit + the Bitter Lesson" (Sutton 2019); `deepagents` (LangChain, LangGraph-based, MIT, v0.6.12) added to Stage 4 framework resources + a plain glossary "Deep Agent" entry. Written analogy-first for non-engineers, jargon glossed inline; Codex `/goal` folded into N1's outer-loop row (no separate section). Tri-locale; gates pass.

## 2026-06-29

- **content** · Stage 1 model table + glossary (frontier + Context-Window entries) + `scripts/freshness-models.yml` whitelist refreshed with late-June-2026 frontier models, all first-party verified: GPT row gains GPT-5.6 (Sol / Terra / Luna, **preview**); Gemini row → 3.5 Flash (3.5 Pro in dev); glossary frontier adds xAI Grok 4.3 (GA) + Mistral Medium 3.5 (open weights, preview), relabeled by half-month (Fable 5 suspension note retained). Preview-vs-GA marked; no fabricated benchmark / context numbers. Tri-locale; anchor / zh-Hans / switcher gates pass.
- **content** · Stage 6 reasoning-model table consistency follow-up: the "current (Jun 2026) frontier" intro + the GPT-5.5 and Gemini 3.1 Pro rows now flag that newer tiers exist (GPT-5.6 Sol / Terra / Luna **preview**; Gemini 3.5 Flash available, 3.5 Pro in dev). Existing verified rows and benchmarks (e.g. Gemini 3.1 Pro GPQA Diamond 94.3%) kept and correctly attributed; no preview-model benchmarks fabricated. Tri-locale; gates pass.

## 2026-06-24

- **catalog** · Added DeusData/codebase-memory-mcp (★ 13.5k, MIT) to §5 Dev Collaboration — a code-intelligence MCP that indexes a codebase into a queryable knowledge graph (query structure / symbols / call paths instead of grep+read). Plain, non-marketing description (notes the re-index-after-edits + verify-load-bearing-claims caveats); tri-locale; §5 TOC count 7→9 (also corrects a pre-existing off-by-one); gates pass.

## 2026-06-13

- **catalog** · Added 12 high-confidence repos (all gh-verified stars/license, none previously listed): microsoft/agent-framework (Stage 4); getzep/graphiti + lancedb/lancedb (Stage 6); comet-ml/opik, pydantic/logfire, NVIDIA-NeMo/Guardrails, BoundaryML/baml (Stage 7, incl. new Safety/Guardrails + Structured-Output rows); bytedance/UI-TARS-desktop + trycua/cua (Stage 8, new Computer Use Agent Stack); awslabs/mcp + ComposioHQ/composio (MCP/Skills catalog §6 / §12); microsoft/mcp-for-beginners (Stage 5.2 reading list). Tri-locale; per-section counts updated; anchor / zh-Hans / switcher gates pass.
- **content** · Stage 5 — plain-language orientation box in 5.1 (Claude Code = terminal agent for devs; Claude Cowork = desktop agent for non-coders; OpenAI parallels = Codex CLI / ChatGPT agent) so beginners see Claude Code is one *shape* among several; plus first-use plain glosses for heavy terms (harness / orchestration / scaffolding / control plane). Tri-locale; Cowork + ChatGPT agent verified first-party; anchor / zh-Hans / switcher gates pass.
- **content** · Reframed Claude Fable 5 across the roadmap after Anthropic suspended all access to Fable 5 + Mythos 5 on 2026-06-12 (US government export-control directive; [status](https://status.claude.com/) · [statement](https://www.anthropic.com/news/fable-mythos-access); no restoration timeline). Documentation tables (`CLAUDE.md` / `examples/` / stages 01·06·07·07.5·08 / glossary) now mark Fable 5 as suspended and currently unavailable, with Opus 4.8 as the current top usable Claude tier; recommendation pick-lists (Path-2 reasoning chooser, Computer Use vendor table, OmniParser / browser-use swap-lists) drop Fable 5 so no reader is pointed at an inaccessible model. Tri-locale; anchor / zh-Hans-localize / language-switcher gates all pass. Suspension verified against two first-party sources, no fabricated facts.
- **docs** · `CITATION.cff` version `2026.05.19` → `2026.06.13` (was stale vs the recent content batches).

## 2026-06-12

- **content** · Claude Fable 5 (Mythos-class, `claude-fable-5`, GA 2026-06-09) added as the new top Claude tier across the trilingual roadmap — model tables in `CLAUDE.md` / `examples/` / stages 01·06·07·07.5·08 + glossary frontier entry; Opus 4.8 reframed as Opus-class flagship + Fable 5 safeguard-fallback. No fabricated context-window or benchmark numbers (Anthropic published none — marked "not yet published"). Also fixed a pre-existing `claude-opus-4-7` → `claude-opus-4-8` inconsistency (`12980b3`).
- **content** · Stage 5 — new **5.6 Dynamic Workflows** section after 5.5 Subagents (ecosystem-level intro + cross-link to the 7.5 deep-dive, no duplication); old 5.6 Source → 5.7, old 5.7 SDK → 5.8, all in-file refs + 7-Layer-map ranges + cross-file anchors (glossary / stages 03·06·07) relinked, tri-locale (`5044008`).
- **catalog** · `1weiho/open-slide` (★4.9k, MIT) added to §2 as an agent-native slide framework — ships Claude Code Skills, distinct from Stage 4 orchestration frameworks; tri-locale (`7d3fd5d`).
- **docs** · MCP/Skills catalog count made drift-proof — stale `62` → robust `65+`, category count reconciled to 15, across 33 files / all locales (`3782dd4`). Propagated the 7→8 stage reality into design notes / style-guide / reader docs (`39d397a`) and fixed outreach-draft count drift (`25785f0`).
- **outreach** · send-day copy-paste packages playbook for awesome-list submissions (`afd7a76`).
- **content** · per-chapter improvement audit (12-agent fan-out + skeptical filter) → 5 gap-fills, all tri-locale: Stage 3 lethal-trifecta security callout + MCP router note + glossary (`f3bde60`); Stage 1 next-token / sampling mental-model box (`1bd171f`); Stage 5 Hooks (L3 control layer) subsection (`9d2897f`); Stage 7 Loop Engineering note + glossary (`eb8e64c`).
- **catalog** · new Web Search / Retrieval category (exa-mcp + tavily-mcp) + Context7 in Dev-Collaboration; category count 15→16 (`b1718d3`).
- **content** · improvement-audit medium batch (6 more tri-locale gap-fills): Stage 3 structured outputs / JSON-mode (`93006a8`); Stage 2 reasoning-vs-CoT + Stage 5 MCP-in-2026 (Registry / FastMCP / security) + Stage 8 accessibility-tree & Playwright-MCP (`ea0633e`); Stage 6 RAG ingest-parsing + embedding-model selection + Stage 7 OTel GenAI conventions / pass^k·τ²-bench / MAST (`2fcfc6b`).

---

## 2026-05-31

- **tooling** · pruned the ops-metric scripts that don't touch stars or URL validity (strategic-review action #1, scoped down per maintainer): removed `scripts/snapshot-traffic.py` (GitHub traffic snapshots), `scripts/refresh-outreach-status.py` (outreach-matrix drift), `scripts/check-catalog-staleness.py` (dormant-entry pinger), and the `docs/traffic/` snapshot dir. **KEPT** the weekly stars + URL auto-update (`weekly-catalog-refresh.yml` + `lint.yml`'s `star-drift` job) — the maintainer values the weekly cadence for star-count refresh and link-rot checking. All correctness + trilingual-parity guards intact (anchor / link-rot / mirror-sync / stage-template / banned-words / overclaim / zh-Hans-localize).

---

## 2026-05-26

- **ci** · `lint.yml` overclaim check expanded (P3-G from audit) — promoted from case-sensitive exact-phrase to case-insensitive (`grep -Fi`), broadened scope to include `tracks/` `examples/` `resources/` (which the previous narrower scope missed — letting 5 uppercase `Production-grade` H2 headers in `examples/` slip through the earlier sweep). Strict-blocking list now includes all style-guide §3 phrases (`首選` / `首选` / `唯一選擇` / `唯一选择` / `業界最佳` / `业界最佳` / `業界最強` / `全世界最好的` / `最緊迫` / `the most canonical`) plus English equivalents (`production-grade` / `world-class` / `best-in-class` / `cutting-edge` / `state-of-the-art` / `industry-leading`). Corpus pre-cleaned across tri-locale before flipping to strict.
- **content** · overclaim residue swept across tri-locale (18 file edits) before the lint flip — 3 × `## Production-grade …` H2 headers in `examples/stage-{6,7}/` normalized to `## Production-ready …`; 3 × inline `首選` in `stages/05` / `stages/06` / `tracks/cli/A1` softened per style-guide §3; `tracks/cli/A1` `最完整的中文社群資源` → `中文社群資源豐富` (marketing → factual).
- **tooling** · `scripts/snapshot-traffic.py` shipped — captures weekly 14-day traffic window (views / clones / referrers / paths + point-in-time totals) to `docs/traffic/snapshots/YYYY-MM-DD.json` so historical trend survives the GitHub API's 14-day visibility limit. Each file ~5 KB. First snapshot included (`docs/traffic/snapshots/2026-05-26.json`).
- **tooling** · `scripts/refresh-outreach-status.py` shipped — reads `.github/channel-partners.md`, extracts PR URLs, queries `gh pr view`, reports drift between recorded status and live PR state (merged / closed / ghosted / approved). Report-only (text / markdown / json), `--check` for CI. Closes P2-F from the 2026-05-25 audit; P2-E closed by snapshot-traffic.

---

## 2026-05-25

- **tooling** · `scripts/check-catalog-staleness.py` shipped — queries `gh api repos/<owner>/<repo>` for `pushed_at` + `archived`, flags catalog entries dormant >= N months (default 12) or archived. Report-only (text / markdown / json). Initial run on the 247-repo catalog surfaced 17 stale entries: 5 archived (incl. `langchain-ai/langserve` archived 2026-05-05 still cited as live, `RooCodeInc/Roo-Code` archived 2026-05-15 in setup-guide) + 12 dormant (oldest: `microsoft/prompt-engine` 37 mo).
- **i18n** · Stage 1 + Stage 2 mirror schema resync — `## 🎯 Curated Projects` regenerated from canonical (en hand-translated · zh-Hans via opencc tw2s + zh-hans-localize vocab); −358 lines of stale H3-card format replaced with compact-table parity to canonical. Also normalized 5 Stage 1 .zh-Hans H2 titles back to canonical wording + emoji. Eliminates the forward-schema drift across all 8 stages.

---

## 2026-05-19

- **catalog** · `microsoft/ai-agents-for-beginners` added to Stage 3 選讀/進階補充 as a parallel beginner course (explicitly *not* a substitute for the stage's hands-on practice), tri-locale (`2d83f72`, `94f2d73`).

## 2026-05-18

- **catalog** · Kimi-K2 + GLM-4.5 added to §11 中文圈專用 — neutral schema, gh-verified Stars/License, tri-locale (`fd81f31`, `ad80845`).
- **ci** · weekly catalog-refresh PR now guarded auto-merge: sanity guard (star-token-only diff, ≤150 lines, anchors pass) → squash-merge, else label `needs-manual-review` (`3dc6ecd`).

## 2026-05-17

- **docs** · per-track Capstone + 4-level self-assess rubric (`CAPSTONE`), tri-locale (`dbf1ef3`, `a31dde5`).
- **docs** · Pages unified — mkdocs at `/`, mdBook at `/book/`, one workflow; README's GitHub-only switcher stripped from rendered site (`5e59c7c`, `001d765`).
- **docs** · README positioning reframed (trilingual, English fully maintained); stale exercise-folder count corrected 27 → 23 (`b4bb862`, `24a87fe`).
- **outreach** · English-audience launch drafts — HN / Reddit / newsletters / awesome-lists (`b8f365b`).

## 2026-05-16

- **governance** · CoC + SECURITY + CITATION.cff + issue-template config added, tri-locale mirrors (`9aa2963`, `84bc58f`).
- **docs** · public ROADMAP.md + learner PROGRESS.md tracker added, tri-locale (`e5cc310`, `3e628e9`).
- **docs** · GitHub Pages site (mkdocs-material, trilingual) + live docs-site badge (`498932c`, `ea4530f`).
- **i18n** · zh-Hans mainland-localization pass + Lint gate blocking Taiwan-vocab/「」 drift (`7f73b8a`, `805ae57`).
- **visuals** · final ASCII concept blocks replaced with generated PNGs — 10/10 complete (tri-locale) (`21a2bbf`).
- **ci** · actions bumped off deprecated Node20 ahead of June 2026 forced migration (`c6a8c19`).
- **outreach** · CONTRIBUTORS — @demo112 (#14) + @Rain120 (#18) (`7040738`).

## 2026-05-15

- **content** · Stage 1 §主流 LLM 家族對比 (US 3 + China 7 + Western-OSS 4 + decision tree + benchmark + caveat) (`8f578bf`).
- **content** · Stage 5 §7-Layer Architecture Map (Claude primitives × 3 engineering disciplines) + embedded figures (`5f99bbb`, `1e5a12b`).
- **content** · subagent teaching deepened — dispatch who/how/what, vs Skill/Slash-Command disambiguation, advanced doc + figures (`009ddf9`, `21c555b`, `e8a919e`).
- **content** · 5 audience branches tableized (使用情境 / 流程 / Tier ladder) + academic-style polish, tri-locale (`184015b`, `6b7e5f6`).
- **i18n** · 97 broken outbound mirror anchors fixed + anchor-checker now enforces mirror files (`e1991a6`, `ab3a6d0`).

## 2026-05-14

- **content** · NEW Stage 7.5 — Advanced Agentic Concepts (OpenAI Harness Engineering 5 principles, Why→What→How map, work-boundary diagram) (`4a6bf18`, `e2c1d11`).
- **content** · Track A3 §6 advanced-concept playbooks for daily CLI work (`876a457`).
- **visuals** · § (513×) and 🔄 (24×) symbols stripped across all user-facing docs; concept diagrams embedded as PNG × 3 locales (`29eb774`, `d04c224`).
- **catalog** · 4 Anthropic-related resources added across stages (`0af7fbc`).
- **ci** · weekly catalog-refresh workflow + `--apply` flag (`dc91a8b`).

## 2026-05-13

- **content** · Stage 4/6/7 verified + merged to main (`cdb0ae3`); Stage 8 NEW — Agent Interfaces, §1-15 across 3 commits A/B/C (`b83c894`, `6c87a2f`, `069406f`).
- **content** · curation positioning crystallized — exercises reframed foundational/illustrative; repo = curation hub + simple cases, depth → hello-agents (`00dc046`, `0206dbc`).
- **content** · 精選 Projects consolidated to single 適合誰 tables across Stages 0-8 + Track A (`fd94d80`, `19a14a8`).
- **content** · Stage 5 expanded (§5.1-5.6: Claude Code basics, MCP/Plugin/Skill 定位, §5.5 Subagents, Harness Internals) (`2c3f1dd`, `f7de4e7`).
- **content** · Stage 6 RAG-first restructure + GraphRAG / Contextual Retrieval / Hybrid Search; 2026 frontier-model refresh (`f00e2c2`, `acbc9dc`).
- **ci** · 4 checks added — anchor validator, mirror-sync reminder, 2026 freshness, stage-template enforce (`a14c809`, `4491e6e`).
- **i18n** · 8-stage tri-locale mirror catch-up via Codex + Gemini delegation; 37 legacy anchors fixed, validator → strict (`8b39c75`, `706d257`).
- **catalog** · whale (DeepSeek terminal) + a-stock-data added to Chinese ecosystem (#14) (`3d375bd`).

## 2026-05-12

- **content** · examples/ bootstrapped — Stage 1 (6) + 2 (4) + 3 (6) + 4 (5) + 6 (5) + 7 (5) inline starters + folder examples, tri-locale (`c1fcaa7`, `8051861`, `7d2c1b7`).
- **content** · dual-path examples — Ollama (default, cost-driven) alongside Anthropic; per-stage budget + LLM recommendation list (`bc37ad8`, `3fa5410`).
- **content** · tool-calling-tutor — installable Claude Code skill + Stage 5 §5.3 meta-example (`3584669`).
- **i18n** · diagrams renamed `.zh-Hans.png` per BCP 47 / W3C convention (`78797a3`).

## 2026-05-11

- **accessibility** · `resources/setup-guide.md` (3 langs) — addresses the dev-fluency assumption gap that subagent audit flagged across 5 non-dev branches. 5 sections covering API key registration, Python install, hello-world, Claude Code first auth, SKILL.md primer (`3c88b2b`). Plus 15 branch-top callouts on all 5 audience branches. `resources/README.{en,zh-Hans}.md` created for trilingual parity.
- **accessibility** · README — promoted setup-guide pointer to top of Quick Start across all 3 langs (`ad47706`). Was buried in Related Resources where non-dev visitors hit technical walls before discovering it.
- **accessibility** · setup-guide opens with a 4-tier on-ramp (Web / Desktop / CLI / API) + official download URLs for Claude.ai, ChatGPT, Gemini, Le Chat, Claude Desktop, ChatGPT Desktop, LM Studio (`3c89952`). Replaces the abstract "decide two things" intro so non-dev readers see "just use claude.ai for free" as the first option, not "register API key → install Python".
- **accessibility** · setup-guide adds a 3rd tier between Desktop and CLI: **IDE with built-in AI** (Cursor, Windsurf, Cline, Continue, Roo Code, Zed, GitHub Copilot) with download URLs (`7e14093`). Distinguishes "AI sidekick while you write code" from "agent runs autonomous task in terminal".

## 2026-05-10

- **funnel** · Stage 1 → Stage 2 callouts added across 3 langs to address visible drop in `traffic/popular/paths` (`0ee2a3a`)
- **outreach** · 3 awesome-list targets backfilled into channel-partners matrix from launch-checklist: `travisvn/awesome-claude-skills`, `WangRongsheng/awesome-LLM-resources`, `AiHubCN/Awesome-Chinese-LLM` (`90a6ad1`)
- **outreach** · PR #6135 to `punkpeye/awesome-mcp-servers` — addressed bot `name-check`, replied to non-applicable `glama-check` + `emoji-check` (`81a7313`)
- **content** · Cookbook Recipe 6 — **Local-LLM × CLI Agent walkthrough** (`5855852`). Bridges Stage 1 (local LLM) + Stage 5 (CLI agent) end-to-end. Explicitly notes Claude Code does **not** support local LLM as backend; routes readers to OpenCode / goose / Aider / Hermes instead. Stage 5 + cli-agents-guide also gain matching pointers.
- **catalog** · Hermes Agent (`NousResearch/hermes-agent` ★142k) added as 7th major CLI agent across `cli-agents-guide`, `tracks/cli/A1`, and 5 dependent files (`698f13a`). Differentiator: cloud-VM-native, model-neutral (200+ LLMs via OpenRouter / NIM / GLM / Kimi / etc.), self-improving skill loop.
- **i18n** · `*.zh-CN.md` → `*.zh-Hans.md` migration per BCP 47 / W3C compliance (`21b653d`). 25 files renamed, ~270 markdown lines updated, tooling (`sync-language-switchers.py`, `lint.yml`, `generate-stage5-stack.py`) migrated. Thanks [@xfq](https://github.com/xfq) (W3C i18n lead) for flagging in [#9](https://github.com/WenyuChiou/awesome-agentic-ai-zh/issues/9). Added to CONTRIBUTORS (`868691d`).
- **visuals** · English README hero (`banner.en.png`), Learning Map (`learning-map.en.png`), and Branch Decision Tree (`branch-decision-tree.en.png`) refreshed to ChatGPT-rendered versions (`c7edff8`, `4be6b88`, `6c03c58`).

## 2026-05-09

- **outreach** · Day 1 PR sent: `punkpeye/awesome-mcp-servers#6135`, adding awesome-agentic-ai-zh to `## Tutorials` (`a0dc4d5`). Plan revised after upstream audit caught `hesreallyhim/awesome-claude-code` mid-reorg (Day 2 = issue not PR) (`708259c`).
- **outreach** · 8 channel-partner pitch templates created in `.github/outreach/` plus tracking matrix `.github/channel-partners.md` (`2f63745`). Targets: Datawhale, liyupi, HuggingFace, LangChain (kyrolabs), awesome-claude-code, awesome-mcp-servers, Zhipu, Moonshot.
- **catalog** · 11 中文圈專用 expanded from 2 → 7 entries: `QwenLM/Qwen-Agent`, `coze-dev/coze-studio`, `coze-dev/coze-loop`, `liaokongVFX/LangChain-Chinese-Getting-Started-Guide`, `chatchat-space/Langchain-Chatchat` (`4809039`).
- **funnel** · Stage 0 → Stage 1 callouts added (`3dfe761`).
- **ci** · zh-Hans companion files excluded from zh-TW banned-word audit (closes #7) (`3acc3f2`).

## 2026-05-08

- **content** · `for-teacher` branch expanded with 3-tier teacher AI use-case framework (Chen 2020, Mittal 2024) via @scott0127 PR #6 (`cd1cad4`).
- **content** · Stage 6 unit guide: memory + RAG overview via @scott0127 PR #5.
- **content** · Branch decision tree (zh-Hans) added, English banner added, `for-developer` branch thickened 56 → 138 lines × 3 langs.

## 2026-05-07

- **catalog** · 3 user-flagged gaps filled: `safishamsi/graphify`, `pbakaus/impeccable`, `netease-youdao/LobsterAI` + context-engineering and harness-engineering coverage.
- **content** · `resources/cookbook.md` added with 5 (now 6) step-by-step recipes covering Skill / MCP / Office / NotebookLM / Zotero / Local-LLM workflows.

## 2026-05-06

- **launch** · Repo announced to bilingual community. Star count: 0 → 519 in week one.
- **content** · `learning-map.png` polished, README hero banner placement finalized.

---

## Conventions

- Each commit SHA is clickable: `https://github.com/WenyuChiou/awesome-agentic-ai-zh/commit/<sha>`
- Categories: `content` (stages/branches/tracks) · `docs` (project meta-docs: README/ROADMAP/PROGRESS/CAPSTONE/Pages site) · `governance` (CoC/SECURITY/CITATION/issue templates) · `accessibility` (on-ramp/setup friction) · `catalog` (mcp-skills-catalog entries) · `funnel` (cross-stage navigation) · `visuals` (diagrams/banners) · `i18n` (translation/locale) · `outreach` (channel partners) · `ci` (workflows/lint) · `launch` (one-time events)
- Maintained manually; not auto-generated. Updated alongside substantive commits.
