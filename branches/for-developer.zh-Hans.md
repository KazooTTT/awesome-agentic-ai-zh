# 开发者延伸路线（For Developers）

> [繁體中文](./for-developer.md) | **简体中文** | [English](./for-developer.en.md)

[← 回到主路线](../README.zh-Hans.md)

<!-- freshness: canonical=branches/for-developer.md; verified_on=2026-08-29; scope=coding-agents,tool-identity,permissions,sandboxing,project-status; max_age_days=90 -->

<a id="使用场景开发场景-ai-怎么帮"></a>

## 📌 这条路帮你做什么

AI 程序助手像会读文件、改代码和跑命令的助手，也可能犯错。这条路先教你缩小任务、看懂改动，再决定是否保留。

建议路线：`A1 → A2 → Stage 5 核心 5.1–5.4 → A3`（[A1](../tracks/cli/A1-cli-intro.zh-Hans.md)、[A2](../tracks/cli/A2-cli-workflow.zh-Hans.md)、[Stage 5](../stages/05-claude-code-ecosystem.zh-Hans.md)、[A3](../tracks/cli/A3-cli-production.zh-Hans.md)）；Stage 8 建议但不影响本页。Track B 可先读 [Stage 7](../stages/07-multi-agent-production.zh-Hans.md)。

## 🎯 学习目标

完成这一页后，你可以：

1. 分清工具的核心身份，以及它在哪些操作接口（surface）出现。
2. 先限制文件、命令和网络权限，再让 agent 动手。
3. 用 diff、test、人工 review 和 rollback 管理一次小改。
4. 分开检查代码质量、agent 行为和 production 观测资料。

<a id="coding-agents"></a>
## 🧩 八个核心词

- **IDE（Integrated Development Environment）**：写代码、看文件和运行工具的工作台，是一种操作接口（surface），不等于 agent 的核心身份。
- **Coding Agent（程序代理）**：能读 code、使用工具、修改文件并依据结果继续工作的软件，可出现在 CLI、IDE、desktop 或 cloud。
- **Provider／Router（供应商／路由器）**：Provider 提供模型服务；Router 转发请求。Router 不是模型，也不管理 repo 权限。
- **Model／Runtime（模型／运行环境）**：Model 生成下一步内容；Runtime 负责执行或调用。本地 runtime 不等于 coding agent。
- **Sandbox（沙箱）**：把程序限制在有限范围内，降低风险但不是百分之百保证。
- **Approval（人工批准）**：高风险动作前由人明确许可。test 通过不等于自动获得 push、merge 或 deploy 权限。
- **Diff／Rollback（差异／回滚）**：Diff 显示改了什么；Rollback 安全撤回不想要的改动，两者一起设计。
- **Eval／Observability（评测／可观测性）**：Eval 用固定案例测质量；Observability 保存 trace、log、成本和错误。

### 不要混淆工具名称

| 名称 | 核心身份 | 白话说法 |
|---|---|---|
| OpenCode | Coding agent／harness | 在代码项目里读、改、测 |
| Pi | Coding agent／harness | 从小核心加入 extensions、skills 或 RPC |
| OpenRouter | API Router | 把模型请求发给 provider，不会改 repo |
| Ollama | Local model runtime | 在本机运行模型和 API，本身不是 coding agent |

**Surface（操作接口）**就是你从哪里使用工具。“工具是什么”和“从哪里操作”是两件事。Cursor、Cline、Continue 都有 coding-agent 能力和多个 surface，不能缩成 IDE-only 工具。

<a id="code-review"></a>
## 🛠 第一个练习：完成一次可回滚的小改

在可丢弃 demo repo 或新 branch 操作，把下面内容贴给 coding agent：

```text
先做 read-only plan，不要修改任何文件。

任务：找出 README.md 中一句可以更清楚、但不改变技术含义的句子。
请先回报：
1. 要改哪一句。
2. 为什么这是小范围改动。
3. 我应该运行哪个 test 或文档检查。
4. rollback 方法。

在我明确人工批准前不要写文件。批准后只准修改 README.md。
完成后显示 git diff -- README.md，并回报 test 结果。
不要 push、merge 或 deploy。
```

读完 plan 后由 human／人工批准。完成后运行：

```powershell
git diff -- README.md
# 接着执行这个 repo 的文档 test 或最小相关 test
```

若改动不对，先确认没有别人的未保存工作，再只回滚本练习的改动；不要清空整个工作区。

<a id="推荐工具"></a>
<a id="tier-升级路径"></a>
## 📚 先选一个入口

| 想做什么 | 先用什么 | 为什么 | 推荐度 |
|---|---|---|---|
| 使用有完整 permission 与 sandbox 文档的 agent | [Claude Code](https://code.claude.com/docs/en/overview) | 学 plan、权限、diff 和多种操作接口 | ⭐⭐⭐⭐⭐ |
| 使用开源、可换 provider 的 coding agent | [OpenCode](https://github.com/anomalyco/opencode) | 分开理解 agent、provider 与 Router | ⭐⭐⭐⭐⭐ |
| 从 IDE 开始但保留逐步批准 | [Cline](https://github.com/cline/cline) | 比较 IDE、CLI 与 SDK surface | ⭐⭐⭐⭐⭐ |

不要只问“哪个最强”。先问它能看到哪些文件、能运行哪些命令、是否能连接网络、谁批准高风险动作，以及失败时如何回滚。

<a id="也适用其他分支"></a>
## ✅ 完成检查与下一站

- [ ] 我能说出 coding agent、Router 和 local runtime 的区别。
- [ ] agent 先给 read-only plan，人工批准后才改一个文件。
- [ ] 我读过完整 diff，也执行了对应 test。
- [ ] 我知道如何只回滚这次改动，且 agent 没有 push、merge 或 deploy。

下一站：设计 Skills／MCP 走 [Stage 5](../stages/05-claude-code-ecosystem.zh-Hans.md)；做 eval、observability 与 production gate 走 [Stage 7](../stages/07-multi-agent-production.zh-Hans.md)；比较 CLI agents 看 [CLI agent 指南](../resources/cli-agents-guide.zh-Hans.md)。

<details markdown="1"><summary>⏱ 展开：时间、环境、费用与 secret 边界</summary>

第一个练习约需 20–40 分钟。使用可丢弃 repo 或新 branch，先确认 `git status`，不要让另一个 agent 覆盖同事或 Claude 正在修改的文件。API key 放环境变量或 secret store，不放 prompt、README 或 commit；先关闭不需要的网络、外部目录与 shell 权限。费用随 model、provider、输入量和重试次数变化。Sandbox 只能缩小爆炸半径，外部服务、credential 和人工批准仍需分别保护。

</details>
<details markdown="1"><summary>📖 展开：建议阅读顺序</summary>

1. [Claude Code overview](https://code.claude.com/docs/en/overview)；2. [Claude Code permissions](https://code.claude.com/docs/en/permissions)；3. [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)；4. [Aider Git integration](https://aider.chat/docs/git.html)；5. [OpenCode V2 docs](https://opencode.ai/v2/docs) 与 [Pi docs](https://pi.dev/docs/latest)；6. [OpenRouter routing](https://openrouter.ai/docs/guides/routing/provider-selection) 与 [Ollama docs](https://docs.ollama.com/)。

</details>
<a id="精选-projects"></a>
<a id="社群备注"></a>
<details markdown="1"><summary>⭐ 展开：完整开发工具与项目表</summary>

<small>工具身份、surface、授权和 repository 状态于 2026-08-29 UTC 依官方文档与 GitHub API 核查。推荐度是编辑评分，不是 GitHub stars 或性能排名。</small>
<table><thead><tr><th scope="col">分类</th><th scope="col">官方工具／项目</th><th scope="col">核心身份</th><th scope="col">主要 surface</th><th scope="col">适合做什么</th><th scope="col">权限／限制与状态</th><th scope="col">推荐度</th></tr></thead>
<tbody><tr><th scope="rowgroup" rowspan="9">Agent／harness</th><td><a href="https://code.claude.com/docs/en/overview">Claude Code</a></td><td>coding agent</td><td>CLI／IDE／desktop／cloud</td><td>学习 permission、sandbox、project rules 与 workflow</td><td>商业产品；保留 permission prompt，从小 repo 开始</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></td><td>coding agent／harness</td><td>terminal／desktop</td><td>切换 provider 或兼容 endpoint</td><td>活跃；MIT；V2 规则使用 <code>AGENTS.md</code></td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/earendil-works/pi">earendil-works/pi</a></td><td>coding agent／harness</td><td>terminal／SDK／RPC</td><td>从小核心加入 extensions、skills 和自定义流程</td><td>活跃；MIT；无内置 sandbox，需自行隔离</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/Aider-AI/aider">Aider-AI/aider</a></td><td>coding agent／pair programmer</td><td>CLI</td><td>用 git diff、commit 与 undo 管理小改</td><td>活跃；Apache-2.0；auto-commit 不等于跳过 hook</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/aaif-goose/goose">aaif-goose/goose</a></td><td>coding／general agent</td><td>CLI／desktop／API</td><td>连接 providers、MCP 与 extensions</td><td>活跃；Apache-2.0；先用低权限 extension</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://cursor.com/docs">Cursor</a></td><td>coding agent + AI editor</td><td>IDE／CLI／cloud／SDK</td><td>从编辑器到后台 agent 的多 surface 流程</td><td>商业产品；分别检查各 surface 的权限和资料边界</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/cline/cline">cline/cline</a></td><td>coding agent</td><td>IDE／CLI／SDK</td><td>逐步批准工具、文件与 browser 操作</td><td>活跃；Apache-2.0；IDE surface 不是安全保证</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/continuedev/continue">continuedev/continue</a></td><td>coding agent</td><td>CLI／VS Code extension／JetBrains plugin</td><td>阅读已有的开源 coding-agent 与 editor 集成</td><td>read-only，不再积极维护；Apache-2.0；官方 2.0.0 是最后版本</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/OpenHands/OpenHands">OpenHands/OpenHands</a></td><td>software-development agent platform</td><td>web／CLI／SDK／cloud</td><td>在 sandbox 中处理较完整的 issue</td><td>活跃；MIT；任务越大越需 checkpoint 和人工 review</td><td>⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="2">工作流支持</th><td><a href="https://github.com/obra/superpowers">obra/superpowers</a></td><td>skills／workflow collection</td><td>agent plugin／skills</td><td>参考 planning、TDD、debug 和 review 流程</td><td>活跃；MIT；模板仍需配合 repo gate</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/yamadashy/repomix">yamadashy/repomix</a></td><td>repo context packer</td><td>CLI／MCP</td><td>整理 codebase context 给 reviewer 或 agent</td><td>活跃；MIT；输出前排除 secrets 和不必要文件</td><td>⭐⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="1">历史</th><td><a href="https://github.com/RooCodeInc/Roo-Code">Roo Code</a></td><td>历史 coding agent</td><td>VS Code extension</td><td>阅读多 mode agent 的设计历史</td><td>已封存；Apache-2.0；不作为新项目首选</td><td>⭐⭐⭐</td></tr></tbody></table>

</details>
<a id="必练流程按使用频率"></a>
<a id="3-个具体-workflow-recipe"></a>
<details markdown="1"><summary>🧪 展开：从每日小改走到团队 workflow</summary>

### 每日开发
`plan → 人工批准 → 小改 → diff → test → review → commit`。每步都能停下，容易找出错误。
### PR review
把 agent 意见当候选 finding，要求文件、行为、复现方式和建议测试；没有证据不要直接阻挡。
### CI
使用只读 token、最小 repo 权限和固定输入。不要把 issue、PR 或网页文字直接变成可执行命令。发布、merge 和 secrets 保留额外批准。
### 批量重构
先建基准测试，再按模块分批；每批都有 checkpoint、diff 与 rollback，不把整个 repo 一次交出去。

</details>
<a id="常见踩坑anti-patterns"></a>
<details markdown="1"><summary>🧯 展开：常见错误、替代方案与 rollback</summary>

| 问题 | 改成什么 |
|---|---|
| 看到 IDE 画面就以为只能在 IDE 用 | 分开看核心身份与所有 surface |
| 把 OpenRouter、Ollama、OpenCode 当一类 | OpenRouter 不是 model，Ollama 不是 coding agent；Router、runtime、coding agent 分开选 |
| agent 说 test 绿就直接接受 | 自己读 diff、确认覆盖需求，再人工批准 |
| 用固定行数判断安全 | 看范围、可测性、可回滚性和 diff 可读性 |
| Aider 自动 commit 就跳过 hook | 启用所需 verify／hook，再走正常 review gate |
| 多个 agent 同时改同一文件 | 分清 ownership，用独立 worktree，最后人工整合 |

Rollback 前先看 `git status` 和 diff，只回滚确认过的目标，不用 broad reset 清掉别人的工作。

</details>
