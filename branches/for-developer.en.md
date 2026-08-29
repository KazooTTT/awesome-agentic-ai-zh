# Extension Path for Developers

> [繁體中文](./for-developer.md) | [简体中文](./for-developer.zh-Hans.md) | **English**

[← Back to the main route](../README.en.md)

<!-- freshness: canonical=branches/for-developer.md; verified_on=2026-08-29; scope=coding-agents,tool-identity,permissions,sandboxing,project-status; max_age_days=90 -->

<a id="use-cases-developer-scenarios--how-ai-helps"></a>

## 📌 What this path helps you do

An AI development assistant reads files, edits code, and runs commands. It can help, and it can be wrong. This path teaches you to narrow the task, understand the change, and then decide whether to keep it.

Recommended route: `A1 → A2 → Stage 5 core 5.1–5.4 → A3` ([A1](../tracks/cli/A1-cli-intro.en.md), [A2](../tracks/cli/A2-cli-workflow.en.md), [Stage 5](../stages/05-claude-code-ecosystem.en.md), [A3](../tracks/cli/A3-cli-production.en.md)). Stage 8 is recommended but does not block this page. Track B readers may start with [Stage 7](../stages/07-multi-agent-production.en.md).

## 🎯 Learning goals

After this page, you can:

1. Separate a tool's core identity from the operating interfaces (surfaces) where it appears.
2. Limit file, command, and network permissions before an agent acts.
3. Manage a small change with a diff, test, human review, and rollback.
4. Check code quality, agent behavior, and production telemetry separately.

<a id="coding-agents"></a>
## 🧩 Eight core terms

- **IDE (Integrated Development Environment)**: a workbench for code, files, and tools. It is one operating interface (surface), not an agent's core identity.
- **Coding Agent**: software that reads code, uses tools, edits files, and continues from results. It may appear in a CLI, IDE, desktop, or cloud.
- **Provider／Router**: a provider supplies model services; a router forwards requests to one or more providers. A router is not a model and does not manage repo permissions.
- **Model／Runtime**: a model generates the next content; a runtime executes or calls it somewhere. A local runtime is not a coding agent.
- **Sandbox**: a limited area in which code can run. It reduces risk but is not a perfect guarantee.
- **Approval**: a human explicitly permits a high-risk action. A passing test does not grant push, merge, or deploy permission.
- **Diff／Rollback**: a diff shows what changed; rollback safely reverses unwanted changes. Design them together.
- **Eval／Observability**: eval tests quality with fixed cases; observability records traces, logs, cost, and errors during execution.

### Do not mix up tool names

| Name | Core identity | Plain-language description |
|---|---|---|
| OpenCode | Coding agent／harness | Reads, edits, and tests in a code project |
| Pi | Coding agent／harness | Adds extensions, skills, or RPC to a small core |
| OpenRouter | API Router | Sends model requests to providers; does not edit your repo |
| Ollama | Local model runtime | Runs models and an API locally; is not itself a coding agent |

**Surface (operating interface)** means where you use a tool. “What a tool is” and “where you operate it” are different questions. Cursor, Cline, and Continue have coding-agent capabilities and multiple surfaces; do not reduce them to IDE-only tools.

<a id="code-review"></a>
## 🛠 First exercise: make one small, reversible change

Use a disposable demo repo or a new branch. Paste this to a coding agent:

```text
First make a read-only plan; do not modify any files.

Task: find one sentence in README.md that could be clearer without changing its technical meaning.
Report first:
1. Which sentence you will change.
2. Why this is a small-scope change.
3. Which test or documentation check I should run.
4. How to rollback.

Before my explicit human approval, do not write files. After approval, modify only README.md.
When finished, show git diff -- README.md and report the test result.
Do not push, merge, or deploy.
```

After reading the plan, a human approves it. Then run:

```powershell
git diff -- README.md
# Then run this repo's documentation test or smallest relevant test
```

If the change is wrong, confirm README.md has no unsaved work from someone else, then rollback only this exercise's change. Never use a command that clears the whole worktree.

<a id="recommended-tools"></a>
<a id="tier-progression"></a>
## 📚 Choose an entry point

| What you want to do | Start with | Why | Rating |
|---|---|---|---|
| Use an agent with documented permissions and sandboxing | [Claude Code](https://code.claude.com/docs/en/overview) | Learn plans, permissions, diffs, and multiple surfaces | ⭐⭐⭐⭐⭐ |
| Use an open-source, provider-flexible coding agent | [OpenCode](https://github.com/anomalyco/opencode) | Keep agent, provider, and router concepts separate | ⭐⭐⭐⭐⭐ |
| Start in an IDE while keeping step-by-step approval | [Cline](https://github.com/cline/cline) | Compare IDE, CLI, and SDK surfaces | ⭐⭐⭐⭐⭐ |

Do not ask only “Which one is strongest?” First ask which files it can see, which commands it can run, whether it can use the network, who approves risky actions, and how you can undo a bad change.

<a id="other-branches-also-apply"></a>
## ✅ Completion check and next stop

- [ ] I can distinguish a coding agent, router, and local runtime.
- [ ] The agent gave a read-only plan and changed one file only after human approval.
- [ ] I read the complete diff and ran the relevant test.
- [ ] I know how to reverse only this change, and the agent did not push, merge, or deploy.

Next: for Skills／MCP, go to [Stage 5](../stages/05-claude-code-ecosystem.en.md); for eval, observability, and production gates, go to [Stage 7](../stages/07-multi-agent-production.en.md); to compare CLI agents, see the [CLI agent guide](../resources/cli-agents-guide.en.md).

<details markdown="1"><summary>⏱ Expand: time, environment, cost, and secret boundaries</summary>

The first exercise takes about 20–40 minutes. Use a disposable repo or new branch, check `git status`, and do not give files another agent is editing to a second agent to overwrite.

- Put API keys in environment variables or a supported secret store, never in prompts, README files, or commits.
- Disable unnecessary network, external-directory, and shell permissions first.
- Cost varies with model, provider, input volume, and retries; do not preserve a fixed guess per run.
- A sandbox limits the blast radius; external services, credentials, and human approval still need separate protection.

</details>

<details markdown="1"><summary>📖 Expand: suggested reading order</summary>

1. [Claude Code overview](https://code.claude.com/docs/en/overview): inspect an agent's surfaces.
2. [Claude Code permissions](https://code.claude.com/docs/en/permissions): understand allow, ask, and deny.
3. [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing): understand file and network isolation.
4. [Aider Git integration](https://aider.chat/docs/git.html): understand auto-commit, diff, undo, and hook boundaries.
5. [OpenCode V2 docs](https://opencode.ai/v2/docs) and [Pi docs](https://pi.dev/docs/latest): compare provider-flexible harnesses.
6. [OpenRouter routing](https://openrouter.ai/docs/guides/routing/provider-selection) and [Ollama docs](https://docs.ollama.com/): confirm that router and runtime are not agents.

</details>

<a id="curated-projects"></a>
<a id="community-note"></a>
<details markdown="1"><summary>⭐ Expand: complete developer tools and projects table</summary>

<small>Tool identity, surface, license, and repository status were checked against official documentation and the GitHub API on 2026-08-29 UTC. Ratings are editorial scores from this learning map, not GitHub stars or performance rankings.</small>

<table><thead><tr><th scope="col">Category</th><th scope="col">Official tool／project</th><th scope="col">Core identity</th><th scope="col">Main surface</th><th scope="col">What it suits</th><th scope="col">Permissions／limits and status</th><th scope="col">Rating</th></tr></thead>
<tbody><tr><th scope="rowgroup" rowspan="9">Agent／harness</th><td><a href="https://code.claude.com/docs/en/overview">Claude Code</a></td><td>coding agent</td><td>CLI／IDE／desktop／cloud</td><td>Learn permissions, sandboxing, project rules, and agent workflows</td><td>Commercial; keep permission prompts and start with a small repo</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></td><td>coding agent／harness</td><td>terminal／desktop</td><td>Switch providers or compatible endpoints</td><td>Active; MIT; V2 project rules use <code>AGENTS.md</code></td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/earendil-works/pi">earendil-works/pi</a></td><td>coding agent／harness</td><td>terminal／SDK／RPC</td><td>Add extensions, skills, and custom workflows to a small core</td><td>Active; MIT; no built-in sandbox, so isolate it yourself</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/Aider-AI/aider">Aider-AI/aider</a></td><td>coding agent／pair programmer</td><td>CLI</td><td>Manage small changes with git diff, commits, and undo</td><td>Active; Apache-2.0; auto-commit does not bypass hooks</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/aaif-goose/goose">aaif-goose/goose</a></td><td>coding／general agent</td><td>CLI／desktop／API</td><td>Connect providers, MCP, and extensions</td><td>Active; Apache-2.0; start with low-privilege extensions</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://cursor.com/docs">Cursor</a></td><td>coding agent + AI editor</td><td>IDE／CLI／cloud／SDK</td><td>Multi-surface workflow from editor to background agent</td><td>Commercial; inspect permissions and data boundaries per surface</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/cline/cline">cline/cline</a></td><td>coding agent</td><td>IDE／CLI／SDK</td><td>Approve tools, files, and browser actions step by step</td><td>Active; Apache-2.0; an IDE surface is not a safety guarantee</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/continuedev/continue">continuedev/continue</a></td><td>coding agent</td><td>CLI／VS Code extension／JetBrains plugin</td><td>Study an existing open-source coding-agent and editor integration</td><td>Read-only and no longer actively maintained; Apache-2.0; 2.0.0 is the final release</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/OpenHands/OpenHands">OpenHands/OpenHands</a></td><td>software-development agent platform</td><td>web／CLI／SDK／cloud</td><td>Handle larger issues in a sandbox</td><td>Active; MIT; larger tasks need checkpoints and human review</td><td>⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="2">Workflow support</th><td><a href="https://github.com/obra/superpowers">obra/superpowers</a></td><td>skills／workflow collection</td><td>agent plugin／skills</td><td>Reference planning, TDD, debugging, and review flows</td><td>Active; MIT; adapt templates to your repo gate</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/yamadashy/repomix">yamadashy/repomix</a></td><td>repo context packer</td><td>CLI／MCP</td><td>Pack one-time codebase context for a reviewer or agent</td><td>Active; MIT; exclude secrets and unnecessary files first</td><td>⭐⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="1">History</th><td><a href="https://github.com/RooCodeInc/Roo-Code">Roo Code</a></td><td>historical coding agent</td><td>VS Code extension</td><td>Read the design history of multi-mode agents</td><td>Archived; Apache-2.0; not a current default for new projects</td><td>⭐⭐⭐</td></tr></tbody></table>

</details>

<a id="workflows-to-master-by-frequency"></a>
<a id="3-concrete-workflow-recipes"></a>
<details markdown="1"><summary>🧪 Expand: from daily small changes to team workflows</summary>

### Daily development
`plan → human approval → small change → diff → test → review → commit`. Each step can stop, making failures easier to locate.

### PR review
Treat an agent's opinion as a candidate finding. Ask for the file, behavior, reproduction, and suggested test; do not block on an unsupported “might be a problem.”

### CI
Use read-only tokens, minimum repository permissions, and fixed inputs. Do not turn issue, PR, or webpage text directly into executable commands. Keep publishing, merge, and secrets behind extra approval.

### Batch refactoring
Create baseline tests, then work module by module. Every batch needs a checkpoint, diff, and rollback; do not hand over the entire repo because an agent can edit many files.

</details>

<a id="common-pitfalls-anti-patterns"></a>
<details markdown="1"><summary>🧯 Expand: common mistakes, alternatives, and rollback</summary>

| Problem | Do this instead |
|---|---|
| An IDE screen makes you think a tool is IDE-only | Separate core identity from every surface |
| Treating OpenRouter, Ollama, and OpenCode as one category | OpenRouter is not a model, and Ollama is not a coding agent; choose router, runtime, and coding agent separately |
| Accepting a green test immediately | Read the diff, check coverage of the request, then approve manually |
| Judging safety by a fixed line count | Consider scope, testability, reversibility, and diff readability |
| Skipping hooks because Aider auto-commits | Enable required verification/hooks and follow the normal review gate |
| Multiple agents editing one file | Define ownership, use separate worktrees, and integrate manually |

Before rollback, inspect `git status` and the diff. Reverse only confirmed targets; never use a broad reset to erase someone else's work.

</details>
