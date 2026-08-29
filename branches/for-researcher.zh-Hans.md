# 研究人员延伸路线（For Researchers）

> [繁體中文](./for-researcher.md) | **简体中文** | [English](./for-researcher.en.md)

[← 回到主路线](../README.zh-Hans.md)

<!-- freshness: canonical=branches/for-researcher.md; verified_on=2026-08-29; scope=research-tools,citations,privacy,reproducibility,project-status; max_age_days=90 -->

<a id="使用场景研究阶段-ai-怎么帮"></a>

## 📌 这条路帮你做什么

这一页不是让 AI 替你当研究者，而是帮你**找到资料、看懂资料，再确认答案确实有资料支持**。

- 会用终端或 Python：先完成 [Track A 的 A3](../tracks/cli/A3-cli-production.zh-Hans.md) 或 [Track B 的 Stage 7](../stages/07-multi-agent-production.zh-Hans.md)。
- 不写程序：可以直接做下面的第一个练习，只需要浏览器和一篇公开 paper。

## 🎯 学习目标

完成这一页后，你可以：

1. 分清“AI 说了什么”和“原文真正写了什么”。
2. 逐条核对引用来源，不因看到引用编号就相信答案。
3. 知道哪些资料可以上传，哪些要先询问机构或资料拥有者。
4. 保存足够记录，让自己或同事能重新做一次。

## 🧩 八个核心词

- **Source（来源）**：用来核对的原始材料，如 paper、数据集或研究记录。
- **Claim（主张）**：可以检查的说法，如“方法 A 在数据集 B 上更好”。
- **Citation（引用）**：带你回到来源位置的路标；不保证来源支持主张。
- **Source Verification（来源核对）**：打开原文，检查作者内容、范围和限制是否与答案一致。
- **Literature RAG（文献 RAG）**：先从允许使用的文献找片段，再交给模型回答。
- **Reproducibility（可重复性）**：别人拿到资料、步骤、版本和设置后能跑出可比较结果。
- **Private Data（私人资料）**：不能任意公开或上传的内容，如受试者资料、病历、未公开稿件和公司机密。
- **Human Review（人工审查）**：人对 claim、citation、程序、表格和最终决定负责；AI 不能替你签名。

<a id="文献-rag--qa"></a>
## 🛠 第一个练习：核对一篇 paper 的三个答案

上传前先确认 **许可或版权** 和 **工具条款** 都允许。paper 公开可读，不代表可以交给另一个服务。

使用公开 paper：[Attention Is All You Need](https://arxiv.org/abs/1706.03762)。把 paper 加到能显示 citation 的工具，再复制：

```text
请只根据这篇 paper 回答下面三题。每个答案都要附 citation；找不到证据就写“unsupported／未支持”，不要猜。

1. 这篇 paper 想解决什么问题？
2. 作者提出的方法包含哪些主要部分？
3. 作者用哪些实验支持结果，又说了哪些限制？

回答后，列出每个 citation 对应的 original text。不要把你的推测写成作者的 claim。
```

接着做三个动作：

1. 点开每一个 citation。
2. 把答案和 original text 放在一起读；数字、数据集和适用范围都要相同。
3. 原文没有支持的句子标成 **unsupported／未支持**，不要为了让答案看起来完整而补一个不相干的引用。

<a id="层级建议"></a>
## 📚 先选一个入口

| 现在想做的事 | 先用什么 | 为什么 | 推荐度 |
|---|---|---|---|
| 在浏览器问一篇 paper | [Gemini Notebook（原 NotebookLM）](https://notebooklm.google.com/) | 从 citation 回到原文 | ⭐⭐⭐⭐⭐ |
| 整理文献库 | [Zotero](https://www.zotero.org/) | 先管理 PDF、作者、年份和笔记 | ⭐⭐⭐⭐⭐ |
| 用 Python 做可重跑的文献 RAG | [PaperQA2](https://github.com/Future-House/paper-qa) | 以科学文件和引用为中心 | ⭐⭐⭐⭐⭐ |

Gemini Notebook 是 Google 在 2026-07-16 为 NotebookLM 使用的现行名称；旧名称仅用于辨识。citation 是核对入口，不保证答案正确。

## ✅ 完成检查与下一站

- [ ] 我核对了三个答案，不只看 citation 编号。
- [ ] 我找到至少一个“原文支持”或“未支持”的例子。
- [ ] 我没有上传未经允许的私人资料。
- [ ] 我保存了来源、问题、工具名称、日期和自己的判断。

下一站：文献 RAG 走 [Stage 6](../stages/06-memory-rag.zh-Hans.md)；多 agent 走 [Stage 7](../stages/07-multi-agent-production.zh-Hans.md)；连接外部工具看 [MCP／Skills catalog](../resources/mcp-skills-catalog.zh-Hans.md)。

<details markdown="1"><summary>⏱ 展开：时间、账号、费用与资料安全</summary>

第一个练习约需 20–40 分钟。私人资料先确认 IRB、机构政策、合同、资料拥有者同意和工具条款。[Gemini Notebook 隐私说明](https://support.google.com/gemininotebook/answer/17004255)说明一般内容不会直接用于训练基础模型，除非用户选择提供 feedback；feedback 可能连同内容交由人员查看。这不代表研究资料自动获准上传。付费功能、配额和机构账号规则会变化，开始前查看官方页面。

</details>
<a id="必修阅读"></a>
<details markdown="1"><summary>📖 展开：建议阅读顺序</summary>

1. [Gemini Notebook citation 说明](https://support.google.com/gemininotebook/answer/16179559)；2. [Gemini Notebook 更名公告](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)；3. [Zotero 文档](https://www.zotero.org/support/)；4. [PaperQA2 README](https://github.com/Future-House/paper-qa)；5. [AI Scientist v2 LICENSE](https://github.com/SakanaAI/AI-Scientist-v2/blob/main/LICENSE)。

</details>
<a id="精选-projects"></a>
<a id="大纲与写作"></a>
<a id="文献管理集成"></a>
<details markdown="1"><summary>⭐ 展开：完整研究工具与项目表</summary>

<small>工具名称、授权和 repository 状态于 2026-08-29 UTC 依官方页面与 GitHub API 核查。推荐度是本学习地图的编辑评分，不是 GitHub stars 或排行榜。</small>
<table><thead><tr><th scope="col">分类</th><th scope="col">官方工具／项目</th><th scope="col">适合做什么</th><th scope="col">状态／授权</th><th scope="col">先知道的限制</th><th scope="col">推荐度</th></tr></thead>
<tbody><tr><th scope="rowgroup" rowspan="3">开始与整理</th><td><a href="https://notebooklm.google.com/">Gemini Notebook（原 NotebookLM）</a></td><td>用来源问答并回到 citation</td><td>正式可用；云服务</td><td>逐条核对引用；私人资料先看政策</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://www.zotero.org/">Zotero</a></td><td>管理 PDF、metadata、笔记与引用</td><td>正式可用；桌面／Web</td><td>解决来源管理，不替你判断研究质量</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/Future-House/paper-qa">Future-House/paper-qa</a></td><td>用 Python 建立 citation-grounded literature RAG</td><td>活跃；Apache-2.0</td><td>需要设置模型和文献来源并自行评测质量</td><td>⭐⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="4">探索与写作</th><td><a href="https://github.com/assafelovic/gpt-researcher">assafelovic/gpt-researcher</a></td><td>多来源搜索与 research brief</td><td>活跃；Apache-2.0</td><td>适合找候选来源，不是引用正确性的最终裁判</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/stanford-oval/storm">stanford-oval/storm</a></td><td>整理多种观点，再写大纲与长文</td><td>可用；MIT；更新较慢</td><td>确认依赖和资料来源仍兼容</td><td>⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/kaixindelele/ChatPaper">kaixindelele/ChatPaper</a></td><td>中文 paper 摘要、翻译与写作辅助</td><td>可用；自定义条款</td><td>不是标准 SPDX 授权；使用前读条款</td><td>⭐⭐⭐⭐⭐</td></tr><tr><td><a href="https://github.com/MuiseDestiny/zotero-gpt">MuiseDestiny/zotero-gpt</a></td><td>在 Zotero 阅读时与文献互动</td><td>可用；AGPL-3.0</td><td>外挂和模型设置需另外维护</td><td>⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="2">研究自动化</th><td><a href="https://github.com/flonat/flonat-research">flonat/flonat-research</a></td><td>参考研究用 skills、agents、hooks 与 LaTeX 流程</td><td>活跃；MIT</td><td>基础设施示例，不是所有领域都能直接套用</td><td>⭐⭐⭐</td></tr><tr><td><a href="https://github.com/SakanaAI/AI-Scientist-v2">SakanaAI/AI-Scientist-v2</a></td><td>研究端到端 multi-agent 实验架构</td><td>研究参考；自定义 source-code license</td><td>不是作者替代品，也不保证可直接投稿</td><td>⭐⭐⭐⭐</td></tr></tbody>
<tbody><tr><th scope="rowgroup" rowspan="1">历史</th><td><a href="https://github.com/langchain-ai/open_deep_research">langchain-ai/open_deep_research</a></td><td>阅读早期 deep-research agent 架构</td><td>已封存；MIT</td><td>仅作历史参考；新项目请改用仍在维护的工具</td><td>⭐⭐⭐⭐⭐</td></tr></tbody></table>

</details>
<a id="研究流程-marketplace"></a>
<a id="multi-llm-研究组合本-repo-维护者的研究-setup"></a>
<a id="multi-agent-for-research"></a>
<a id="必练流程按使用频率"></a>
<details markdown="1"><summary>🧪 展开：把单篇练习变成可重跑研究流程</summary>

### 文献 inbox
1. 保存 DOI、URL、作者、年份和取得日期。2. 让工具生成摘要，但把每个 claim 连回原文。3. 人工决定“阅读、排除、待确认”并记录理由。

### 跨 paper synthesis
先问每篇 paper 各自说什么，再比较它们同意、冲突或条件不同之处。不要先让模型写完整故事，再回头找引用。

### 程序与实验
保存数据版本、environment、seed、prompt、模型／工具版本、输出和人工修改。能重跑不代表结论正确。

### 投稿前
逐一核对 claim、citation、表格、图、程序和期刊规范。AI 可提供第二双眼睛，作者仍作最终判断并按期刊政策披露。

</details>
<details markdown="1"><summary>🧯 展开：常见错误、替代方案与排错</summary>

| 问题 | 先怎么做 |
|---|---|
| citation 不支持答案 | 标为未支持，缩小问题，不要硬补相似引用 |
| 工具读不到扫描 PDF | 先 OCR，再抽查页码和公式 |
| 多篇 paper 结论混在一起 | 要求每个 claim 列 paper 名称、页码或段落后再综合 |
| 资料不能上传云端 | 使用机构批准环境，必要时看 [Stage 6](../stages/06-memory-rag.zh-Hans.md) 的本机 RAG 路线 |
| 自动化太复杂 | 回到“一篇 paper、三个问题、逐条核对”，可靠后再加工具 |

没有任何工具能替代 IRB、资料治理、作者责任或领域专家判断。

</details>
