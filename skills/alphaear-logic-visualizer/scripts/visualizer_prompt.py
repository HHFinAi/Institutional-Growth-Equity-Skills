"""
Draw.io XML generation prompts for programmatic (API) use.
Mirrors the content in references/PROMPTS.md — that file is the human-readable
source of truth; this module exposes the same content for API calls.
"""

def get_drawio_system_prompt() -> str:
    return """You are an expert at creating Draw.io (MxGraph) diagrams in XML format.
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
"""


def get_drawio_task(nodes_data: list, title: str) -> str:
    """
    Build the user-turn task message for Draw.io XML generation.

    nodes_data: list of dicts with keys:
        id           - unique string identifier
        node_name    - display label
        impact_type  - "Positive" | "Negative" | "Neutral" | "Decision"
        logic        - short rationale for this node
        parent_id    - id of parent node (omit for root nodes)
    """
    import json
    nodes_json = json.dumps(nodes_data, ensure_ascii=False, indent=2)
    return f"""Please generate a Draw.io XML diagram for the following logic flow:

**Title**: {title}

**Nodes and Logic**:
{nodes_json}

Layout direction: Left to Right (use Top to Bottom only for hierarchy/org-chart structures).
Apply the colour conventions from the system prompt based on each node's impact_type field.
"""
