# Geopolitical Risk & 10-K Analysis Reference

## Table of Contents
1. Supply Chain Chokepoints
2. China Risk Framework
3. Taiwan Strait Risk
4. Export Control Analysis
5. 10-K Red Flags for Semiconductors
6. ESG Materiality

---

## 1. Supply Chain Chokepoints

### Critical Single Points of Failure

| Stage | Dominant Player | Share | Risk |
|-------|-----------------|-------|------|
| EUV Lithography | ASML | ~100% | Extreme |
| Advanced Foundry | TSMC | ~90% | Extreme |
| EDA Software | Synopsys/Cadence/Siemens | ~85% | High |
| Advanced Packaging | TSMC, ASE | ~70% | High |
| Silicon Wafers | Shin-Etsu, SUMCO | ~60% | Medium |

### Geographic Concentration

| Region | Capability | Risk |
|--------|------------|------|
| **Taiwan** | Advanced logic, packaging | Extreme |
| **South Korea** | Memory, display | High |
| **Japan** | Materials, equipment | High |
| **Netherlands** | EUV lithography | Extreme |
| **USA** | Design, EDA, some equipment | Moderate |

---

## 2. China Risk Framework

### Scenario Probabilities

| Scenario | Probability | Description |
|----------|-------------|-------------|
| Status Quo | 55-60% | Current controls maintained |
| Moderate Escalation | 25-30% | Expanded entity list |
| Severe Escalation | 10-12% | Near-total embargo |
| Normalization | 3-5% | Relaxation of controls |

### Revenue Impact by Segment

| Scenario | Equipment | Memory | Fabless |
|----------|-----------|--------|---------|
| Status Quo | -5% | -2% | -3% |
| Moderate | -15-20% | -5-8% | -8-12% |
| Severe | -25-35% | -10-15% | -15-25% |

### Multiple Impact

| Scenario | Equipment | Memory | Fabless |
|----------|-----------|--------|---------|
| Status Quo | -1x P/E | Neutral | Neutral |
| Moderate | -2-3x P/E | -0.3x P/BV | -2-3x P/E |
| Severe | -4-5x P/E | -0.5x P/BV | -5-7x P/E |

---

## 3. Taiwan Strait Risk

### Conflict Scenarios

| Scenario | Probability | Economic Impact | Duration |
|----------|-------------|-----------------|----------|
| Status Quo | 70% | None | N/A |
| Elevated Tensions | 20% | Supply premium | Ongoing |
| Blockade | 7% | 30-50% chip disruption | 6-18 mo |
| Invasion | 3% | Near-total disruption | Years |

### Company Exposure

| Company | Taiwan Revenue | TSMC Dependency | Discount |
|---------|----------------|-----------------|----------|
| TSMC | 100% | N/A | 10-20% |
| MediaTek | 100% | Manufacturing | 15-20% |
| Nvidia | Minimal | 100% supply | 10-15% |
| AMD | Minimal | 100% supply | 10-15% |
| Intel | Minimal | Partial | 3-5% |

### Probability-Weighted Discount
```
= P(status quo) × 0%
+ P(elevated) × 12.5%
+ P(blockade) × 35%
+ P(invasion) × 50%

= 0.70×0 + 0.20×0.125 + 0.07×0.35 + 0.03×0.50 = ~6-8%
```

---

## 4. Export Control Analysis

### Current Control Framework

| Control | Target | Impact |
|---------|--------|--------|
| Entity List | Specific Chinese cos | Direct revenue loss |
| FDPR | Chips using US tech | Broad supply impact |
| Advanced Computing | High-end GPUs/AI | Nvidia, AMD restricted |
| Equipment Controls | Sub-14nm equipment | ASML, AMAT, LAM |

### Escalation Levels

| Level | Restrictions | Most Affected |
|-------|--------------|---------------|
| Current | Maintained | All with China exposure |
| Level 2 | Legacy node equipment | AMAT, LAM, TEL |
| Level 3 | All China semi | Equipment, EDA |
| Level 4 | Allied coordination | ASML, TEL |

---

## 5. 10-K Red Flags for Semiconductors

### Revenue Quality

| Red Flag | Threshold | Interpretation |
|----------|-----------|----------------|
| AR growth > Revenue | AR +20% vs Rev +10% | Recognition issues |
| Deferred revenue declining | -10% YoY | Future revenue risk |
| Related party revenue | >5% of total | Quality concern |

### Inventory Analysis

| Red Flag | Threshold | Interpretation |
|----------|-----------|----------------|
| Inventory days +50% YoY | 60→90 days | Demand weakness |
| Inventory reserve declining | -20% | Aggressive accounting |
| Finished goods spiking | +50% YoY | Demand miss |

### Cash Flow Quality

| Red Flag | Threshold | Interpretation |
|----------|-----------|----------------|
| OCF < Net Income | 2+ years | Earnings quality |
| Capex < Depreciation | 2+ years | Under-investing |
| Working capital drain | >20% OCF | Cash conversion |
| SBC > 20% OpIncome | Persistent | Dilution |

### Margin Analysis

| Segment | Healthy GM% | Warning | Critical |
|---------|-------------|---------|----------|
| Equipment | 45-55% | <42% | <38% |
| Memory | 35-50% | <25% | <15% |
| Foundry | 50-55% | <45% | <40% |
| Fabless (GPU) | 65-75% | <60% | <55% |
| Analog | 55-65% | <50% | <45% |

### R&D Productivity

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| R&D % Revenue | 12-18% | <10% | <8% |
| Revenue per R&D $ | Growing | Flat | Declining |
| Design wins | Growing | Flat | Losing |

---

## 6. ESG Materiality

### Environmental (SASB)

| Issue | Materiality | Financial Impact |
|-------|-------------|------------------|
| GHG Emissions | High | Carbon pricing |
| Water Management | Very High | Fab water intensity |
| Hazardous Waste | High | Chemical handling |
| Product Energy | Medium | Customer requirements |

### Water Risk by Region

| Region | Stress | Companies |
|--------|--------|-----------|
| Taiwan | High | TSMC, UMC |
| Arizona | Very High | Intel, TSMC Arizona |
| Texas | High | Samsung, TI, NXP |
| Singapore | Low | GlobalFoundries |

### Social Factors

| Issue | Materiality |
|-------|-------------|
| Supply chain labor | High |
| Conflict minerals | Medium |
| Data privacy | Medium |
| Workforce diversity | Low-Medium |

### Governance

| Issue | Focus |
|-------|-------|
| Board tech expertise | % with semi background |
| Executive compensation | Alignment with LT R&D |
| Related party transactions | China JVs, government |
| Dual-class shares | Founder control |

---

## Risk Score Template

| Category | Weight | Score (1-5) |
|----------|--------|-------------|
| China revenue | 20% | |
| Taiwan/TSMC dependency | 20% | |
| Cycle position | 15% | |
| Customer concentration | 15% | |
| Technology execution | 15% | |
| Financial quality | 15% | |
| **Total** | 100% | |

### Score Interpretation

| Score | Risk Level | CoE Adjustment |
|-------|------------|----------------|
| 1.0-2.0 | Low | Standard |
| 2.0-3.0 | Medium | +100bps |
| 3.0-4.0 | High | +200bps |
| 4.0-5.0 | Very High | +300bps |

---

## Documentation Template

```
GEOPOLITICAL RISK ASSESSMENT
----------------------------
China Revenue: XX%
TSMC Dependency: XX%
Taiwan Exposure: XX%

Scenarios:
- Status Quo (XX%): [impact]
- Escalation (XX%): [impact]
- Severe (XX%): [impact]

Applied Discount: XX%

10-K RED FLAGS
--------------
Inventory Days: [status]
AR vs Revenue: [status]
GM Trend: [status]
R&D Productivity: [status]
Customer Concentration: XX%

Financial Quality: [High/Medium/Low]
Adjustment: [none/premium/discount]
```
