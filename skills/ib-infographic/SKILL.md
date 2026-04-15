---
name: ib-infographic
description: "Create institutional-quality one-page infographics for presenting complex data and insights. Use when the user asks to create an infographic, one-pager, visual summary, data visualization summary, or executive dashboard from financial data, research, or analysis. Supports investment banking professional formatting with detailed charts, metrics, callouts, and key summary insights. Produces polished PNG outputs (with transparency support) or PDF following Goldman/Morgan Stanley/JP Morgan visual standards."
---

# Investment Banking Infographic Skill

Create museum-quality, one-page infographics that distill complex data and analysis into visually compelling summaries following institutional standards.

## When to Trigger

- "Create an infographic from this data"
- "Summarize this analysis as a one-pager"
- "Build a visual executive summary"
- "Turn this into an IB-style infographic"
- "Create a data visualization summary"
- "Make a visual one-pager with key insights"
- "Professional infographic with charts"

## Output Format

**PNG (Recommended)**: Transparent background for easy layering, 1920x1080 (1080p) or 3840x2160 (4K)
**PDF**: For print-ready documents

Generated via Python using `PIL/Pillow` and `matplotlib` with grid-based layout to prevent overlapping.

---

## Workflow

### Step 1: Data Assessment

Before creating, identify:
1. **Primary narrative** – What's the single most important insight?
2. **Supporting data points** – 3-5 key metrics that reinforce the narrative
3. **Comparison dimensions** – Time series, peer comparison, category breakdown
4. **Visual hierarchy** – What should the eye hit first, second, third?

### Step 2: Layout Selection

Choose layout based on data complexity:

| Layout | Best For | Structure |
|--------|----------|-----------|
| Hero Metric | Single dominant insight | Large central KPI + supporting visuals |
| Quadrant | 4 balanced themes | 2x2 grid with central title |
| Flow | Process or timeline | Left-to-right or top-to-bottom progression |
| Dashboard | Multiple KPIs | Grid of cards with unified styling |
| Comparison | A vs B analysis | Split screen with visual contrast |

### Step 3: Visual Component Selection

Select from these IB-standard visualization types:

**Charts (use `matplotlib` with IB styling)**
- Bar charts (horizontal preferred for readability)
- Waterfall charts (for bridge analysis)
- Donut/ring charts (for composition, never pie)
- Line charts (time series with area fill)
- Bullet charts (actual vs target)
- Sparklines (inline trends)
- Heatmaps (correlation or performance matrices)

**Metrics & Callouts**
- Hero numbers (large, bold, with context)
- Delta indicators (▲/▼ with color coding)
- Mini KPI cards (icon + number + label)
- Comparison tables (compact, max 5 rows)

**Visual Elements**
- Section dividers (thin lines, never heavy)
- Icon sets (minimal, geometric)
- Progress bars (for completion/utilization)
- Traffic lights (RAG status)

### Step 4: Apply IB Design Standards

**Typography**
- Headers: Arial Bold 18-24pt
- Subheaders: Arial Bold 12-14pt
- Body/Labels: Arial Regular 9-10pt
- Metrics: Arial Bold 28-48pt (hero numbers)

**Color Palette (Goldman/MS Standard)**
```
Primary Navy:    #1F3864
Secondary Blue:  #2E75B6
Accent Gold:     #C5A572
Positive Green:  #00B050
Negative Red:    #C00000
Neutral Gray:    #7F7F7F
Light Fill:      #E8F1F8
Background:      #FFFFFF
```

**Layout Rules**
- Margins: 0.5" minimum (0.75" preferred)
- Gutters: 0.25" between elements
- White space: 30% minimum (breathing room is premium)
- Alignment: Strict grid, no floating elements
- Balance: Visual weight distributed evenly

**Chart Styling**
- No chart borders or boxes
- Axis lines: light gray (#D0D0D0), thin (0.5pt)
- Grid lines: dotted, very light (#E8E8E8)
- Data labels: inside bars or end-of-line (never legends when avoidable)
- Title: above chart, left-aligned, bold

### Step 5: Key Insight Highlighting

Every infographic MUST include:

1. **Executive Headline** – Single sentence capturing the "so what"
   - Position: Top center, largest text
   - Example: "Revenue Growth Accelerating: +23% YoY Driven by Enterprise Expansion"

2. **Key Takeaways Box** – 3-4 bullet points
   - Position: Top-right or bottom
   - Format: Icon + short phrase (no full sentences)
   - Color: Light background fill (#E8F1F8)

3. **Source & Date Stamp**
   - Position: Bottom-left footer
   - Format: "Source: [source] | Data as of [date]"
   - Size: 8pt, gray (#7F7F7F)

4. **Confidentiality Mark** (optional)
   - Position: Bottom-right or watermark
   - Text: "CONFIDENTIAL" or "DRAFT"

---

## Implementation

### Dependencies

```bash
pip install matplotlib pillow numpy --break-system-packages
```

### Grid-Based Layout System

The canvas uses a 12x12 grid system to **prevent overlapping**:
- Elements snap to grid cells
- Specify `row`, `col`, `row_span`, `col_span` for positioning
- Grid automatically tracks occupied cells
- 60px margins, 24px gutters between elements

### Size Presets

| Preset | Dimensions | Use Case |
|--------|------------|----------|
| `landscape_1080p` | 1920×1080 | Screen presentations, web |
| `landscape_4k` | 3840×2160 | High-res displays |
| `a3_landscape` | 4961×3508 | Print (300 DPI) |
| `letter_landscape` | 3300×2550 | US Letter print (300 DPI) |
| `slide_16_9` | 1920×1080 | Slide decks |

### Core Generation Script

Read: `scripts/generate_infographic.py`

The script provides:
- `InfographicCanvas` class with grid-based layout
- `IBCharts` class with pre-styled matplotlib charts
- `IBColors` class with IB color palette
- PNG transparency support
- Automatic element positioning

### Quick Start Template

```python
from scripts.generate_infographic import InfographicCanvas, IBCharts, IBColors

# Initialize canvas (transparent PNG)
canvas = InfographicCanvas(
    output_path="infographic.png",
    title="Q3 2024 Performance Summary",
    subtitle="Enterprise Division",
    size='landscape_1080p',
    transparent=True  # Set False for white background
)

# Add hero metric (grid position: row 1, col 0, spans 2 rows × 2 cols)
canvas.add_hero_metric(
    value="$847M",
    label="Revenue",
    delta="+23% YoY",
    delta_positive=True,
    row=1, col=0, row_span=2, col_span=2
)

# Add chart (grid position: row 1, col 2, spans 5 rows × 5 cols)
chart = IBCharts.waterfall(
    categories=["Q3'23", "New Logos", "Expansion", "Churn", "Q3'24"],
    values=[680, 120, 85, -38, 847],
    title="Revenue Bridge ($M)",
    transparent=True
)
canvas.add_chart(chart, row=1, col=2, row_span=5, col_span=5)

# Add key takeaways (grid position: row 1, col 10, spans 5 rows × 2 cols)
canvas.add_takeaways([
    "Enterprise logos grew 34% YoY",
    "Net revenue retention at 118%",
    "APAC expansion driving growth"
], row=1, col=10, row_span=5, col_span=2)

# Add data table
canvas.add_table(
    headers=["Metric", "Q3'23", "Q3'24", "Δ"],
    rows=[
        ["Revenue", "$680M", "$847M", "+24.6%"],
        ["Customers", "1,240", "1,662", "+34.0%"],
        ["NRR", "112%", "118%", "+6pp"]
    ],
    row=7, col=0, row_span=4, col_span=5
)

# Add footer
canvas.add_footer("Internal Finance Data", "September 30, 2024", confidential=True)

# Generate
canvas.save()
```

---

## Chart Type Reference

All charts support `transparent=True` for PNG transparency.

### Waterfall Chart
```python
IBCharts.waterfall(
    categories=["Start", "Add1", "Add2", "Sub1", "End"],
    values=[100, 30, 20, -15, 135],
    title="Value Bridge",
    transparent=True
)
```

### Horizontal Bar
```python
IBCharts.hbar(
    categories=["Product A", "Product B", "Product C"],
    values=[45, 32, 23],
    title="Revenue Mix (%)",
    highlight_index=0,  # Highlight top bar
    transparent=True
)
```

### Donut Chart
```python
IBCharts.donut(
    labels=["North America", "EMEA", "APAC"],
    values=[55, 30, 15],
    title="Revenue by Region",
    center_label="$847M\nTotal",
    transparent=True
)
```

### Line with Area
```python
IBCharts.line_area(
    x_labels=["Q1", "Q2", "Q3", "Q4"],
    y_values=[100, 120, 135, 155],
    title="Quarterly Revenue Trend",
    fill_alpha=0.25,
    transparent=True
)
```

### Bullet Chart
```python
IBCharts.bullet(
    actual=85,
    target=100,
    ranges=[50, 75, 100],
    title="Target Achievement",
    transparent=True
)
```

### Heatmap
```python
IBCharts.heatmap(
    row_labels=["Q1", "Q2", "Q3", "Q4"],
    col_labels=["NA", "EMEA", "APAC"],
    values=[[80, 60, 40], [85, 65, 50], [90, 70, 55], [95, 75, 60]],
    title="Performance Matrix",
    cmap="RdYlGn",  # Red-Yellow-Green
    transparent=True
)
```

---

## Layout Templates (12×12 Grid)

### Hero Metric Layout
```
Grid: 12 columns × 12 rows (row 0 = header, row 11 = footer)

Row 0:  [HEADLINE: spans all 12 columns]
        ─────────────────────────────────────────────────
Row 1-2: │ KPI 1   │                                │ TAKEAWAYS │
         │ (0-1)   │     [PRIMARY CHART]            │ (10-11)   │
Row 3-4: │ KPI 2   │     (col 2-6, row 1-5)         │           │
         │ (0-1)   │                                │           │
Row 5-6: │ KPI 3   │                                │           │
         │ (0-1)   │                                │           │
        ─────────────────────────────────────────────────
Row 7-10:│     [CHART 2]      │    [TABLE]    │  [CHART 3]  │
         │    (0-4)           │    (5-8)      │   (9-11)    │
        ─────────────────────────────────────────────────
Row 11: [FOOTER: source, date, confidential]
```

### Dashboard Layout
```
Row 0:   [HEADLINE]
         ─────────────────────────────────────────────────
Row 1-2: │ KPI 1 │ KPI 2 │ KPI 3 │ KPI 4 │ KPI 5 │ KPI 6 │
         │ (0-1) │ (2-3) │ (4-5) │ (6-7) │ (8-9) │(10-11)│
         ─────────────────────────────────────────────────
Row 3-6: │      [CHART 1]       │       [CHART 2]        │
         │      (0-5)           │       (6-11)           │
         ─────────────────────────────────────────────────
Row 7-10:│              [COMPARISON TABLE]               │
         │                   (0-11)                      │
         ─────────────────────────────────────────────────
Row 11:  [FOOTER]
```

### Quadrant Layout
```
Row 0:   [HEADLINE]
         ─────────────────────────────────────────────────
Row 1-5: │    THEME 1 + CHART   │    THEME 2 + CHART    │
         │       (0-5)          │        (6-11)         │
         ─────────────────────────────────────────────────
Row 6-10:│    THEME 3 + CHART   │    THEME 4 + CHART    │
         │       (0-5)          │        (6-11)         │
         ─────────────────────────────────────────────────
Row 11:  [FOOTER]
```

---

## Quality Checklist

Before finalizing, verify:

- [ ] **Headline** captures the "so what" in one sentence
- [ ] **Visual hierarchy** is clear (eye path is intentional)
- [ ] **Data labels** are readable (9pt minimum)
- [ ] **Colors** follow IB palette (no random colors)
- [ ] **Alignment** is pixel-perfect (use grid)
- [ ] **White space** is generous (30%+ of page)
- [ ] **Takeaways** are actionable, not descriptive
- [ ] **Source** and date are included
- [ ] **No chartjunk** (gridlines, borders, legends minimized)
- [ ] **Numbers formatted** correctly (commas, decimals, units)

---

## Common Patterns

### Financial Summary
- Hero: Key financial metric (revenue, EBITDA)
- Charts: Waterfall bridge, trend line, peer comparison
- Table: Condensed financials (3-5 rows max)

### Competitive Analysis
- Hero: Market position or share
- Charts: Horizontal bar comparison, radar/spider
- Table: Feature comparison matrix

### Performance Dashboard
- Hero: Overall score or rating
- Charts: Bullet charts, heatmap
- Table: KPI summary with RAG status

### Investment Thesis
- Hero: Target price or recommendation
- Charts: Football field, sensitivity table
- Callouts: Key drivers and risks

---

## References

See `references/` folder:
- `chart-gallery.md` – Visual examples of all chart types
- `color-systems.md` – Extended color palettes and usage
- `typography-guide.md` – Font pairing and hierarchy
- `layout-grids.md` – Detailed grid specifications
