---
name: alphaear-logic-visualizer
description: Create finance logic diagrams and charts to explain investment transmission chains, signal flows, and market logic. Use this skill whenever the user wants to visualize an investment thesis, map a macro signal chain, draw a logic flow, show cause-and-effect relationships between market variables, or chart sentiment/ISQ/stock data. Trigger phrases include "visualize this", "draw my thesis", "map this logic", "show the transmission chain", "diagram this signal", "chart this flow", "create a logic diagram", "visualize the causal chain", "render this as a diagram", "show the mechanism". Also triggers when building outputs from the alphaear-sentiment skill that require chart rendering.
---

# AlphaEar Logic Visualizer Skill

## Overview

This skill creates visual representations of investment logic flows and financial data. It supports two rendering paths:

1. **Inline rendering** (preferred in claude.ai) — use the native `show_widget` / Visualizer tool to render SVG or HTML directly in chat
2. **File rendering** — use `scripts/visualizer.py` to save an HTML file for download

Use inline rendering for simple diagrams and quick visualizations. Use file rendering for complex multi-panel outputs or when the user explicitly wants a downloadable file.

---

## Chart Types & When to Use Each

### 1. Logic Transmission Graph (`generate_transmission_graph`)
**Best for**: Investment signal chains, macro transmission mechanisms, thesis visualizations, cause-and-effect maps.

Renders an interactive force-directed graph via pyecharts. Nodes are colour-coded by impact type:
- 🟢 Green — bullish / positive impact (`"Positive"`)
- 🔴 Red — bearish / negative impact (`"Negative"`)
- ⚫ Grey — neutral (`"Neutral"`)

**Input — nodes_data** (list of dicts):
```json
[
  {
    "node_name": "Fed Rate Cut",
    "impact_type": "Positive",
    "logic": "Lower real yields → risk-on",
    "id": "1"
  },
  {
    "node_name": "USD Weakens",
    "impact_type": "Positive",
    "logic": "Dollar index falls as rate differential narrows",
    "id": "2",
    "parent_id": "1"
  },
  {
    "node_name": "Gold Rallies",
    "impact_type": "Positive",
    "logic": "Inverse USD relationship + safe haven demand",
    "id": "3",
    "parent_id": "2"
  }
]
```

**Tool call**:
```python
from scripts.visualizer import VisualizerTools
graph = VisualizerTools.generate_transmission_graph(nodes_data, title="Fed Cut → Gold Transmission")
VisualizerTools.render_chart_to_file(graph, filename="output/chain.html")
```

---

### 2. Draw.io Diagram (`render_drawio_to_html`)
**Best for**: Structured flowcharts, decision trees, process diagrams, architecture-style layouts that need to be shared as a diagrams.net-compatible HTML file.

**Workflow**:
1. Use the Draw.io XML generation prompt in `references/PROMPTS.md` to produce valid `<mxGraphModel>` XML
2. Pass the XML to `render_drawio_to_html(xml_content, filename)`

**Tool call**:
```python
VisualizerTools.render_drawio_to_html(
    xml_content="<mxGraphModel>...</mxGraphModel>",
    filename="output/diagram.html",
    title="My Logic Diagram"
)
```

The output HTML embeds the diagrams.net viewer JS — the user can open it in any browser.

**Node colour convention**:
- Positive → `fillColor=#d5e8d4` (green)
- Negative → `fillColor=#f8cecc` (red)
- Neutral → `fillColor=#f5f5f5` (grey)

See `references/PROMPTS.md` for the full XML generation prompt and node/edge template.

---

### 3. Sentiment Trend Chart (`generate_sentiment_trend_chart`)
**Best for**: Rendering time-series output from the alphaear-sentiment skill — showing sentiment score evolution over time.

**Input**:
```python
sentiment_history = [
    {"date": "2025-01-01", "score": 0.72},
    {"date": "2025-01-02", "score": -0.15},
]
```

**Tool call**:
```python
chart = VisualizerTools.generate_sentiment_trend_chart(sentiment_history)
VisualizerTools.render_chart_to_file(chart, filename="output/sentiment.html")
```

---

### 4. ISQ Radar Chart (`generate_isq_radar_chart`)
**Best for**: Visualizing signal quality across five dimensions — sentiment strength, confidence, intensity, expectation gap, timeliness.

**Tool call**:
```python
chart = VisualizerTools.generate_isq_radar_chart(
    sentiment=0.8,
    confidence=0.9,
    intensity=4,
    expectation_gap=0.6,
    timeliness=0.85,
    title="Signal Quality: NVDA Earnings"
)
VisualizerTools.render_chart_to_file(chart, filename="output/isq_radar.html")
```

---

### 5. Stock K-Line Chart (`generate_stock_chart`)
**Best for**: Rendering OHLCV candlestick charts with optional prediction overlays or ground truth comparison lines.

**Input**: A `pandas.DataFrame` with columns `date`, `open`, `close`, `low`, `high`, `volume`.

**Tool call**:
```python
chart = VisualizerTools.generate_stock_chart(df, ticker="NVDA", title="NVDA Price Action")
VisualizerTools.render_chart_to_file(chart, filename="output/kline.html")
```

---

## Decision Guide: Which Path to Use?

| Situation | Recommended approach |
|---|---|
| Quick inline thesis map in chat | Native `show_widget` with SVG or inline HTML |
| Investment logic chain with branching | `generate_transmission_graph` → HTML file |
| Structured flowchart / process diagram | Draw.io XML path → `render_drawio_to_html` |
| Sentiment time-series from alphaear-sentiment | `generate_sentiment_trend_chart` → HTML file |
| ISQ signal quality output | `generate_isq_radar_chart` → HTML file |
| Stock price / candlestick chart | `generate_stock_chart` → HTML file |

---

## Agentic Workflow (file rendering path)

```
1. Parse user's logic description → extract nodes, links, impact types
2. Choose chart type using Decision Guide above
3. Structure input data (nodes_data dict list or DataFrame)
4. Call the appropriate VisualizerTools method
5. Call render_chart_to_file() or render_drawio_to_html() to save HTML
6. Present the file to the user via present_files tool
```

---

## Dependencies

```
pandas
loguru
pyecharts
```

Install with:
```bash
pip install pandas loguru pyecharts --break-system-packages
```

---

## Reference Files

- `references/PROMPTS.md` — Draw.io XML generation prompt and node/edge template (read this when using the Draw.io path)
- `scripts/visualizer.py` — All chart generation and rendering methods (`VisualizerTools` class)
- `scripts/visualizer_prompt.py` — Programmatic version of the Draw.io prompt for API-based generation
