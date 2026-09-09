# AGENTS.md

Project context for AI coding agents (Claude Code, OpenAI Codex, etc.) working in this repo. This file replaces the old `CLAUDE.md`, which predated the September 2026 reorg and pointed at paths (`rubric.md`, `reports/`) that no longer exist.

## What this repo is

A personal equity-research workflow for Jim: aggressive risk profile, retired (no new capital, not drawing income), taxable account, 2–3 year horizon. The workflow runs on cadences, not one-shot commands: theme development → watchlist → quarterly quant pre-screen → per-company rubric scoring → periodic briefs → buy/sell decisions.

**Read `spec/cadence-spec.md` before building or changing any skill.** It's the binding contract: every cadence has a trigger, defined inputs, an ordered process, an exact output artifact, an escalation rule, and an explicit anti-scope. Per that spec's own rule: *if a step isn't specified there, no skill should exist for it; if a skill exists that isn't specified there, either specify it or delete it.*

## Data sources, in trust order

1. **Value Line** — primary. PDF one-pager per stock, attached to the conversation at runtime.
2. **Morningstar** — secondary / cross-check. PDF data sheet, attached at runtime.
3. **SEC EDGAR** — fallback, live via the `sec-edgar-mcp` MCP server.

Never substitute a model estimate for a figure that should come from one of these. If a source doesn't cover a data point, say so explicitly rather than filling the gap.

### SEC EDGAR MCP tools available

- `mcp__sec-edgar-mcp__get_cik_by_ticker` — resolve ticker to CIK
- `mcp__sec-edgar-mcp__get_company_info` — basic company profile
- `mcp__sec-edgar-mcp__get_key_metrics` — financial ratios and valuation metrics
- `mcp__sec-edgar-mcp__get_financials` — income statement, balance sheet, cash flow
- `mcp__sec-edgar-mcp__get_recent_filings` — list of recent SEC filings
- `mcp__sec-edgar-mcp__get_filing_sections` — read 10-K sections (business, risk factors, MD&A)
- `mcp__sec-edgar-mcp__get_segment_data` — revenue/profit by business segment
- `mcp__sec-edgar-mcp__analyze_8k` — parse material events from 8-K filings
- `mcp__sec-edgar-mcp__get_insider_transactions` — Form 4 insider activity
- `mcp__sec-edgar-mcp__get_insider_summary` — summarized insider buying/selling

## Repo layout

See the table in `README.md` for the full layout; the short version:

- `themes/`, `watchlist/` — current investment themes and the live watchlist
- `rubric/` — `rubric-v2.md` is the scoring rubric, source of truth; `CHANGELOG.md` explains changes
- `spec/` — `cadence-spec.md` (the cadence contract) and `conventions.md` (naming/tiering/constraints)
- `skills/` — skill definitions that implement each cadence
- `companies/`, `screens/`, `briefs/`, `decisions/` — per-cadence output artifacts
- `data/valueline/` — source Value Line PDFs
- `archive/` — superseded material kept for reference

File-naming patterns and tiers are in `spec/conventions.md` — follow them exactly; don't invent a new pattern per run.

## Architecture: stages and cadences

Every cadence sits at one stage: **explore → planner → worker → critic → promoter**. Specified so far (see `spec/cadence-spec.md` for full detail):

- **Weekly Watchlist Brief** (explore) — watchlist-scoped news scan, escalates on tripped falsifiers
- **Quarterly Theme Refresh & Adversarial Pass** (explore → critic) — updates theme thesis status, includes a deliberate falsification pass

Still to be specified: Monthly Watchlist Re-Rank (planner), Equity Deep Dive (worker), Transaction Prep (promoter), Annual Portfolio Review (planner + promoter).

**Commit discipline:** a commit is a file written to the repo. Everything between commits is exploration and may be discarded. No cadence "completes" without writing its output artifact — a conversation is not an output.

**Anti-scope is binding.** Each cadence's anti-scope section in `spec/cadence-spec.md` exists to prevent skill overlap — don't let one skill quietly start doing another's job.

## Rubric

Source of truth: `rubric/rubric-v2.md`. Five categories (Growth, Fundamentals, Value, Quality & Moat, Risk & Catalysts), each with 3–4 metrics scored 1 (poor) / 3 (average) / 5 (excellent), summed to a total out of 100.

## Portfolio constraints (apply to every cadence)

- No new capital — every buy is a pair trade; the funding sale is part of the decision, not an afterthought
- Taxable account — realized gain from any funding sale is a real cost and must appear in the decision memo
- Aggressive risk profile, 2–3 year horizon, non-income-generating

## Guardrails

- No score without a cited source figure — no scoring from memory or estimation
- Flag low-confidence/missing data explicitly rather than filling a gap silently
- Every analysis output ends with a markdown summary table (the repo's standing convention)
- Never commit secrets (API keys, MCP config) — use environment variables / local config excluded via `.gitignore`

## Open questions — do not resolve unilaterally, ask Jim

1. **Layout naming mismatch.** `spec/cadence-spec.md`'s Section 0 layout sketch uses different names (`/tearsheets/`, `/rubric/scores/<TICKER>_<YYYY-QN>.md`, `decision_<YYYY-MM-DD>_<TICKER>.md`) than what's actually on disk (`companies/<TICKER>/`, `rubric/rubric-v2.md`, hyphenated `decisions/<YYYY-MM-DD>-<slug>.md`). Nothing has been written under the new naming yet — reconcile before the worker or promoter stages produce real output.
2. **Five-analyst design's place in the stack.** A separate design (one analyst per rubric category — Growth/Fundamentals/Value/Quality & Moat/Risk & Catalysts — each tool-grounded with structured per-metric JSON output) has been proposed but isn't referenced in the cadence spec. Best guess: it's the internal implementation of the Equity Deep Dive worker stage's rubric-scoring half — not confirmed.

## History

- **AGENTS.md replaces `CLAUDE.md`** (removed) as of this change — CLAUDE.md predated the September 2026 reorg and referenced paths (`rubric.md`, `reports/TICKER-YYYY-MM-DD.md`) that no longer exist. Note: the local `.claude/commands/` slash commands (`analyze-equity`, `screen-equity`, `sec-deep-dive`) are gitignored/local-only and still reference the old paths — they haven't been updated yet.
- Repo reorganized into its current structure in September 2026; prior layout lived under `My Stack/`.
