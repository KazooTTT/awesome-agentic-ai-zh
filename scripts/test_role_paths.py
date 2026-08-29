"""Reader, fact, resource, and mirror contracts for role-path C2a."""

from __future__ import annotations

import re
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "researcher": {
        "zh-TW": ROOT / "branches/for-researcher.md",
        "en": ROOT / "branches/for-researcher.en.md",
        "zh-Hans": ROOT / "branches/for-researcher.zh-Hans.md",
    },
    "developer": {
        "zh-TW": ROOT / "branches/for-developer.md",
        "en": ROOT / "branches/for-developer.en.md",
        "zh-Hans": ROOT / "branches/for-developer.zh-Hans.md",
    },
}

CORE_TERMS = {
    "researcher": (
        "Source",
        "Claim",
        "Citation",
        "Source Verification",
        "Literature RAG",
        "Reproducibility",
        "Private Data",
        "Human Review",
    ),
    "developer": (
        "IDE",
        "Coding Agent",
        "Provider／Router",
        "Model／Runtime",
        "Sandbox",
        "Approval",
        "Diff／Rollback",
        "Eval／Observability",
    ),
}

RESOURCE_PAIRS = {
    "researcher": (
        ("https://notebooklm.google.com/", "⭐⭐⭐⭐⭐"),
        ("https://www.zotero.org/", "⭐⭐⭐⭐⭐"),
        ("https://github.com/Future-House/paper-qa", "⭐⭐⭐⭐⭐"),
        ("https://github.com/assafelovic/gpt-researcher", "⭐⭐⭐⭐"),
        ("https://github.com/stanford-oval/storm", "⭐⭐⭐⭐"),
        ("https://github.com/kaixindelele/ChatPaper", "⭐⭐⭐⭐⭐"),
        ("https://github.com/MuiseDestiny/zotero-gpt", "⭐⭐⭐⭐"),
        ("https://github.com/flonat/flonat-research", "⭐⭐⭐"),
        ("https://github.com/SakanaAI/AI-Scientist-v2", "⭐⭐⭐⭐"),
        ("https://github.com/langchain-ai/open_deep_research", "⭐⭐⭐⭐⭐"),
    ),
    "developer": (
        ("https://code.claude.com/docs/en/overview", "⭐⭐⭐⭐⭐"),
        ("https://github.com/anomalyco/opencode", "⭐⭐⭐⭐⭐"),
        ("https://github.com/earendil-works/pi", "⭐⭐⭐⭐"),
        ("https://github.com/Aider-AI/aider", "⭐⭐⭐⭐⭐"),
        ("https://github.com/aaif-goose/goose", "⭐⭐⭐⭐"),
        ("https://cursor.com/docs", "⭐⭐⭐⭐⭐"),
        ("https://github.com/cline/cline", "⭐⭐⭐⭐⭐"),
        ("https://github.com/continuedev/continue", "⭐⭐⭐⭐"),
        ("https://github.com/OpenHands/OpenHands", "⭐⭐⭐⭐"),
        ("https://github.com/obra/superpowers", "⭐⭐⭐⭐"),
        ("https://github.com/yamadashy/repomix", "⭐⭐⭐⭐⭐"),
        ("https://github.com/RooCodeInc/Roo-Code", "⭐⭐⭐"),
    ),
}

ROWGROUPS = {"researcher": (3, 4, 2, 1), "developer": (9, 2, 1)}

VISIBLE_STARTING_URLS = {
    "researcher": (
        "https://notebooklm.google.com/",
        "https://www.zotero.org/",
        "https://github.com/Future-House/paper-qa",
    ),
    "developer": (
        "https://code.claude.com/docs/en/overview",
        "https://github.com/anomalyco/opencode",
        "https://github.com/cline/cline",
    ),
}

RESOURCE_STATUS = {
    "https://notebooklm.google.com/": "available",
    "https://www.zotero.org/": "available",
    "https://github.com/Future-House/paper-qa": "active",
    "https://github.com/assafelovic/gpt-researcher": "active",
    "https://github.com/stanford-oval/storm": "usable",
    "https://github.com/kaixindelele/ChatPaper": "usable",
    "https://github.com/MuiseDestiny/zotero-gpt": "usable",
    "https://github.com/flonat/flonat-research": "active",
    "https://github.com/SakanaAI/AI-Scientist-v2": "research",
    "https://github.com/langchain-ai/open_deep_research": "archived",
    "https://code.claude.com/docs/en/overview": "commercial",
    "https://github.com/anomalyco/opencode": "active",
    "https://github.com/earendil-works/pi": "active",
    "https://github.com/Aider-AI/aider": "active",
    "https://github.com/aaif-goose/goose": "active",
    "https://cursor.com/docs": "commercial",
    "https://github.com/cline/cline": "active",
    "https://github.com/continuedev/continue": "read-only",
    "https://github.com/OpenHands/OpenHands": "active",
    "https://github.com/obra/superpowers": "active",
    "https://github.com/yamadashy/repomix": "active",
    "https://github.com/RooCodeInc/Roo-Code": "archived",
}

STATUS_TOKENS = {
    "available": {"zh-TW": "正式可用", "en": "Available", "zh-Hans": "正式可用"},
    "active": {"zh-TW": "活躍", "en": "Active", "zh-Hans": "活跃"},
    "usable": {"zh-TW": "可用", "en": "Usable", "zh-Hans": "可用"},
    "research": {"zh-TW": "研究參考", "en": "Research reference", "zh-Hans": "研究参考"},
    "archived": {"zh-TW": "已封存", "en": "archived", "zh-Hans": "已封存"},
    "commercial": {"zh-TW": "商業", "en": "Commercial", "zh-Hans": "商业"},
    "read-only": {"zh-TW": "read-only", "en": "Read-only", "zh-Hans": "read-only"},
}

RESOURCE_LICENSE_OR_SERVICE = {
    "https://notebooklm.google.com/": {"zh-TW": "雲端服務", "en": "cloud service", "zh-Hans": "云服务"},
    "https://www.zotero.org/": {"zh-TW": "桌面", "en": "desktop", "zh-Hans": "桌面"},
    "https://github.com/Future-House/paper-qa": "Apache-2.0",
    "https://github.com/assafelovic/gpt-researcher": "Apache-2.0",
    "https://github.com/stanford-oval/storm": "MIT",
    "https://github.com/kaixindelele/ChatPaper": {"zh-TW": "自訂條款", "en": "custom terms", "zh-Hans": "自定义条款"},
    "https://github.com/MuiseDestiny/zotero-gpt": "AGPL-3.0",
    "https://github.com/flonat/flonat-research": "MIT",
    "https://github.com/SakanaAI/AI-Scientist-v2": "source-code license",
    "https://github.com/langchain-ai/open_deep_research": "MIT",
    "https://code.claude.com/docs/en/overview": {"zh-TW": "商業", "en": "Commercial", "zh-Hans": "商业"},
    "https://github.com/anomalyco/opencode": "MIT",
    "https://github.com/earendil-works/pi": "MIT",
    "https://github.com/Aider-AI/aider": "Apache-2.0",
    "https://github.com/aaif-goose/goose": "Apache-2.0",
    "https://cursor.com/docs": {"zh-TW": "商業", "en": "Commercial", "zh-Hans": "商业"},
    "https://github.com/cline/cline": "Apache-2.0",
    "https://github.com/continuedev/continue": "Apache-2.0",
    "https://github.com/OpenHands/OpenHands": "MIT",
    "https://github.com/obra/superpowers": "MIT",
    "https://github.com/yamadashy/repomix": "MIT",
    "https://github.com/RooCodeInc/Roo-Code": "Apache-2.0",
}

RESOURCE_LIMIT_TOKENS = {
    "https://notebooklm.google.com/": {"zh-TW": "citation", "en": "citations", "zh-Hans": "引用"},
    "https://www.zotero.org/": {"zh-TW": "研究品質", "en": "research quality", "zh-Hans": "研究质量"},
    "https://github.com/Future-House/paper-qa": {"zh-TW": "評測", "en": "evaluate", "zh-Hans": "评测"},
    "https://github.com/assafelovic/gpt-researcher": {"zh-TW": "引用", "en": "citation", "zh-Hans": "引用"},
    "https://github.com/stanford-oval/storm": {"zh-TW": "依賴", "en": "dependencies", "zh-Hans": "依赖"},
    "https://github.com/kaixindelele/ChatPaper": {"zh-TW": "SPDX", "en": "SPDX", "zh-Hans": "SPDX"},
    "https://github.com/MuiseDestiny/zotero-gpt": {"zh-TW": "模型", "en": "model", "zh-Hans": "模型"},
    "https://github.com/flonat/flonat-research": {"zh-TW": "領域", "en": "field", "zh-Hans": "领域"},
    "https://github.com/SakanaAI/AI-Scientist-v2": {"zh-TW": "作者", "en": "authors", "zh-Hans": "作者"},
    "https://github.com/langchain-ai/open_deep_research": {"zh-TW": "仍在維護", "en": "default", "zh-Hans": "仍在维护"},
    "https://code.claude.com/docs/en/overview": {"zh-TW": "permission", "en": "permission", "zh-Hans": "permission"},
    "https://github.com/anomalyco/opencode": {"zh-TW": "AGENTS.md", "en": "AGENTS.md", "zh-Hans": "AGENTS.md"},
    "https://github.com/earendil-works/pi": {"zh-TW": "sandbox", "en": "sandbox", "zh-Hans": "sandbox"},
    "https://github.com/Aider-AI/aider": {"zh-TW": "hook", "en": "hooks", "zh-Hans": "hook"},
    "https://github.com/aaif-goose/goose": {"zh-TW": "權限", "en": "privilege", "zh-Hans": "权限"},
    "https://cursor.com/docs": {"zh-TW": "權限", "en": "permissions", "zh-Hans": "权限"},
    "https://github.com/cline/cline": {"zh-TW": "安全", "en": "safety", "zh-Hans": "安全"},
    "https://github.com/continuedev/continue": {"zh-TW": "2.0.0", "en": "2.0.0", "zh-Hans": "2.0.0"},
    "https://github.com/OpenHands/OpenHands": {"zh-TW": "人工", "en": "human", "zh-Hans": "人工"},
    "https://github.com/obra/superpowers": {"zh-TW": "gate", "en": "gate", "zh-Hans": "gate"},
    "https://github.com/yamadashy/repomix": {"zh-TW": "secret", "en": "secrets", "zh-Hans": "secrets"},
    "https://github.com/RooCodeInc/Roo-Code": {"zh-TW": "仍在維護", "en": "default", "zh-Hans": "仍在维护"},
}

DEVELOPER_ROW_FACTS = {
    "https://code.claude.com/docs/en/overview": (("coding agent",), ("CLI", "IDE", "desktop", "cloud")),
    "https://github.com/anomalyco/opencode": (("coding agent", "harness"), ("terminal", "desktop")),
    "https://github.com/earendil-works/pi": (("coding agent", "harness"), ("terminal", "SDK", "RPC")),
    "https://github.com/Aider-AI/aider": (("coding agent", "pair programmer"), ("CLI",)),
    "https://github.com/aaif-goose/goose": (("coding", "general agent"), ("CLI", "desktop", "API")),
    "https://cursor.com/docs": (("coding agent", "AI editor"), ("IDE", "CLI", "cloud", "SDK")),
    "https://github.com/cline/cline": (("coding agent",), ("IDE", "CLI", "SDK")),
    "https://github.com/continuedev/continue": (("coding agent",), ("CLI", "VS Code", "JetBrains")),
    "https://github.com/OpenHands/OpenHands": (("software-development agent platform",), ("web", "CLI", "SDK", "cloud")),
    "https://github.com/obra/superpowers": (("workflow collection",), ("agent plugin", "skills")),
    "https://github.com/yamadashy/repomix": (("repo context packer",), ("CLI", "MCP")),
    "https://github.com/RooCodeInc/Roo-Code": (("coding agent",), ("VS Code extension",)),
}
FRESHNESS = {
    "researcher": (
        "<!-- freshness: canonical=branches/for-researcher.md; "
        "verified_on=2026-08-29; "
        "scope=research-tools,citations,privacy,reproducibility,project-status; "
        "max_age_days=90 -->"
    ),
    "developer": (
        "<!-- freshness: canonical=branches/for-developer.md; "
        "verified_on=2026-08-29; "
        "scope=coding-agents,tool-identity,permissions,sandboxing,project-status; "
        "max_age_days=90 -->"
    ),
}

LEGACY_ANCHORS = {
    "researcher": {
        "zh-TW": (
            "使用情境研究階段-ai-怎麼幫",
            "精選-projects",
            "研究流程-marketplace",
            "文獻-rag--qa",
            "大綱與寫作",
            "文獻管理整合",
            "multi-llm-研究組合本-repo-維護者的研究-setup",
            "multi-agent-for-research",
            "必修閱讀",
            "必練流程按使用頻率",
            "層級建議",
        ),
        "en": (
            "use-cases",
            "curated-projects",
            "research-workflow-marketplaces",
            "literature-rag--qa",
            "outline--writing",
            "citation-manager-integrations",
            "multi-llm-research-stack-maintainer-setup",
            "multi-agent-for-research",
            "required-reading",
            "workflows-to-master",
            "tier-recommendations",
        ),
        "zh-Hans": (
            "使用场景研究阶段-ai-怎么帮",
            "精选-projects",
            "研究流程-marketplace",
            "文献-rag--qa",
            "大纲与写作",
            "文献管理集成",
            "multi-llm-研究组合本-repo-维护者的研究-setup",
            "multi-agent-for-research",
            "必修阅读",
            "必练流程按使用频率",
            "层级建议",
        ),
    },
    "developer": {
        "zh-TW": (
            "使用情境開發場景-ai-怎麼幫",
            "精選-projects",
            "coding-agents",
            "code-review",
            "推薦工具",
            "必練流程按使用頻率",
            "3-個具體-workflow-recipe",
            "常見踩坑anti-patterns",
            "tier-升級路徑",
            "也適用其他分支",
            "社群備註",
        ),
        "en": (
            "use-cases-developer-scenarios--how-ai-helps",
            "curated-projects",
            "coding-agents",
            "code-review",
            "recommended-tools",
            "workflows-to-master-by-frequency",
            "3-concrete-workflow-recipes",
            "common-pitfalls-anti-patterns",
            "tier-progression",
            "other-branches-also-apply",
            "community-note",
        ),
        "zh-Hans": (
            "使用场景开发场景-ai-怎么帮",
            "精选-projects",
            "coding-agents",
            "code-review",
            "推荐工具",
            "必练流程按使用频率",
            "3-个具体-workflow-recipe",
            "常见踩坑anti-patterns",
            "tier-升级路径",
            "也适用其他分支",
            "社群备注",
        ),
    },
}


def _without_details(text: str) -> str:
    return re.sub(r"<details\b[^>]*>.*?</details>", "", text, flags=re.DOTALL)


def _resource_table(text: str, first_url: str) -> str:
    tables = re.findall(r"<table>.*?</table>", text, flags=re.DOTALL)
    matches = [table for table in tables if first_url in table]
    assert len(matches) == 1
    return matches[0]


def _resource_rows(table: str) -> list[str]:
    rows: list[str] = []
    for group in re.findall(r"<tbody>(.*?)</tbody>", table, flags=re.DOTALL):
        rows.extend(re.findall(r"<tr>(.*?)</tr>", group, flags=re.DOTALL))
    return rows


def _row_for_url(text: str, url: str) -> str:
    rows = [row for row in re.findall(r"<tr>(.*?)</tr>", text, flags=re.DOTALL) if url in row]
    assert len(rows) == 1, (url, len(rows))
    return rows[0]


def _localized_token(value: str | dict[str, str], locale: str) -> str:
    return value[locale] if isinstance(value, dict) else value


@pytest.mark.parametrize("role", PAGES)
@pytest.mark.parametrize("locale", ("zh-TW", "en", "zh-Hans"))
def test_visible_path_is_progressive_and_keeps_core_terms(role: str, locale: str) -> None:
    text = PAGES[role][locale].read_text(encoding="utf-8")
    visible = _without_details(text)
    landmarks = ("## 📌", "## 🎯", "## 🧩", "## 🛠", "## 📚", "## ✅")
    positions = [visible.index(icon) for icon in landmarks]
    assert positions == sorted(positions)
    for term in CORE_TERMS[role]:
        assert f"**{term}" in visible
        assert visible.index(f"**{term}") < visible.index("## 🛠")
    for url in VISIBLE_STARTING_URLS[role]:
        assert url in visible
    assert visible.count("⭐⭐⭐⭐⭐") == len(VISIBLE_STARTING_URLS[role])

    openings = re.findall(r"^<details\b[^>]*>", text, flags=re.MULTILINE)
    assert len(openings) >= 5
    assert openings == ['<details markdown="1">'] * len(openings)


@pytest.mark.parametrize("locale", ("zh-TW", "en", "zh-Hans"))
def test_research_copy_block_teaches_source_verification(locale: str) -> None:
    visible = _without_details(PAGES["researcher"][locale].read_text(encoding="utf-8"))
    assert "https://arxiv.org/abs/1706.03762" in visible
    assert len(re.findall(r"^[123]\. ", visible, flags=re.MULTILINE)) >= 3
    for token in ("citation", "original", "unsupported"):
        assert token.casefold() in visible.casefold()


@pytest.mark.parametrize("locale", ("zh-TW", "en", "zh-Hans"))
def test_developer_copy_block_is_small_reviewable_and_human_gated(locale: str) -> None:
    visible = _without_details(PAGES["developer"][locale].read_text(encoding="utf-8"))
    for token in (
        "read-only plan",
        "README.md",
        "git diff -- README.md",
        "test",
        "rollback",
        "push",
        "merge",
        "deploy",
    ):
        assert token.casefold() in visible.casefold()
    assert re.search(r"human|人工", visible, flags=re.IGNORECASE)


@pytest.mark.parametrize("role", PAGES)
def test_resource_tables_have_structured_trilingual_parity(role: str) -> None:
    expected_pairs = RESOURCE_PAIRS[role]
    expected_groups = ROWGROUPS[role]
    observed_tables: list[tuple[tuple[str, str], ...]] = []

    for page in PAGES[role].values():
        text = page.read_text(encoding="utf-8")
        table = _resource_table(text, expected_pairs[0][0])
        groups = re.findall(r"<tbody>(.*?)</tbody>", table, flags=re.DOTALL)
        assert len(groups) == len(expected_groups)
        for group, size in zip(groups, expected_groups):
            assert len(re.findall(r"<tr>", group)) == size
            assert f'scope="rowgroup" rowspan="{size}"' in group

        pairs = []
        for row in _resource_rows(table):
            url = re.search(r'<a href="(https?://[^"]+)">', row)
            rating = re.search(r"⭐{3,5}", row)
            assert url and rating
            pairs.append((url.group(1), rating.group()))
        assert tuple(pairs) == expected_pairs
        observed_tables.append(tuple(pairs))

    assert len(set(observed_tables)) == 1


@pytest.mark.parametrize("role", PAGES)
@pytest.mark.parametrize("locale", ("zh-TW", "en", "zh-Hans"))
def test_each_resource_row_keeps_status_license_and_limitation(role: str, locale: str) -> None:
    text = PAGES[role][locale].read_text(encoding="utf-8")
    for url, _rating in RESOURCE_PAIRS[role]:
        row = _row_for_url(text, url)
        expected_status = STATUS_TOKENS[RESOURCE_STATUS[url]][locale]
        expected_license = _localized_token(RESOURCE_LICENSE_OR_SERVICE[url], locale)
        expected_limit = RESOURCE_LIMIT_TOKENS[url][locale]
        for token in (expected_status, expected_license, expected_limit):
            assert token.casefold() in row.casefold(), (url, locale, token)

        if role == "developer":
            identities, surfaces = DEVELOPER_ROW_FACTS[url]
            for token in identities + surfaces:
                assert token.casefold() in row.casefold(), (url, locale, token)


def test_row_lookup_does_not_borrow_facts_from_an_earlier_row() -> None:
    text = """
<table><tbody>
<tr><td>coding agent</td><td>CLI／cloud／SDK</td><td>permission gate</td></tr>
<tr><td><a href="https://example.com/target">Target</a></td><td>IDE only</td></tr>
</tbody></table>
"""
    row = _row_for_url(text, "https://example.com/target")
    for leaked_token in ("coding agent", "CLI", "cloud", "SDK", "permission gate"):
        assert leaked_token.casefold() not in row.casefold()


@pytest.mark.parametrize("role", PAGES)
def test_freshness_urls_and_legacy_landings_are_mirrored(role: str) -> None:
    expected_urls: list[str] | None = None
    for locale, page in PAGES[role].items():
        text = page.read_text(encoding="utf-8")
        assert text.count(FRESHNESS[role]) == 1
        landing_markers = {
            "researcher": (
                "## 📌", "<summary>⭐", "<summary>🧪", "## 🛠", "<summary>⭐",
                "<summary>⭐", "<summary>🧪", "<summary>🧪", "<summary>📖",
                "<summary>🧪", "## 📚",
            ),
            "developer": (
                "## 📌", "<summary>⭐", "## 🧩", "## 🛠", "## 📚",
                "<summary>🧪", "<summary>🧪", "<summary>🧯", "## 📚",
                "## ✅", "<summary>⭐",
            ),
        }[role]
        anchor_positions = []
        for anchor, marker in zip(LEGACY_ANCHORS[role][locale], landing_markers, strict=True):
            anchor_text = f'<a id="{anchor}"></a>'
            assert text.count(anchor_text) == 1
            anchor_at = text.index(anchor_text)
            marker_at = text.index(marker, anchor_at)
            assert 0 < marker_at - anchor_at < 240, (anchor, marker, marker_at - anchor_at)
            anchor_positions.append(anchor_at)
        assert min(anchor_positions) > text.index("<!-- freshness:")
        assert len(set(anchor_positions)) >= 8

        expected_return = {
            "zh-TW": "[← 回主路線](../README.md)",
            "en": "[← Back to the main route](../README.en.md)",
            "zh-Hans": "[← 回到主路线](../README.zh-Hans.md)",
        }[locale]
        visible = _without_details(text)
        assert expected_return in visible
        assert visible.index(expected_return) < visible.index("## 📌")
        urls = re.findall(r"https?://[^)\s<>\"]+", text)
        if expected_urls is None:
            expected_urls = urls
        else:
            assert urls == expected_urls


def test_current_research_name_privacy_status_and_curation_rules() -> None:
    for page in PAGES["researcher"].values():
        text = page.read_text(encoding="utf-8")
        assert "Gemini Notebook" in text and "NotebookLM" in text
        assert "https://support.google.com/gemininotebook/answer/17004255" in text
        assert re.search(
            r"open_deep_research.{0,300}(archived|封存|历史|歷史)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        assert "WenyuChiou/" not in text
        assert "1M context" not in text and "1M token" not in text
        assert not re.search(r"★\s*[\d,.]+[kKmM]?\+?", text)


def test_public_access_is_not_treated_as_upload_permission() -> None:
    required = {
        "zh-TW": ("授權或著作權", "工具條款", "公開可讀，不等於"),
        "en": ("license or copyright", "tool's terms", "not permission to upload"),
        "zh-Hans": ("许可或版权", "工具条款", "公开可读，不代表"),
    }
    forbidden = {
        "zh-TW": "公開 paper 可以直接使用",
        "en": "A public paper is fine to use",
        "zh-Hans": "公开 paper 可以直接使用",
    }
    import_action = {
        "zh-TW": "把 paper 加進",
        "en": "Add the paper",
        "zh-Hans": "把 paper 加到",
    }
    for locale, page in PAGES["researcher"].items():
        text = page.read_text(encoding="utf-8")
        visible = _without_details(text)
        assert all(token in visible for token in required[locale])
        assert visible.index(required[locale][0]) < visible.index(import_action[locale])
        assert forbidden[locale] not in text


def test_developer_identity_and_surface_are_separate_axes() -> None:
    for page in PAGES["developer"].values():
        text = page.read_text(encoding="utf-8")
        assert "OpenRouter" in text and "Ollama" in text
        assert re.search(r"OpenRouter.{0,250}(Router|router)", text, re.DOTALL)
        assert re.search(r"Ollama.{0,250}(runtime|執行環境|运行环境)", text, re.DOTALL)
        assert "核心身分" in text or "Core identity" in text or "核心身份" in text
        assert "surface" in text
        for url, surfaces in (
            ("https://cursor.com/docs", ("IDE", "CLI", "cloud", "SDK")),
            ("https://github.com/cline/cline", ("IDE", "CLI", "SDK")),
            ("https://github.com/continuedev/continue", ("CLI", "VS Code", "JetBrains")),
        ):
            row = _row_for_url(text, url)
            assert "coding agent" in row.casefold()
            for surface in surfaces:
                assert surface.casefold() in row.casefold()
        assert re.search(
            r"Roo Code.{0,300}(archived|封存|历史|歷史)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        assert re.search(
            r"continuedev/continue.{0,500}(read-only|不再積極維護|不再积极维护)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        assert not re.search(r"★\s*[\d,.]+[kKmM]?\+?", text)


@pytest.mark.parametrize("page", tuple(path for role in PAGES.values() for path in role.values()))
def test_role_pages_drop_known_stale_or_unsafe_claims(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    forbidden = (
        "採用度最高",
        "highest adoption",
        "采用度最高",
        "< 50 LOC",
        "read:user",
        "classic PAT",
        "首選",
        "首选",
        '""',
        "“”",
    )
    assert not any(token in text for token in forbidden)
