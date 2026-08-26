# Equity Analysis Project

This project is a framework for analyzing individual equities using three data sources and a custom analysis rubric.

## Data Sources

| Source | Format | How Provided |
|--------|--------|--------------|
| **Value Line** | PDF one-pager per stock | Attached to conversation at runtime |
| **Morningstar** | PDF data sheet per stock | Attached to conversation at runtime |
| **SEC Edgar** | Live via MCP | Queried automatically by ticker |

## Available SEC Edgar MCP Tools

Use these tools to pull live data from SEC filings:

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

## Custom Slash Commands

| Command | Purpose |
|---------|---------|
| `/analyze-equity` | Full analysis using all three sources → structured report |
| `/sec-deep-dive` | Deep dive into SEC filings only (no PDFs required) |
| `/screen-equity` | Quick metrics screen from SEC Edgar only |

## Analysis Rubric

The structured report template is defined in `rubric.md`. All full analyses must follow that rubric exactly.

## Output Convention

- Full reports are saved to `reports/TICKER-YYYY-MM-DD.md`
- Use today's date in the filename
- Always note which data sources were available for that analysis
