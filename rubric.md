# Value Line Scoring Rubric (5–3–1 System)

## Rules

- Every metric receives exactly **5**, **3**, or **1** — no intermediate values.
- **20 metrics** across 5 equally-weighted categories → maximum score = **100**.
- **Value Line PDF is required.** If not attached, block the analysis and ask the user to provide it before proceeding.
- **Morningstar PDF** is used for Competitive Advantage (moat rating). If not attached, ask the user to provide a score of 5, 3, or 1 before finalizing the report.
- **Relative P/E** is calculated as: (Stock P/E) ÷ (S&P 500 P/E). Use WebSearch to get the current S&P 500 trailing P/E if not already known.

## Verdict Thresholds

| Total Score | Verdict |
|-------------|---------|
| ≥ 80 | **Buy** |
| 60 – 79 | **Watch** |
| < 60 | **Avoid** |

---

## Category 1: Growth (max 20 pts)

| Metric | Score 5 (Excellent) | Score 3 (Average) | Score 1 (Poor) | Data Source |
|--------|--------------------|--------------------|----------------|-------------|
| Revenue Growth (8q) | >20% YoY, beats industry avg | 5–10% YoY, in line with market | Flat/negative, below avg | Value Line / SEC |
| EPS Growth (8q) | >20% YoY, consistent upward | 5–10% YoY, some variability | Negative or inconsistent | Value Line / SEC |
| Cash Flow/Share Growth | Strong, in line with EPS | Modest (~5% YoY) | Declining | Value Line |
| Projected EPS Growth (2–3 yrs) | >15% CAGR | 7–10% CAGR | <5% CAGR | Value Line |

## Category 2: Fundamentals (max 20 pts)

| Metric | Score 5 (Excellent) | Score 3 (Average) | Score 1 (Poor) | Data Source |
|--------|--------------------|--------------------|----------------|-------------|
| Operating Margin Trend | Rising, >20% | Stable, 10–15% | Falling or <5% | Value Line / SEC |
| ROE Trend | >15% and rising | 8–12%, stable | <5% or falling | Value Line / SEC |
| Debt Level | <1× EBITDA, declining | 1–2× EBITDA, stable | >3× EBITDA, rising | Value Line / SEC |
| Share Count Trend | Declining (buybacks) | Stable | Rising quickly | Value Line / SEC |

## Category 3: Value (max 20 pts)

| Metric | Score 5 (Excellent) | Score 3 (Average) | Score 1 (Poor) | Data Source |
|--------|--------------------|--------------------|----------------|-------------|
| PEG Ratio | ≤1.0 | 1.3–1.5 | >2.0 | Value Line / SEC |
| Relative P/E (vs. S&P 500) | <1.0 (discount to market) | ~1.2 | >1.5 (premium to market) |Value Line + WebSearch for S&P 500 P/E |
| P/FCF | <15 | 18–22 | >30 | Value Line / SEC |
| Price vs. Value Line 18-mo Target | ≥30% below midpoint | 10–15% below midpoint | At or above midpoint | Value Line |

## Category 4: Quality & Moat (max 20 pts)

| Metric | Score 5 (Excellent) | Score 3 (Average) | Score 1 (Poor) | Data Source |
|--------|--------------------|--------------------|----------------|-------------|
| Earnings Predictability | ≥80 VL score | ~60 VL score | <40 VL score | Value Line |
| Price Stability | ≥80 VL score | ~60 VL score | <40 VL score | Value Line |
| Financial Strength | A or higher | B | C or lower | Value Line |
| Competitive Advantage | Wide moat (Morningstar) | Narrow moat (Morningstar) | No moat (Morningstar) | Morningstar PDF — if unavailable, ask user |

## Category 5: Risk & Catalysts (max 20 pts)

| Metric | Score 5 (Excellent) | Score 3 (Average) | Score 1 (Poor) | Data Source |
|--------|--------------------|--------------------|----------------|-------------|
| Industry Timeliness | Top quintile | Middle quintiles | Bottom quintile | Value Line |
| Company Timeliness | Rank 1 or 2 | Rank 3 | Rank 4 or 5 | Value Line |
| Key Catalysts | Multiple clear catalysts | One catalyst | None | 10-K / 8-K / analyst view |
| Major Risks | Minimal | Manageable | Significant | 10-K Risk Factors / SEC |

---

## Scoring Summary Table (use in every report)

| Category | Metrics Scored | Category Score | Max |
|----------|---------------|----------------|-----|
| Growth | 4 | /20 | 20 |
| Fundamentals | 4 | /20 | 20 |
| Value | 4 | /20 | 20 |
| Quality & Moat | 4 | /20 | 20 |
| Risk & Catalysts | 4 | /20 | 20 |
| **TOTAL** | **20** | **/100** | **100** |

**Verdict:** [ Buy ≥80 / Watch 60–79 / Avoid <60 ]

---

## Scoring Rationale Format

Every metric in the report requires **two things**: a summary row in the category table, and a dedicated analysis block immediately after the table. The analysis block must follow this format exactly.

### Structure of each metric analysis block

```
#### [Metric Name] — Score: X

[Opening sentence stating the headline value and what it means in plain English.]

[Supporting data table — always include at least one table of the actual numbers that
drove the score. Choose the table type that best fits the metric:
  - Time-series table for trend metrics (revenue, EPS, margins, share count, ROE)
  - Comparison table for relative metrics (PEG, Relative P/E, P/FCF)
  - Balance sheet snapshot for debt metrics
  Use the most recent available periods. Label actuals vs. estimates clearly.]

[Analysis paragraph(s): explain where the metric sits relative to the rubric thresholds.
Be explicit — name the threshold, name the actual value, state whether it clears the bar.
If the metric falls between two thresholds, explain why you chose the score you did.
If GAAP and non-GAAP tell different stories, address both and explain which was used for scoring.
If data was unavailable or had to be estimated, say so and explain the assumption.]

**Score X — [one-sentence summary of the decisive reason for that score.]**
```

---

### Rules for the analysis blocks

1. **Always show the numbers.** A score without a data table is not acceptable. If the data is in the PDFs, reproduce the relevant rows. If it requires calculation (e.g., Debt/EBITDA, Relative P/E), show the arithmetic.

2. **Name the threshold explicitly.** Don't just say "this is good." Say "the rubric threshold for Score 5 is >20% YoY; the trailing 8-quarter average is 29%, which exceeds the threshold."

3. **Address complicating factors directly.** Common ones:
   - GAAP vs. non-GAAP divergence (quantify the gap; state which was used for scoring)
   - Metric trending in the wrong direction despite being above a threshold (e.g., ROE >15% but falling — explain why that costs the Score 5)
   - Missing data (e.g., Industry Timeliness not on the VL sheet — state the assumption)
   - Metric sitting between two thresholds (explain the tiebreak reasoning)

4. **End every block with a bold verdict sentence.** Format: `**Score X — [reason].**` This makes it easy to skim the report and understand each scoring decision at a glance.

5. **Calibrate depth to complexity.** Simple metrics with clean data (e.g., Financial Strength = A+) need one short paragraph. Complex or ambiguous metrics (e.g., EPS Growth with a GAAP/non-GAAP switch, Competitive Advantage with a nuanced moat) merit 3–4 paragraphs.

---

### Reference examples by metric type

**Trend metric (e.g., Revenue Growth):**
> Show a table of all 8 quarters with YoY % growth. Note whether growth is accelerating or decelerating. Compare to the >20% / 5–10% / flat thresholds. Note industry context if available from Value Line.

**Profitability metric (e.g., Operating Margin):**
> Show a 3–5 year table of annual margins. Note the direction (rising/falling/stable). If non-GAAP, show the GAAP equivalent and quantify the difference. Compare to the >20% / 10–15% / <5% thresholds.

**Balance sheet metric (e.g., Debt Level):**
> Show LT debt, estimated EBITDA, and the calculated Debt/EBITDA ratio. Show the trend (is debt rising or falling?). Note cash position and net debt if relevant. Compare to the <1x / 1–2x / >3x thresholds.

**Valuation metric (e.g., P/FCF):**
> Show the calculation: market cap, FCF figure used, resulting multiple. Cross-reference sources if multiple FCF figures are available. Compare to the <15x / 18–22x / >30x thresholds. Note FCF yield as a cross-check.

**Qualitative metric (e.g., Competitive Advantage):**
> State the Morningstar moat rating and its source date. Summarize the key factors supporting or undermining a moat claim (switching costs, network effects, cost advantages, intangibles). Note any material difference between Morningstar's view and the VL analyst's characterization.

**Catalyst/Risk metric:**
> For Key Catalysts: list each catalyst as a numbered item with a sentence on the mechanism and timing. For Major Risks: list each risk as a numbered item with a sentence on severity and likelihood. Don't just list topics — explain why each matters for the investment thesis.
