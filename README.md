# Institutional Growth Equity Skills

A 16-skill research bundle covering analysis, valuation and presentation. These
frameworks structure analyst work; they are not a substitute for source checks,
model validation or investment judgment.

## Installation

```bash
git clone --recurse-submodules https://github.com/HHFinAi/Institutional-Growth-Equity-Skills.git
cd Institutional-Growth-Equity-Skills
git submodule update --init --recursive
python tools/build_bundle.py
```

Install individual ZIPs from `dist/` in a compatible Agent Skills runtime. CI
builds the same ZIPs after checks. The earnings component is a commit-pinned
submodule of `HHFinAi/earnings-analysis`; it now has the correct scripts and
references layout and v2 missing-data behavior. GitHub's ordinary Download ZIP
omits submodule contents. Use a recursive clone or a successful CI artifact.
For an unmerged maintenance release, first check out its PR branch.

Copying Markdown into a custom assistant can provide an analytical framework,
but does not itself supply scripts, reference loading, web access or native skill
routing. Consult each platform's current documentation rather than relying on
fixed UI paths, model names or context-window claims.

## What to use

| Workflow | Entry point |
|---|---|
| Growth thesis | growth-stock-analysis |
| Competitive position | competitive-analysis |
| Quarterly results | earnings-analysis |
| Themes and value chains | thematic-investment-research, supply-chain-pass-through |
| Corporate relationships | corporate-network-analysis |
| Read source reports | investment-report-reader |
| General operating-company DCF | dcf-valuation |
| Semiconductor valuation | semi-dcf-modeler |
| Historical financial diagnostics | analyzing-financial-statements |
| General financial assessment | financial-analysis |
| Scenario/sensitivity implementation | creating-financial-models |
| Requested transaction models and Excel production | ib-excel-professional |
| Written and visual outputs | ib-report-formatting, ib-infographic, complex-logic-visualizer |

See [workflow routing](docs/WORKFLOW_ROUTING.md) before chaining overlapping models.

## Evidence and output contract

Keep reported facts, inference, model impacts and open questions separate.
Timestamp data; reconcile fiscal periods, currencies and GAAP/non-GAAP bases.
Never invent consensus, a missing filing, prices or execution capabilities.
Require disconfirming evidence and explicitly state where inputs are missing.
Self-assessed confidence and heuristic scores are not calibrated probabilities.
Use synthetic or publication-authorized examples, never private positions or
licensed source documents in public fixtures.

## Maintenance

The earnings implementation is maintained upstream and pinned in the gitlink and
`bundle.json`. Upgrade through a reviewed PR after upstream tests pass; do not
edit an independent copy or use an unpinned remote update in CI. Other skills
remain local and have not all been empirically benchmarked. Historical installation
and positioning text is archived in `docs/archive/README-v1.md`.

Run `python -m unittest discover -s tests -v` and
`python -m unittest discover -s skills/earnings-analysis/tests -v`.

MIT; see [LICENSE](LICENSE). Research tools only, not investment advice.
