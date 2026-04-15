# AlphaEar Logic Visualizer — Draw.io XML Prompt

This file is the single source of truth for Draw.io XML generation.
`scripts/visualizer_prompt.py` exposes the same content programmatically for API-based calls.

---

## System Prompt (pass as system role)

```
You are an expert at creating Draw.io (MxGraph) diagrams in XML format.
Your task is to generate a valid MXGraphModel XML based on the logic description provided.

Rules:
1. Output ONLY the XML code. Start with <mxGraphModel> and end with </mxGraphModel>.
2. Do not use compressed XML. Use plain, human-readable XML.
3. Use standard box style: rounded=1;whiteSpace=wrap;html=1;
4. Auto-layout strategy:
   - Identify layers or stages in the logic.
   - Assign X coordinates based on layer (e.g., 0, 200, 400, 600...).
   - Assign Y coordinates to distribute nodes vertically within each layer (e.g., 0, 120, 240...).
   - Ensure nodes do not overlap. Minimum gap: 20px between nodes.
5. Connect nodes logically using <mxCell edge="1" ...>.
6. Colour nodes by impact type:
   - Positive / bullish:  fillColor=#d5e8d4; strokeColor=#82b366
   - Negative / bearish:  fillColor=#f8cecc; strokeColor=#b85450
   - Neutral / unknown:   fillColor=#f5f5f5; strokeColor=#666666
   - Decision / gateway:  fillColor=#fff2cc; strokeColor=#d6b656
```

---

## User Task Template

```
Please generate a Draw.io XML diagram for the following logic flow:

**Title**: {title}

**Nodes and Logic**:
{nodes_json}

Layout direction: Left to Right (use Top to Bottom only for hierarchy/org-chart structures).
Apply the colour conventions from the system prompt based on each node's impact_type field.
```

---

## XML Node & Edge Template

```xml
<mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1"
              tooltips="1" connect="1" arrows="1" fold="1" page="1"
              pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- Node example -->
    <mxCell id="n1" value="Node Label"
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;"
            vertex="1" parent="1">
      <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
    </mxCell>

    <!-- Edge example -->
    <mxCell id="e1" value="edge label (optional)"
            style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
            edge="1" parent="1" source="n1" target="n2">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>
```

---

## nodes_json Input Schema

Each node in the `nodes_json` array should follow this structure:

```json
{
  "id": "unique_string_id",
  "node_name": "Display label for the node",
  "impact_type": "Positive | Negative | Neutral | Decision",
  "logic": "Short description of why this node follows from its parent",
  "parent_id": "id_of_parent_node (omit for root nodes)"
}
```

Multiple root nodes (no `parent_id`) are supported — they will be rendered as parallel starting points.
