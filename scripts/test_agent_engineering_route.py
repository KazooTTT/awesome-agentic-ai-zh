"""Cross-chapter entry/deepening checks for Agent Loop and workflow graphs."""

from __future__ import annotations

from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "zh-TW": (
        ROOT / "stages/03-tool-use-and-hello-agent.md",
        ROOT / "stages/04-agent-frameworks.md",
    ),
    "en": (
        ROOT / "stages/03-tool-use-and-hello-agent.en.md",
        ROOT / "stages/04-agent-frameworks.en.md",
    ),
    "zh-Hans": (
        ROOT / "stages/03-tool-use-and-hello-agent.zh-Hans.md",
        ROOT / "stages/04-agent-frameworks.zh-Hans.md",
    ),
}
GLOSSARIES = {
    "zh-TW": ROOT / "resources/glossary.md",
    "en": ROOT / "resources/glossary.en.md",
    "zh-Hans": ROOT / "resources/glossary.zh-Hans.md",
}
GLOSSARY_MARKERS = {
    "zh-TW": (
        "### Agent Production Engineering",
        "課程會依序教 [Stage 3 的 Agent Loop](../stages/03-tool-use-and-hello-agent.md) → [Stage 4 的 Workflow Graph／Agent Framework](../stages/04-agent-frameworks.md) → [Stage 7 的 Agent Production Engineering：Harness、Loop 與 Graph](../stages/07-multi-agent-production.md)",
        "Prompt → Context → Harness → Loop → Graph 是五個互相重疊的**控制問題**",
        "可以在一次長 run 裡，也可以跨 session／排程",
        "這個名稱已出現在產業文章與研究討論中",
        "現有研究也沒有量測整體採用率",
        "這個總稱已有人採用，底下的做法更早就存在",
        "Prompt→Context→Harness→Loop→Graph 五個控制問題",
    ),
    "en": (
        "### Agent Production Engineering",
        "the course teaches [Stage 3 Agent Loop](../stages/03-tool-use-and-hello-agent.en.md) → [Stage 4 Workflow Graph / Agent Framework](../stages/04-agent-frameworks.en.md) → [Stage 7 Agent Production Engineering: Harness, Loops, and Graphs](../stages/07-multi-agent-production.en.md)",
        "Prompt → Context → Harness → Loop → Graph are five overlapping **control questions**",
        "can happen inside one long run or across sessions and schedules",
        "This name is already used in industry writing and research discussion",
        "Existing research has not measured overall adoption",
        "The umbrella term is already in use; the underlying practice is older",
        "Prompt→Context→Harness→Loop→Graph five control questions",
    ),
    "zh-Hans": (
        "### Agent Production Engineering",
        "课程会依序教 [Stage 3 的 Agent Loop](../stages/03-tool-use-and-hello-agent.zh-Hans.md) → [Stage 4 的 Workflow Graph／Agent Framework](../stages/04-agent-frameworks.zh-Hans.md) → [Stage 7 的 Agent Production Engineering：Harness、Loop 与 Graph](../stages/07-multi-agent-production.zh-Hans.md)",
        "Prompt → Context → Harness → Loop → Graph 是五个互相重叠的**控制问题**",
        "可以在一次长 run 里，也可以跨 session／调度",
        "这个名称已经出现在产业文章和研究讨论中",
        "现有研究也没有测量整体采用率",
        "这个总称已经有人采用，底下的做法更早就存在",
        "Prompt→Context→Harness→Loop→Graph 五个控制问题",
    ),
}
GLOSSARY_FORBIDDEN = {
    "zh-TW": ("這是正在形成的名稱", "Stage 7 Harness Engineering"),
    "en": ("This name is still emerging", "Stage 7 Harness Engineering"),
    "zh-Hans": ("这是正在形成的名称", "Stage 7 Harness Engineering"),
}
GLOSSARY_SOURCE_URLS = (
    "https://www.ibm.com/think/topics/loop-engineering",
    "https://arxiv.org/abs/2608.21884",
    "https://docs.langchain.com/oss/python/langgraph/workflows-agents",
    "https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/",
    "https://arxiv.org/abs/2608.21156",
)


@pytest.mark.parametrize("locale,pages", PAGES.items())
def test_existing_entry_chapters_support_the_stage7_route(
    locale: str, pages: tuple[Path, Path]
) -> None:
    stage3, stage4 = (page.read_text(encoding="utf-8") for page in pages)
    assert "**Agent Loop" in stage3
    assert "Workflow" in stage4
    assert "Graph" in stage4


@pytest.mark.parametrize("pages", PAGES.values())
def test_graph_engineering_is_not_misdefined_as_knowledge_graph(
    pages: tuple[Path, Path]
) -> None:
    _stage3, stage4 = (page.read_text(encoding="utf-8") for page in pages)
    assert "GraphRAG" not in stage4


@pytest.mark.parametrize("locale,glossary", GLOSSARIES.items())
def test_glossary_keeps_loop_and_graph_boundaries_current(
    locale: str, glossary: Path
) -> None:
    text = glossary.read_text(encoding="utf-8")
    assert all(marker in text for marker in GLOSSARY_MARKERS[locale])
    assert all(url in text for url in GLOSSARY_SOURCE_URLS)
    assert all(term not in text for term in GLOSSARY_FORBIDDEN[locale])
