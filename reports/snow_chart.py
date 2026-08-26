"""
SNOW price/fundamentals chart — generated for equity analysis report
Data sources: Value Line (April 3, 2026), Morningstar (April 15, 2026)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np

# ── Annual price data (calendar year high / low) ──────────────────────────────
# Source: Morningstar historical table + VL
years_hist   = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
price_high   = [429.0, 405.0, 344.0, 202.8, 237.7, 280.7, 236.3]
price_low    = [208.5, 184.7, 110.3, 119.3, 107.1, 120.1, 118.3]   # 2026 YTD

current_price = 144.48   # Morningstar last close April 15, 2026
vl_price      = 174.20   # Value Line price April 3, 2026

# ── VL 18-month target range (midpoint April 2026 → ~Oct 2027) ────────────────
target_year_center = 2027.75   # ~18 months from April 2026
target_low         = 105
target_mid         = 197
target_high        = 288

# ── VL 2029-31 projection range ───────────────────────────────────────────────
proj_year_center = 2030.0
proj_low         = 240
proj_high        = 400
proj_mid         = (proj_low + proj_high) / 2   # 320

# ── Revenue data ($M) — fiscal year ending Jan 31 ─────────────────────────────
rev_years    = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
rev_values   = [592,  1219, 2066, 2807, 3626, 4684, 5350, 5850]
rev_actual   = [True, True, True, True, True, True, False, False]

# ── Non-GAAP EPS — fiscal year ending Jan 31 ──────────────────────────────────
eps_years    = [2025, 2026, 2027, 2030]
eps_values   = [1.26, 1.40, 1.60, 2.50]
eps_actual   = [True, False, False, False]

# ─────────────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 9), facecolor="#1a1a2e")
fig.suptitle(
    "Snowflake Inc. (SNOW) — Price History & Estimates",
    fontsize=15, fontweight="bold", color="white", y=0.98
)

gs = fig.add_gridspec(3, 1, hspace=0.08, height_ratios=[3.2, 1.2, 1.0],
                      left=0.07, right=0.93, top=0.94, bottom=0.07)

ax_price = fig.add_subplot(gs[0])
ax_rev   = fig.add_subplot(gs[1], sharex=ax_price)
ax_eps   = fig.add_subplot(gs[2], sharex=ax_price)

for ax in [ax_price, ax_rev, ax_eps]:
    ax.set_facecolor("#0f0f23")
    ax.tick_params(colors="white", labelsize=8)
    ax.spines["bottom"].set_color("#444")
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_color("#444")
    ax.spines["right"].set_visible(False)
    ax.yaxis.label.set_color("white")
    ax.grid(axis="y", color="#333", linewidth=0.5, linestyle="--")

# ── PRICE PANEL ───────────────────────────────────────────────────────────────
BAR_W = 0.35

for i, yr in enumerate(years_hist):
    color = "#5bc0eb" if yr < 2026 else "#aaa"   # 2026 YTD greyed
    ax_price.bar(yr, price_high[i] - price_low[i],
                 bottom=price_low[i], width=BAR_W,
                 color=color, alpha=0.85, zorder=3)
    # tick marks at high/low
    ax_price.hlines(price_high[i], yr - BAR_W/2, yr + BAR_W/2,
                    colors=color, linewidths=1.5, zorder=4)
    ax_price.hlines(price_low[i], yr - BAR_W/2, yr + BAR_W/2,
                    colors=color, linewidths=1.5, zorder=4)

# Current price marker
ax_price.scatter([2026.15], [current_price], color="#ff6b6b",
                 s=80, zorder=6, label=f"Current price ${current_price:.2f} (Apr 15)")
ax_price.hlines(current_price, 2025.8, 2026.5,
                colors="#ff6b6b", linewidths=1.2, linestyles="--", zorder=5)

# VL price annotation
ax_price.scatter([2026.0], [vl_price], color="#ffd166",
                 s=60, zorder=6, marker="D",
                 label=f"VL price ${vl_price:.2f} (Apr 3)")

# 18-month target zone (~Oct 2027)
ax_price.bar(target_year_center, target_high - target_low,
             bottom=target_low, width=0.45,
             color="#4ecdc4", alpha=0.35, zorder=2)
ax_price.hlines(target_mid, target_year_center - 0.225, target_year_center + 0.225,
                colors="#4ecdc4", linewidths=2.0, zorder=4)
ax_price.hlines(target_high, target_year_center - 0.225, target_year_center + 0.225,
                colors="#4ecdc4", linewidths=1.5, zorder=4)
ax_price.hlines(target_low, target_year_center - 0.225, target_year_center + 0.225,
                colors="#4ecdc4", linewidths=1.5, zorder=4)
ax_price.text(target_year_center + 0.3, target_mid,
              f"VL 18-mo target\n$105–$288\nmid ${target_mid}",
              color="#4ecdc4", fontsize=7, va="center")

# 2029-31 projection zone
ax_price.bar(proj_year_center, proj_high - proj_low,
             bottom=proj_low, width=1.2,
             color="#a29bfe", alpha=0.30, zorder=2)
ax_price.hlines(proj_mid, proj_year_center - 0.6, proj_year_center + 0.6,
                colors="#a29bfe", linewidths=2.0, linestyles="-", zorder=4)
ax_price.hlines(proj_high, proj_year_center - 0.6, proj_year_center + 0.6,
                colors="#a29bfe", linewidths=1.5, zorder=4)
ax_price.hlines(proj_low, proj_year_center - 0.6, proj_year_center + 0.6,
                colors="#a29bfe", linewidths=1.5, zorder=4)
ax_price.text(proj_year_center + 0.8, proj_mid,
              f"VL 2029-31 proj.\n$240–$400\nmid ${proj_mid:.0f}",
              color="#a29bfe", fontsize=7, va="center")

# Morningstar fair value line
ax_price.axhline(223, color="#fdcb6e", linewidth=1.0,
                 linestyle=":", zorder=3, alpha=0.8,
                 label="Morningstar fair value $223")

ax_price.set_yscale("log")
ax_price.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda y, _: f"${y:.0f}" if y >= 10 else f"${y:.1f}"
))
ax_price.set_ylim(60, 600)
ax_price.set_ylabel("Price (log scale)", color="white", fontsize=9)
ax_price.tick_params(axis="x", labelbottom=False)

# Annotations: key events
ax_price.annotate("IPO Sep 2020\n$120/sh",
                  xy=(2020, 208), xytext=(2019.0, 135),
                  color="#aaa", fontsize=6.5,
                  arrowprops=dict(arrowstyle="->", color="#aaa", lw=0.7))
ax_price.annotate("ATH $429\nNov 2021",
                  xy=(2020, 429), xytext=(2019.0, 480),
                  color="#5bc0eb", fontsize=6.5,
                  arrowprops=dict(arrowstyle="->", color="#5bc0eb", lw=0.7))
ax_price.annotate("−66% from ATH",
                  xy=(2026.15, current_price), xytext=(2024.5, 80),
                  color="#ff6b6b", fontsize=6.5,
                  arrowprops=dict(arrowstyle="->", color="#ff6b6b", lw=0.7))

legend = ax_price.legend(fontsize=7, loc="upper right",
                         facecolor="#1a1a2e", edgecolor="#444",
                         labelcolor="white", framealpha=0.9)

# divider between actual and estimates
ax_price.axvline(2025.5, color="#666", linewidth=0.8, linestyle="--", zorder=1)
ax_price.text(2025.52, 90, "◄ Actual  |  Estimates ►",
              color="#888", fontsize=6.5, va="bottom")

# ── REVENUE PANEL ─────────────────────────────────────────────────────────────
bar_colors_rev = ["#5bc0eb" if a else "#a29bfe" for a in rev_actual]
bars = ax_rev.bar(rev_years, rev_values, width=0.55,
                  color=bar_colors_rev, alpha=0.85, zorder=3)

for bar, val, actual in zip(bars, rev_values, rev_actual):
    ax_rev.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 60,
                f"${val/1000:.1f}B", ha="center", va="bottom",
                color="white", fontsize=6.5, fontweight="bold" if actual else "normal")

ax_rev.axvline(2025.5, color="#666", linewidth=0.8, linestyle="--", zorder=1)
ax_rev.set_ylabel("Revenue ($M)", color="white", fontsize=8)
ax_rev.set_ylim(0, 7500)
ax_rev.tick_params(axis="x", labelbottom=False)
ax_rev.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda y, _: f"${y/1000:.0f}B"))

# YoY growth labels
for i in range(1, len(rev_values)):
    if rev_actual[i-1]:   # only for transitions with known prior
        g = (rev_values[i] / rev_values[i-1] - 1) * 100
        color = "#a29bfe" if not rev_actual[i] else "#5bc0eb"
        ax_rev.text(rev_years[i], rev_values[i]/2,
                    f"+{g:.0f}%", ha="center", va="center",
                    color="white", fontsize=6, alpha=0.9)

actual_patch = mpatches.Patch(color="#5bc0eb", alpha=0.85, label="Actual")
est_patch    = mpatches.Patch(color="#a29bfe", alpha=0.85, label="VL Estimate")
ax_rev.legend(handles=[actual_patch, est_patch], fontsize=7,
              loc="upper left", facecolor="#1a1a2e", edgecolor="#444",
              labelcolor="white", framealpha=0.9)

# ── NON-GAAP EPS PANEL ────────────────────────────────────────────────────────
eps_colors = ["#5bc0eb" if a else "#a29bfe" for a in eps_actual]
ax_eps.bar(eps_years, eps_values, width=0.45,
           color=eps_colors, alpha=0.85, zorder=3)

for yr, val, actual in zip(eps_years, eps_values, eps_actual):
    ax_eps.text(yr, val + 0.05, f"${val:.2f}",
                ha="center", va="bottom",
                color="white", fontsize=7,
                fontweight="bold" if actual else "normal")

ax_eps.axvline(2025.5, color="#666", linewidth=0.8, linestyle="--", zorder=1)
ax_eps.set_ylabel("Non-GAAP EPS", color="white", fontsize=8)
ax_eps.set_ylim(0, 3.2)
ax_eps.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"${y:.2f}"))
ax_eps.set_xlabel("Year", color="white", fontsize=9)

# ── X-AXIS ticks ──────────────────────────────────────────────────────────────
all_years = list(range(2019, 2032))
ax_eps.set_xlim(2018.5, 2031.5)
ax_eps.set_xticks([y for y in all_years])
ax_eps.set_xticklabels(
    [str(y) if y <= 2027 else ("2029-31" if y == 2030 else "") for y in all_years],
    color="white", fontsize=8
)

# Caption
fig.text(0.07, 0.01,
         "Sources: Value Line (Apr 3, 2026) · Morningstar (Apr 15, 2026) · SEC EDGAR\n"
         "All EPS figures non-GAAP (VL methodology). GAAP EPS remains negative. "
         "Prices in USD. Log scale on price panel.",
         color="#888", fontsize=6.5)

out_path = "/Users/jimcuene/codingprojects/Equity Analysis/reports/SNOW-chart.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {out_path}")
