#!/usr/bin/env python3
"""Generate the light-themed «Расход на ИИ на чел.» chart.

Content-slide aspect (1600x780 ≈ 2.05:1), light/transparent SVG used under the H1
on the slide «ИИ в 2026 — удобная и дорогая технология» in the Data Fest Siberia 7
deck. Light theme to match the deck (white canvas, Inter, hairline gridlines).

Model releases on the spend curve: OpenAI / Anthropic / Google / Qwen /
DeepSeek — key milestones only (labeled dots; no legend, no unlabeled dots).
Below the x-axis — a GPU lane with consumer + server (datacenter) releases,
since hardware has no position on the spend curve.

Labels sit centered above their dot (text-anchor "middle") by default — this
keeps leader lines short and vertical and avoids labels sweeping across the
rising spend line. A collision-avoidance pass then nudges each label to the
nearest clear spot (higher above the dot, then below, then to the side) until
it clears every other label and the fixed annotation boxes (era pills, phase
boxes, callouts).

Structure colours mirror the deck CSS tokens (hardcoded hex, since the SVG is an
<img> and cannot read document CSS vars):
  grid --hairline #e5e7eb · axis --muted #6b7280 · caption/source --muted-soft
  #898989 · text --ink #111 / --body #374151 · spend line --accent #3b82f6 →
  #2563eb · red accents (arrow / phase-3 / peak) --error #ef4444.

Run:  python3 setup/gen_ai_spend_chart.py
Out:  public/img/ai-spend-milestones.svg
"""

import os
from collections import defaultdict

# --------------------------------------------------------------------------- #
# Data                                                                        #
# --------------------------------------------------------------------------- #
# Month index 0 = Sep 2023 ... 36 = Sep 2026. Spend = Ramp Top-1% $/employee/month.
SPEND = [
    (0, 120),
    (1, 130),
    (2, 140),
    (3, 150),
    (4, 160),
    (5, 170),
    (6, 180),
    (7, 190),
    (8, 200),
    (9, 210),
    (10, 220),
    (11, 230),
    (12, 250),
    (13, 270),
    (14, 290),
    (15, 310),
    (16, 330),
    (17, 360),
    (18, 400),
    (19, 450),
    (20, 520),
    (21, 600),
    (22, 700),
    (23, 850),
    (24, 1000),
    (25, 1200),
    (26, 1500),
    (27, 1800),
    (28, 2470),
    (29, 3200),
    (30, 4200),
    (31, 5500),
    (32, 6500),
    (33, 7449),
    (34, 7400),
    (35, 8200),
    (36, 9000),
]
SPEND_BY_IDX = dict(SPEND)

# Model releases: (month_idx, name, vendor, label).
# label=None -> dot only, no text. Only the key milestones are labelled, so the
# points and labels do not crowd each other.
RELEASES = [
    (0, "o1-preview", "openai", None),
    (2, "GPT-4 Turbo", "openai", None),
    (2, "Qwen-72B", "qwen", None),
    (5, "Gemini 1.5 Pro", "google", None),
    (5, "Qwen1.5", "qwen", None),
    (6, "GPT-4", "openai", None),
    (6, "Claude 3 Opus", "anthropic", None),
    (8, "GPT-4o", "openai", "GPT-4o"),
    (8, "Gemini 1.5 Flash", "google", None),
    (9, "Claude 3.5 Sonnet", "anthropic", None),
    (9, "Qwen2", "qwen", None),
    (10, "GPT-4o mini", "openai", None),
    (12, "o1 / o1-mini", "openai", "o1"),
    (12, "Qwen2.5", "qwen", None),
    (13, "MCP", "anthropic", "MCP"),
    (14, "Gemini 2.0 Flash", "google", None),
    (14, "Qwen2.5-Coder", "qwen", None),
    (14, "QwQ-32B-Preview", "qwen", None),
    (15, "o3 / o4-mini", "openai", None),
    (16, "DeepSeek R1", "deepseek", "DeepSeek R1"),
    (16, "o3-mini", "openai", None),
    (16, "Gemini 2.0 Flash GA", "google", None),
    (17, "Claude 3.7 Sonnet + Claude Code", "anthropic", "Claude Code"),
    (17, "Gemini 2.0 Pro", "google", None),
    (18, "GPT-4.5", "openai", None),
    (18, "Gemini 2.5 Pro", "google", None),
    (18, "QwQ-32B", "qwen", None),
    (19, "GPT-4.1", "openai", None),
    (19, "Qwen3", "qwen", "Qwen3"),
    (20, "Claude Opus 4 / Sonnet 4", "anthropic", None),
    (21, "Gemini 2.5 Flash", "google", None),
    (22, "Qwen3-Coder", "qwen", "Qwen3-Coder"),
    (23, "Claude Opus 4.1", "anthropic", None),
    (23, "GPT-5", "openai", "GPT-5"),
    (24, "Claude Sonnet 4.5", "anthropic", None),
    (25, "Claude Haiku 4.5", "anthropic", None),
    (26, "GPT-5.1", "openai", None),
    (26, "Gemini 3 Pro", "google", "Gemini 3 Pro"),
    (26, "Claude Opus 4.5", "anthropic", None),
    (27, "GPT-5.2", "openai", None),
    (27, "Gemini 3 Flash", "google", None),
    (27, "Qwen3.5", "qwen", "Qwen3.5"),
    (28, "GPT-5.3 Instant", "openai", None),
    (28, "Claude Opus 4.6", "anthropic", None),
    (29, "GPT-5.3-Codex", "openai", "GPT-5.3-Codex"),
    (29, "Claude Sonnet 4.6", "anthropic", None),
    (29, "Gemini 3.1 Pro", "google", None),
    (29, "Qwen3.6", "qwen", None),
    (30, "GPT-5.4", "openai", None),
    (30, "Gemini 3.1 Flash-Lite", "google", None),
    (31, "Gemma 4", "google", None),
    (31, "Claude Opus 4.7", "anthropic", None),
    (31, "GPT-5.5", "openai", None),
    (32, "GPT-5.5 Instant", "openai", None),
    (32, "Gemini 3.5 Flash", "google", None),
    (32, "Claude Opus 4.8", "anthropic", None),
    (33, "Claude Fable 5", "anthropic", None),
    (33, "Claude Sonnet 5", "anthropic", None),
    (33, "Qwen3.8", "qwen", None),
    (34, "GPT-5.6 Sol", "openai", None),
    (34, "Gemini 3.6 Flash", "google", None),
    (34, "Claude Opus 5", "anthropic", None),
    (35, "Gemini 3.7 Flash", "google", None),
    (36, "Gemini 3.8 Flash", "google", None),
    (36, "GPT-6 Astra", "openai", None),
    (36, "Fable 5.1 / Mythos 5.1", "anthropic", None),
]

# Technology-era bands: (start_idx, end_idx, label, color).
# Four eras, one per calendar year (the accepted granularity for LLM capability
# eras — see the year-based timelines in aitimeline.in / toloka.ai / LLM-Data-Hub).
# Year boundaries: idx 4 = Jan 2024, idx 16 = Jan 2025, idx 28 = Jan 2026.
# This also fixes two timing errors in the old 8-era split: MCP shipped Nov 2024
# (not 2025) and Computer Use started Oct 2024 (not Dec 2025).
ERAS = [
    (0, 4, "Чат + RAG", "#3b82f6"),  # 2023: function calling, RAG, ReAct
    (4, 16, "ReAct + Рассуждения + MCP", "#8b5cf6"),  # 2024: o1/o3, MCP, Computer Use
    (16, 28, "Агентный кодинг", "#f59e0b"),  # 2025: DeepSeek R1, Claude Code, GPT-5
    (28, 36, "To the Moon", "#ec4899"),  # 2026: 1M+ context, multi-agent, Codex
]

# --------------------------------------------------------------------------- #
# Layout & scales (light theme, deck tokens)                                  #
# --------------------------------------------------------------------------- #
W, H = 1600, 780
FONT = "Inter, -apple-system, 'Segoe UI', sans-serif"
GRID = "#e5e7eb"  # --hairline
AXIS = "#6b7280"  # --muted
MUTED = "#898989"  # --muted-soft
BODY = "#374151"  # --body
INK = "#111111"  # --ink
ACCENT = "#3b82f6"  # --accent (spend line)
ACCENT2 = "#2563eb"  # darker blue (gradient end)
RED = "#ef4444"  # --error (arrow, phase 3, peak)
VENDOR = {
    "openai": "#2563eb",
    "anthropic": "#16a34a",
    "google": "#d97706",
    "qwen": "#7c3aed",
    "deepseek": "#0d9488",
}
GPU = "#475569"  # slate — consumer GPU markers (lane below the x-axis)

# phase tints (soft fills + borders)
P1_FILL, P1_BORDER = "#eff6ff", "#bfdbfe"  # blue
P2_FILL, P2_BORDER = "#fffbeb", "#fde68a"  # amber
P3_FILL, P3_BORDER = "#fef2f2", "#fecaca"  # red

PL, PR, PT, PB = 120, 1580, 92, 640  # plot rect
YMAX = 10000
IDX0, IDXN = 0, 36


def x(idx):
    return PL + (idx - IDX0) / (IDXN - IDX0) * (PR - PL)


def y(val):
    return PB - val / YMAX * (PB - PT)


MONTHS = [
    "янв",
    "фев",
    "мар",
    "апр",
    "мая",
    "июн",
    "июл",
    "авг",
    "сен",
    "окт",
    "ноя",
    "дек",
]


def month_label(idx):
    m0 = (8 + idx) % 12
    yr = 2023 + (8 + idx) // 12
    return f"{MONTHS[m0]} {yr}"


# --------------------------------------------------------------------------- #
# SVG helpers                                                                 #
# --------------------------------------------------------------------------- #
out = []


def s(line):
    out.append(line)


def esc(t):
    return (
        t.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def fmt(v):  # 2470 -> "2 470" (ru spacing)
    return f"{v:,}".replace(",", " ")


def text(
    xp,
    yp,
    t,
    size=15,
    fill=BODY,
    weight="400",
    anchor="start",
    ls=None,
    opacity=None,
    fam=FONT,
):
    a = f' letter-spacing="{ls}"' if ls else ""
    o = f' opacity="{opacity}"' if opacity else ""
    s(
        f'<text x="{xp:.1f}" y="{yp:.1f}" font-family="{fam}" font-size="{size}" '
        f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{a}{o}>{esc(t)}</text>'
    )


def line(x1, y1, x2, y2, stroke, w=1, dash=None, opacity=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{opacity}"' if opacity else ""
    s(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{w}"{d}{o}/>'
    )


def rect(xp, yp, w, h, fill, rx=8, stroke=None, sw=1, opacity=None):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity else ""
    s(
        f'<rect x="{xp:.1f}" y="{yp:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx}" fill="{fill}"{st}{o}/>'
    )


def est_w(t, size):  # rough text width for auto-sizing boxes
    return len(t) * size * 0.56


def place_box(
    anchor_x,
    anchor_y,
    lines_,
    size,
    fill,
    border,
    text_fill=INK,
    pad=13,
    line_gap=1.5,
    max_right=None,
    weight="700",
):
    """Draw a rounded box with stacked text lines. (anchor_x,anchor_y) = top-left.

    Returns (bx, by, bw, bh). If max_right is set, the box is clamped so its right
    edge never passes max_right (keeps the rightmost box inside the plot)."""
    longest = max(est_w(l, size) for l in lines_)
    bw = longest + 2 * pad
    bh = len(lines_) * size * line_gap + 2 * (pad - 4)
    bx = anchor_x
    if max_right is not None:
        bx = max(PL + 4, min(anchor_x, max_right - bw))
    rect(bx, anchor_y, bw, bh, fill, rx=10, stroke=border, sw=1.5)
    for i, l in enumerate(lines_):
        text(
            bx + pad,
            anchor_y + pad + 2 + i * size * line_gap,
            l,
            size=size,
            fill=text_fill,
            weight=weight,
        )
    return bx, anchor_y, bw, bh


def halo_label(xp, yp, t, size, fill, anchor="start", weight="600"):
    """Text with a soft white halo behind it so labels stay legible over the line."""
    tw = est_w(t, size)
    if anchor == "middle":
        hx = xp - tw / 2 - 5
        hw = tw + 10
    elif anchor == "end":
        hx = xp - tw - 5
        hw = tw + 10
    else:
        hx = xp - 5
        hw = tw + 10
    rect(hx, yp - size - 2, hw, size + 9, "#ffffff", rx=6, opacity=0.85)
    text(xp, yp, t, size=size, fill=fill, weight=weight, anchor=anchor)


# --------------------------------------------------------------------------- #
# Document head                                                               #
# --------------------------------------------------------------------------- #
s(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    'role="img" aria-label="Расход на ИИ на чел. (Ramp AI Index Top 1%), '
    'релизы моделей и технологические вехи, 2023–2026">'
)
s("<defs>")
s(
    '<marker id="arrow" markerWidth="14" markerHeight="14" refX="9" refY="4" '
    'orient="auto" markerUnits="userSpaceOnUse">'
)
s(f'<path d="M0,0 L10,4 L0,8 Z" fill="{RED}"/>')
s("</marker>")
# small per-vendor arrowheads for the label→dot leader lines
for v, col in VENDOR.items():
    s(
        f'<marker id="arr-{v}" markerWidth="10" markerHeight="8" refX="5" refY="3" '
        f'orient="auto" markerUnits="userSpaceOnUse">'
    )
    s(f'<path d="M0,0 L8,3 L0,6 Z" fill="{col}"/>')
    s("</marker>")
s('<linearGradient id="linegrad" x1="0" y1="1" x2="1" y2="0">')
s(f'<stop offset="0" stop-color="{ACCENT}"/>')
s(f'<stop offset="1" stop-color="{ACCENT2}"/>')
s("</linearGradient>")
s("</defs>")


# --------------------------------------------------------------------------- #
# Era bands (behind everything in the plot) — subtle pale tints on white      #
# --------------------------------------------------------------------------- #
for a, b, label, color in ERAS:
    xa, xb = x(a), x(b)
    s(
        f'<rect x="{xa:.1f}" y="{PT}" width="{xb - xa:.1f}" height="{PB - PT}" '
        f'fill="{color}" opacity="0.07"/>'
    )
    line(xb, PT, xb, PB, color, w=1, opacity=0.22)

# --------------------------------------------------------------------------- #
# Gridlines + axes                                                            #
# --------------------------------------------------------------------------- #
for gv in range(0, YMAX + 1, 1000):
    gy = y(gv)
    line(PL, gy, PR, gy, GRID, w=1, dash="3 5" if gv else None)
    lab = "$0" if gv == 0 else f"${fmt(gv)}"
    text(PL - 14, gy + 5, lab, size=15, fill=AXIS, anchor="end")

# vertical gridlines + x tick labels (every 6 months)
for i in range(0, 37, 6):
    gx = x(i)
    line(gx, PT, gx, PB, GRID, w=1, dash="3 5", opacity=0.8)
    # последний тик у правого края — якорь end, чтобы подпись не ушла за viewBox
    text(
        gx,
        PB + 28,
        month_label(i),
        size=15,
        fill=AXIS,
        anchor="end" if i == 36 else "middle",
    )

# axis titles
text(PL - 14, PT - 14, "$ / чел. / мес", size=15, fill=AXIS, anchor="end")
s(
    f'<text x="42" y="{(PT + PB) / 2}" font-family="{FONT}" font-size="15" fill="{AXIS}" '
    f'font-weight="600" text-anchor="middle" '
    f'transform="rotate(-90 42 {(PT + PB) / 2})">Расход на чел. ($/мес)</text>'
)

# --------------------------------------------------------------------------- #
# Era pills (top of plot) — white fill, colored border + text                 #
# --------------------------------------------------------------------------- #
blocked = []  # fixed annotation rects (pills, phase boxes, callouts) that
# release labels must not overlap


def register_box(b):
    bx, by, bw, bh = b
    blocked.append((bx, by, bx + bw, by + bh))


for a, b, label, color in ERAS:
    xc = (x(a) + x(b)) / 2
    pw = est_w(label, 15) + 22
    ph = 26
    px = xc - pw / 2
    py = PT + 8
    px = max(PL + 4, min(px, PR - pw - 4))
    rect(px, py, pw, ph, "#ffffff", rx=13, stroke=color, sw=1.4)
    text(xc, py + 17.5, label, size=15, fill=color, weight="600", anchor="middle")
    blocked.append((px, py, px + pw, py + ph))

# --------------------------------------------------------------------------- #
# Model-release dots — labeled milestones only (no legend, no unlabeled dots) #
# --------------------------------------------------------------------------- #
per_month = defaultdict(list)
for mi, name, vendor, lab in RELEASES:
    if lab:
        per_month[mi].append(name)

for mi, name, vendor, lab in RELEASES:
    if not lab:
        continue
    cx = x(mi)
    base_y = y(SPEND_BY_IDX[mi])
    same = per_month[mi]
    k = same.index(name)
    jitter = (k - (len(same) - 1) / 2) * 15
    cy = base_y + jitter
    col = VENDOR[vendor]
    s(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{col}" opacity="0.95"/>')


def dot_pos(mi, name, vendor):
    """Center of a release dot (accounts for same-month jitter across vendors)."""
    cx = x(mi)
    base_y = y(SPEND_BY_IDX[mi])
    same = per_month[mi]
    k = same.index(name)
    jitter = (k - (len(same) - 1) / 2) * 15
    return cx, base_y + jitter


# --------------------------------------------------------------------------- #
# Spend line (on top)                                                         #
# --------------------------------------------------------------------------- #
pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for (i, v) in SPEND)
s(
    f'<polyline points="{pts}" fill="none" stroke="url(#linegrad)" stroke-width="3.5" '
    f'stroke-linejoin="round" stroke-linecap="round"/>'
)
for i, v in SPEND:
    s(
        f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="2.6" fill="#ffffff" '
        f'stroke="{ACCENT2}" stroke-width="1.4"/>'
    )

# --------------------------------------------------------------------------- #
# Phase annotations (drawn before labels; their rects block label placement)  #
# --------------------------------------------------------------------------- #
# --- PHASE 1: ПЛАТО (bottom-left, above the flat curve) ---
register_box(
    place_box(
        PL + 30,
        455,
        ["ФАЗА 1: ПЛАТО", "2023 — начало 2025", "Чат + RAG"],
        size=16,
        fill=P1_FILL,
        border=P1_BORDER,
    )
)
# ~$160 flat callout below Phase 1, connector to the line at idx 5
c1 = place_box(
    PL + 30,
    585,
    ["≈$160 · плато 2024"],
    size=15,
    fill="#ffffff",
    border=ACCENT,
    text_fill=ACCENT2,
)
register_box(c1)
line(c1[0] + c1[2] - 6, c1[1] + 15, x(5), y(170), ACCENT, w=1.2, dash="3 3")

# --- Рост ×4 (center, above the inflection) ---
register_box(
    place_box(
        x(18.5),
        460,
        ["Рост ×4", "(фев 2025 → фев 2026)"],
        size=15,
        fill="#ffffff",
        border=RED,
        text_fill=RED,
    )
)

# --- PHASE 2: УСКОРЕНИЕ (center, above the rising curve) ---
register_box(
    place_box(
        x(20),
        340,
        [
            "ФАЗА 2: УСКОРЕНИЕ",
            "середина 2025 — начало 2026",
            "Агенты + MCP + Computer Use",
        ],
        size=16,
        fill=P2_FILL,
        border=P2_BORDER,
    )
)
# $2,470 callout near idx 28 (Jan 2026) — bottom, below the Gemini 3 Pro label,
# clear of the GPT-5 label
c2 = place_box(
    x(28) + 14,
    560,
    ["$2 470 · Ramp: ×4 г/г"],
    size=15,
    fill="#ffffff",
    border=ACCENT,
    text_fill=ACCENT2,
)
register_box(c2)
line(c2[0] + 20, c2[1], x(28), y(2470) + 4, ACCENT, w=1.2, dash="3 3")

# --- PHASE 3: ВЗРЫВ (upper-right, left of the peak callout) ---
register_box(
    place_box(
        x(24),
        150,
        [
            "ФАЗА 3: ВЗРЫВ",
            "середина 2026 →",
            "Frontier-агенты, 1M+ контекст,",
            "$7 400+/чел./мес",
        ],
        size=16,
        fill=P3_FILL,
        border=P3_BORDER,
        text_fill=RED,
        max_right=x(33) - 8,
    )
)
# ~$9,000 peak callout — below the era pills, left of the peak (x36, y9000)
c3 = place_box(
    x(33) + 2,
    155,
    ["≈$9 000 · пик GPT-6 Astra"],
    size=15,
    fill="#ffffff",
    border=RED,
    text_fill=RED,
    max_right=PR - 6,
)
register_box(c3)
line(c3[0] + c3[2] - 6, c3[1] + 15, x(36), y(9000) - 4, RED, w=1.2, dash="3 3")

# --- red acceleration arrow: short, in the empty space below the curve,       #
# --- sweeping up-right (not into the corner)                                  #
ax1, ay1 = x(34), 580
ax2, ay2 = x(36) - 18, y(9000) + 150
s(
    f'<path d="M {ax1:.1f} {ay1:.1f} Q {(ax1 + ax2) / 2 - 24:.1f} {(ay1 + ay2) / 2 - 8:.1f} '
    f'{ax2:.1f} {ay2:.1f}" fill="none" stroke="{RED}" stroke-width="3" '
    f'stroke-linecap="round" marker-end="url(#arrow)"/>'
)

# --------------------------------------------------------------------------- #
# Release labels — collision-avoiding placement (labeled milestones only)     #
# --------------------------------------------------------------------------- #
# Each label defaults to centered above its dot (anchor "middle", dy -16), then
# tries candidate offsets until it clears every other label and the fixed
# annotation boxes. Candidates are vertical-first (higher above the dot, then
# below), with side placement as a last resort. "GPT-6 Astra" is not labelled
# separately — the peak callout already names it.
LABEL_DY = {}  # per-label dy override (optional); default is -16 (above)
LABEL_ANCHOR = {}  # per-label anchor override (optional); default is "middle"
LABEL_SIZE = 16
LABEL_CANDIDATES = [
    (-16, "middle"),
    (-34, "middle"),
    (-52, "middle"),
    (-70, "middle"),
    (22, "middle"),
    (40, "middle"),
    (-16, "start"),
    (-16, "end"),
]


def _overlap(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def label_rect(cx, cy, lab, dy, anchor):
    """Bbox of a label at dot (cx, cy) + offset; returns (rect, lx, anchor).

    "middle" centers the label on the dot's x (lx = cx) and clamps it to the
    plot so it never runs off the left/right edge (lx shifts with the clamp so
    the text stays aligned with its bbox)."""
    tw = est_w(lab, LABEL_SIZE)
    if anchor == "middle":
        lx = cx
        r = (lx - tw / 2 - 4, cy + dy - LABEL_SIZE - 2, lx + tw / 2 + 4, cy + dy + 5)
        if r[0] < PL + 2:  # clamp left
            shift = PL + 2 - r[0]
            r = (r[0] + shift, r[1], r[2] + shift, r[3])
            lx += shift
        if r[2] > PR - 2:  # clamp right
            shift = r[2] - (PR - 2)
            r = (r[0] - shift, r[1], r[2] - shift, r[3])
            lx -= shift
        return r, lx, "middle"
    if anchor != "end" and cx + 10 + tw > PR - 4:  # would run off the right edge
        anchor = "end"
    if anchor == "end":
        lx = cx - 10
        r = (lx - tw, cy + dy - LABEL_SIZE - 2, lx + 4, cy + dy + 5)
    else:
        lx = cx + 10
        r = (lx - 4, cy + dy - LABEL_SIZE - 2, lx + tw, cy + dy + 5)
    return r, lx, anchor


def connector(cx, cy, r, col, vendor):
    """Thin leader line from the label box to its dot, with a small vendor-coloured
    arrowhead at the dot end, so it is clear which label belongs to which release.
    Skipped when the label sits adjacent to the dot (nothing to connect)."""
    r0, r1, r2, r3 = r
    px = min(max(cx, r0), r2)  # closest point on the label bbox to the dot
    py = min(max(cy, r1), r3)
    dx, dy = px - cx, py - cy
    dist = (dx * dx + dy * dy) ** 0.5
    if dist < 9:
        return
    ux, uy = dx / dist, dy / dist
    ex = cx + ux * min(10, dist - 1)  # stop just outside the dot (r=6)
    ey = cy + uy * min(10, dist - 1)
    s(
        f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" '
        f'stroke="{col}" stroke-width="1.6" marker-end="url(#arr-{vendor})"/>'
    )


placed = []
for mi, name, vendor, lab in RELEASES:
    if not lab:
        continue
    cx, cy = dot_pos(mi, name, vendor)
    col = VENDOR[vendor]
    cands = [(LABEL_DY.get(lab, -16), LABEL_ANCHOR.get(lab, "middle"))]
    cands += [c for c in LABEL_CANDIDATES if c not in cands]
    choice = None
    for dy, anchor in cands:
        r, lx, a = label_rect(cx, cy, lab, dy, anchor)
        if not any(_overlap(r, o) for o in placed + blocked):
            choice = (dy, a, lx)
            break
    if choice is None:  # fallback: preferred position anyway
        dy, anchor = cands[0]
        r, lx, a = label_rect(cx, cy, lab, dy, anchor)
    halo_label(lx, cy + dy, lab, size=LABEL_SIZE, fill=col, anchor=a)
    connector(cx, cy, r, col, vendor)
    placed.append(r)

# --------------------------------------------------------------------------- #
# Consumer GPU release lane (below the x-axis — hardware has no position      #
# on the spend curve, so it gets its own timeline row)                        #
# --------------------------------------------------------------------------- #
GPUS = [
    # (month_idx, label or None, label row). Dense cluster Dec 2024 – May 2025:
    # labels alternate above/below the lane to avoid horizontal collisions.
    # Server (datacenter) releases share the lane with consumer ones.
    (4, "RTX 40 SUPER", "below"),  # consumer, Jan 2024
    (5, "H200 · B200", "above"),  # server, GTC 2024
    (13, "MI325X · MI350", "below"),  # server, Advancing AI Oct 2024
    (15, "Arc B580", "above"),  # consumer, Dec 2024
    (16, "RTX 5090/5080", "below"),  # consumer, Jan 2025
    (17, None, None),  # RTX 5070 Ti
    (18, "RX 9070 · B300", "above"),  # consumer + server (GTC 2025), Mar 2025
    (19, None, None),  # RX 9060 XT, RTX 5060 Ti
    (20, "RTX 5060", "below"),  # consumer, May 2025
]
GLANE = 706
line(PL, GLANE, PR, GLANE, GRID, w=1)
text(PL - 14, GLANE + 4, "GPU", size=12, fill=AXIS, anchor="end")
# A100 (2020) and H100 (2022) predate the chart window — noted at the lane start
text(PL, GLANE + 16, "A100 (2020) · H100 (2022)", size=11, fill=MUTED)
for mi, lab, pos in GPUS:
    gx = x(mi)
    s(f'<rect x="{gx - 3:.1f}" y="{GLANE - 3}" width="6" height="6" fill="{GPU}"/>')
    if lab:
        ly_ = GLANE - 8 if pos == "above" else GLANE + 16
        text(gx + 10, ly_, lab, size=12, fill=AXIS)

# --------------------------------------------------------------------------- #
# Source (bottom)                                                             #
# --------------------------------------------------------------------------- #
text(
    PR,
    H - 18,
    "",
    size=14,
    fill=MUTED,
    anchor="end",
)

s("</svg>")

# --------------------------------------------------------------------------- #
# Write                                                                       #
# --------------------------------------------------------------------------- #
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
outdir = os.path.join(root, "public", "img")
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, "ai-spend-milestones.svg")
with open(path, "w") as f:
    f.write("\n".join(out) + "\n")
print(f"wrote {path} ({os.path.getsize(path):,} bytes)")
