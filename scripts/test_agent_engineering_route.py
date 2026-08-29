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
        "可以在一次長 run 裡，也可以跨 session／排程",
        "2026-08 的 survey preprint 把 Graph Engineering 提為新興典範",
        "Prompt→Context→Harness→Loop→Graph 五層工程分工",
    ),
    "en": (
        "can happen inside one long run or across sessions and schedules",
        "A 2026-08 survey preprint presents Graph Engineering as an emerging paradigm",
        "Prompt→Context→Harness→Loop→Graph five-layer engineering split",
    ),
    "zh-Hans": (
        "可以在一次长 run 里，也可以跨 session／调度",
        "2026-08 的 survey preprint 把 Graph Engineering 提为新兴范式",
        "Prompt→Context→Harness→Loop→Graph 五层工程分工",
    ),
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
