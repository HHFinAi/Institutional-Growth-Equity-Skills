# Memory Company Valuation Reference

## Table of Contents
1. SOTP Methodology
2. P/BV Cross-Check
3. Bit Shipment & ASP Modeling
4. Learning Curve Application
5. Competitive Dynamics
6. Company-Specific Parameters

---

## 1. SOTP Methodology

### Segment the Business

| Segment | Description | Multiple |
|---------|-------------|----------|
| Commodity DRAM | DDR4/DDR5 for PC, server, mobile | 2-3x P/S |
| HBM | High Bandwidth Memory for AI | 5-7x P/S |
| NAND | Flash storage | 1-2x P/S |
| Enterprise SSD | Value-add storage | 2-3x P/S |

### SOTP Calculation Example (Micron)

| Segment | Revenue | Multiple | Value |
|---------|---------|----------|-------|
| Core DRAM+NAND | $32B | 3.0x | $96B |
| HBM | $12B | 6.0x | $72B |
| **Total EV** | | | **$168B** |
| - Net Debt | | | ($5B) |
| **Equity Value** | | | **$163B** |
| ÷ Shares | | | 1.1B |
| **Per Share** | | | **$148** |

---

## 2. P/BV Cross-Check

### Justified P/BV Formula
```
Justified P/BV = Long-Term ROE / Cost of Equity
```

### Example (SK Hynix)

| Input | Value |
|-------|-------|
| LT ROE | 34.3% |
| CoE | 11.5% |
| Justified P/BV | 3.0x |

### P/BV by Cycle Position

| Cycle Position | P/BV Range |
|----------------|------------|
| Trough | 0.8-1.5x |
| Mid-cycle | 1.5-2.5x |
| Peak | 2.5-3.5x |
| Super-cycle (HBM) | 3.0-4.0x |

---

## 3. Bit Shipment & ASP Modeling

### DRAM Demand by End Market

| End Market | % of Demand | Growth Driver |
|------------|-------------|---------------|
| Server/DC | 35-40% | AI, cloud |
| Mobile | 30-35% | Unit + content |
| PC | 15-20% | Replacement cycle |
| Consumer | 5-10% | Gaming, devices |

### HBM Revenue Model
```
HBM Revenue = AI Accelerator Units × HBM per Unit × HBM ASP

Example:
- Nvidia H100 equivalents: 3M units
- HBM per unit: 80GB average
- ASP: $15/GB
- HBM Revenue: 3M × 80 × $15 = $3.6B
```

### NAND Demand by End Market

| End Market | % of Demand | Growth Driver |
|------------|-------------|---------------|
| Enterprise SSD | 30-35% | Data center |
| Client SSD | 25-30% | PC storage |
| Mobile | 25-30% | Content/phone |
| Consumer | 10-15% | USB, cards |

---

## 4. Learning Curve Application

### Core Principle
Revenue (cost) per transistor declines ~30% per year on learning curve (Dr. Rhines).

### ASP Position Analysis

| Position vs Curve | Indicator | Forecast |
|-------------------|-----------|----------|
| **Above** (shortage) | ASP near 3Q18 peak | Model peak then decline |
| **On curve** (balanced) | Stable spot-contract | Trend decline 20-30%/yr |
| **Below** (glut) | Falling spot | Model bottom then recovery |

### Current Context (HBM Era)
- HBM demand consuming DDR capacity
- DDR undersupply persists
- ASPs approaching 3Q18 peak levels
- Expected duration: through 1Q27 for DDR

---

## 5. Competitive Dynamics

### DRAM Market Structure (Oligopoly)

| Company | Share | HBM Position |
|---------|-------|--------------|
| Samsung | ~40% | #2, catching up |
| SK Hynix | ~30% | #1, 56% share |
| Micron | ~25% | #3, ramping |
| CXMT (China) | ~5% | Minimal |

### Why Oligopoly Matters
- 3 players with 95%+ combined share
- More rational capacity additions
- Reduced price wars
- Structurally higher margins
- Apply premium to historical multiples

### HBM Leadership

| Metric | SK Hynix | Samsung | Micron |
|--------|----------|---------|--------|
| HBM3E production | First | Ramping | Ramping |
| Nvidia allocation | Primary | Secondary | Growing |
| 2026e HBM share | ~55% | ~30% | ~15% |

---

## 6. Company-Specific Parameters

### Micron

| Parameter | Value | Notes |
|-----------|-------|-------|
| Core P/S | 2-3x | DDR + NAND |
| HBM P/S | 5-7x | AI premium |
| Target P/BV | 2.0-2.5x | LT ROE 15-20% |
| CoE | 11-12% | Semi beta |

### SK Hynix

| Parameter | Value | Notes |
|-----------|-------|-------|
| Target P/BV | 2.5-3.5x | HBM leader |
| LT ROE | 25-35% | HBM-driven |
| CoE | 11-12% | Korea + semi |
| HBM Share | ~55% | Market leader |

### Samsung Memory

| Parameter | Value | Notes |
|-----------|-------|-------|
| Target P/BV | 1.5-2.5x | Diversified |
| LT ROE | 15-25% | Lower vs Hynix |
| CoE | 10-11% | Lower beta |

---

## Margin Analysis

### Historical Range

| Cycle Position | DRAM OpMargin | NAND OpMargin |
|----------------|---------------|---------------|
| Trough | -10% to +10% | -20% to 0% |
| Mid-cycle | 25-40% | 15-30% |
| Peak | 50-65% | 35-45% |
| Current (HBM) | 65-77% | 35-42% |

### Segment Margins

| Segment | Steady-State Margin |
|---------|---------------------|
| Commodity DDR | 35-45% |
| HBM | 60-70% |
| NAND | 25-35% |
| Enterprise SSD | 30-40% |

---

## Scenario Analysis

### Bull Case (+30-40% upside)
- HBM demand exceeds expectations
- DDR pricing remains above curve
- China DRAM uncompetitive
- Capex discipline maintained
- Multiple: P/BV 3.5-4.0x or P/S 4x core + 8x HBM

### Base Case
- HBM per model assumptions
- DDR pricing mean-reverts
- Normal capacity additions
- Multiple: P/BV 2.5-3.0x or P/S 3x core + 6x HBM

### Bear Case (-30-40% downside)
- AI capex slowdown
- DDR oversupply develops
- China DRAM competitive
- Price war resumes
- Multiple: P/BV 1.5-2.0x or P/S 2x core + 4x HBM

---

## Red Flags

| Warning Sign | Interpretation |
|--------------|----------------|
| Spot prices falling | Demand weakening |
| Customer inventory rising | Demand pullback |
| Capacity additions accelerating | Future oversupply |
| HBM competitor gaining share | Premium at risk |
| China DRAM improving | Long-term margin pressure |
