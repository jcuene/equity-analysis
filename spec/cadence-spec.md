# Project Snowbird — Cadence Spec

*Version 0.1 · Draft for review · Owner: Jim*

This document defines every recurring step in the research stack. It is the contract that the skills implement. If a step is not specified here, no skill should exist for it; if a skill exists that is not specified here, either specify it or delete it.

---

## 0. Conventions

### Repo layout

```
/themes/          investmenttheme_*.md          (one file per theme)
/watchlist/       claude_watchlist.md
/rubric/          scoring_rubric_v2.md, scores/<TICKER>_<YYYY-QN>.md
/tearsheets/      <TICKER>_<YYYY-MM-DD>.md
/briefs/          weekly_<YYYY-WW>.md, quarterly_<YYYY-QN>.md
/decisions/       decision_<YYYY-MM-DD>_<TICKER>.md
/spec/            cadence-spec.md  (this file)
/skills/          *.skill
```

### Commit discipline

A **commit** is a file written to the repo. Everything between commits is exploration and may be discarded. No cadence "completes" without writing its output artifact — a conversation is not an output.

### Conviction tiers

- **High** — full workup required (rubric score, tear sheet, peer ranking, bear case)
- **Medium** — lighter analysis; rubric score only
- **Low** — watchlist presence only, no workup

### Action tiers

- **Overweight** — hold or add gradually
- **High-conviction commitment** — concentrated position, funded by selling an existing holding

### Portfolio constraints (apply to every cadence)

- No new capital. Every buy is a pair trade; the funding sale is part of the decision, not an afterthought.
- Taxable account. Realized gain is a real cost of any funding sale and must appear in the decision memo.
- Aggressive risk profile, 2–3 year horizon, non-income-generating.

---

## 1. Template

Copy this block for each cadence. Every field is required. If a field cannot be filled, the step is not ready to be built.

```markdown
### <Cadence name>

**Stage(s):** explore | planner | worker | critic | promoter
**Frequency:**
**Trigger:**            What starts it. Calendar date, event, or condition.
**Inputs:**             Specific files and data sources read. Name paths.
**Process:**            Ordered steps. Terse. What a skill would encode.
**Output artifact:**    Exact path and filename pattern. One artifact per run.
**Decision it feeds:**  What you can decide after this that you couldn't before.
**Done when:**          Objective exit criteria. Not "when it feels complete."
**Escalation:**         Conditions that promote this into a higher cadence.
**Tooling:**            Skill, MCP servers, model class, interface (Code/Cowork/chat).
**Anti-scope:**         What this step must NOT do. Prevents skill overlap.
**Time budget:**
```

### Field notes

**Decision it feeds** is the load-bearing field. If you can't name a decision, the step is research theater — cut it. "Stay informed" is not a decision. "Determine whether any name has tripped a bearish falsifier and warrants promotion to a quarterly deep dive" is.

**Anti-scope** prevents the most common failure: two skills that both sort of do the same thing, so you never know which to run. State explicitly what each step refuses to do.

**Escalation** is what makes the stack adaptive rather than merely periodic. A weekly scan that can promote a name into an off-cycle deep dive is far more useful than one that only reports.

---

## 2. Worked example — Weekly

### Weekly Watchlist Brief

**Stage(s):** explore

**Frequency:** Weekly, Sunday

**Trigger:** Calendar. Also on demand after any week with a >15% single-day move in a watchlist name.

**Inputs:**
- `/watchlist/claude_watchlist.md` (name list, current conviction tiers)
- `/themes/investmenttheme_*.md` (falsifier lists from each theme's Recommendations section)
- Web search, past 7 days, scoped to watchlist tickers

**Process:**
1. Pull the past week's news for each watchlist name: earnings, guidance, ratings changes, material price moves, M&A, leadership change.
2. Group findings by theme, not by ticker.
3. For each theme, check findings against that theme's explicit bullish-confirmation and bearish-escalation falsifiers.
4. Flag any name where a falsifier was tripped, in either direction.
5. Note earnings dates falling in the next 14 days.

**Output artifact:** `/briefs/weekly_<YYYY-WW>.md` — target ~600 words, three theme sections plus a "Falsifiers tripped" section and a "Coming up" section.

**Decision it feeds:** Whether any name needs off-cycle attention before the next monthly re-rank. Default answer is no.

**Done when:** Every watchlist name has been checked (even if the finding is "nothing material"), and the falsifier section is either populated or explicitly states none tripped.

**Escalation:**
- A bearish falsifier tripped on a **High** conviction name → schedule an off-cycle tear sheet + rubric re-score within 7 days.
- Two or more names in the same theme tripping bearish falsifiers in one week → schedule an off-cycle theme refresh (quarterly process, run early).
- A bullish confirmation on a name currently held at **Medium** → flag for promotion review at the next monthly.

**Tooling:** `weekly-watchlist-brief` skill; web search; Sonnet-class (mechanical, scoped). Runs well in Cowork.

**Anti-scope:**
- Does NOT run rubric scores or produce price targets.
- Does NOT cover broad market or macro news — watchlist-scoped only.
- Does NOT edit the watchlist or change conviction tiers. It flags; the monthly decides.
- Does NOT make buy/sell recommendations.

**Time budget:** 20 minutes to read. Unattended to generate.

---

## 3. Worked example — Quarterly (shows the critic stage)

### Quarterly Theme Refresh & Adversarial Pass

**Stage(s):** explore → critic

**Frequency:** Quarterly, ~3 weeks after the close of each calendar quarter (allows most watchlist names to have reported).

**Trigger:** Calendar. Also triggered early by the weekly escalation rule (two bearish falsifiers in one theme).

**Inputs:**
- The three theme files in `/themes/`, specifically each one's **Thesis Status** and **Recommendations** sections
- The last 13 weekly briefs in `/briefs/`
- Fresh research: earnings releases, transcripts, Morningstar moat/fair-value changes, sell-side commentary
- SEC filings via EDGAR MCP for any name where the accounting question is live

**Process:**
1. **Confirm:** For each theme, list what the prior quarter's stated falsifiers predicted, and what actually happened. Score the theme's own predictions.
2. **Update:** Rewrite the Thesis Status section — Confirmed / What Changed / Skeptic's Voice / Net Assessment.
3. **Critic pass (separate step, run deliberately):** Argue the theme is wrong. Not the "Skeptic's Voice" paragraph you'd write anyway — a genuine attempt to falsify. Required questions:
   - What assumption in the original thesis is doing the most work, and what would it look like if it were inverting right now?
   - Which of my sources are commercial research vendors with an interest in the conclusion?
   - If this theme were already consensus-priced, what evidence would I be seeing? Am I seeing it?
   - What is the strongest argument that the recent price action is the market knowing something I don't?
4. **Re-scope if warranted.** A theme whose central assumption has inverted gets re-scoped, not deleted.
5. **Rewrite falsifiers** for the coming quarter — explicit, dated, checkable.

**Output artifact:** Updated `/themes/investmenttheme_<name>_<season><year>.md` (one commit per theme), plus `/briefs/quarterly_<YYYY-QN>.md` summarizing cross-theme changes and the resulting watchlist actions.

**Decision it feeds:** Which names enter, exit, or change conviction tier — and therefore which get full workups next quarter. Themes are screens, not buy signals; this step sets the candidate pool.

**Done when:** All three theme files carry the current quarter's date, each has a fresh falsifier set, and every conviction-tier change is written down with a one-line reason.

**Escalation:** A theme whose core assumption has inverted (the Enterprise Marketing Software pattern — assumed tailwind became headwind) triggers an immediate position review on every name in that theme, not a wait for the annual.

**Tooling:** Advanced Research for the explore half; Opus-class for the critic half; EDGAR MCP; Morningstar pulled manually. Run in Project Snowbird chat, commit files to repo via Claude Code.

**Anti-scope:**
- Does NOT score individual equities — that is the worker stage.
- Does NOT size positions or select funding trades — that is the promoter stage.
- Does NOT skip the critic pass because the quarter went well. A theme that only gets stress-tested when it's losing is not being stress-tested.

**Time budget:** One session per theme, plus one dedicated critic session. Half a day total.

---

## 4. To be specified

Fill these in using the template above. Suggested shape only — the field values are yours to set.

### Monthly Watchlist Re-Rank
**Stage(s):** planner. Likely trigger: calendar, first weekend of the month. Likely decision fed: conviction tier changes and the ordered queue of which names get full workups. Likely anti-scope: no new research — works only from the last four weekly briefs and the current theme docs.

### Equity Deep Dive
**Stage(s):** worker. Not calendar-driven — triggered by the monthly queue or by weekly escalation. Produces two distinct artifacts that should stay distinct: a narrative tear sheet (`public-company-first-pass`, no scores or targets) and a numeric rubric score. Likely anti-scope: no position sizing, no buy decision — it produces evidence, not a verdict.

### Transaction Prep
**Stage(s):** promoter. Trigger: a High-conviction name clearing the deep dive. This is the artifact that doesn't exist yet and probably matters most. Must include, at minimum: the funding sale (which position, why it's the weakest), the realized gain and tax cost, the position size and its rationale, the bear case in the buyer's own words, and the pre-committed conditions under which the position gets cut. Likely anti-scope: does not revisit the thesis — if the thesis is in question, go back to critic.

### Annual Portfolio Review
**Stage(s):** planner + promoter. Trigger: calendar, December (aligns with the tax-year-split logic in the consolidation plan). Likely decision fed: theme roster itself — add, retire, or reframe themes; rebalance across the three; review whether the rubric is still calibrated.

---

## 5. Stack map

| Stage | Cadence | Output artifact | Interface |
|---|---|---|---|
| explore | Weekly | `/briefs/weekly_*.md` | Cowork (unattended) |
| planner | Monthly | updated `/watchlist/` | Chat |
| explore + critic | Quarterly | updated `/themes/*.md` | Chat (Opus) |
| worker | On trigger | `/tearsheets/`, `/rubric/scores/` | Cowork (Sonnet) |
| promoter | On trigger | `/decisions/` | Chat |
| planner + promoter | Annual | portfolio plan | Chat |

---

## 6. Open questions

- Does the monthly re-rank earn its place, or does the weekly escalation logic plus the quarterly refresh cover it? Build it last and see whether you miss it.
- Should the rubric v2 rebuild be a one-time project or a recurring annual calibration step?
- Is Battery / Power & Grid Infrastructure a fourth theme, or a re-scope of the AI Infrastructure theme's power-constraint axis? Decide before the next quarterly, since it changes the watchlist scope.
- Where does the Value Line manual-entry step live? It's a dependency of the worker stage but has its own cadence (PDF pull) that isn't specified anywhere.
- **Layout naming mismatch.** This spec's Section 0 layout sketch uses different names (`/tearsheets/`, `/rubric/scores/<TICKER>_<YYYY-QN>.md`, `decision_<YYYY-MM-DD>_<TICKER>.md`, underscore-separated theme/watchlist filenames) than what's actually on disk (`companies/<TICKER>/`, `rubric/rubric-v2.md`, hyphenated `decisions/<YYYY-MM-DD>-<slug>.md`, `themes/ai-infrastructure.md`-style names). Nothing has been written under the new naming yet — pick one convention and reconcile before the worker or promoter stages produce real output. See `spec/conventions.md`.
- **Five-analyst design's place in the stack.** A separate design (one analyst per rubric category — Growth, Fundamentals, Value, Quality & Moat, Risk & Catalysts — each tool-grounded with structured per-metric JSON output) has been proposed but isn't referenced anywhere in this spec. Best guess: it's the internal implementation of the Equity Deep Dive worker stage's rubric-scoring half. Not confirmed — decide before building `public-company-first-pass`.
