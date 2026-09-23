# Model routing and reconciliation

Choose one primary valuation engine per company/scenario. Other skills may supply
inputs or checks; do not average contradictory model outputs without reconciling
the underlying cash flows, discount rates, balance-sheet adjustments and dilution.

- `dcf-valuation`: operating-company intrinsic valuation and equity-value bridge.
- `semi-dcf-modeler`: semiconductor cycle and segment-specific valuation; reconcile
  its assumptions with the primary DCF rather than adding two enterprise values.
- `analyzing-financial-statements`: historical ratios and accounting diagnostics,
  not an independent price target.
- `financial-analysis`: broad diagnostics and model selection; delegate a full
  valuation to the chosen specialist rather than rebuilding it inconsistently.
- `creating-financial-models`: implementation of sensitivity/scenario calculations
  using the primary model's definitions and assumptions.
- `ib-excel-professional`: spreadsheet engineering and explicitly requested
  transaction models; do not trigger an LBO or merger model for an earnings note.

Checks: FCFF versus FCFE, capex and working-capital signs, cash taxes/NOLs,
terminal assumptions, enterprise-to-equity adjustments, share counts and units.
Show financing proceeds and dilution consistently in each financing scenario.
Keep source/model version, valuation date and assumption changes with the output.

Clinical-stage assets require an explicit stage-risk and development-spend model;
a generic mature-company DCF must not be applied without adapting its economics.
