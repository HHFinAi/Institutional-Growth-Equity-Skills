# Quick Reference Guide

## Valuation Method Matrix

| Company Type | Method | Metric | Examples |
|--------------|--------|--------|----------|
| Equipment | Cycle-Peak P/E | 25-35x peak EPS | ASML, LAM, AMAT |
| Memory | SOTP + P/BV | 3x core + 6x HBM | Micron, SK Hynix |
| Foundry | Residual Income | CoE 9-11%, g 4-5% | TSMC |
| Fabless | Forward P/E | 20-50x | Nvidia, AMD |

---

## Share Dilution Quick Reference

### TSM Formula (Options/Warrants)
```
Net New Shares = Options × (1 - Strike / Current Price)
```

### If-Converted Formula (Convertibles)
```
Dilutive Shares = Principal ÷ Conversion Price
```

### Typical Dilution by Company Type

| Type | Dilution % | SBC % Rev |
|------|------------|-----------|
| Equipment | 3-6% | 3-5% |
| Memory | 2-5% | 2-4% |
| Foundry | 2-4% | 2-3% |
| Fabless (mature) | 5-10% | 8-12% |
| Fabless (growth) | 10-20% | 15-25% |

### SBC-Adjusted FCF
```
Adjusted UFCF = UFCF - SBC Expense
```

---

## Industry Constants (Rhines)

| Constant | Value |
|----------|-------|
| Learning curve decline | ~30%/year |
| Revenue / silicon area | ~$70/sq.in |
| R&D % of semi revenue | ~14% |
| EDA % of semi revenue | ~2% |
| Revenue vs profit correlation | 0.07 |

---

## Cycle Position Checklist

### At Trough (Buy Signal)
- [ ] Memory spot below learning curve
- [ ] Equipment P/E at 50-60x
- [ ] Fab utilization <70%
- [ ] Customer capex being cut
- [ ] Inventory days elevated (60+)

### At Peak (Sell Signal)
- [ ] Memory spot above learning curve
- [ ] Equipment P/E at 25-30x
- [ ] Fab utilization >90%
- [ ] Customer capex aggressive
- [ ] Inventory days low (<35)

---

## Equipment Multiples (Peak)

| Company | P/E | Notes |
|---------|-----|-------|
| ASML | 30-35x | EUV monopoly |
| KLA | 30-32x | Highest margins |
| LAM | 28-30x | Memory exposure |
| AMAT | 26-28x | Diversified |

---

## Memory Multiples

| Segment | P/S | P/BV |
|---------|-----|------|
| Core DDR | 2-3x | 1.5-2.5x |
| HBM | 5-7x | 3.0-3.5x |
| NAND | 1-2x | 1.0-2.0x |

---

## Foundry RIM Parameters

| Parameter | TSMC | GF | UMC |
|-----------|------|-----|-----|
| CoE | 9.2% | 11.5% | 10.5% |
| Terminal g | 4.5% | 2.5% | 2.5% |
| Terminal ROE | 20% | 13% | 11% |

---

## Fabless P/E

| Company | P/E | Growth |
|---------|-----|--------|
| Nvidia | 35-50x | Hyper |
| AMD | 25-35x | High |
| Broadcom | 18-25x | Moderate |
| Qualcomm | 12-18x | Mature |

---

## GPM% Hierarchy

| Rank | Segment | GPM% |
|------|---------|------|
| 1 | FPGAs | 65-70% |
| 2 | Analog | 55-65% |
| 3 | MPUs | 50-60% |
| 4 | Fabless | 45-55% |
| 5 | Memory | 25-45% |
| 6 | Discrete | 20-35% |

---

## China Risk Premiums

| Exposure | Base Impact | Escalation |
|----------|-------------|------------|
| >30% | -5% rev, -1x | -20% rev, -3x |
| 15-30% | -3% rev | -10% rev, -2x |
| <15% | Minimal | Minimal |

---

## Taiwan Risk Discount

| Scenario | Probability | Discount |
|----------|-------------|----------|
| Status quo | 70% | 0% |
| Elevated | 20% | 10-15% |
| Blockade | 7% | 30-40% |
| Conflict | 3% | 50%+ |

---

## 10-K Red Flags

| Metric | Warning |
|--------|---------|
| Inventory days | +50% YoY |
| AR vs Revenue | AR > Rev growth |
| Capex vs D&A | Capex < D&A |
| R&D % | Declining |
| Top 3 customers | >60% |

---

## Chokepoint Map

| Chokepoint | Leader | Share |
|------------|--------|-------|
| EUV | ASML | ~100% |
| Advanced foundry | TSMC | ~90% |
| EDA | Syn/Cad/Sie | ~85% |
| HBM | SK Hynix/Samsung | ~95% |
| x86 | Intel/AMD | ~95% |

---

## Data Sources

| Source | Data | Freq |
|--------|------|------|
| DRAMeXchange | Memory prices | Weekly |
| SEMI | Equipment billings | Monthly |
| TSMC | Monthly revenue | Monthly |
| Company filings | Guidance | Quarterly |

---

## Model Checklist

- [ ] Cycle position documented
- [ ] Appropriate methodology
- [ ] **Diluted shares (TSM/If-Converted)**
- [ ] **SBC-adjusted FCF**
- [ ] **Per-share at basic AND diluted**
- [ ] China/Taiwan risk modeled
- [ ] Learning curve for ASP
- [ ] Sensitivity tables
- [ ] Bull/Base/Bear scenarios
- [ ] All assumptions sourced
