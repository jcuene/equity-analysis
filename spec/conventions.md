# Conventions

Naming, tiering, and process constraints referenced across the repo. This file describes the actual current repo layout; see `spec/cadence-spec.md` for the cadence contract these conventions support.

## File naming patterns (current, as used on disk)

- Company work: `companies/<TICKER>/` — per-ticker folder holding tearsheets, rubric scores, and notes (e.g. `companies/ANET/ANET-2026-04-16.md`)
- Weekly briefs: `briefs/weekly/<YYYY-Www>.md`
- Quarterly briefs: `briefs/quarterly/<YYYY-Qn>.md`
- Decisions: `decisions/<YYYY-MM-DD>-<slug>.md`
- Screens: `screens/<YYYY-Qn>-<slug>.md`
- Themes: one file per theme under `themes/` (e.g. `themes/ai-infrastructure.md`)
- Watchlist: `watchlist/watchlist.md`
- Rubric: `rubric/rubric-v2.md` is current/source of truth; changes logged in `rubric/CHANGELOG.md`

**Open question:** `spec/cadence-spec.md`'s layout sketch (Section 0) uses a different set of names — `/tearsheets/`, `/rubric/scores/<TICKER>_<YYYY-QN>.md`, `decision_<YYYY-MM-DD>_<TICKER>.md`, underscore-separated theme/watchlist filenames — that don't match what's actually on disk. Nothing has been written under the new naming yet, so pick one convention and reconcile before the worker or promoter stages start producing real output; see the cadence spec's Open Questions section.

## Watchlist tiers

- **Conviction tiers:** High (full workup — rubric score, tear sheet, peer ranking, bear case) / Medium (rubric score only) / Low (watchlist presence only, no workup)
- **Action tiers:** Overweight (hold or add gradually) / High-conviction commitment (concentrated position, funded by selling an existing holding)

## Portfolio constraints (apply to every cadence)

- No new capital — every buy is a pair trade; the funding sale is part of the decision, not an afterthought
- Taxable account — realized gain from any funding sale is a real cost and must appear in the decision memo
- Aggressive risk profile, 2–3 year horizon, non-income-generating

## Data source trust order

Value Line (primary) → Morningstar (secondary/cross-check) → SEC EDGAR via `sec-edgar-mcp` (fallback for anything not covered by the first two). Never substitute a model estimate for a figure that should come from one of these.
