# Share Dilution Analysis Reference

## Table of Contents
1. Dilution Bridge Overview
2. Treasury Stock Method (TSM)
3. If-Converted Method
4. RSUs and PSUs
5. SBC-Adjusted FCF
6. Per-Share Value Impact
7. Diluted_Shares Tab Structure
8. Semiconductor-Specific Considerations

---

## 1. Dilution Bridge Overview

### Complete Dilution Bridge

```
Basic Shares Outstanding              (10-K/10-Q cover page)
+ Restricted Stock Units (RSUs)       (1-for-1 addition)
+ Net New Shares from Options (TSM)   (Treasury Stock Method)
+ Net New Shares from Warrants (TSM)  (Treasury Stock Method)
+ Shares from Convertibles            (If-Converted Method)
+ Performance Share Units (PSUs)      (Probability-weighted)
= FULLY DILUTED SHARES OUTSTANDING
```

### Data Sources

| Item | Primary Source | Secondary Source |
|------|----------------|------------------|
| Basic Shares | 10-K/10-Q Cover | Proxy Statement |
| RSUs | 10-K Stock Comp Note | Proxy Statement |
| Stock Options | 10-K Stock Comp Note | 10-Q |
| Warrants | 10-K Equity Note | 8-K Filings |
| Convertibles | Prospectus | 10-K Debt Note |
| PSUs | 10-K Stock Comp Note | Proxy Statement |
| SBC Expense | Income Statement | Cash Flow Statement |

---

## 2. Treasury Stock Method (TSM)

### Core Concept (Rosenbaum & Pearl)

The TSM assumes:
1. All in-the-money options/warrants are exercised at strike price
2. Company receives cash proceeds from exercise
3. Proceeds used to repurchase shares at current market price
4. NET difference is the dilutive impact

### TSM Formula

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

```
Options are IN-THE-MONEY when:
Current Share Price > Weighted Average Exercise Price

OUT-OF-THE-MONEY options are EXCLUDED from dilution.
```

### Worked Example (from Rosenbaum & Pearl)

**Assumptions:**
| Item | Value |
|------|-------|
| Current Share Price | $20.00 |
| Basic Shares Outstanding | 100.0M |
| In-the-Money Options | 5.0M |
| Weighted Average Exercise Price | $18.00 |

**Calculation:**
```
Step 1: Option Proceeds = 5.0M × $18.00 = $90.0M
Step 2: Shares Repurchased = $90.0M ÷ $20.00 = 4.5M
Step 3: Net New Shares = 5.0M - 4.5M = 0.5M

Verification: 5.0M × (1 - $18/$20) = 5.0M × 10% = 0.5M ✓
```

### Multiple Tranches

Calculate each tranche separately:

| Tranche | Options | Strike | In-Money? | Proceeds | Repurchased | Net New |
|---------|---------|--------|-----------|----------|-------------|---------|
| 1 | 2.0M | $15.00 | Yes | $30.0M | 1.50M | 0.50M |
| 2 | 1.5M | $18.00 | Yes | $27.0M | 1.35M | 0.15M |
| 3 | 1.0M | $22.00 | No | - | - | 0.00M |
| 4 | 0.5M | $25.00 | No | - | - | 0.00M |
| **TOTAL** | 5.0M | | | $57.0M | 2.85M | **0.65M** |

---

## 3. If-Converted Method

### When to Apply

Apply to **in-the-money convertible securities**:
```
Convertible is IN-THE-MONEY when:
Current Share Price > Conversion Price
```

### If-Converted Formula

```
Dilutive Shares = Principal Amount ÷ Conversion Price
```

### Treatment in Valuation

When a convertible is in-the-money:
1. **ADD** dilutive shares to fully diluted shares
2. **REMOVE** convertible debt from Enterprise Value
3. The convert becomes equity, not debt

### Worked Example (from Rosenbaum & Pearl)

**Assumptions:**
| Item | Value |
|------|-------|
| Current Share Price | $20.00 |
| Convertible Principal | $150.0M |
| Conversion Price | $15.00 |

**In-the-Money Test:**
```
$20.00 (current) > $15.00 (conversion) → IN-THE-MONEY
```

**Calculation:**
```
Dilutive Shares = $150.0M ÷ $15.00 = 10.0M shares
```

**Impact on Valuation:**
- Add 10.0M shares to diluted count
- Remove $150.0M from debt in EV calculation

### Net Share Settlement (NSS)

Some convertibles use net share settlement:
- Company pays cash up to principal amount
- Only excess value is settled in shares

**NSS Formula:**
```
Dilutive Shares = (Current Price - Conversion Price) × Conversion Shares / Current Price
```

---

## 4. RSUs and PSUs

### RSUs: Add 1-for-1

RSUs have **no exercise price** - convert directly to shares upon vesting.

```
Dilutive Shares from RSUs = Total RSUs Outstanding
```

**Where to Find:**
- 10-K Notes → Stock-Based Compensation
- Look for "RSUs Outstanding" or "Unvested RSUs"

### PSUs: Probability-Weighted

PSUs vest contingent on performance targets.

```
Dilutive Shares from PSUs = PSUs Outstanding × Probability of Achievement
```

**Probability Assessment:**

| Performance Status | Probability |
|-------------------|-------------|
| Target achieved | 100% |
| On track | 75-100% |
| Uncertain | 50% |
| Behind target | 25-50% |
| Unlikely | 0-25% |

**Conservative Approach:** Many analysts exclude PSUs entirely.

---

## 5. SBC-Adjusted FCF

### Why Adjust?

Stock-Based Compensation (SBC) is a **real economic cost** that dilutes existing shareholders. While non-cash, ignoring it overstates value.

### SBC Adjustment Formula

```
Adjusted Unlevered FCF = UFCF - Projected SBC Expense
```

### SBC Projection Methods

| Method | Formula |
|--------|---------|
| % of Revenue | Historical SBC% × Projected Revenue |
| % of OpEx | Historical SBC/OpEx × Projected OpEx |
| Per Employee | SBC/Employee × Projected Headcount |

### Semi-Specific SBC Benchmarks

| Company Type | SBC % of Revenue | SBC % of OpEx |
|--------------|------------------|---------------|
| Equipment | 3-5% | 8-12% |
| Memory | 2-4% | 6-10% |
| Foundry | 2-3% | 5-8% |
| Fabless (mature) | 8-12% | 15-20% |
| Fabless (growth) | 15-25% | 25-35% |

### Example FCF Adjustment

```
($ millions)           | FY26E | FY27E | FY28E | FY29E | FY30E
-------------------------------------------------------------
Unlevered FCF          | $100  | $150  | $200  | $250  | $300
Less: SBC Expense      | (25)  | (30)  | (35)  | (40)  | (45)
Adjusted UFCF          | $75   | $120  | $165  | $210  | $255
```

---

## 6. Per-Share Value Impact

### Dilution Impact on Valuation

```
                           | Basic  | Diluted | Impact
----------------------------------------------------
Equity Value ($M)          | $2,000 | $2,000  | -
÷ Shares Outstanding       | 100.0  | 113.95  | +13.95%
= Per Share Value          | $20.00 | $17.55  | -12.2%
----------------------------------------------------
Current Share Price        | $15.00 | $15.00  |
Implied Upside             | 33.3%  | 17.0%   | -16.3 ppt
```

**Key Insight:** Using basic shares overstates per-share value.

### Dilution Percentage Formula

```
Dilution % = (Fully Diluted - Basic) / Basic × 100
```

---

## 7. Diluted_Shares Tab Structure

### Required Sections

**Section A: Basic Shares**
```
Basic Shares Outstanding         | XX.X M | Source: 10-Q Cover [Date]
```

**Section B: RSUs (1-for-1)**
```
Unvested RSUs Outstanding        | X.X M  | Source: 10-K Note X
Dilutive Shares from RSUs        | X.X M  |
```

**Section C: Options (TSM)**
```
Options Outstanding              | X.X M  |
  Tranche 1 (Strike $XX)         | X.X M  | In-Money: Yes/No
  Tranche 2 (Strike $XX)         | X.X M  | In-Money: Yes/No
Weighted Avg Strike Price        | $XX.XX |
Current Share Price              | $XX.XX |
Option Proceeds                  | $XX.X M|
Shares Repurchased               | X.X M  |
Net New Shares from Options      | X.X M  |
```

**Section D: Warrants (TSM)**
```
Warrants Outstanding             | X.X M  |
Weighted Avg Strike Price        | $XX.XX |
Shares Repurchased               | X.X M  |
Net New Shares from Warrants     | X.X M  |
```

**Section E: Convertibles (If-Converted)**
```
Convertible Principal            | $XX.X M|
Conversion Price                 | $XX.XX |
In-the-Money Test                | Yes/No |
Dilutive Shares from Converts    | X.X M  |
Treatment in EV                  | Equity/Debt |
```

**Section F: PSUs (Probability-Weighted)**
```
PSUs Outstanding                 | X.X M  |
Probability of Achievement       | XX%    |
Expected Shares from PSUs        | X.X M  |
```

**Section G: Dilution Summary**
```
Basic Shares Outstanding         | XX.X M |
+ RSUs                          | X.X M  |
+ Net Options (TSM)             | X.X M  |
+ Net Warrants (TSM)            | X.X M  |
+ Convertibles (If-Converted)   | X.X M  |
+ PSUs (Probability-Weighted)   | X.X M  |
= FULLY DILUTED SHARES          | XX.X M |

Dilution %                       | XX.X%  |
```

**Section H: SBC-Adjusted FCF**
```
($ millions)    | FY26E | FY27E | FY28E | FY29E | FY30E
------------------------------------------------------
Unlevered FCF   | $XXX  | $XXX  | $XXX  | $XXX  | $XXX
SBC Expense     | ($XX) | ($XX) | ($XX) | ($XX) | ($XX)
Adjusted UFCF   | $XXX  | $XXX  | $XXX  | $XXX  | $XXX
```

**Section I: Per-Share Impact**
```
                        | Basic  | Diluted | Impact
--------------------------------------------------
Equity Value ($M)       | $X,XXX | $X,XXX  | -
÷ Shares               | XX.X M | XX.X M  | +XX.X%
= Value per Share      | $XX.XX | $XX.XX  | -XX.X%
--------------------------------------------------
Current Price          | $XX.XX |
Upside (Basic)         | XX.X%  |
Upside (Diluted)       | XX.X%  | -XX.X ppt |
```

---

## 8. Semiconductor-Specific Considerations

### Typical Dilution Ranges by Company Type

| Company Type | Typical Dilution % | SBC % of Rev |
|--------------|-------------------|--------------|
| Equipment | 3-6% | 3-5% |
| Memory | 2-5% | 2-4% |
| Foundry | 2-4% | 2-3% |
| Fabless (mature) | 5-10% | 8-12% |
| Fabless (growth) | 10-20% | 15-25% |

### Semi-Specific Dilution Sources

1. **Equity Offerings**
   - Common for fabless companies needing R&D capital
   - Model future dilution if capital raise expected

2. **At-the-Market (ATM) Facilities**
   - Check for authorized but unissued ATM capacity
   - Common for smaller semi companies

3. **Acquisition-Related Equity**
   - Semi industry has active M&A
   - Stock deals create dilution

4. **Employee Stock Purchase Plans (ESPP)**
   - Usually minor (1-2% annually)
   - Often ignored in models

### Semi Company Examples

| Company | Typical SBC% | Dilution Profile |
|---------|--------------|------------------|
| ASML | 1-2% | Low dilution, stable |
| Nvidia | 12-15% | High SBC, significant |
| AMD | 8-12% | Moderate-high |
| Micron | 3-5% | Low-moderate |
| TSMC | 2-3% | Low dilution |
| Intel | 4-6% | Moderate |

### Red Flags

| Warning Sign | Interpretation |
|--------------|----------------|
| SBC > 20% of OpIncome | Excessive dilution |
| Dilution % > 15% | High option overhang |
| Convertible near in-money | Watch for conversion |
| Rising SBC% of revenue | Compensation inflation |

---

## Key Formulas Summary

### Treasury Stock Method
```
Net New Shares = Options × (1 - Strike Price / Current Price)
```

### If-Converted Method
```
Dilutive Shares = Principal Amount ÷ Conversion Price
```

### Dilution Percentage
```
Dilution % = (Fully Diluted - Basic) / Basic × 100
```

### SBC-Adjusted FCF
```
Adjusted UFCF = Unlevered FCF - Stock-Based Compensation Expense
```

### Per-Share Impact
```
Value per Diluted Share = Equity Value ÷ Fully Diluted Shares
```

---

## Quality Checklist

Before finalizing dilution analysis:

- [ ] Basic shares from most recent 10-K/10-Q cover page
- [ ] All RSUs included 1-for-1
- [ ] Options calculated using TSM (only in-the-money)
- [ ] Warrants calculated using TSM (only in-the-money)
- [ ] Convertibles tested for in-the-money status
- [ ] Convertibles removed from debt if in-the-money
- [ ] PSUs probability-weighted (or excluded with note)
- [ ] SBC projection included for FCF adjustment
- [ ] All sources documented
- [ ] Dilution bridge reconciles to fully diluted count
- [ ] Per-share value shown at both basic and diluted
