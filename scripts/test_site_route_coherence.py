from __future__ import annotations

from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]

LOCALES = {
    "zh-TW": {
        "suffix": "",
        "track_a": "### Track A",
        "track_b": "### Track B",
        "optional": ("建議", "不擋"),
        "stage5_core": "5.1–5.4",
        "legacy_a2_anchor": "-進-a3-前的自我檢查",
        "legacy_stage5_anchor": "-進入-stage-6-前的自我檢查",
        "legacy_roadmap_anchors": (
            "近期想補的缺口",
            "進行中--隨時可貢獻",
            "-動手練習覆蓋補齊",
            "-audience-branch-深化",
            "-stage-2--stage-3-2026-freshness-小修",
            "基礎建設maintainer-進行中",
            "想法箱待討論還沒承諾",
        ),
        "foundation_route": "`Stage 0 → Stage 1 → Stage 2`",
        "track_a_route": "`A1 → A2 → Stage 5 → A3 → Stage 8`",
        "track_b_route": "`Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 7.5 → Stage 8`",
        "roadmap_stale": (
            "2026-05 snapshot",
            "Stage 2 / Stage 3 2026 freshness 小修",
            "GitHub Pages,評估中",
        ),
        "stage3_title": "Stage 3 — 工具使用與第一個 Agent Loop",
        "stage3_topic": "工具使用與第一個 Agent Loop",
        "stage4_title": "Stage 4 — Workflow Graph 與 Agent 框架",
        "stage4_topic": "Workflow Graph 與 Agent 框架",
        "stage7_title": "Stage 7 — Agent Production Engineering：Harness、Loop 與 Graph",
        "stage7_topic": "Agent Production Engineering：Harness、Loop 與 Graph",
        "stage7_compact": "Stage 7 — Agent Production Engineering",
    },
    "en": {
        "suffix": ".en",
        "track_a": "### Track A",
        "track_b": "### Track B",
        "optional": ("recommended", "does not block"),
        "stage5_core": "5.1–5.4",
        "legacy_a2_anchor": "-self-check-before-a3",
        "legacy_stage5_anchor": "-self-check-before-stage-6",
        "legacy_roadmap_anchors": (
            "near-term-gaps-we-want-to-fill",
            "in-progress--always-open-to-contributions",
            "-fill-out-hands-on-exercise-coverage",
            "-deepen-the-audience-branch-files",
            "-stage-2--stage-3-2026-freshness-touch-up",
            "infrastructure-maintainer-in-progress",
            "idea-box-pending-discussion-not-committed-yet",
        ),
        "foundation_route": "`Stage 0 → Stage 1 → Stage 2`",
        "track_a_route": "`A1 → A2 → Stage 5 → A3 → Stage 8`",
        "track_b_route": "`Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 7.5 → Stage 8`",
        "roadmap_stale": (
            "2026-05 snapshot",
            "Stage 2 / Stage 3 2026 freshness",
            "GitHub Pages, under evaluation",
        ),
        "stage3_title": "Stage 3 — Tool Use & Your First Agent Loop",
        "stage3_topic": "Tool Use & Your First Agent Loop",
        "stage4_title": "Stage 4 — Workflow Graphs & Agent Frameworks",
        "stage4_topic": "Workflow Graphs & Agent Frameworks",
        "stage7_title": "Stage 7 — Agent Production Engineering: Harness, Loops, and Graphs",
        "stage7_topic": "Agent Production Engineering: Harness, Loops, and Graphs",
        "stage7_compact": "Stage 7 — Agent Production Engineering",
    },
    "zh-Hans": {
        "suffix": ".zh-Hans",
        "track_a": "### Track A",
        "track_b": "### Track B",
        "optional": ("建议", "不影响"),
        "stage5_core": "5.1–5.4",
        "legacy_a2_anchor": "-进入-a3-前的自我检查",
        "legacy_stage5_anchor": "-进入-stage-6-前的自我检查",
        "legacy_roadmap_anchors": (
            "近期想补的缺口",
            "进行中--随时可贡献",
            "-动手练习覆盖补齐",
            "-audience-branch-深化",
            "-stage-2--stage-3-2026-freshness-小修",
            "基础建设maintainer-进行中",
            "想法箱待讨论还没承诺",
        ),
        "foundation_route": "`Stage 0 → Stage 1 → Stage 2`",
        "track_a_route": "`A1 → A2 → Stage 5 → A3 → Stage 8`",
        "track_b_route": "`Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 7.5 → Stage 8`",
        "roadmap_stale": (
            "2026-05 snapshot",
            "Stage 2 / Stage 3 2026 freshness 小修",
            "GitHub Pages,评估中",
        ),
        "stage3_title": "Stage 3 — 工具使用与第一个 Agent Loop",
        "stage3_topic": "工具使用与第一个 Agent Loop",
        "stage4_title": "Stage 4 — Workflow Graph 与 Agent 框架",
        "stage4_topic": "Workflow Graph 与 Agent 框架",
        "stage7_title": "Stage 7 — Agent Production Engineering：Harness、Loop 与 Graph",
        "stage7_topic": "Agent Production Engineering：Harness、Loop 与 Graph",
        "stage7_compact": "Stage 7 — Agent Production Engineering",
    },
}


def locale_path(stem: str, suffix: str) -> Path:
    return ROOT / f"{stem}{suffix}.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def between(text: str, start: str, end: str) -> str:
    start_at = text.index(start)
    end_at = text.index(end, start_at + len(start))
    return text[start_at:end_at]


def assert_in_order(text: str, needles: tuple[str, ...]) -> None:
    positions = [text.index(needle) for needle in needles]
    assert positions == sorted(positions), dict(zip(needles, positions, strict=True))


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_readme_uses_one_track_a_order(locale: str, config: dict[str, object]) -> None:
    text = read(locale_path("README", str(config["suffix"])))
    track_a = between(text, str(config["track_a"]), str(config["track_b"]))
    assert_in_order(
        track_a,
        (
            "tracks/cli/A1-cli-intro",
            "tracks/cli/A2-cli-workflow",
            "stages/05-claude-code-ecosystem",
            "tracks/cli/A3-cli-production",
            "stages/08-agent-interfaces",
        ),
    )


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_readme_keeps_shared_foundation_and_track_b_order(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("README", str(config["suffix"])))
    assert_in_order(
        text,
        (
            "stages/00-foundations",
            "stages/01-llm-basics",
            "stages/02-prompt-engineering",
        ),
    )
    track_b = text[text.index(str(config["track_b"])) :]
    assert_in_order(
        track_b,
        (
            "stages/03-tool-use-and-hello-agent",
            "stages/04-agent-frameworks",
            "stages/05-claude-code-ecosystem",
            "stages/06-memory-rag",
            "stages/07-multi-agent-production",
            "stages/07.5-advanced-agentic-concepts",
            "stages/08-agent-interfaces",
        ),
    )


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_progress_matches_route_and_marks_stage8_recommended(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("PROGRESS", str(config["suffix"])))
    track_a = between(text, "## Track A", "## Track B")
    assert_in_order(
        track_a,
        (
            "tracks/cli/A1-cli-intro",
            "tracks/cli/A2-cli-workflow",
            "stages/05-claude-code-ecosystem",
            "tracks/cli/A3-cli-production",
            "stages/08-agent-interfaces",
        ),
    )
    stage8_line = next(line for line in track_a.splitlines() if "08-agent-interfaces" in line)
    for marker in config["optional"]:
        assert marker in stage8_line, (locale, marker, stage8_line)


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_a2_sends_reader_to_stage5_not_directly_to_a3(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("tracks/cli/A2-cli-workflow", str(config["suffix"])))
    header = "\n".join(text.splitlines()[:8])
    self_check = text[text.index("## ✅") :]
    target = "../../stages/05-claude-code-ecosystem"
    assert target in header
    assert target in self_check
    assert "A3-cli-production" not in header


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_stage5_routes_track_a_to_a3_and_track_b_to_stage6(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("stages/05-claude-code-ecosystem", str(config["suffix"])))
    entry = text[text.index("## 🚪") : text.index("<details", text.index("## 🚪"))]
    self_check = text[text.index("## ✅") :]
    assert "../tracks/cli/A2-cli-workflow" in entry
    assert "../tracks/cli/A3-cli-production" in entry
    assert "../tracks/cli/A3-cli-production" in self_check
    assert "06-memory-rag" in self_check


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_a3_requires_stage5_and_recommends_stage8_next(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("tracks/cli/A3-cli-production", str(config["suffix"])))
    before_exercises = text[: text.index("## 🛠")]
    self_check = text[text.index("## ✅") :]
    assert "../../stages/05-claude-code-ecosystem" in before_exercises
    assert "../../stages/08-agent-interfaces" in self_check


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_track_a_capstone_keeps_stage8_optional(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("CAPSTONE", str(config["suffix"])))
    track_a = between(text, "## Track A", "## Track B")
    assert "Stage 0" in track_a
    assert "A1" in track_a and "A2" in track_a and "A3" in track_a
    assert "Stage 5" in track_a and "Stage 8" in track_a
    assert str(config["stage5_core"]) in track_a
    for marker in config["optional"]:
        assert marker in track_a, (locale, marker)


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_roadmap_states_the_exact_canonical_routes(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("ROADMAP", str(config["suffix"])))
    assert str(config["foundation_route"]) in text
    assert str(config["track_a_route"]) in text
    assert str(config["track_b_route"]) in text


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_developer_branch_uses_the_canonical_track_a_route(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("branches/for-developer", str(config["suffix"])))
    route_line = next(
        line
        for line in text.splitlines()
        if "A1-cli-intro" in line and "05-claude-code-ecosystem" in line
    )
    assert "A1 → A2 →" in route_line
    assert "stages/05-claude-code-ecosystem" in route_line
    assert "→ A3" in route_line
    for marker in config["optional"]:
        assert marker in route_line, (locale, marker, route_line)


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_roadmap_drops_completed_or_stale_gap_claims(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("ROADMAP", str(config["suffix"])))
    for stale in config["roadmap_stale"]:
        assert stale not in text, (locale, stale)


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_renamed_route_headings_keep_legacy_deep_links(
    locale: str, config: dict[str, object]
) -> None:
    suffix = str(config["suffix"])
    a2 = read(locale_path("tracks/cli/A2-cli-workflow", suffix))
    stage5 = read(locale_path("stages/05-claude-code-ecosystem", suffix))
    roadmap = read(locale_path("ROADMAP", suffix))

    assert f'<a id="{config["legacy_a2_anchor"]}"></a>' in a2
    assert f'<a id="{config["legacy_stage5_anchor"]}"></a>' in stage5
    for anchor in config["legacy_roadmap_anchors"]:
        assert f'<a id="{anchor}"></a>' in roadmap


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_stage3_stage4_titles_match_across_reader_entry_points(
    locale: str, config: dict[str, object]
) -> None:
    suffix = str(config["suffix"])
    stage3_title = str(config["stage3_title"])
    stage3_topic = str(config["stage3_topic"])
    stage4_title = str(config["stage4_title"])
    stage4_topic = str(config["stage4_topic"])

    readme = read(locale_path("README", suffix))
    index = read(locale_path("index", suffix))
    progress = read(locale_path("PROGRESS", suffix))
    stage2 = read(locale_path("stages/02-prompt-engineering", suffix))
    examples_index = read(locale_path("examples/README", suffix))

    assert f"[{stage3_topic}]" in readme
    assert f"[{stage4_topic}]" in readme
    assert f"__{stage3_title}__" in index
    assert f"__{stage4_title}__" in index
    assert f"**{stage3_title}**" in progress
    assert f"**{stage4_title}**" in progress
    assert f"[{stage3_title}]" in stage2
    assert stage3_topic in examples_index
    assert stage4_topic in examples_index


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_all_stage3_companion_pages_use_the_current_localized_title(
    locale: str, config: dict[str, object]
) -> None:
    suffix = str(config["suffix"])
    stage3_title = str(config["stage3_title"])
    label = f"[{stage3_title}]"

    examples = sorted((ROOT / "examples/stage-3").glob(f"*/README{suffix}.md"))
    assert len(examples) == 6, (locale, examples)
    for page in examples:
        assert label in read(page), (locale, page)

    tutor = ROOT / f"examples/stage-5/tool-calling-tutor/README{suffix}.md"
    cheatsheet = locale_path("resources/schema-design-cheatsheet", suffix)
    assert label in read(tutor)
    assert read(cheatsheet).count(label) == 2


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_stage7_umbrella_title_matches_all_direct_reader_routes(
    locale: str, config: dict[str, object]
) -> None:
    suffix = str(config["suffix"])
    stage7_title = str(config["stage7_title"])
    stage7_topic = str(config["stage7_topic"])
    stage7_compact = str(config["stage7_compact"])

    stage7 = read(locale_path("stages/07-multi-agent-production", suffix))
    readme = read(locale_path("README", suffix))
    index = read(locale_path("index", suffix))
    progress = read(locale_path("PROGRESS", suffix))
    stage6 = read(locale_path("stages/06-memory-rag", suffix))
    examples_index = read(locale_path("examples/README", suffix))

    assert stage7.startswith(f"# {stage7_title}\n")
    assert f"[{stage7_topic}]" in readme
    assert f"__{stage7_compact}__" in index
    assert f"**{stage7_title}**" in progress
    assert f"[{stage7_title}]" in stage6
    assert stage7_compact.removeprefix("Stage 7 — ") in examples_index

    examples = sorted((ROOT / "examples/stage-7").glob(f"*/README{suffix}.md"))
    assert len(examples) == 5, (locale, examples)
    for page in examples:
        assert f"[{stage7_title}]" in read(page), (locale, page)

    if locale == "zh-TW":
        assert f"- {stage7_title}: stages/07-multi-agent-production.md" in (
            ROOT / "mkdocs.yml"
        ).read_text(encoding="utf-8")
        assert f"[{stage7_title}](stages/07-multi-agent-production.md)" in (
            ROOT / "scripts/build-mdbook.sh"
        ).read_text(encoding="utf-8")


def test_secondary_stage4_route_surfaces_put_the_graph_before_the_framework() -> None:
    expected_en = "Stage 4 (Workflow Graphs & Agent Frameworks)"
    for path in (
        ROOT / ".github/outreach/_send-day-packages.md",
        ROOT / ".github/outreach/langchain-ai.md",
    ):
        assert expected_en in read(path), path

    assert "Stage 4（Workflow Graph／Agent Framework）" in read(
        ROOT / "docs/HOW_TO_USE.md"
    )
    assert "Stage 4 — Workflow Graphs & Agent Frameworks" in read(
        ROOT / ".github/ISSUE_TEMPLATE/project-suggestion.md"
    )


@pytest.mark.parametrize("locale,config", LOCALES.items())
def test_readme_explains_learning_order_separately_from_control_scope(
    locale: str, config: dict[str, object]
) -> None:
    text = read(locale_path("README", str(config["suffix"])))
    route = next(line for line in text.splitlines() if line.startswith("> 🔭"))
    stages = tuple(f"Stage {number}" for number in range(2, 8))
    positions = [route.index(stage) for stage in stages]

    assert positions == sorted(positions)
    assert "**Agent Loop**" in route
    assert "**Workflow Graph**" in route
    assert "**Context Engineering**" in route
    assert "`prompt → context → harness → loop → graph`" in route


def test_legacy_stage_titles_are_absent_repo_wide() -> None:
    stale = (
        "Tool Use & Hello Agent",
        "Tool Use & Agent Intro",
        "Tool Use & Agent intro",
        "Tool Use and Agent Basics",
        "Tool Use & Agent 入門",
        "Tool Use & Agent 入门",
        "Tool Use 與 Agent 入門",
        "Tool Use 与 Agent 入门",
        "Stage 3 — 工具呼叫__",
        "Stage 3 — 工具调用__",
        "Stage 4 (Agent Frameworks)",
        "**4** Agent 框架 |",
        "Stage 7 — Loop／Graph Engineering：多 Agent 與穩定運作",
        "Stage 7 — Loop & Graph Engineering: Multi-Agent Production",
        "Stage 7 — Loop／Graph Engineering：多 Agent 与稳定运行",
        "Stage 7 — Multi-Agent · 進階應用",
        "Stage 7 — Multi-Agent · Advanced Applications",
        "Stage 7 — Multi-Agent · 进阶应用",
        "Stage 7 — Multi-Agent 與 Production",
        "Stage 7 — Multi-Agent & Production",
        "Stage 7 — Multi-Agent 与 Production",
    )
    excluded = {ROOT / "CHANGELOG.md"}
    excluded_root = ROOT / "docs/plans"
    generated_or_private = {ROOT / ".ai", ROOT / ".git", ROOT / "_build"}
    offenders: list[tuple[Path, str]] = []

    for page in ROOT.rglob("*.md"):
        if (
            page in excluded
            or excluded_root in page.parents
            or any(root in page.parents for root in generated_or_private)
        ):
            continue
        text = read(page)
        for phrase in stale:
            if phrase in text:
                offenders.append((page.relative_to(ROOT), phrase))

    assert not offenders, offenders
