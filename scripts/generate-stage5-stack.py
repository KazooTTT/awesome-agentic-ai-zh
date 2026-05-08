"""Generate the Stage 5 Claude Code Stack diagram using PIL.

Produces resources/diagrams/stage5-stack{,en}.png at 1920×1080.

Why PIL not SVG: cairosvg's font fallback fails on Windows for CJK +
emoji. PIL takes explicit TTF paths so we control exactly what renders.

Why no emoji icons: rendering color emojis (CBDT / COLR fonts) is
unreliable across PIL versions. Colored circle bullets in the layer
stroke color work better and look more professional anyway.

Run:
    python scripts/generate-stage5-stack.py [--lang zh-TW|en]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LAYERS = [
    # name, sub, ability_zh-TW, ability_en, ability_zh-CN, fill, stroke
    (
        "Plugins / Marketplaces",
        "5.4 — packaging",
        "把 Skills、hooks、commands、MCP 設定打包發佈",
        "Package & ship Skills, hooks, commands, MCP configs as one unit",
        "把 Skills、hooks、commands、MCP 设置打包发布",
        "#fef3c7", "#b45309",
    ),
    (
        "Skills",
        "5.3 — behavior",
        "Claude Code 的行為包，可封裝 MCP tool",
        "Behavior bundles for Claude Code that can wrap MCP tools",
        "Claude Code 的行为包，可封装 MCP tool",
        "#dbeafe", "#1e40af",
    ),
    (
        "MCP",
        "5.2 — protocol",
        "標準化協定，任何 LLM host 都能用任何 tool server",
        "Standardized protocol — any LLM host can use any tool server",
        "标准化协议，任何 LLM host 都能用任何 tool server",
        "#dcfce7", "#166534",
    ),
    (
        "Tool Use / Function Calling",
        "Stage 3",
        "讓 LLM 呼叫你定義的 function",
        "Let the LLM call functions you define",
        "让 LLM 调用你定义的 function",
        "#f3e8ff", "#6b21a8",
    ),
    (
        "Anthropic API + SDK",
        "Stage 1, Stage 7",
        "用程式存取 LLM",
        "Programmatic access to the LLM",
        "用程序访问 LLM",
        "#fee2e2", "#991b1b",
    ),
    (
        "LLM (Claude)",
        "foundation",
        "底層基礎模型",
        "Foundation model",
        "底层基础模型",
        "#e5e7eb", "#374151",
    ),
]

# Windows font paths
FONT_CJK_BOLD = r"C:\Windows\Fonts\msjhbd.ttc"   # Microsoft JhengHei Bold
FONT_CJK_REG = r"C:\Windows\Fonts\msjh.ttc"      # Microsoft JhengHei
FONT_LATIN_BOLD = r"C:\Windows\Fonts\seguisb.ttf"  # Segoe UI Semibold
FONT_LATIN_REG = r"C:\Windows\Fonts\segoeui.ttf"   # Segoe UI


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Pillow's rounded_rectangle wrapper for older versions."""
    if hasattr(draw, "rounded_rectangle"):
        draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)
    else:
        draw.rectangle(xy, fill=fill, outline=outline, width=width)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", default="zh-TW", choices=["zh-TW", "en", "zh-CN"])
    args = parser.parse_args()

    from PIL import Image, ImageDraw, ImageFont

    W, H = 1920, 1080
    lang = args.lang

    title = "Claude Code Ecosystem Stack"
    if lang == "en":
        subtitle = "Each layer adds one capability · 4 sub-sections of Stage 5"
        footer = ('Both tracks use this stack — Track A reads "how to use it", '
                  'Track B reads "how it works"')
    elif lang == "zh-CN":
        subtitle = "Each layer adds one capability · Stage 5 的 4 个子章节"
        footer = ("两条学习路径都会用到这个 stack — Track A（CLI Power User）"
                  "读“怎么用”，Track B（Agent Builder）读“怎么运作”")
    else:
        subtitle = "Each layer adds one capability · Stage 5 之 4 個子章節"
        footer = ("兩條學習路徑都會用到這個 stack — Track A（CLI Power User）"
                  "讀「怎麼用」，Track B（Agent Builder）讀「怎麼運作」")
    repo = "github.com/WenyuChiou/awesome-agentic-ai-zh"

    # Pick fonts based on language. zh-CN uses YaHei (msyh.ttc), zh-TW uses JhengHei (msjh.ttc)
    if lang == "en":
        f_title = ImageFont.truetype(FONT_LATIN_BOLD, 60)
        f_sub = ImageFont.truetype(FONT_LATIN_REG, 26)
        f_layer_name = ImageFont.truetype(FONT_LATIN_BOLD, 38)
        f_layer_sub = ImageFont.truetype(FONT_LATIN_REG, 22)
        f_ability = ImageFont.truetype(FONT_LATIN_REG, 22)
        f_footer = ImageFont.truetype(FONT_LATIN_REG, 22)
    else:
        cjk_bold = FONT_CJK_BOLD if lang == "zh-TW" else r"C:\Windows\Fonts\msyhbd.ttc"
        cjk_reg = FONT_CJK_REG if lang == "zh-TW" else r"C:\Windows\Fonts\msyh.ttc"
        f_title = ImageFont.truetype(FONT_LATIN_BOLD, 60)
        f_sub = ImageFont.truetype(cjk_reg, 26)
        f_layer_name = ImageFont.truetype(cjk_bold, 36)
        f_layer_sub = ImageFont.truetype(FONT_LATIN_REG, 22)
        f_ability = ImageFont.truetype(cjk_reg, 22)
        f_footer = ImageFont.truetype(cjk_reg, 22)
    f_repo = ImageFont.truetype(FONT_LATIN_REG, 20)

    img = Image.new("RGB", (W, H), color=(250, 250, 250))
    d = ImageDraw.Draw(img)

    # Title (top center)
    title_y = 80
    tw = d.textlength(title, font=f_title)
    d.text((W/2 - tw/2, title_y), title, fill=(17, 17, 17), font=f_title)

    # Subtitle
    sub_y = 165
    sw = d.textlength(subtitle, font=f_sub)
    d.text((W/2 - sw/2, sub_y), subtitle, fill=(107, 114, 128), font=f_sub)

    # Stack layout
    stack_top = 230
    stack_bottom = 920
    layer_total = stack_bottom - stack_top
    layer_h = layer_total / 6  # ~115

    stack_x = 80
    stack_w = 1080
    ability_x = 1200
    ability_w = 640

    for i, (name, sub, abil_zh_tw, abil_en, abil_zh_cn, fill, stroke) in enumerate(LAYERS):
        if lang == "en":
            abil = abil_en
        elif lang == "zh-CN":
            abil = abil_zh_cn
        else:
            abil = abil_zh_tw
        y = stack_top + i * layer_h
        # Slight pyramid widening for foundation feel
        widen = i * 14
        x = stack_x - widen / 2
        w = stack_w + widen

        rect_h = layer_h - 14
        # Layer rect
        rounded_rect(
            d,
            (x, y, x + w, y + rect_h),
            radius=14,
            fill=hex_to_rgb(fill),
            outline=hex_to_rgb(stroke),
            width=3,
        )

        # Colored disk bullet (left)
        bullet_r = 16
        bullet_x = x + 50
        bullet_y = y + rect_h / 2
        d.ellipse(
            (bullet_x - bullet_r, bullet_y - bullet_r,
             bullet_x + bullet_r, bullet_y + bullet_r),
            fill=hex_to_rgb(stroke),
        )

        # Layer name + sub
        text_x = bullet_x + 36
        # Name vertical: slightly above midline
        name_h = 38 if lang == "en" else 36
        d.text(
            (text_x, bullet_y - name_h + 4),
            name,
            fill=hex_to_rgb(stroke),
            font=f_layer_name,
        )
        # Sub label (italic visual via gray + smaller)
        d.text(
            (text_x, bullet_y + 6),
            sub,
            fill=(107, 114, 128),
            font=f_layer_sub,
        )

        # Ability column (right)
        ay = y + 8
        ah = rect_h - 16
        rounded_rect(
            d,
            (ability_x, ay, ability_x + ability_w, ay + ah),
            radius=10,
            fill=(255, 255, 255),
            outline=(229, 231, 235),
            width=2,
        )
        # Ability text (vertically centered, wraps if needed)
        # For now, single-line
        d.text(
            (ability_x + 24, ay + ah / 2 - 14),
            abil,
            fill=(55, 65, 81),
            font=f_ability,
        )

        # Dotted divider between layers (visual hint of single stack)
        if i < len(LAYERS) - 1:
            sep_y = y + layer_h - 7
            # Draw dotted line manually (PIL has no native dash)
            x0 = stack_x + 40
            x1 = stack_x + stack_w - 40
            cur = x0
            while cur < x1:
                d.line(
                    [(cur, sep_y), (min(cur + 6, x1), sep_y)],
                    fill=(209, 213, 219),
                    width=1,
                )
                cur += 12

    # Footer
    footer_y = 1010
    d.text((80, footer_y), footer, fill=(107, 114, 128), font=f_footer)
    rw = d.textlength(repo, font=f_repo)
    d.text((W - 80 - rw, footer_y + 2), repo, fill=(156, 163, 175), font=f_repo)

    suffix = {"en": ".en", "zh-CN": ".zh-CN", "zh-TW": ""}[lang]
    out = REPO_ROOT / "resources" / "diagrams" / f"stage5-stack{suffix}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, format="PNG", optimize=True)
    print(f"[PIL] {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
