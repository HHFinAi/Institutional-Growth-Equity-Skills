# Institutional Growth Equity Skills

> _This is an institutional-quality research and investment skill._

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
| `complex-logic-visualizer` | Finance logic diagrams, transmission chains, signal flows |

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
    └── complex-logic-visualizer/
```

Each skill folder contains a `SKILL.md` (the entry point Claude reads) plus any supporting `assets/`, `references/`, or `scripts/` it needs.

---

## How to Use These Skills

### In Claude.ai (recommended starting point)

This is the simplest way to get started. No terminal or coding experience is required. There are two approaches, depending on whether you want the skills available everywhere or only within a specific project.

#### Option A: Install account-wide via Customize (recommended)

This makes the skills available in all your conversations and in Cowork.

1. Download this repository as a ZIP file (on the repository's main page, click the green **Code** button, then **Download ZIP**).
2. Each skill in `skills/` needs to be uploaded individually. Either zip each skill folder separately, or download the repo ZIP and re-zip each subfolder under `skills/` so its `SKILL.md` sits at the root of its own ZIP.
3. Open claude.ai. In the left sidebar, click **Customize** (the toolbox icon), then go to **Skills**.
4. Click the **+** button, then **+ Create skill**, and upload one skill ZIP at a time. Repeat for each of the 16 skills you want to install.
5. Each skill will appear in your Skills list. Make sure its toggle is turned on.
6. Start any conversation and ask Claude to do equity research. For example:

   > Build a growth-stock investment thesis for Shopify. Here is the latest 10-Q:
   >
   > [paste your text]

   Claude will recognize that the request matches the relevant skills, load them, and produce a structured analysis. You can also upload financial filings as PDFs or paste sections directly.

> **Note:** Each ZIP must contain the skill folder at the root level. If your ZIP contains `growth-stock-analysis/SKILL.md` (not just a loose `SKILL.md`), you're set.

#### Option B: Add to a specific Project's knowledge base

If you prefer to limit the skills to a particular project (for example, a project dedicated to a single name or sector):

1. Download the `SKILL.md` file(s) you want from the relevant skill folder(s) in this repository.
2. Open or create a Project in Claude.ai.
3. In the Project's knowledge base, click **Add content** and upload the `SKILL.md` file(s).
4. Start a conversation inside that Project and ask Claude to apply the framework.

This approach keeps the skills scoped to one project, which is useful if you are working on multiple coverage names with different conventions.

### In Claude Code (terminal agent)

Place each skill folder in `.claude/skills/<skill-name>/` inside your project directory, then launch Claude Code and ask for analysis. For example, drop `growth-stock-analysis/` into `.claude/skills/growth-stock-analysis/` and Claude Code will discover it automatically.

### In Claude's Cowork (desktop agent)

If you installed the skills account-wide via Customize (Option A above), they are already available in Cowork — no additional setup needed.

If you prefer to work with the files directly, you can also place the relevant `SKILL.md` files in the folder you point Cowork at (or in a subfolder). Then ask Cowork to run the analysis on a file in that same folder:

> Analyze the 10-Q in this folder using the growth-stock-analysis framework.

### In ChatGPT

Because OpenAI has adopted the Agent Skills standard, you can use these skills in ChatGPT through a Custom GPT:

1. Open the `SKILL.md` file you want to use and copy its full contents (everything below the closing `---` of the header).
2. Go to chat.openai.com, click your profile icon, then **My GPTs → Create a GPT**.
3. In the **Configure** tab, paste the contents of the skill into the **Instructions** field. You may also want to add the YAML header's description text at the top so the GPT knows when to apply these instructions.
4. Name the GPT something descriptive (e.g., "Growth Stock Analyst") and save it.
5. Open the GPT and paste your filing or research material. The output format and reasoning will follow the same structure as in Claude.

You will need a separate Custom GPT per skill, since ChatGPT does not auto-route between multiple skill files.

### In Google Gemini

Gemini does not yet natively support the `SKILL.md` format, but you can achieve a similar result using a **Gem** (Gemini's equivalent of a custom assistant):

1. Open gemini.google.com and navigate to **Gems** (in the left sidebar, or via the Gem manager).
2. Create a new Gem.
3. In the instructions field, paste the full body of the `SKILL.md` file (everything after the YAML header).
4. Save the Gem and open a conversation with it.
5. Paste your filing or research material and ask for the analysis.

### General approach for any AI tool

If your preferred AI tool is not listed above, the pattern is the same:

1. Find the tool's mechanism for persistent instructions (custom assistants, system prompts, project instructions, or similar).
2. Paste the contents of the relevant `SKILL.md` into that mechanism.
3. Provide your filing or research material and ask for the analysis.

The skills are plain Markdown with no dependencies on any specific platform. They work wherever you can give an AI tool a block of instructions to follow.

---

## Tips for Getting Good Results

**Provide enough context.** A single line item or sentence from a filing is hard to analyze for thesis quality, competitive positioning, or earnings trajectory. A full section, MD&A, or transcript gives the skills enough material to identify patterns — margin trajectory, capital allocation tone shifts, or competitive dynamics that span multiple paragraphs.

**Pick the right skill for the job.** If you already know you need a DCF, invoke `dcf-valuation` directly rather than triggering the broader `growth-stock-analysis`. This produces faster, more focused output. The *Suggested workflows* section below shows good combinations.

**Use the frameworks as a structured starting point, not the final word.** The skills produce institutional-quality analysis, but your domain expertise is the final quality check. Occasionally a "moat" the framework flags as weak is actually structurally durable for industry-specific reasons (e.g., regulatory licensing in financial infrastructure). Use your judgment.

**Iterate.** If a thesis or valuation output misses a key consideration, tell the AI what's missing and ask it to revise. The skills' structured reasoning means the AI can explain *why* it scored a company a particular way, which makes it easy to have a productive back-and-forth.

---

## Suggested workflows

**Full company deep-dive.** `investment-report-reader` (ingest sell-side & 10-K) → `growth-stock-analysis` + `competitive-analysis` (frame the thesis) → `dcf-valuation` or `semi-dcf-modeler` (value it) → `ib-report-formatting` (write the memo) → `ib-infographic` (one-pager).

**Theme to portfolio.** `thematic-investment-research` (validate the theme) → `supply-chain-pass-through` (map beneficiaries) → `corporate-network-analysis` (find non-obvious linkages) → `growth-stock-analysis` per name.

**Quarterly maintenance.** `earnings-analysis` (parse the print) → `complex-logic-visualizer` (diagram the read-through) → update DCF.

## License

MIT — see `LICENSE`. The skills are provided as research frameworks; nothing here is investment advice.

## Contributing

Issues and pull requests welcome. Please keep contributions focused on improving analytical rigor, fixing factual errors, or clarifying methodology.
