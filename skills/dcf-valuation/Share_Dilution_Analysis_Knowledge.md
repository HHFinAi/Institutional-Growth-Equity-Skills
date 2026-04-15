# Share Dilution Analysis - Complete Methodology

## Executive Summary

This document is the **single source of truth** for calculating fully diluted shares outstanding, following the Treasury Stock Method (TSM) and If-Converted method as detailed in Rosenbaum & Pearl's "Investment Banking: Valuation, LBOs, M&A, and IPOs."

**Key Principle:** Always use fully diluted shares for per-share valuation. Using basic shares overstates value and upside potential.

---

## 1. Dilution Bridge Overview

```
Basic Shares Outstanding                    (10-K/10-Q cover page)
+ Restricted Stock Units (RSUs)             (1-for-1 addition)
+ Net New Shares from Options (TSM)         (Treasury Stock Method)
+ Net New Shares from Warrants (TSM)        (Treasury Stock Method)
+ Shares from Convertibles (If-Converted)   (if in-the-money)
+ Performance Share Units (PSUs)            (probability-weighted)
= FULLY DILUTED SHARES OUTSTANDING
```

---

## 2. Basic Shares Outstanding

**Source:** Cover page of most recent 10-K or 10-Q

**Location:** "As of [date], there were X shares of Common Stock outstanding"

**Notes:**
- Use most recent filing date
- Adjust for subsequent equity issuances if material
- Document source date for audit trail

---

## 3. Restricted Stock Units (RSUs)

### Treatment: Add 1-for-1

RSUs have no exercise price - they convert directly to shares upon vesting.

**Formula:**
```
Dilutive Shares from RSUs = Total RSUs Outstanding
```

**Where to Find:** 10-K Notes → Stock-Based Compensation → "RSUs Outstanding" or "Unvested RSUs"

**Excel:**
```excel
=2500000  ' Source: 10-K FY2024, Note 12, Page 78
```

---

## 4. Stock Options - Treasury Stock Method (TSM)

### Core Concept

The TSM assumes:
1. All in-the-money options are exercised at their strike price
2. The company receives cash proceeds from exercise
3. These proceeds are used to repurchase shares at the current market price
4. The NET difference is the dilutive impact

### TSM Formulas

**Full Calculation:**
```
Option Proceeds = In-the-Money Options × Weighted Average Exercise Price
Shares Repurchased = Option Proceeds ÷ Current Share Price
Net New Shares = In-the-Money Options - Shares Repurchased
```

**Simplified Formula:**
```
Net New Shares = Options × (1 - Exercise Price / Current Price)
```

### In-the-Money Test

**Options are in-the-money when:** Current Share Price > Exercise Price

**Out-of-the-money options are EXCLUDED** from dilution calculation.

### Worked Example (Rosenbaum & Pearl)

| Item | Value |
|------|-------|
| Current Share Price | $20.00 |
| Basic Shares Outstanding | 100.0 million |
| In-the-Money Options | 5.0 million |
| Weighted Avg Exercise Price | $18.00 |

**Step-by-Step:**
```
Step 1: Option Proceeds = 5.0M × $18.00 = $90.0M
Step 2: Shares Repurchased = $90.0M ÷ $20.00 = 4.5M
Step 3: Net New Shares = 5.0M - 4.5M = 0.5M

Verification: 5.0M × (1 - $18/$20) = 5.0M × 10% = 0.5M ✓
```

### Multiple Tranches

When options have different strike prices, calculate each tranche separately:

| Tranche | Options (M) | Strike | In-Money? | Proceeds | Repurchased | Net New |
|---------|-------------|--------|-----------|----------|-------------|---------|
| 1 | 2.0 | $15.00 | Yes | $30.0M | 1.50M | 0.50M |
| 2 | 1.5 | $18.00 | Yes | $27.0M | 1.35M | 0.15M |
| 3 | 1.0 | $22.00 | No | - | - | 0.00M |
| 4 | 0.5 | $25.00 | No | - | - | 0.00M |
| **TOTAL** | 5.0 | - | - | $57.0M | 2.85M | **0.65M** |

### Excel Implementation

```excel
' B15: Options Outstanding (input, blue)
=5000000
' B16: Wtd Avg Exercise Price (input, blue)
=18.00
' B17: Current Share Price (input, blue)
=20.00
' B18: In-the-Money Test (formula, black)
=IF(B17>B16,"YES","NO")
' B19: Net New Shares from Options (formula, black)
=IF(B17>B16, B15*(1-B16/B17), 0)
```

### Where to Find Option Data

**10-K Location:** Notes to Financial Statements → Stock-Based Compensation → "Stock Option Activity"

**Required Data:**
1. Options Outstanding (total)
2. Weighted Average Exercise Price
3. By tranche if available (for precision)

---

## 5. Warrants - Treasury Stock Method

### Treatment: Identical to Options

```
Net New Shares from Warrants = Warrants × (1 - Exercise Price / Current Price)
```

**Only include in-the-money warrants** (strike < current price).

**Where to Find:**
- 10-K Equity Note
- 8-K filings for recent warrant issuances
- Prospectus supplements

**Excel:**
```excel
=IF(Current_Price > Warrant_Strike, Warrants * (1 - Warrant_Strike / Current_Price), 0)
```

---

## 6. Convertible Securities - If-Converted Method

### When to Apply

Apply the if-converted method to **in-the-money convertible securities**:

```
Convertible is In-the-Money when: Current Price > Conversion Price
```

### If-Converted Formula

```
Dilutive Shares = Principal Amount ÷ Conversion Price
```

### Critical Valuation Adjustment

**When a convertible is in-the-money:**
1. **ADD** the dilutive shares to fully diluted share count
2. **REMOVE** the convertible debt from Enterprise Value calculation
3. The convert becomes **equity**, not debt

**Failing to adjust debt for in-the-money converts double-counts the value.**

### Worked Example (Rosenbaum & Pearl)

| Item | Value |
|------|-------|
| Current Share Price | $20.00 |
| Convertible Principal | $150.0 million |
| Conversion Price | $15.00 |

**In-the-Money Test:**
```
$20.00 (current) > $15.00 (conversion) → IN-THE-MONEY
```

**Calculation:**
```
Dilutive Shares = $150.0M ÷ $15.00 = 10.0 million shares
```

**Valuation Impact:**
- Add 10.0M shares to diluted count
- Remove $150.0M from debt in EV calculation

### Net Share Settlement (NSS)

Some convertibles use net share settlement:
- Company pays cash up to principal amount
- Only excess value above principal is settled in shares

**NSS Formula:**
```
Dilutive Shares (NSS) = (Current Price - Conversion Price) × Conversion Shares / Current Price
```

**Check the prospectus or 10-K footnotes for settlement mechanics.**

### Excel Implementation

```excel
' B40: Convertible Principal (input, blue)
=150000000
' B41: Conversion Price (input, blue)
=15.00
' B42: In-the-Money Test (formula, black)
=IF(B17>B41,"YES","NO")
' B43: Dilutive Shares from Converts (formula, black)
=IF(B17>B41, B40/B41, 0)
' Debt Adjustment (for EV calculation):
=IF(B17>B41, B40, 0)  ' Amount to subtract from total debt
```

---

## 7. Performance Share Units (PSUs)

### Treatment: Probability-Weighted

PSUs vest contingent on performance targets. Include based on likelihood of achievement:

```
Dilutive Shares from PSUs = PSUs Outstanding × Probability of Achievement
```

### Probability Assessment

| Performance Status | Probability |
|-------------------|-------------|
| Target already achieved | 100% |
| On track to achieve | 75-100% |
| Uncertain / 50-50 | 50% |
| Behind target | 25-50% |
| Unlikely to achieve | 0-25% |

**Conservative Approach:** Exclude PSUs entirely (0% probability)
**Senior Analyst Approach:** Include at 75% probability (default)

### Where to Find

- 10-K → Stock-Based Compensation → "Performance-Based Awards"
- Proxy Statement (DEF 14A) for executive PSU details

**Excel:**
```excel
' B50: PSUs Outstanding (input, blue)
=1000000
' B51: Probability of Achievement (input, blue)
=0.75  ' 75% default
' B52: Expected Shares from PSUs (formula, black)
=B50*B51
```

---

## 8. Stock-Based Compensation (SBC) Adjustment to FCF

### Why Adjust?

SBC is a **real economic cost** that dilutes existing shareholders. While it's a non-cash expense (added back in cash flow), ignoring it overstates the value available to current shareholders.

### Recommended Approach

**Subtract SBC from Unlevered Free Cash Flow:**
```
Adjusted Unlevered FCF = UFCF - Projected SBC Expense
```

### SBC Projection Methods

1. **SBC as % of Revenue** (historical trend)
2. **SBC as % of Operating Expenses**
3. **SBC per Employee × Projected Headcount**

### Sector Benchmarks

| Sector | SBC % of Revenue |
|--------|------------------|
| Large-cap tech | 3-8% |
| High-growth software | 10-20% |
| Clinical-stage biotech | 15-25% of OpEx |
| Mature pharma | 2-5% |
| Financials | 3-7% |

### Example SBC Projection

| Year | Revenue | UFCF | SBC | SBC-Adj UFCF | SBC % Rev |
|------|---------|------|-----|--------------|-----------|
| FY26E | $500M | $100M | ($25M) | $75M | 5.0% |
| FY27E | $625M | $150M | ($30M) | $120M | 4.8% |
| FY28E | $780M | $200M | ($35M) | $165M | 4.5% |
| FY29E | $935M | $250M | ($40M) | $210M | 4.3% |
| FY30E | $1,120M | $300M | ($45M) | $255M | 4.0% |

---

## 9. Complete Dilution Bridge Template

```
DILUTED SHARES CALCULATION
(shares in millions)

ITEM                              | Shares | Source
----------------------------------------------------|
Basic Shares Outstanding          | 100.00 | 10-Q Cover, Q3 2024
                                  |        |
PLUS: RSUs                        |        |
  Unvested RSUs Outstanding       | 2.50   | 10-K Note 12, p.78
                                  |        |
PLUS: Options (TSM)               |        |
  In-the-Money Options            | 5.00   | 10-K Note 12, p.80
  Wtd Avg Exercise Price          | $18.00 |
  Current Share Price             | $20.00 | Yahoo Finance
  × (1 - Strike/Price)            | 10.0%  | =1-18/20
  Net New Shares from Options     | 0.50   | =5.0×10%
                                  |        |
PLUS: Warrants (TSM)              |        |
  In-the-Money Warrants           | 1.00   | 10-K Note 15, p.92
  Exercise Price                  | $16.00 |
  × (1 - Strike/Price)            | 20.0%  | =1-16/20
  Net New Shares from Warrants    | 0.20   | =1.0×20%
                                  |        |
PLUS: Convertibles (If-Converted) |        |
  Principal Amount                | $150M  | Prospectus, 2023
  Conversion Price                | $15.00 |
  In-the-Money?                   | YES    | $20>$15
  Dilutive Shares                 | 10.00  | =$150M/$15
                                  |        |
PLUS: PSUs (Probability-Weighted) |        |
  PSUs Outstanding                | 1.00   | 10-K Note 12, p.81
  × Probability                   | 75%    | Analyst estimate
  Expected Shares from PSUs       | 0.75   | =1.0×75%
----------------------------------------------------|
FULLY DILUTED SHARES              | 113.95 |
----------------------------------------------------|

DILUTION SUMMARY
Basic Shares                      | 100.00 |
Fully Diluted Shares              | 113.95 |
Dilution %                        | 13.95% | =(113.95-100)/100
```

---

## 10. Per-Share Value Impact

### Dilution Impact on Valuation

```
VALUATION IMPACT OF DILUTION

                           | Basic  | Diluted | Impact
----------------------------------------------------
Enterprise Value           | $2,500M| $2,500M | -
(-) Total Debt             | ($500M)| ($500M) |
(+) Remove ITM Convert     | -      | $150M   | Convert → equity
= Adjusted Net Debt        | ($500M)| ($350M) |
Equity Value               | $2,000M| $2,150M | +$150M
÷ Shares Outstanding       | 100.00 | 113.95  | +13.95%
= Per Share Value          | $20.00 | $18.87  | -5.7%
----------------------------------------------------

Current Share Price        | $15.00 | $15.00  |
Implied Upside             | 33.3%  | 25.8%   | -7.5 ppt
```

**Key Insight:** Using basic shares overstates upside by 7.5 percentage points in this example.

### EV-to-Equity Bridge with Convertibles

**Standard Bridge:**
```
Enterprise Value              $2,500M
(-) Total Debt                ($500M)
(+) Cash                      $200M
= Equity Value                $2,200M
```

**Adjusted for ITM Converts:**
```
Enterprise Value              $2,500M
(-) Total Debt                ($500M)
(+) Remove ITM Convert Debt   $150M    ← Convert becomes equity
(+) Cash                      $200M
= Equity Value                $2,350M  ← Higher because convert is now equity
```

---

## 11. Special Considerations by Sector

### Technology Companies

- **High SBC:** Often 5-15% of revenue
- **Large option pools:** Significant TSM dilution
- **RSU-heavy:** Add 1-for-1
- **Annual dilution:** 2-5% typical

### Biotech/Pharma

**Common Dilution Sources:**
1. **Equity Offerings** - Model future raises: Shares = Capital Needed ÷ Expected Price
2. **ATM Facilities** - Check for authorized but unissued capacity
3. **Warrants** - Often issued with equity/debt financings
4. **Milestone-Based CVRs** - Contingent Value Rights may convert to shares
5. **ESPP** - Usually minor (1-2% annually)

**Pre-Money vs Post-Money:** For companies likely to raise capital, model both scenarios.

### Financial Services

- **Lower SBC:** Typically 3-7% of revenue
- **Fewer options:** More cash bonus compensation
- **Convertible preferreds:** Common in bank recapitalizations

---

## 12. Data Sources Reference

| Item | Primary Source | Secondary | Where in Filing |
|------|---------------|-----------|-----------------|
| Basic Shares | 10-K/10-Q Cover | Proxy | Cover page |
| RSUs | 10-K Stock Comp Note | Proxy | "RSUs Outstanding" |
| Stock Options | 10-K Stock Comp Note | 10-Q | "Stock Option Activity" |
| Warrants | 10-K Equity Note | 8-K | Equity section |
| Convertibles | Prospectus | 10-K Debt Note | Debt footnote |
| PSUs | 10-K Stock Comp Note | Proxy | "Performance Awards" |
| SBC Expense | Income Statement | CF Statement | Operating expenses |

---

## 13. Key Formulas Summary

| Method | Formula | Excel |
|--------|---------|-------|
| **TSM (Options/Warrants)** | Options × (1 - Strike/Price) | `=IF(Price>Strike, Opts*(1-Strike/Price), 0)` |
| **If-Converted** | Principal ÷ Conversion Price | `=IF(Price>ConvPrice, Principal/ConvPrice, 0)` |
| **RSUs** | Add 1-for-1 | `=RSUs_Outstanding` |
| **PSUs** | PSUs × Probability | `=PSUs * Probability` |
| **Dilution %** | (Diluted - Basic) / Basic | `=(Diluted-Basic)/Basic` |
| **SBC-Adj FCF** | UFCF - SBC | `=UFCF - SBC` |
| **Debt Adjustment** | Debt - ITM Convert Principal | `=Debt - IF(Price>ConvPrice, Principal, 0)` |
| **Per-Share Value** | Equity Value ÷ Diluted Shares | `=Equity_Value/Diluted_Shares` |

---

## 14. Quality Checklist

Before finalizing any dilution analysis:

**Share Count:**
- [ ] Basic shares from most recent 10-K/10-Q cover page
- [ ] RSUs included 1-for-1
- [ ] Options calculated using TSM (only in-the-money)
- [ ] Warrants calculated using TSM (only in-the-money)
- [ ] Convertibles tested for in-the-money status
- [ ] PSUs probability-weighted (or excluded with note)
- [ ] Dilution bridge reconciles to fully diluted count

**Valuation Adjustments:**
- [ ] Convertibles removed from debt if in-the-money
- [ ] SBC projected and subtracted from FCF
- [ ] All sensitivity tables use diluted shares
- [ ] All scenario analyses use diluted shares
- [ ] EV-to-Equity bridge adjusts for ITM convertibles

**Documentation:**
- [ ] All sources documented with filing references
- [ ] All model tabs use same diluted share count
- [ ] Cover sheet shows both basic AND diluted targets

---

## 15. Common Mistakes to Avoid

1. **Using basic shares** - Always use fully diluted for per-share metrics
2. **Including OTM options in TSM** - Only in-the-money options dilute
3. **Forgetting debt adjustment for ITM converts** - Double-counts value
4. **Ignoring SBC in FCF** - Overstates cash flows available to shareholders
5. **Using target price in TSM** - Use current market price
6. **Missing warrant data** - Check equity footnotes and 8-K filings
7. **Treating RSUs like options** - RSUs add 1-for-1, no TSM calculation
8. **Inconsistent dilution across tabs** - Use same count everywhere
9. **Not documenting sources** - Always cite 10-K page references for audit trail

---

## References

- Rosenbaum, Joshua and Joshua Pearl. "Investment Banking: Valuation, LBOs, M&A, and IPOs." Wiley, 2020. Chapter on Treasury Stock Method.
- SEC EDGAR - Company 10-K, 10-Q, 8-K, Proxy Statement filings
- Damodaran, Aswath. "Investment Valuation." Wiley.
