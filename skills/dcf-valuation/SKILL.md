---
name: dcf-valuation
description: "Conduct DCF (Discounted Cash Flow) valuations for stocks with institutional-grade share dilution analysis. Use when the user asks to value a company, build a DCF model, or perform intrinsic valuation. Includes Treasury Stock Method (TSM) for options/warrants, If-Converted method for convertibles, RSU/PSU dilution, and SBC-adjusted FCF. Produces a multi-tab Excel workbook with historical financials, projections, sensitivity tables, diluted shares bridge, and scenario analysis. Tailored for Information Technology and Biotech sectors with appropriate model structures (two-stage, three-stage, or SOTP)."
---

# DCF Valuation Skill (with Share Dilution Analysis)

Build professional DCF valuation models for publicly traded companies with institutional-grade share dilution analysis following Rosenbaum & Pearl's "Investment Banking: Valuation, LBOs, M&A, and IPOs" methodology.

## Workflow Overview

1. **Gather company info** – Identify ticker, sector, and business model
2. **Fetch financial data** – Pull 5 years of historical financials from Yahoo Finance; supplement with SEC 10-K if needed
3. **Select model structure** – Choose two-stage, three-stage, or SOTP based on company profile
4. **Build projections** – Forecast revenue, margins, and free cash flow
5. **Calculate DCF** – Discount FCF and terminal value to present value
6. **Build dilution bridge** – Calculate fully diluted shares using TSM/If-Converted methods
7. **SBC-adjusted FCF** – Subtract stock-based compensation from FCF for true shareholder value
8. **Per-share valuation** – Show impact at basic vs fully diluted shares
9. **Sensitivity & scenarios** – Generate tables and bull/base/bear cases
10. **Output Excel workbook** – Multi-tab model with formatting per xlsx skill standards

---

## Model Structure Selection

| Structure | Use Case | Characteristics |
|-----------|----------|-----------------|
| **Two-Stage DCF** | Mature companies | 5-10 year forecast + terminal value |
| **Three-Stage DCF** | High-growth (tech/biotech) | High growth → Transition → Terminal |
| **Sum-of-the-Parts** | Conglomerates | Value segments separately, sum, subtract net debt |

---

## Data Fetching

**Network Requirements**: Requires access to Yahoo Finance (`query1.finance.yahoo.com`, `query2.finance.yahoo.com`) and SEC EDGAR (`data.sec.gov`, `www.sec.gov`).

### Yahoo Finance (Primary)

```python
import yfinance as yf
ticker = yf.Ticker("AAPL")
income_stmt = ticker.financials
balance_sheet = ticker.balance_sheet
cash_flow = ticker.cashflow
info = ticker.info
```

### SEC EDGAR (Supplementary)

For detailed segment data, MD&A, or dilution data if Yahoo incomplete:
- Fetch 10-K filing via SEC EDGAR API
- Parse revenue breakdown, segment margins, risk factors
- **Critical for dilution**: Stock-based compensation note, equity footnotes, warrant disclosures

---

## Key Assumptions (User-Customizable)

| Assumption | Default | Notes |
|------------|---------|-------|
| Revenue growth (Y1-5) | Historical CAGR | User can override |
| EBIT margin | Historical avg or target | User can set target margin |
| Tax rate | Effective rate from financials | |
| D&A % of revenue | Historical avg | |
| Capex % of revenue | Historical avg | |
| NWC % of revenue | Historical change avg | |
| Risk-free rate | 10Y Treasury yield | Fetch current |
| Equity risk premium | 5.5% | Damodaran default |
| Terminal growth | 2.5% (tech) / 2.0% (other) | |
| SBC % of revenue | Historical avg | Project forward |
| PSU achievement probability | 75% | 0% for conservative |

---

## Share Dilution Analysis

**⭐ REFERENCE:** For complete methodology, formulas, worked examples, and templates, see **Share_Dilution_Analysis_Knowledge.md** in project knowledge.

### Quick Reference

| Method | Formula | Knowledge MD Section |
|--------|---------|---------------------|
| RSUs | Add 1-for-1 | Section 3 |
| Options (TSM) | Options × (1 - Strike/Price) | Section 4 |
| Warrants (TSM) | Same as options | Section 5 |
| Convertibles | Principal ÷ Conversion Price | Section 6 |
| PSUs | PSUs × Probability | Section 7 |
| SBC-Adjusted FCF | UFCF - SBC | Section 8 |

### Key Principles

1. **Always use fully diluted shares** for per-share valuation
2. **Only include in-the-money** options/warrants/convertibles
3. **Remove ITM convertible debt** from EV calculation to avoid double-counting
4. **Subtract SBC from FCF** for true shareholder value
5. **Document all sources** with 10-K page references

### Dilution Data Sources

| Item | Primary Source | Where in Filing |
|------|---------------|-----------------|
| Basic Shares | 10-K/10-Q Cover | Cover page |
| RSUs | 10-K Stock Comp Note | "RSUs Outstanding" |
| Stock Options | 10-K Stock Comp Note | "Stock Option Activity" |
| Warrants | 10-K Equity Note | Equity section |
| Convertibles | Prospectus | Debt footnote |
| PSUs | 10-K Stock Comp Note | "Performance Awards" |
| SBC Expense | Income Statement | Operating expenses |

---

## Excel Output Structure

Create workbook with these tabs (in order):

### Tab 1: CoverSheet
- Company name, ticker, valuation date
- Implied share price vs current price (**both basic and diluted**)
- Upside/downside percentage (**both basic and diluted**)
- Key assumptions summary
- **Dilution summary**: Basic shares, diluted shares, dilution %

### Tab 2: IS (Income Statement)
- Historical (5 years) and projected (5 years)
- **SBC as separate line item**
- Key margins and growth rates
- SBC as % of Revenue (historical and projected)

### Tab 3: BS (Balance Sheet)
- Historical (5 years)
- **Convertible Debt** separately identified
- Key ratios

### Tab 4: CF (Cash Flow Statement)
- Historical (5 years)
- **SBC add-back clearly shown**
- FCF and **SBC-Adjusted FCF**

### Tab 5: DCF
- UFCF build-up
- **SBC-Adjusted UFCF line**
- Terminal value (Gordon Growth + Exit Multiple)
- PV calculations
- EV bridge (**adjusted for ITM convertibles**)
- Equity Value per share (**both basic and fully diluted**)
- WACC components inline

### Tab 6: Diluted_Shares
**Purpose:** TSM/If-Converted dilution bridge, SBC-adjusted FCF, per-share impact

**Section 1: Dilution Bridge**
- Basic shares + RSUs + Options (TSM) + Warrants (TSM) + Convertibles + PSUs = Fully Diluted
- See Knowledge MD Section 9 for complete template

**Section 2: SBC-Adjusted FCF Analysis**
- Project SBC as % of revenue over forecast period
- Show UFCF vs SBC-Adjusted UFCF

**Section 3: Per-Share Value Impact**
- Show Basic vs Diluted equity value and price target
- Highlight upside difference (dilution impact on returns)

### Tab 7: Reverse_DCF
- Market-implied assumptions analysis
- Goal-seek revenue growth and EBIT margin
- **Show at both basic and diluted share counts**

### Tab 8: Sensitivity
Two sensitivity tables (using **fully diluted shares**):
1. Revenue Growth vs Terminal Multiple/Growth
2. Revenue Growth vs EBIT Margin

### Tab 9: Scenarios
Three probability-weighted scenarios (**at fully diluted shares**):
- **Bull** (25%): Higher growth, margin expansion
- **Base** (50%): Management guidance / consensus
- **Bear** (25%): Growth slowdown, margin pressure

### Tab 10: Trading_Comps
- Peer company trading multiples
- EV/Revenue, EV/EBITDA, P/E
- Ensure peer multiples use diluted shares for per-share metrics

---

## Formatting Standards

Follow xlsx skill conventions:

| Element | Format |
|---------|--------|
| Blue text | Input assumptions (including dilution inputs) |
| Black text | Formulas |
| Green text | Cross-sheet links |
| Yellow highlight | Key outputs (diluted share price targets) |
| Years | Text format ("2024" not 2,024) |
| Currency | $#,##0 with units in headers |
| Percentages | 0.0% format (one decimal) |
| Negatives | Parentheses (123) not minus -123 |

**Dilution-specific:**
- Clearly label "Basic" vs "Diluted" in all per-share metrics
- Highlight dilution % prominently
- Include source citations for all dilution inputs (10-K page references)

---

## WACC Calculation

### Formula

```
WACC = (E/V) × Re + (D/V) × Rd × (1 - T)
```

### Cost of Equity (CAPM)

```
Re = Rf + β × ERP
```

| Component | Source | Default |
|-----------|--------|---------|
| Rf | 10-Year Treasury | Fetch current |
| β | Yahoo Finance `info['beta']` | 5-year monthly |
| ERP | Damodaran | 5.5% |

### Size Premium

| Market Cap | Premium |
|------------|---------|
| Micro-cap (<$300M) | +3.5% |
| Small-cap ($300M-$2B) | +2.0% |
| Mid-cap ($2B-$10B) | +1.0% |
| Large-cap (>$10B) | 0% |

### Cost of Debt

| Rating | Spread (bps) |
|--------|-------------|
| AAA | 50-75 |
| AA | 75-100 |
| A | 100-150 |
| BBB | 150-225 |
| BB | 250-350 |
| B | 400-500 |

### WACC Reasonableness

| WACC | Company Profile |
|------|-----------------|
| 6-8% | Large-cap, stable, IG |
| 8-10% | Mid-cap, moderate growth |
| 10-12% | Small-cap, higher risk |
| 12%+ | High-growth, speculative |

---

## Terminal Value

### Gordon Growth Model

```
Terminal Value = FCF_n × (1 + g) / (WACC - g)
```

| Company Type | Terminal Growth |
|--------------|-----------------|
| Tech with network effects | 2.5-3.5% |
| Mature industrials | 1.5-2.5% |
| Declining industries | 0-1.5% |

### Exit Multiple Method

```
Terminal Value = EBITDA_n × Exit Multiple
```

Typically 6-12x EBITDA. **Best Practice:** Calculate using both methods.

---

## Sector Adjustments

### Information Technology

- **High SBC**: 10-20% of revenue for growth stage; always subtract from FCF
- **Heavy option/RSU pools**: Significant TSM dilution; 2-5% annual dilution typical
- **Higher terminal growth**: 2.5-3.5% for platform businesses with network effects
- **Key metrics**: ARR, NRR, CAC Payback, Rule of 40

### Biotech/Pharma

- **Pipeline valuation**: Use rNPV with probability by phase (Phase 1: 10-15%, Phase 2: 25-35%, Phase 3: 50-70%)
- **High dilution environment**: Frequent equity raises, warrants, milestone-based CVRs
- **SBC**: Often 15-25% of operating expenses for clinical-stage
- **Patent cliff**: Model revenue decline at LOE; biosimilar erosion 30-50% within 2 years

---

## Quality Checklist

**⭐ REFERENCE:** See **Share_Dilution_Analysis_Knowledge.md Section 14** for complete checklist.

**Quick Validation:**
- [ ] Basic shares from most recent 10-K/10-Q cover page
- [ ] All dilutive securities calculated (RSUs, options, warrants, convertibles, PSUs)
- [ ] Only in-the-money securities included
- [ ] ITM convertibles removed from debt in EV bridge
- [ ] SBC subtracted from FCF
- [ ] All tabs use same diluted share count
- [ ] Cover sheet shows both basic AND diluted price targets
- [ ] All sources documented with 10-K page references

---

## Common Mistakes to Avoid

**⭐ REFERENCE:** See **Share_Dilution_Analysis_Knowledge.md Section 15** for complete list.

**Critical Errors:**
1. Using basic shares instead of fully diluted
2. Including out-of-the-money options in TSM
3. Forgetting to remove ITM convert debt from EV
4. Ignoring SBC in FCF calculation
5. Inconsistent dilution counts across model tabs

---

## Example Usage

**User**: "Build a DCF model for NVIDIA"

**Steps**:
1. Fetch NVDA financials from Yahoo Finance
2. Identify sector: Information Technology (Semiconductors)
3. Select model: Three-stage DCF (high growth AI/GPU company)
4. Fetch dilution data from 10-K: RSUs, options outstanding
5. Build dilution bridge using Knowledge MD methodology
6. Calculate SBC-adjusted FCF: Project SBC as % of revenue
7. Project 10 years with fade to terminal
8. Build sensitivity tables (using diluted shares)
9. Show per-share impact: Basic vs Diluted price targets
10. Output `NVDA_DCF_Model.xlsx`

---

## References

- Rosenbaum & Pearl, "Investment Banking: Valuation, LBOs, M&A, and IPOs" - TSM, If-Converted Method
- Damodaran, "Investment Valuation" - WACC, Terminal Value, Sector Adjustments
- McKinsey, "Valuation: Measuring and Managing the Value of Companies" - DCF Framework
- **Share_Dilution_Analysis_Knowledge.md** - Complete dilution methodology (project knowledge)
