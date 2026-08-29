# Extension Path for Researchers

> [繁體中文](./for-researcher.md) | [简体中文](./for-researcher.zh-Hans.md) | **English**

[← Back to the main route](../README.en.md)

<!-- freshness: canonical=branches/for-researcher.md; verified_on=2026-08-29; scope=research-tools,citations,privacy,reproducibility,project-status; max_age_days=90 -->

<a id="use-cases"></a>

## 📌 What this path helps you do

This page is not meant to make AI your researcher. It helps with one simpler job: **find information, understand it, and check that the answer is truly supported by evidence.**

- If you use a terminal or Python: complete [Track A's A3](../tracks/cli/A3-cli-production.en.md) or [Track B's Stage 7](../stages/07-multi-agent-production.en.md) first.
- If you do not code: you can start with the first exercise below. You only need a browser and one public paper.

## 🎯 Learning goals

After this page, you can:

1. Distinguish what AI said from what the original text actually says.
2. Check each numbered reference instead of trusting an answer just because it has reference numbers.
3. Know which data may be uploaded and which requires permission from an institution or data owner first.
4. Keep enough records for yourself or a colleague to repeat the work.

## 🧩 Eight core terms

- **Source**: the original material you use for verification, such as a paper, dataset, or research record. Think of it as the textbook behind an answer.
- **Claim**: a statement that can be checked, such as “Method A performs better on Dataset B.”
- **Citation**: a signpost back to a source location. It tells you where to look; it does not guarantee that the source supports the claim.
- **Source Verification**: open the original and check whether the authors' wording, scope, and limitations match the answer.
- **Literature RAG**: find passages in literature you allow the tool to use, then give those passages to a model to answer. Like looking in the book before answering.
- **Reproducibility**: someone with your data, steps, versions, and settings can rerun the work and obtain comparable results.
- **Private Data**: material that cannot be freely disclosed or uploaded, such as participant data, medical records, unpublished manuscripts, or company secrets.
- **Human Review**: a person remains responsible for claims, citations, code, tables, and the final decision. AI cannot sign for you or bear that responsibility.

<a id="literature-rag--qa"></a>
## 🛠 First exercise: verify three answers about one paper

Before uploading, check that the paper's **license or copyright** and the **tool's terms** allow it. Public to read is not permission to upload.

Use the public paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Add the paper to a citation-capable tool, then copy the following:

```text
Answer the three questions below using only this paper. Attach a citation to every answer; if you cannot find evidence, write “unsupported／未支持” and do not guess.

1. What problem does this paper aim to solve?
2. What are the major parts of the method proposed by the authors?
3. Which experiments support the results, and what limitations do the authors mention?

After answering, list the original text corresponding to every citation. Do not turn your inference into an author's claim.
```

Then do three things:

1. Open every citation.
2. Read the answer beside the original text; numbers, datasets, and scope must match.
3. Mark a sentence **unsupported／未支持** when the original does not support it; do not add an unrelated citation just to make the answer look complete.

<a id="tier-recommendations"></a>
## 📚 Choose an entry point

| What you want to do | Start with | Why | Rating |
|---|---|---|---|
| Ask about a paper in a browser | [Gemini Notebook (formerly NotebookLM)](https://notebooklm.google.com/) | Upload a source and return to the original from each citation | ⭐⭐⭐⭐⭐ |
| Organize your literature library | [Zotero](https://www.zotero.org/) | Manage PDFs, authors, years, and notes before adding AI | ⭐⭐⭐⭐⭐ |
| Build rerunnable literature RAG with Python | [PaperQA2](https://github.com/Future-House/paper-qa) | Centers answers on scientific documents and citations | ⭐⭐⭐⭐⭐ |

Gemini Notebook is Google's current name for NotebookLM as of 2026-07-16; the old name remains only for recognition. A citation is an entry point for verification, not a guarantee that an answer is correct.

## ✅ Completion check and next stop

- [ ] I checked all three answers, not just the citation numbers.
- [ ] I found at least one example of “supported by the original” or “unsupported.”
- [ ] I did not upload private data without permission.
- [ ] I saved the sources, questions, tool name, date, and my own judgment.

Next: for literature RAG, go to [Stage 6](../stages/06-memory-rag.en.md); for multiple agents, go to [Stage 7](../stages/07-multi-agent-production.en.md); to connect the workflow to external tools, see the [MCP／Skills catalog](../resources/mcp-skills-catalog.en.md).

<details markdown="1">
<summary>⏱ Expand: time, accounts, cost, and data safety</summary>

The first exercise takes about 20–40 minutes. For private data, pause and confirm IRB requirements, institutional policy, contracts, the data owner's consent, and the tool's terms.

[Gemini Notebook privacy information](https://support.google.com/gemininotebook/answer/17004255) says ordinary content is not directly used to train foundation models unless a user chooses to provide feedback; feedback may be reviewed by people together with its content. This does not mean your research data is automatically approved for upload. Medical records, participant data, unpublished manuscripts, and company secrets still follow your own governance rules.

Paid features, quotas, and institutional-account rules change. Check official pages before starting; do not preserve an easily outdated fixed price in the teaching material.

</details>

<a id="required-reading"></a>
<details markdown="1">
<summary>📖 Expand: suggested reading order</summary>

1. [Gemini Notebook citation guide](https://support.google.com/gemininotebook/answer/16179559): learn to return from an answer to the original.
2. [Gemini Notebook rename announcement](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/): confirm the current name and product positioning.
3. [Zotero documentation](https://www.zotero.org/support/): organize sources first.
4. [PaperQA2 README](https://github.com/Future-House/paper-qa): then examine programmatic literature RAG.
5. [AI Scientist v2 LICENSE](https://github.com/SakanaAI/AI-Scientist-v2/blob/main/LICENSE): read the boundaries before advanced research automation.

</details>

<a id="curated-projects"></a>
<a id="outline--writing"></a>
<a id="citation-manager-integrations"></a>
<details markdown="1">
<summary>⭐ Expand: complete research tools and projects table</summary>

<small>Tool names, licenses, and repository status were checked against official pages and the GitHub API on 2026-08-29 UTC. Ratings are editorial scores from this learning map, not GitHub stars or a ranking.</small>

<table>
<thead><tr><th scope="col">Category</th><th scope="col">Official tool／project</th><th scope="col">What it suits</th><th scope="col">Status／license</th><th scope="col">Limitation to know first</th><th scope="col">Rating</th></tr></thead>
<tbody>
<tr><th scope="rowgroup" rowspan="3">Start and organize</th><td><a href="https://notebooklm.google.com/">Gemini Notebook (formerly NotebookLM)</a></td><td>Ask questions from sources and return to citations</td><td>Available; cloud service</td><td>Check citations one by one; review policy before private data</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://www.zotero.org/">Zotero</a></td><td>Manage PDFs, metadata, notes, and citations</td><td>Available; desktop／Web</td><td>It solves source management first; it does not judge research quality for you</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/Future-House/paper-qa">Future-House/paper-qa</a></td><td>Build citation-grounded literature RAG with Python</td><td>Active; Apache-2.0</td><td>Configure models and literature sources; evaluate quality yourself</td><td>⭐⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="4">Explore and write</th><td><a href="https://github.com/assafelovic/gpt-researcher">assafelovic/gpt-researcher</a></td><td>Multi-source search and research briefs</td><td>Active; Apache-2.0</td><td>Good for candidate sources, not the final judge of citation accuracy</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/stanford-oval/storm">stanford-oval/storm</a></td><td>Organize perspectives, then write outlines and long-form text</td><td>Usable; MIT; slower updates</td><td>Check that dependencies and sources remain compatible</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/kaixindelele/ChatPaper">kaixindelele/ChatPaper</a></td><td>Chinese paper summaries, translation, and writing support</td><td>Usable; custom terms</td><td>Not a standard SPDX license; read terms before commercial use or redistribution</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/MuiseDestiny/zotero-gpt">MuiseDestiny/zotero-gpt</a></td><td>Interact with literature while reading in Zotero</td><td>Usable; AGPL-3.0</td><td>Maintain the plugin and model settings separately</td><td>⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="2">Research automation</th><td><a href="https://github.com/flonat/flonat-research">flonat/flonat-research</a></td><td>Reference skills, agents, hooks, and LaTeX research workflows</td><td>Active; MIT</td><td>Infrastructure examples, not a direct fit for every field</td><td>⭐⭐⭐</td></tr>
<tr><td><a href="https://github.com/SakanaAI/AI-Scientist-v2">SakanaAI/AI-Scientist-v2</a></td><td>End-to-end multi-agent research experiment architecture</td><td>Research reference; custom source-code license</td><td>Not a replacement for authors and not a guarantee of submission readiness</td><td>⭐⭐⭐⭐</td></tr>
</tbody>
<tbody>
<tr><th scope="rowgroup" rowspan="1">History</th><td><a href="https://github.com/langchain-ai/open_deep_research">langchain-ai/open_deep_research</a></td><td>Read an early deep-research agent architecture</td><td>archived; MIT</td><td>Historical reference only, not a current default for new projects</td><td>⭐⭐⭐⭐⭐</td></tr>
</tbody>
</table>

</details>

<a id="research-workflow-marketplaces"></a>
<a id="multi-llm-research-stack-maintainer-setup"></a>
<a id="multi-agent-for-research"></a>
<a id="workflows-to-master"></a>
<details markdown="1">
<summary>🧪 Expand: turn one exercise into a rerunnable research workflow</summary>

### Literature inbox

1. Save the DOI, URL, author, year, and retrieval date.
2. Let the tool produce a summary, but link every claim back to the original.
3. Decide manually “read, exclude, or verify later,” and record why.

### Cross-paper synthesis

Ask what each paper says on its own first, then compare where they agree, conflict, or use different conditions. Do not ask the model for a complete-looking story first and search for citations afterward.

### Code and experiments

Save data versions, environment, seed, prompt, model／tool version, outputs, and manual edits. Being able to rerun does not make a conclusion correct, but without these records errors are usually harder to find.

### Before submission

Check every claim, citation, table, figure, piece of code, and journal rule. AI can provide a second pair of eyes; authors still make the final judgment and disclose use according to journal policy.

</details>

<details markdown="1">
<summary>🧯 Expand: common mistakes, alternatives, and troubleshooting</summary>

| Problem | What to do first |
|---|---|
| A citation does not support the answer | Mark the sentence unsupported; narrow the question; do not force in a seemingly related citation |
| The tool cannot read a scanned PDF | Run OCR first, then spot-check page numbers and formulas |
| Conclusions from several papers get mixed together | Require each claim to list the paper name, page, or section before synthesis |
| Data cannot be uploaded to the cloud | Use an institution-approved environment; if needed, see the local RAG path in [Stage 6](../stages/06-memory-rag.en.md) |
| Automation becomes too complex | Return to “one paper, three questions, one-by-one verification”; add tools only after the small workflow is reliable |

No tool can replace IRB, data governance, author responsibility, or a domain expert's judgment.

</details>
