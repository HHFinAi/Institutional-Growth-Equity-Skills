# Chart Gallery Reference

Visual guide for IB-standard chart types and when to use them.

## Chart Selection Matrix

| Data Type | Comparison | Composition | Distribution | Trend | Relationship |
|-----------|------------|-------------|--------------|-------|--------------|
| Categorical | Horizontal Bar | Donut | - | - | - |
| Time Series | Grouped Bar | Stacked Area | - | Line + Area | - |
| Part-to-Whole | - | Donut, Treemap | - | - | - |
| Flow/Bridge | Waterfall | - | - | - | Sankey |
| Performance | Bullet | - | - | - | - |
| Matrix | Heatmap | - | Heatmap | - | Heatmap |

## Waterfall Chart

**Best For**: Explaining how a starting value becomes an ending value through sequential positive/negative changes.

**Use Cases**:
- Revenue bridges (period to period)
- EBITDA walk (revenue → EBITDA)
- Valuation bridges
- Cash flow reconciliation

**Design Notes**:
- First and last bars are totals (navy)
- Positive changes: green
- Negative changes: red
- Connecting lines show cumulative progression
- Labels inside bars (white text)

## Horizontal Bar Chart

**Best For**: Comparing values across categories, especially with long labels.

**Use Cases**:
- Peer comparison (market cap, revenue)
- Regional breakdown
- Product mix
- Ranking analysis

**Design Notes**:
- Horizontal preferred over vertical for readability
- Highlight top performer with darker color
- Value labels at end of bars
- Sort by value (descending usually)

## Donut Chart

**Best For**: Showing part-to-whole relationships (max 5-6 segments).

**Use Cases**:
- Revenue by segment/region
- Market share
- Portfolio allocation
- Customer mix

**Design Notes**:
- NEVER use pie charts - always donut
- Max 5-6 segments (combine small into "Other")
- Start at 12 o'clock position
- Center label for total
- Percentages inside segments

## Line Chart with Area Fill

**Best For**: Time series trends with emphasis on growth.

**Use Cases**:
- Revenue/earnings progression
- User growth
- Market trends
- Forecast visualization

**Design Notes**:
- Subtle area fill (alpha 0.3)
- Markers at data points
- Value labels above line
- Single line per chart (use small multiples for comparison)

## Bullet Chart

**Best For**: Actual vs. target performance in compact space.

**Use Cases**:
- KPI dashboards
- Sales vs. quota
- Budget vs. actual
- Goal attainment

**Design Notes**:
- Gray ranges show poor/ok/good zones
- Navy bar for actual
- Red marker for target
- Very space-efficient

## Heatmap

**Best For**: Two-dimensional performance or correlation matrices.

**Use Cases**:
- Performance by region × quarter
- Correlation matrices
- Feature comparison
- Risk assessment

**Design Notes**:
- Use diverging colormap (RdYlGn)
- Value labels in cells
- White text on dark cells, black on light
- Grid lines between cells

## Grouped Bar Chart

**Best For**: Comparing multiple series across categories.

**Use Cases**:
- Period-over-period comparison
- Actual vs. plan vs. prior year
- Multiple metrics side-by-side

**Design Notes**:
- Max 3-4 series
- Consistent color across charts
- Legend only if necessary
- Consider small multiples instead

## Chart Combinations

### Financial Summary
- Waterfall (revenue bridge) + Line (trend) + Table (metrics)

### Competitive Landscape
- Horizontal bar (ranking) + Heatmap (capability matrix)

### Performance Dashboard
- Multiple bullet charts + KPI cards + Trend sparklines

### Investment Thesis
- Football field (not in base kit - custom) + Sensitivity table + Donut (risk factors)
