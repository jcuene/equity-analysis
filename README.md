# Equity Analysis

Personal equity research workflow: theme development → watchlist → quarterly quant pre-screen → per-company rubric scoring → periodic briefs → buy/sell decisions. Sourced from Value Line PDFs, Morningstar PDFs, and SEC Edgar (live via MCP).

## Layout

| Folder | What lives here |
|---|---|
| `spec/` | The contract for how the cadences work (`cadence-spec.md`) and shared naming/tiering rules (`conventions.md`) |
| `prompts/` | Reusable research prompts, e.g. `theme-research.md` for developing/refreshing investment themes |
| `rubric/` | The scoring rubric — `rubric-v2.md` is current/source of truth; prior versions and `CHANGELOG.md` explain why it changed |
| `skills/` | Skill definitions that drive the recurring cadences (weekly watchlist brief, first-pass company analysis) |
| `themes/` | Current investment themes (one file each) |
| `watchlist/` | The live watchlist |
| `screens/` | Quarterly quant pre-screen output |
| `companies/` | Per-ticker folder with tearsheets, scores, and notes |
| `briefs/` | Weekly and quarterly summary briefs |
| `decisions/` | Dated buy/sell decision records |
| `data/valueline/` | Source Value Line PDFs |
| `archive/` | Superseded material kept for reference |

## Running a cadence

See `spec/cadence-spec.md` (not yet written — TODO) for what each cadence expects as input and produces as output.

## History

Reorganized into this structure in September 2026; prior layout lived under `My Stack/`.
