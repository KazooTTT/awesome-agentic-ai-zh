"""Stage 07 reader path, current-fact, diagram, and locale regression checks."""

from __future__ import annotations

import hashlib
import re
import struct
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "zh-TW": ROOT / "stages/07-multi-agent-production.md",
    "en": ROOT / "stages/07-multi-agent-production.en.md",
    "zh-Hans": ROOT / "stages/07-multi-agent-production.zh-Hans.md",
}
DIAGRAMS = {
    "zh-TW": (
        ROOT / "resources/diagrams/agent-engineering-5layer.png",
        ROOT / "resources/diagrams/inside-a-graph.png",
    ),
    "en": (
        ROOT / "resources/diagrams/agent-engineering-5layer.en.png",
        ROOT / "resources/diagrams/inside-a-graph.en.png",
    ),
    "zh-Hans": (
        ROOT / "resources/diagrams/agent-engineering-5layer.zh-Hans.png",
        ROOT / "resources/diagrams/inside-a-graph.zh-Hans.png",
    ),
}
CORE_LABELS = {
    "zh-TW": (
        "Multi-Agent（多 Agent）",
        "Orchestration",
        "Handoff",
        "Harness",
        "Eval",
        "Observability",
        "Guardrail",
        "Loop Engineering",
        "Graph Engineering",
    ),
    "en": (
        "Multi-Agent",
        "Orchestration",
        "Handoff",
        "Harness",
        "Eval",
        "Observability",
        "Guardrail",
        "Loop Engineering",
        "Graph Engineering",
    ),
    "zh-Hans": (
        "Multi-Agent（多 Agent）",
        "Orchestration",
        "Handoff",
        "Harness",
        "Eval",
        "Observability",
        "Guardrail",
        "Loop Engineering",
        "Graph Engineering",
    ),
}
CORE_SECTION_HEADINGS = {
    "zh-TW": ("## 🧩 九個核心詞", "## 🚪 進入條件"),
    "en": ("## 🧩 Nine Core Terms", "## 🚪 Entry Conditions"),
    "zh-Hans": ("## 🧩 九个核心词", "## 🚪 进入条件"),
}
PAGE_TITLES = {
    "zh-TW": "# Stage 7 — Loop／Graph Engineering：讓 Agent 穩定運作",
    "en": "# Stage 7 — Loop & Graph Engineering: Making Agents Reliable",
    "zh-Hans": "# Stage 7 — Loop／Graph Engineering：让 Agent 稳定运行",
}
OLD_PAGE_TITLES = {
    "zh-TW": "# Stage 7 — Loop／Graph Engineering：多 Agent 與穩定運作",
    "en": "# Stage 7 — Loop & Graph Engineering: Multi-Agent Production",
    "zh-Hans": "# Stage 7 — Loop／Graph Engineering：多 Agent 与稳定运行",
}
EXERCISE_DIRS = (
    "01-multi-agent-debate",
    "02-eval",
    "03-observability",
    "04-sdk-advanced",
    "05-deploy",
)
CURRENT_FACT_URLS = {
    "https://openai.github.io/openai-agents-python/running_agents/",
    "https://openai.github.io/openai-agents-python/multi_agent/",
    "https://www.ibm.com/think/topics/loop-engineering",
    "https://arxiv.org/abs/2608.21884",
    "https://docs.langchain.com/oss/python/langgraph/workflows-agents",
    "https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/",
    "https://arxiv.org/abs/2608.21156",
    "https://platform.claude.com/docs/en/test-and-evaluate/develop-tests",
    "https://github.com/open-telemetry/semantic-conventions-genai",
    "https://github.com/earendil-works/pi",
    "https://github.com/anomalyco/opencode",
    "https://github.com/stablyai/orca",
    "https://github.com/yc-software/qm",
}
REQUIRED_READING_URLS = (
    "https://www.anthropic.com/engineering/building-effective-agents",
    "https://openai.github.io/openai-agents-python/running_agents/",
    "https://openai.github.io/openai-agents-python/multi_agent/",
    "https://docs.langchain.com/oss/python/langgraph/workflows-agents",
    "https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/",
)
FORBIDDEN_TERMINOLOGY = (
    "Loop Engineering（本專案教學用語）",
    "Graph Engineering（本專案教學用語）",
    "Loop Engineering (a teaching term in this project)",
    "Graph Engineering (a teaching term in this project)",
    "Loop Engineering（本项目教学用语）",
    "Graph Engineering（本项目教学用语）",
)
ROUTE_MARKERS = {
    "zh-TW": (
        "Stage 3：Agent Loop 入門",
        "Stage 4：Workflow Graph 入門",
        "Stage 7：Loop／Graph Engineering 整合",
    ),
    "en": (
        "Stage 3: Agent Loop entry",
        "Stage 4: Workflow Graph entry",
        "Stage 7: Loop & Graph Engineering integration",
    ),
    "zh-Hans": (
        "Stage 3：Agent Loop 入门",
        "Stage 4：Workflow Graph 入门",
        "Stage 7：Loop／Graph Engineering 整合",
    ),
}
RESOURCE_URL_RATINGS = (
    ("https://www.anthropic.com/engineering/building-effective-agents", "⭐⭐⭐⭐⭐"),
    ("https://openai.github.io/openai-agents-python/multi_agent/", "⭐⭐⭐⭐⭐"),
    ("https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/", "⭐⭐⭐⭐"),
    ("https://github.com/langchain-ai/langgraph", "⭐⭐⭐⭐⭐"),
    ("https://platform.claude.com/docs/en/test-and-evaluate/develop-tests", "⭐⭐⭐⭐⭐"),
    ("https://github.com/promptfoo/promptfoo", "⭐⭐⭐⭐⭐"),
    ("https://github.com/open-telemetry/semantic-conventions-genai", "⭐⭐⭐⭐"),
    ("https://github.com/langfuse/langfuse", "⭐⭐⭐⭐⭐"),
    ("https://github.com/Arize-ai/phoenix", "⭐⭐⭐⭐"),
    ("https://github.com/comet-ml/opik", "⭐⭐⭐⭐"),
    ("https://github.com/anthropics/claude-agent-sdk-python", "⭐⭐⭐⭐⭐"),
    ("https://github.com/deepseek-ai/deepseek-harness", "⭐⭐⭐"),
    ("https://github.com/xai-org/grok-build", "⭐⭐⭐"),
    ("https://github.com/NVIDIA/NemoClaw", "⭐⭐⭐"),
    ("https://github.com/bentoml/BentoML", "⭐⭐⭐⭐"),
    ("https://github.com/crewAIInc/crewAI", "⭐⭐⭐⭐"),
    ("https://github.com/stablyai/orca", "⭐⭐⭐⭐"),
    ("https://github.com/yc-software/qm", "⭐⭐⭐⭐"),
    ("https://github.com/AMAP-ML/LongHorizon-Harness", "⭐⭐⭐"),
    ("https://github.com/cft0808/edict", "⭐⭐⭐"),
)


def _without_closed_details(text: str) -> str:
    return re.sub(
        r"<details(?![^>]*\bopen\b)[^>]*>.*?</details>",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )


def _external_urls(text: str) -> list[str]:
    return re.findall(r"https://[^\s<>)\"']+", text)


@pytest.mark.parametrize("locale,page", PAGES.items())
def test_reader_path_has_six_closed_disclosures(locale: str, page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    assert text.startswith(PAGE_TITLES[locale])
    assert OLD_PAGE_TITLES[locale] not in text
    assert len(re.findall(r'<details markdown="1">', text)) == 6
    assert not re.search(r"<details[^>]*\bopen\b", text)
    visible = _without_closed_details(text)
    assert "Stage 7" in visible
    assert "python test.py" in visible


@pytest.mark.parametrize("locale,page", PAGES.items())
def test_all_core_terms_are_bold_and_defined_before_exercises(
    locale: str, page: Path
) -> None:
    text = page.read_text(encoding="utf-8")
    core_heading, next_heading = CORE_SECTION_HEADINGS[locale]
    core_start = text.index(core_heading)
    core_end = text.index(next_heading, core_start)
    core = text[core_start:core_end]
    positions = []
    for label in CORE_LABELS[locale]:
        marker = f"**{label}**"
        assert marker in core
        positions.append(core.index(marker))
    assert positions == sorted(positions)


@pytest.mark.parametrize("locale,page", PAGES.items())
def test_five_layer_map_is_scope_not_chapter_numbering(locale: str, page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    visible = _without_closed_details(text)
    assert all(marker in visible for marker in ROUTE_MARKERS[locale])
    assert not any(term in text for term in FORBIDDEN_TERMINOLOGY)


@pytest.mark.parametrize("page", PAGES.values())
def test_required_reading_and_featured_resources_are_visible(page: Path) -> None:
    visible = _without_closed_details(page.read_text(encoding="utf-8"))
    assert all(url in visible for url in REQUIRED_READING_URLS)
    assert all(url in visible and rating in visible for url, rating in RESOURCE_URL_RATINGS)


@pytest.mark.parametrize("page", PAGES.values())
def test_five_real_exercises_are_visible_and_no_fake_sixth_exists(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    visible = _without_closed_details(text)
    for folder in EXERCISE_DIRS:
        assert f"cd examples/stage-7/{folder}" in visible
        assert (ROOT / "examples/stage-7" / folder / "README.md").is_file()
    assert not re.search(r"^### .*(Exercise|練習|练习) 6", text, flags=re.MULTILINE)


def test_three_locales_have_the_same_external_urls_and_current_fact_sources() -> None:
    url_lists = {
        locale: _external_urls(page.read_text(encoding="utf-8"))
        for locale, page in PAGES.items()
    }
    assert url_lists["zh-TW"] == url_lists["en"] == url_lists["zh-Hans"]
    assert CURRENT_FACT_URLS <= set(url_lists["zh-TW"])
    for page in PAGES.values():
        assert "2026-08-29 UTC" in page.read_text(encoding="utf-8")


@pytest.mark.parametrize("page", PAGES.values())
def test_resource_table_has_accessible_merged_groups_and_20_ratings(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    table = re.search(r"<table>.*?⭐{3,5}.*?</table>", text, flags=re.DOTALL)
    assert table
    assert len(re.findall(r'<th scope="col">', table.group())) == 5
    groups = re.findall(r"<tbody>(.*?)</tbody>", table.group(), flags=re.DOTALL)
    expected = [4, 6, 5, 5]
    assert len(groups) == len(expected)
    for group, rows in zip(groups, expected):
        assert len(re.findall(r"<tr>", group)) == rows
        assert f'scope="rowgroup" rowspan="{rows}"' in group
    pairs = tuple(
        re.findall(
            r'<a href="([^"]+)">.*?</a></td><td>(⭐{3,5})</td>',
            table.group(),
        )
    )
    assert pairs == RESOURCE_URL_RATINGS


@pytest.mark.parametrize("page", PAGES.values())
def test_static_leaderboard_and_stale_project_claims_are_absent(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    forbidden = (
        "benchmarkingagents.com",
        "rapidclaw.dev",
        "anthropics/anthropic-cookbook",
        "laude-institute/terminal-bench",
        "princeton-nlp/SWE-agent",
        "geekan/MetaGPT",
        "hiyouga/LLaMA-Factory",
        "langchain-ai/langserve",
        "qwen2.5:3b",
        "Prompt Caching（Anthropic-only）",
        "Fable 5",
        "Mythos 5",
        "Opus 4.8",
        '""',
        "“”",
    )
    assert not any(term in text for term in forbidden)
    assert not re.search(
        r"SOTA.{0,80}\d+(?:\.\d+)?%|\d+(?:\.\d+)?%.{0,80}SOTA",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )


def test_locale_diagrams_are_distinct_large_pngs_and_referenced() -> None:
    hashes: set[str] = set()
    for locale, diagrams in DIAGRAMS.items():
        page_text = PAGES[locale].read_text(encoding="utf-8")
        for diagram in diagrams:
            data = diagram.read_bytes()
            assert data.startswith(b"\x89PNG\r\n\x1a\n")
            width, height = struct.unpack(">II", data[16:24])
            assert width >= 1600 and height >= 900
            hashes.add(hashlib.sha256(data).hexdigest())
            assert f"../resources/diagrams/{diagram.name}" in page_text
    assert len(hashes) == 6


def test_english_page_has_no_untranslated_cjk() -> None:
    text = PAGES["en"].read_text(encoding="utf-8")
    text = text.replace("繁體中文", "").replace("简体中文", "")
    assert re.search(r"[\u3400-\u9fff]", text) is None
