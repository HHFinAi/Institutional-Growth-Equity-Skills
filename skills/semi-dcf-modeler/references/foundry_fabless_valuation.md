# Foundry & Fabless Valuation Reference

## Table of Contents
1. Foundry: Residual Income Model
2. TSMC Valuation Framework
3. Fabless: Forward P/E Methodology
4. TAM Analysis Framework
5. Moat Assessment
6. Company-Specific Parameters

---

## 1. Foundry: Residual Income Model

### Why RIM for Foundries
- High PP&E, significant book value
- ROE spread from technology leadership
- Fading ROE as nodes mature
- Clear terminal value framework

### RIM Formula
```
Equity Value = Book Value + Σ PV(Residual Income) + PV(Terminal Value)

Where:
Residual Income = (ROE - CoE) × Beginning Equity
Terminal Value = Final Year RI × (1 + g) / (CoE - g)
```

---

## 2. TSMC Valuation Framework

### RIM Input Parameters

| Parameter | Base | Bull | Bear |
|-----------|------|------|------|
| Cost of Equity | 9.2% | 8.5% | 10.5% |
| Risk-free rate | 2.0% | 2.0% | 2.5% |
| Beta | 1.2 | 1.1 | 1.3 |
| Equity risk premium | 6.0% | 5.5% | 6.5% |
| Terminal growth | 4.0% | 5.0% | 3.0% |

### ROE Fade Assumptions

| Year | ROE | ROE Spread (vs 9.2% CoE) |
|------|-----|--------------------------|
| 2026e | 38.0% | 28.8% |
| 2027e | 35.0% | 25.8% |
| 2028e | 31.2% | 22.0% |
| 2029e | 28.2% | 19.0% |
| 2030e | 26.2% | 17.0% |
| Terminal | 20.0% | 10.8% |

### Capacity Model

| Node | Utilization | GM% |
|------|-------------|-----|
| N3/N3E | 85-90% | 55-60% |
| N5/N4 | 80-85% | 50-55% |
| N7/N6 | 75-80% | 45-50% |
| Mature | 85%+ | 40-45% |

### Customer Concentration

| Customer | % Revenue | Risk |
|----------|-----------|------|
| Apple | ~25% | High single-customer |
| Nvidia | ~10% | AI-driven growth |
| AMD | ~8% | Growing share |
| Qualcomm | ~7% | Stable |
| Other | ~50% | Diversified |

### Geopolitical Risk Discount

| Scenario | Probability | Discount |
|----------|-------------|----------|
| Status quo | 70% | 0% |
| Elevated tensions | 20% | 10-15% |
| Blockade | 7% | 30-40% |
| Conflict | 3% | 50%+ |

**Expected Discount Calculation:**
```
= 0.70×0 + 0.20×0.125 + 0.07×0.35 + 0.03×0.50 = ~6-8%
```

---

## 3. Fabless: Forward P/E Methodology

### Growth Phase Framework

| Phase | Growth Rate | Multiple |
|-------|-------------|----------|
| Hyper-growth | >40% | 40-60x fwd P/E |
| High growth | 20-40% | 25-40x fwd P/E |
| Growth | 10-20% | 18-28x fwd P/E |
| Mature | <10% | 12-20x fwd P/E |

### Typical Fabless Margins

| Company Type | GM% | OpMargin% |
|--------------|-----|-----------|
| AI/GPU leader | 70-75% | 55-65% |
| CPU | 50-55% | 20-30% |
| Diversified | 60-70% | 35-50% |
| Mobile | 55-60% | 25-35% |

---

## 4. TAM Analysis Framework

### TAM Build-Up
```
TAM = Σ (Segment TAM × Company Addressability)
```

### Example (Nvidia)
| Segment | TAM | Addressable |
|---------|-----|-------------|
| Data Center AI | $100B | $80B (80%) |
| Gaming GPU | $25B | $19B (75%) |
| Auto AI | $15B | $5B (30%) |
| Pro Viz | $5B | $3B (60%) |
| **Total** | | **$107B** |

### Market Share Trajectory

| Company | Current | 5-Year Target |
|---------|---------|---------------|
| Nvidia (DC AI) | 80% | 70-75% |
| AMD (Server CPU) | 25% | 35-40% |
| Qualcomm (Mobile) | 30% | 28-32% |

---

## 5. Moat Assessment

### Scoring Framework

| Factor | Weight |
|--------|--------|
| Architecture lock-in | 25% |
| Ecosystem/software | 25% |
| Technology leadership | 20% |
| Scale advantages | 15% |
| Switching costs | 15% |

### Company Scores (1-5 scale)

| Company | Arch | Eco | Tech | Scale | Switch | **Overall** |
|---------|------|-----|------|-------|--------|-------------|
| Nvidia | 5 | 5 | 5 | 4 | 5 | **4.8** |
| AMD | 3 | 3 | 4 | 3 | 3 | **3.2** |
| Qualcomm | 4 | 4 | 4 | 4 | 3 | **3.8** |
| Broadcom | 3 | 3 | 4 | 5 | 4 | **3.8** |

### Moat → Multiple Premium

| Score | Premium vs Peers |
|-------|------------------|
| 4.5-5.0 | +30-50% |
| 3.5-4.4 | +10-25% |
| 2.5-3.4 | In-line |
| <2.5 | Discount |

---

## 6. Company-Specific Parameters

### TSMC

| Parameter | Value | Notes |
|-----------|-------|-------|
| CoE | 9.2% | Taiwan premium |
| Terminal g | 4.5% | Above GDP |
| Terminal ROE | 20% | Fade target |
| Geo Risk Discount | 6-8% | Probability-weighted |

### GlobalFoundries

| Parameter | Value | Notes |
|-----------|-------|-------|
| CoE | 11.5% | Higher risk |
| Terminal g | 2.5% | Mature focus |
| Terminal ROE | 13% | Lower margin |
| Geo Risk | Low | US/Singapore |

### UMC

| Parameter | Value | Notes |
|-----------|-------|-------|
| CoE | 10.5% | Taiwan exposure |
| Terminal g | 2.5% | Mature nodes |
| Terminal ROE | 11% | Commodity |
| Geo Risk | Medium | Taiwan-based |

### Nvidia

| Parameter | Value | Notes |
|-----------|-------|-------|
| Forward P/E | 35-50x | AI dominance |
| GM Target | 70-75% | Strong pricing |
| Moat Score | 4.8 | CUDA ecosystem |
| TSMC Dependency | 100% | High risk |

### AMD

| Parameter | Value | Notes |
|-----------|-------|-------|
| Forward P/E | 25-35x | Share gains |
| GM Target | 50-55% | Improving |
| Moat Score | 3.2 | ROCm developing |
| TSMC Dependency | 100% | High risk |

### Qualcomm

| Parameter | Value | Notes |
|-----------|-------|-------|
| Forward P/E | 12-18x | Mobile mature |
| GM Target | 55-60% | Licensing boost |
| Moat Score | 3.8 | Patent portfolio |
| Diversification | Growing | Auto, IoT |

### Broadcom

| Parameter | Value | Notes |
|-----------|-------|-------|
| Forward P/E | 18-25x | Diversified |
| GM Target | 65-70% | High quality |
| M&A Strategy | Active | Value creation |
| AI Exposure | Growing | Custom silicon |

---

## TSMC Dependency Risk

### Risk by Company

| Company | TSMC % | Risk Premium |
|---------|--------|--------------|
| Apple | 100% | 10-15% |
| Nvidia | 100% | 12-18% |
| AMD | 100% | 10-15% |
| Qualcomm | ~90% | 8-12% |
| Broadcom | ~70% | 5-10% |

### Risk-Adjusted Value
```
Risk-Adj Value = Base Value × (1 - TSMC Premium × Geo Probability)

Example (Nvidia):
Base: $150, Premium: 15%, Geo Prob: 30%
Discount: 15% × 30% = 4.5%
Adjusted: $150 × 0.955 = $143
```

---

## Scenario Analysis

### Foundry (TSMC)

| Scenario | Drivers | Adjustment |
|----------|---------|------------|
| Bull | Capacity tight, N2 ramps, Arizona success | +20% |
| Base | Per guidance | Base case |
| Bear | Utilization drops, customer diversifies | -20% |

### Fabless (Nvidia)

| Scenario | Drivers | Adjustment |
|----------|---------|------------|
| Bull | AI TAM exceeds, share holds | +30-40% |
| Base | TAM per forecast, modest share loss | Base case |
| Bear | AI spending pause, AMD/custom gains | -30-40% |

---

## Red Flags

### Foundry
- Utilization declining
- Customer concentration worsening
- Capex cuts
- Technology delays

### Fabless
- Market share loss
- Gross margin compression
- Design win losses
- Customer DIY (custom silicon)
