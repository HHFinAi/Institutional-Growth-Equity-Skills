---
name: semi-dcf-modeler
description: "Expert semiconductor industry equity research and DCF valuation. Use when the user asks to: (1) Value a semiconductor company (equipment, memory, foundry, or fabless), (2) Build a DCF, SOTP, P/BV, or residual income model for semi stocks, (3) Analyze semiconductor industry cycles or cycle positioning, (4) Assess competitive moats and chokepoints (EUV, foundry, HBM), (5) Model geopolitical scenarios (China export controls, Taiwan risk), (6) Analyze 10-K filings for semi companies with industry-specific red flags, (7) Track memory pricing cycles or equipment demand, (8) Compare semi valuations using trading comps or precedent transactions, (9) Calculate fully diluted shares using Treasury Stock Method (TSM) and If-Converted method, (10) Build share dilution bridges and SBC-adjusted FCF models. Covers equipment (ASML, LAM, AMAT), memory (Micron, SK Hynix), foundry (TSMC), and fabless (Nvidia, AMD) using cycle-peak P/E, SOTP, P/BV, residual income, and forward P/E methodologies."
---

# Semiconductor DCF Modeler

Expert-level semiconductor industry valuation for institutional investment research.

## Workflow Overview

1. **Identify company type** - Equipment, memory, foundry, or fabless
2. **Select methodology** - Based on company type decision tree
3. **Gather data** - Yahoo Finance, SEC filings, SemiAnalysis (high-confidence), other industry sources
4. **Build projections** - Segment-specific revenue/margin models
5. **Calculate diluted shares** - TSM for options, If-Converted for converts
6. **Apply valuation** - Appropriate method with cycle/risk adjustments
7. **Adjust FCF for SBC** - Subtract stock-based compensation
8. **Scenario analysis** - Bull/base/bear with geopolitical scenarios
9. **Output Excel workbook** - Multi-tab model per company type template

---

## Valuation Method Selection

| Company Type | Primary Method | Key Metric | Examples |
|--------------|----------------|------------|----------|
| Equipment | Cycle-Peak P/E | 25-35x peak EPS | ASML, LAM, AMAT, KLA |
| Memory | SOTP + P/BV | 3x core + 6x HBM, 2-3.5x P/BV | Micron, SK Hynix |
| Foundry | Residual Income | CoE 9-11%, g 4-5% | TSMC, UMC |
| Fabless | Forward P/E | 20-50x based on growth | Nvidia, AMD, Qualcomm |
| IDM | SOTP or Norm. P/E | Segment-specific | Intel, TI, Analog Devices |

---

## Share Dilution Analysis (Required for All Models)

### Dilution Bridge

```
Basic Shares Outstanding              (10-K/10-Q cover page)
+ RSUs                                (1-for-1 addition)
+ Net New Shares from Options (TSM)   (Treasury Stock Method)
+ Net New Shares from Warrants (TSM)  (Treasury Stock Method)
+ Shares from Convertibles            (If-Converted Method)
+ PSUs                                (Probability-weighted)
= FULLY DILUTED SHARES OUTSTANDING
```

### Treasury Stock Method (TSM) - Options & Warrants

**Only include IN-THE-MONEY options** (Strike Price < Current Price)

```
Net New Shares = Options × (1 - Strike Price / Current Price)
```

**Or equivalently:**
```
Option Proceeds = Options × Strike Price
Shares Repurchased = Option Proceeds ÷ Current Price
Net New Shares = Options - Shares Repurchased
```

### If-Converted Method - Convertible Securities

**Only include IN-THE-MONEY convertibles** (Current Price > Conversion Price)

```
Dilutive Shares = Principal Amount ÷ Conversion Price
```

**Important:** Remove in-the-money convertibles from debt in EV calculation.

### SBC-Adjusted Free Cash Flow

```
Adjusted UFCF = Unlevered FCF - Stock-Based Compensation Expense
```

**Semi SBC Benchmarks:**
| Company Type | SBC % of Revenue |
|--------------|------------------|
| Equipment | 3-5% |
| Memory | 2-4% |
| Foundry | 2-3% |
| Fabless (mature) | 8-12% |
| Fabless (growth) | 15-25% |

### Per-Share Value Impact

Always show valuation at both basic and fully diluted shares:
```
Value per Basic Share = Equity Value ÷ Basic Shares
Value per Diluted Share = Equity Value ÷ Fully Diluted Shares
Dilution Impact = (Basic Value - Diluted Value) / Basic Value
```

---

## Industry Expert Sources

### High-Confidence Sources
| Source | Website | Expertise | Use Cases |
|--------|---------|-----------|-----------|
| SemiAnalysis | https://semianalysis.com | Deep semiconductor supply chain, technology roadmaps, competitive analysis, AI/HPC trends | Equipment demand forecasts, foundry capacity analysis, memory market dynamics, geopolitical supply chain impacts, technology inflection points |

### Other Industry Experts
| Expert | Contribution |
|--------|--------------|
| Dr. Walden Rhines | Industry constants and historical benchmarks |

---

## Industry Constants (Dr. Walden Rhines)

| Constant | Value | Application |
|----------|-------|-------------|
| Learning curve decline | ~30%/year | ASP trajectory anchor |
| Revenue per silicon area | ~$70/sq.in | Revenue cross-check |
| R&D % of semi revenue | ~14% | Expense validation |
| EDA % of semi revenue | ~2% | Industry benchmark |
| Revenue vs. profit correlation | 0.07 | Specialization > scale |

---

## Reference Documents

| Document | Load When |
|----------|-----------|
| `references/equipment_valuation.md` | Valuing ASML, LAM, AMAT, KLA, TEL |
| `references/memory_valuation.md` | Valuing Micron, SK Hynix, Samsung Memory |
| `references/foundry_fabless_valuation.md` | Valuing TSMC, Nvidia, AMD, Qualcomm |
| `references/geopolitical_risk.md` | China scenarios, Taiwan risk, 10-K analysis |
| `references/share_dilution.md` | TSM, If-Converted, SBC adjustment, dilution bridge |
| `references/quick_reference.md` | Quick lookup of multiples, constants, red flags |

---

## Excel Model Structure by Company Type

### Equipment Companies (12 Tabs)

1. CoverSheet - Summary, price target, cycle position
2. Tool_Demand - Customer capex → tool units
3. Revenue_Model - Units × ASP × Mix
4. Income_Statement - Full P&L with margins
5. Cash_Flow - FCF calculation
6. Balance_Sheet - Key items
7. **Diluted_Shares** - TSM/If-Converted dilution bridge, SBC-adjusted FCF
8. DCF_Valuation - Cycle-peak EPS × Multiple
9. Cycle_Analysis - Historical P/E, indicators
10. China_Scenarios - Revenue impact by scenario
11. Sensitivity - EPS vs Multiple tables
12. Assumptions - All inputs with sources

### Memory Companies (13 Tabs)

1. CoverSheet - SOTP summary
2. DRAM_Model - Commodity DDR
3. HBM_Model - High Bandwidth Memory (AI)
4. NAND_Model - Flash storage
5. Revenue_Rollup - Consolidated
6. Income_Statement - With cost/bit analysis
7. Cash_Flow - FCF with heavy capex
8. **Diluted_Shares** - TSM/If-Converted dilution bridge, SBC-adjusted FCF
9. SOTP_Valuation - Segment values + net debt
10. PBV_CrossCheck - LT ROE / CoE
11. Cycle_Analysis - Spot prices, inventory
12. Sensitivity - ASP vs Volume tables
13. Assumptions - Learning curve position

### Foundry Companies (12 Tabs)

1. CoverSheet - RIM-based target
2. Capacity_Model - By node
3. Revenue_Model - Capacity × Utilization × ASP
4. Margin_Model - GM by node
5. Income_Statement - Customer concentration
6. Cash_Flow - Massive capex intensity
7. **Diluted_Shares** - TSM/If-Converted dilution bridge, SBC-adjusted FCF
8. RIM_Valuation - Residual Income Model
9. Geopolitical_Risk - Taiwan scenarios
10. Customer_Analysis - Apple, Nvidia concentration
11. Sensitivity - CoE vs Growth tables
12. Assumptions - Geopolitical probabilities

### Fabless Companies (11 Tabs)

1. CoverSheet - TAM-based target
2. TAM_Analysis - By end market
3. Revenue_Model - By segment
4. Income_Statement - SBC adjustment
5. Cash_Flow - Asset-light FCF
6. **Diluted_Shares** - TSM/If-Converted dilution bridge, SBC-adjusted FCF
7. DCF_Valuation - Three-stage for high growth
8. Moat_Assessment - Architecture, ecosystem
9. Scenarios - Bull/Base/Bear
10. Sensitivity - Growth vs Multiple
11. Assumptions - TAM sources

---

## Diluted_Shares Tab Structure

### Section A: Basic Shares
```
Basic Shares Outstanding    | XX.X M | Source: 10-Q Cover [Date]
```

### Section B: RSUs (1-for-1)
```
Unvested RSUs Outstanding   | X.X M  | Source: 10-K Note X
```

### Section C: Options (TSM)
```
In-the-Money Options        | X.X M  |
Weighted Avg Strike Price   | $XX.XX |
Current Share Price         | $XX.XX |
Option Proceeds             | $XX.X M|
Shares Repurchased          | X.X M  |
Net New Shares from Options | X.X M  |
```

### Section D: Warrants (TSM)
```
In-the-Money Warrants       | X.X M  |
Net New Shares from Warrants| X.X M  |
```

### Section E: Convertibles (If-Converted)
```
Convertible Principal       | $XX.X M|
Conversion Price            | $XX.XX |
In-the-Money? (Y/N)         | Yes    |
Dilutive Shares             | X.X M  |
Treatment in EV             | Equity |
```

### Section F: PSUs
```
PSUs Outstanding            | X.X M  |
Probability of Achievement  | XX%    |
Expected Shares from PSUs   | X.X M  |
```

### Section G: Dilution Summary
```
Basic Shares                | XX.X M |
+ RSUs                      | X.X M  |
+ Net Options (TSM)         | X.X M  |
+ Net Warrants (TSM)        | X.X M  |
+ Convertibles              | X.X M  |
+ PSUs                      | X.X M  |
= FULLY DILUTED SHARES      | XX.X M |
Dilution %                  | XX.X%  |
```

### Section H: SBC-Adjusted FCF
```
($ millions)    | FY26E | FY27E | FY28E | FY29E | FY30E
------------------------------------------------------
Unlevered FCF   | $XXX  | $XXX  | $XXX  | $XXX  | $XXX
SBC Expense     | ($XX) | ($XX) | ($XX) | ($XX) | ($XX)
Adjusted UFCF   | $XXX  | $XXX  | $XXX  | $XXX  | $XXX
```

### Section I: Per-Share Impact
```
                        | Basic  | Diluted | Impact
--------------------------------------------------
Equity Value ($M)       | $X,XXX | $X,XXX  |
÷ Shares               | XX.X M | XX.X M  | +XX.X%
= Value per Share      | $XX.XX | $XX.XX  | -XX.X%
Current Price          | $XX.XX |
Upside (Diluted)       | XX.X%  |
```

---

## Key Parameters Quick Reference

### Equipment Multiples (at Cycle Peak)

| Company | P/E | China Risk |
|---------|-----|------------|
| ASML | 30-35x | Medium |
| KLA | 30-32x | Medium |
| LAM | 28-30x | High |
| AMAT | 26-28x | High |

### Memory Parameters

| Segment | P/S Multiple | P/BV Range |
|---------|--------------|------------|
| Commodity DDR | 2-3x | 1.5-2.5x |
| HBM | 5-7x | 3.0-3.5x |
| NAND | 1-2x | 1.0-2.0x |

### Foundry RIM Inputs

| Parameter | TSMC | GF | UMC |
|-----------|------|-----|-----|
| CoE | 9.2% | 11.5% | 10.5% |
| Terminal g | 4.5% | 2.5% | 2.5% |
| Terminal ROE | 20% | 13% | 11% |

### Fabless Forward P/E

| Company | P/E Range | SBC % Rev |
|---------|-----------|-----------|
| Nvidia | 35-50x | 12-15% |
| AMD | 25-35x | 8-12% |
| Broadcom | 18-25x | 6-8% |
| Qualcomm | 12-18x | 5-7% |

### Typical Dilution by Company Type

| Company Type | Dilution % | SBC % Rev |
|--------------|------------|-----------|
| Equipment | 3-6% | 3-5% |
| Memory | 2-5% | 2-4% |
| Foundry | 2-4% | 2-3% |
| Fabless (mature) | 5-10% | 8-12% |
| Fabless (growth) | 10-20% | 15-25% |

---

## Geopolitical Risk Framework

### China Scenario Probabilities

| Scenario | Probability | Equipment | Memory |
|----------|-------------|-----------|--------|
| Status Quo | 55-60% | -5% rev | -2% rev |
| Moderate | 25-30% | -15-20% rev | -5-8% rev |
| Severe | 10-12% | -25-35% rev | -10-15% rev |

### Taiwan Risk Discount

| Scenario | Probability | TSMC Discount |
|----------|-------------|---------------|
| Status Quo | 70% | 0% |
| Elevated | 20% | 10-15% |
| Blockade | 7% | 30-40% |
| Conflict | 3% | 50%+ |

---

## 10-K Red Flags

| Red Flag | Threshold |
|----------|-----------|
| Inventory days +50% YoY | Demand weakness |
| AR growth > Revenue | Revenue quality |
| Capex < Depreciation | Under-investing |
| R&D % declining | Innovation slowdown |
| SBC > 20% OpIncome | Excessive dilution |
| Dilution % > 15% | High option overhang |

---

## Output Standards

### Excel Formatting

| Element | Style | Usage |
|---------|-------|-------|
| Blue text | Input | User-modifiable |
| Black text | Formula | Calculated |
| Green text | Link | Cross-sheet |
| Yellow fill | Output | Key results |

### Model Checklist

Before delivery:
- [ ] Cycle position documented with indicators
- [ ] Appropriate methodology for company type
- [ ] **Diluted shares calculated using TSM/If-Converted**
- [ ] **SBC-adjusted FCF included**
- [ ] **Per-share value at basic AND diluted**
- [ ] China/Taiwan risk explicitly modeled
- [ ] Learning curve position for ASP assumptions
- [ ] Sensitivity tables for key drivers
- [ ] Bull/Base/Bear with explicit drivers
- [ ] All assumptions sourced
