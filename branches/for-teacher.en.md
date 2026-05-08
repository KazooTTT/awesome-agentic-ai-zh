# For Teachers — Specialized Branch

> [繁體中文](./for-teacher.md) | [简体中文](./for-teacher.zh-CN.md) | **English**


> [← Back to main path README](../README.en.md) · Continue here after **Track A's A3** or **Track B's Stage 7**. Apply agentic AI to teaching workflows.

## Use Cases

- Lesson plan generation
- Quiz / rubric creation
- Slide deck preparation
- Student feedback synthesis
- Curriculum mapping

## Curated Projects

### Teaching Workflow Skills

(Most are not yet skill-marketplace packaged. This branch has the most room for community contribution — see CONTRIBUTING.md.)

### Useful Building Blocks

#### [obra/superpowers](https://github.com/obra/superpowers) ⭐⭐⭐⭐
General writing / brainstorming skills. Adaptable for lesson prep.

#### [Claude Code](https://github.com/anthropics/claude-code) (with custom CLAUDE.md) ⭐⭐⭐⭐⭐
★ 120k+ — A good place for teachers to start. Use Claude.ai (web) for low-barrier exploration; upgrade to Claude Code when a workflow becomes repeatable.

### Teaching Course Materials (for teachers preparing classes)

#### [huggingface/agents-course](https://github.com/huggingface/agents-course) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 28k+ |
| License | Apache-2.0 |

**What it teaches**: Hugging Face's official agents curriculum — notebooks, exercises, certifications. A ready-made **AI agent teaching artifact**.

**Best for**: Teachers running an "AI agents intro" workshop or class who want existing materials to teach from or adapt.

**Notes**: This teaches *how to build agents* — it's not an "AI tutor for students" tool.

---

#### [datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) ⭐⭐⭐⭐ (Chinese)

| Field | Value |
|---|---|
| Language | Chinese (zh-CN) |
| Stars | ★ 13k+ |
| License | NOASSERTION |

**What it teaches**: Datawhale's Chinese-language LLM application development course — RAG, agents, chapter exercises. A ready-made template for Chinese-speaking teachers preparing class material.

**Best for**: Chinese-language teachers wanting a ready LLM curriculum to adapt to their students' level.

**Notes**: Same caveat as `huggingface/agents-course` — it's "teach students to build LLM apps," not "AI assistant for the teacher."

---

### Prompt Libraries

#### [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) ⭐⭐⭐⭐

| Field | Value |
|---|---|
| Stars | ★ 161k+ |
| License | NOASSERTION (CC0 / public-domain-style, but no SPDX) |

**What it teaches**: Community-maintained prompt megacatalog — "act as X" templates covering hundreds of roles (teacher, interviewer, stand-up comedian, debater, ...). Teachers can use it as "prompt writing examples" to show students, or borrow specific prompts for in-class demos.

**Best for**: Teachers introducing "prompt engineering" who want concrete examples of different writing styles to compare.

**Notes**: Quality varies — treat as a sourcebook to pick from, not "use everything as-is."

---

### Reading Material

#### [The Effortless Academic — Beginner Guides](https://effortlessacademic.com/claude-code-and-cowork-for-academics-beginner-guide-part-1/)
Multi-part guide for academics adopting Claude Code, applicable to teachers.

## Workflows To Build

These are templates — adapt to your subject:

- **Lesson plan generator**: Prompt with curriculum + topic → outline → slides → assessment
- **Rubric creation**: Sample student work + learning objective → rubric draft
- **Personalized feedback**: Student submission + rubric → individualized written feedback (with human review)

### 3 Copy-Paste Prompt Templates

**1. Lesson outline generator** (paste into Claude.ai):
```
You are a [SUBJECT] teacher. I'm preparing a [DURATION]-minute class for
[GRADE] students on the topic "[TOPIC]". Prior knowledge: [SUMMARY].
Produce:
1. Learning goals (3-4 bullets, use Bloom's taxonomy verbs)
2. Class outline with time allocation
3. 1 in-class activity / discussion prompt
4. 1 follow-up assessment item
Don't introduce content outside the topic I gave.
```

**2. Rubric draft**:
```
I have a [ASSIGNMENT TYPE] for [GRADE] students on [TOPIC].
Learning objectives: [2-3 bullets].
Produce a 4-level rubric (Excellent / Proficient / Developing / Needs work)
with one paragraph per level across 4 dimensions:
content depth / organization / argumentation or calculation / clarity.
Make descriptions concrete and observable, not vague terms like "high quality".
```

**3. Student feedback synthesis**:
```
Below are [N] student submission excerpts:
[PASTE TEXT]

Please:
1. Summarize 3 common strengths across this batch
2. Summarize 3 common weaknesses
3. For the most common weakness, suggest 1-2 things to reinforce next class
Don't write per-student feedback — I'll do that myself.
```

## Privacy + Ethics (Important)

Teachers using LLMs are different from regular users — **student data is involved**. Hard rules:

- **Don't put student PII into public LLMs** (names, IDs, contact info, grades). Anonymize first ("Student A / B / C")
- **AI assistance ≠ AI grading**: drafting feedback / rubrics with LLM is fine, but **final grades require human judgment** — LLMs aren't reliable on complex evaluation yet
- **Disclose to students**: if class material is AI-assisted, disclose it (similar to declaring AI tool use in papers). Teaching integrity matters
- **Fact-check**: LLMs hallucinate citations, scholar names, research data. Domain content **must be verified** before class
- **Student work copyright**: don't bulk-upload student writing to third-party services for analysis — risks FERPA / GDPR violations

If your school / institution has an AI policy, **that takes priority** over this guide.

## Tier Recommendations for Teachers

Most teachers should stay at **Tier 0 (browser chat)** or **Tier 1 (Claude Desktop)**:

- **Tier 0**: Claude.ai web chat — copy/paste prompts, no install
  - Good for: occasional lesson prep, one-off tasks, item generation, writing emails
  - Example: copy the lesson-outline prompt above, fill in topic, run
- **Tier 1**: Claude Desktop / [NotebookLM](https://notebooklm.google.com/) — file uploads, conversation history
  - Good for: grading / organizing a semester's data, course mapping, bulk-importing reading list PDFs and querying them
  - Example: upload your full course reading list to NotebookLM; query throughout the semester
- **Tier 2+ (CLI / SDK)**: only if you're **automating a recurring flow**
  - Example: every week 30 student submissions → auto-generated draft feedback
  - Non-coder teachers: **ask the school IT or a student RA** to set up; you only use the output

> Once you're at Tier 2+, follow [Track A — CLI Power User](../tracks/cli/A1-cli-intro.en.md).

## Other Branches Also Apply

Many teachers are also researchers / knowledge workers. These branches overlap:

- **Also doing research** (lit review, paper writing, references) → [Researcher branch](./for-researcher.en.md)
- **Reports / meeting notes / cross-tool integration** (Notion, Excel, email) → [Knowledge Worker branch](./for-knowledge-worker.en.md)
- **Connect AI to Notion / Obsidian / Lark / etc.** → [`resources/mcp-skills-catalog.en.md`](../resources/mcp-skills-catalog.en.md)

## Community Note

This branch is the smallest curated section currently. Contributions especially welcome:

- Lesson plan generation skills
- Subject-specific prompt libraries (literature teacher's prompts, math teacher's prompts, language teacher's prompts...)
- Teacher-specific MCP servers (gradebook integrations, LMS connections like Canvas / Moodle / Google Classroom)
- **Subject + grade-level case studies** (e.g., "I used AI to teach middle-school math for a semester — here's my workflow")

See [CONTRIBUTING.md](../CONTRIBUTING.md).
