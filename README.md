# Institutional Growth Equity Skills

A curated bundle of 16 Claude skills for **institutional-quality growth equity research** — covering the full research workflow from thesis construction through valuation modeling to final deliverable production. Built to mirror the methodology used by long-only growth shops (Baillie Gifford, T. Rowe, Capital Group) and bulge-bracket equity research desks.

## What's inside

The 16 skills are organized into three workflow layers:

### 🔍 Analysis & Investment Frameworks (7)

For building the investment thesis — markets, moats, management, and signals.

| Skill | What it does |
| --- | --- |
| `growth-stock-analysis` | Moat / tech adoption / narrative framework for high-growth equities |
| `competitive-analysis` | 11-dimension competitive positioning (Porter, value chain, moat, supply chain) |
| `earnings-analysis` | Quarterly earnings parsing and scoring (10-Q, release, transcript) |
| `thematic-investment-research` | Secular theme validation and stock universe construction |
| `supply-chain-pass-through` | Mapping listed-equity beneficiaries of secular trends |
| `corporate-network-analysis` | Supplier/customer/board interlock alpha |
| `investment-report-reader` | Read broker notes, 10-Ks, multi-report triangulation |

### 💰 Valuation & Financial Modeling (6)

For turning the thesis into numbers.

| Skill | What it does |
| --- | --- |
| `dcf-valuation` | DCF with full share dilution (TSM, if-converted, SBC-adjusted FCF) |
| `semi-dcf-modeler` | Semiconductor-specific valuation (cycle P/E, SOTP, P/BV) |
| `financial-analysis` | DCF, ratios, statement evaluation |
| `creating-financial-models` | DCF, Monte Carlo, sensitivity, scenarios |
| `analyzing-financial-statements` | Ratio and metric calculation from financials |
| `ib-excel-professional` | IB-grade Excel models (LBO, M&A accretion/dilution, sensitivity) |

### 📝 Document & Visual Production (3)

For producing the final institutional deliverable.

| Skill | What it does |
| --- | --- |
| `ib-report-formatting` | Institutional Word formatting (pitch books, CIMs, fairness opinions) |
| `ib-infographic` | One-page infographics in Goldman/MS/JPM visual style |
| `alphaear-logic-visualizer` | Finance logic diagrams, transmission chains, signal flows |

## Repository structure

```
institutional-growth-equity-skills/
├── README.md
├── LICENSE
├── .gitignore
└── skills/
    ├── growth-stock-analysis/
    ├── competitive-analysis/
    ├── earnings-analysis/
    ├── thematic-investment-research/
    ├── supply-chain-pass-through/
    ├── corporate-network-analysis/
    ├── investment-report-reader/
    ├── dcf-valuation/
    ├── semi-dcf-modeler/
    ├── financial-analysis/
    ├── creating-financial-models/
    ├── analyzing-financial-statements/
    ├── ib-excel-professional/
    ├── ib-report-formatting/
    ├── ib-infographic/
    └── alphaear-logic-visualizer/
```

Each skill folder contains a `SKILL.md` (the entry point Claude reads) plus any supporting `assets/`, `references/`, or `scripts/` it needs.

## Installation

### Option 1: Install all skills

```bash
git clone https://github.com/<your-username>/institutional-growth-equity-skills.git
cp -r institutional-growth-equity-skills/skills/* ~/.claude/skills/
```

(Adjust the destination path for your environment — Claude Code, Claude Desktop, or the Claude API runtime each have their own skills directory.)

### Option 2: Install a single skill

Copy just the folder you want from `skills/` into your Claude skills directory.

### Option 3: Read directly

Open any `SKILL.md` and paste relevant sections into a Claude conversation as context.

## Suggested workflows

**Full company deep-dive.** `investment-report-reader` (ingest sell-side & 10-K) → `growth-stock-analysis` + `competitive-analysis` (frame the thesis) → `dcf-valuation` or `semi-dcf-modeler` (value it) → `ib-report-formatting` (write the memo) → `ib-infographic` (one-pager).

**Theme to portfolio.** `thematic-investment-research` (validate the theme) → `supply-chain-pass-through` (map beneficiaries) → `corporate-network-analysis` (find non-obvious linkages) → `growth-stock-analysis` per name.

**Quarterly maintenance.** `earnings-analysis` (parse the print) → `alphaear-logic-visualizer` (diagram the read-through) → update DCF.

## License

MIT — see `LICENSE`. The skills are provided as research frameworks; nothing here is investment advice.

## Contributing

Issues and pull requests welcome. Please keep contributions focused on improving analytical rigor, fixing factual errors, or clarifying methodology.
