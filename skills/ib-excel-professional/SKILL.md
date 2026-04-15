---
name: ib-excel-professional
description: "Professional investment banking Excel modeling for complex financial analysis. Use when creating: DCF models, LBO models, M&A analysis (accretion/dilution), sensitivity analysis (data tables), Monte Carlo simulations, tornado charts, waterfall charts, football field valuations, comparable company analysis, precedent transactions, three-statement models, model auditing, error detection and fixing, circular reference handling, or any institutional-quality financial model requiring sophisticated formulas, professional formatting, and advanced analytical techniques."
license: Proprietary
---

# Investment Banking Excel Professional Skill

## When to Use This Skill
- Building DCF, LBO, or M&A models
- Three-statement model integration
- M&A accretion/dilution analysis
- Trading comps and precedent transactions
- Creating sensitivity analysis (1-way/2-way data tables)
- Monte Carlo simulations for valuation ranges
- Tornado charts for sensitivity visualization
- Waterfall charts (EV-to-Equity bridges)
- Football field valuation summaries
- Professional financial tables with IB formatting standards
- Complex formula linkages across multiple sheets
- **Handling intentional circular references (LBO debt/interest)**
- **Auditing models for errors, broken references, and circular dependencies**
- **Model integrity checks (balance sheet, cash flow reconciliation)**

## Prerequisites
- Use in conjunction with the base `/mnt/skills/public/xlsx/SKILL.md` for core Excel operations
- Always run `recalc.py` after creating formulas

---

# PART 1: COMPLETE IB FUNCTIONS REFERENCE

## Formula Frequency in Professional IB Models
| Function | % of All Formulas | Notes |
|----------|------------------|-------|
| SUM | ~59% | Most common by far |
| SUMIFS/SUMPRODUCT | ~6% each | Critical for weighted calculations |
| IF/IFS | ~5% | Conditional logic |
| INDEX/MATCH | ~4% | Primary lookup method |
| Other | ~20% | Various specialized functions |

---

## 1. FINANCIAL FUNCTIONS (Core Valuation)

### Time Value of Money - CRITICAL
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **XNPV** | `=XNPV(rate, values, dates)` | **ALWAYS use for DCF** - handles specific dates |
| **XIRR** | `=XIRR(values, dates, [guess])` | **ALWAYS use for LBO returns** - handles uneven timing |
| NPV | `=NPV(rate, value1, ...)` | Legacy - assumes period-end, discounts first CF |
| IRR | `=IRR(values, [guess])` | Legacy - assumes equal periods |
| **MIRR** | `=MIRR(values, finance_rate, reinvest_rate)` | More realistic IRR with reinvestment assumption |
| PV | `=PV(rate, nper, pmt, [fv], [type])` | Present value of annuity |
| FV | `=FV(rate, nper, pmt, [pv], [type])` | Future value calculations |
| **RATE** | `=RATE(nper, pmt, pv, [fv], [type], [guess])` | Back-solve for yield/interest rate |
| NPER | `=NPER(rate, pmt, pv, [fv], [type])` | Number of periods |

### Debt & Loan Functions
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **PMT** | `=PMT(rate, nper, pv, [fv], [type])` | Total debt payment |
| **IPMT** | `=IPMT(rate, per, nper, pv, [fv], [type])` | Interest portion - debt schedules |
| **PPMT** | `=PPMT(rate, per, nper, pv, [fv], [type])` | Principal portion - amortization |
| CUMIPMT | `=CUMIPMT(rate, nper, pv, start, end, type)` | Cumulative interest |
| CUMPRINC | `=CUMPRINC(rate, nper, pv, start, end, type)` | Cumulative principal |

### Fixed Income / Bond Functions
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **YIELD** | `=YIELD(settle, maturity, rate, pr, redemption, freq, [basis])` | Bond yield calculation |
| **PRICE** | `=PRICE(settle, maturity, rate, yld, redemption, freq, [basis])` | Bond pricing |
| **DURATION** | `=DURATION(settle, maturity, coupon, yld, freq, [basis])` | Macaulay duration |
| **MDURATION** | `=MDURATION(settle, maturity, coupon, yld, freq, [basis])` | Modified duration - interest rate sensitivity |
| ACCRINT | `=ACCRINT(issue, first_int, settle, rate, par, freq, [basis])` | Accrued interest |
| **EFFECT** | `=EFFECT(nominal_rate, npery)` | Convert nominal to effective rate |
| **NOMINAL** | `=NOMINAL(effect_rate, npery)` | Convert effective to nominal rate |

### Depreciation
| Function | Syntax | IB Application |
|----------|--------|----------------|
| SLN | `=SLN(cost, salvage, life)` | Straight-line |
| DB | `=DB(cost, salvage, life, period, [month])` | Declining balance |
| DDB | `=DDB(cost, salvage, life, period, [factor])` | Double declining |
| VDB | `=VDB(cost, salvage, life, start, end, [factor], [no_switch])` | Flexible MACRS modeling |

---

## 2. LOOKUP FUNCTIONS

### INDEX/MATCH - The IB Standard
**Always use INDEX/MATCH over VLOOKUP** - bidirectional, immune to column insertions.

```
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```

| Function | Syntax | IB Application |
|----------|--------|----------------|
| **INDEX** | `=INDEX(array, row, [col])` | Return value at intersection |
| **MATCH** | `=MATCH(lookup, array, [match_type])` | Return position (use 0 for exact) |
| VLOOKUP | `=VLOOKUP(lookup, table, col_index, [range_lookup])` | Legacy - breaks on column insert |
| HLOOKUP | `=HLOOKUP(lookup, table, row_index, [range_lookup])` | Horizontal lookup for time series |
| **OFFSET** | `=OFFSET(ref, rows, cols, [height], [width])` | Dynamic ranges - essential for data tables |
| **INDIRECT** | `=INDIRECT(ref_text, [a1])` | Scenario switching with text references |
| **CHOOSE** | `=CHOOSE(index, val1, val2, ...)` | Scenario/case selection |

### Modern Lookups (Excel 365+ Only)
**WARNING: Use only internally - breaks on older Excel versions**

| Function | Syntax | Advantage over INDEX/MATCH |
|----------|--------|---------------------------|
| **XLOOKUP** | `=XLOOKUP(lookup, lookup_array, return_array, [not_found], [match_mode], [search_mode])` | Built-in error handling, reverse search |
| **XMATCH** | `=XMATCH(lookup, array, [match_mode], [search_mode])` | Wildcard support, binary search |

```python
# Compatibility check before using XLOOKUP in deliverables
# If model will be shared externally → Use INDEX/MATCH
# If internal use only on Excel 365 → XLOOKUP is fine
```

---

## 3. MATH & AGGREGATION FUNCTIONS

### The Power Functions
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **SUM** | `=SUM(range)` | ~59% of all IB formulas |
| **SUMPRODUCT** | `=SUMPRODUCT(array1, [array2], ...)` | **CRITICAL** - weighted averages, conditional sums without helper columns |
| **SUMIFS** | `=SUMIFS(sum_range, criteria_range1, criteria1, ...)` | Multi-criteria aggregation |
| **AVERAGE** | `=AVERAGE(range)` | Mean calculation |
| **MEDIAN** | `=MEDIAN(range)` | **PREFERRED for comps** - reduces outlier impact |
| MIN/MAX | `=MIN(range)` / `=MAX(range)` | Range bounds |
| LARGE/SMALL | `=LARGE(array, k)` | k-th largest/smallest |
| **ROUND** | `=ROUND(number, digits)` | Standard rounding |
| ROUNDUP/ROUNDDOWN | `=ROUNDUP(number, digits)` | Conservative/aggressive rounding |
| ABS | `=ABS(number)` | Absolute value |
| PRODUCT | `=PRODUCT(range)` | Multiply all values |

### SUMPRODUCT Patterns (Essential)
```
# Weighted average (e.g., WACC)
=SUMPRODUCT(weights, values)/SUM(weights)

# Conditional sum without SUMIFS
=SUMPRODUCT((criteria_range="X")*(sum_range))

# Multiple criteria
=SUMPRODUCT((range1="A")*(range2>100)*(values))
```

---

## 4. STATISTICAL FUNCTIONS

### Descriptive Statistics
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **MEDIAN** | `=MEDIAN(range)` | Preferred for valuation multiples |
| **AVERAGE** | `=AVERAGE(range)` | Mean - use with caution for comps |
| **STDEV.S** | `=STDEV.S(range)` | Sample standard deviation - volatility |
| VAR.S | `=VAR.S(range)` | Sample variance |
| **PERCENTILE.INC** | `=PERCENTILE.INC(array, k)` | Valuation ranges (25th/75th) |
| QUARTILE.INC | `=QUARTILE.INC(array, quart)` | Quartile values |
| COUNT/COUNTA | `=COUNT(range)` | Count numbers/non-empty |
| COUNTIFS | `=COUNTIFS(range1, criteria1, ...)` | Conditional counting |

### Regression & Correlation (CAPM, Beta)
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **SLOPE** | `=SLOPE(known_y, known_x)` | **Calculate Beta** for CAPM |
| INTERCEPT | `=INTERCEPT(known_y, known_x)` | Regression intercept (alpha) |
| **CORREL** | `=CORREL(array1, array2)` | Correlation coefficient |
| RSQ | `=RSQ(known_y, known_x)` | R-squared |
| LINEST | `=LINEST(known_y, known_x, [const], [stats])` | Full regression output |

### Monte Carlo Functions
| Function | Syntax | IB Application |
|----------|--------|----------------|
| RAND | `=RAND()` | Uniform random 0-1 |
| RANDBETWEEN | `=RANDBETWEEN(bottom, top)` | Random integer |
| **NORM.INV** | `=NORM.INV(probability, mean, stdev)` | **Key for Monte Carlo** |
| LOGNORM.INV | `=LOGNORM.INV(prob, mean, stdev)` | Stock prices, multiples |
| T.INV | `=T.INV(probability, df)` | T-distribution |
| BETA.INV | `=BETA.INV(prob, alpha, beta)` | Bounded probabilities |

---

## 5. LOGICAL & CONDITIONAL FUNCTIONS

| Function | Syntax | IB Application |
|----------|--------|----------------|
| **IF** | `=IF(test, true_val, false_val)` | Basic conditional |
| **IFS** | `=IFS(cond1, val1, cond2, val2, ...)` | Multiple conditions |
| AND/OR | `=AND(cond1, cond2)` | Combine conditions |
| **IFERROR** | `=IFERROR(value, value_if_error)` | **ESSENTIAL** - trap errors |
| IFNA | `=IFNA(value, value_if_na)` | Handle #N/A specifically |
| **SWITCH** | `=SWITCH(expr, val1, result1, ..., [default])` | Scenario selection |
| ISERROR/ISNA | `=ISERROR(value)` | Check for errors |
| ISBLANK | `=ISBLANK(value)` | Check empty cells |

---

## 6. DATE & TIME FUNCTIONS

| Function | Syntax | IB Application |
|----------|--------|----------------|
| **YEARFRAC** | `=YEARFRAC(start, end, [basis])` | **CRITICAL for DCF** - stub periods |
| **EOMONTH** | `=EOMONTH(start_date, months)` | Period end dates |
| **EDATE** | `=EDATE(start_date, months)` | Add months |
| DATE | `=DATE(year, month, day)` | Construct date |
| YEAR/MONTH/DAY | `=YEAR(date)` | Extract components |
| DAYS360 | `=DAYS360(start, end, [method])` | 360-day convention |
| NETWORKDAYS | `=NETWORKDAYS(start, end, [holidays])` | Business days |
| TODAY/NOW | `=TODAY()` | Current date/time |

---

## 7. TEXT FUNCTIONS

| Function | Syntax | IB Application |
|----------|--------|----------------|
| **TEXT** | `=TEXT(value, format)` | Format numbers as text |
| VALUE | `=VALUE(text)` | Convert text to number |
| **TEXTJOIN** | `=TEXTJOIN(delimiter, ignore_empty, text1, ...)` | Combine text |
| CONCATENATE/CONCAT | `=CONCAT(text1, text2)` | Join strings |
| LEFT/RIGHT/MID | `=LEFT(text, chars)` | Extract characters |
| LEN | `=LEN(text)` | Character count |
| TRIM/CLEAN | `=TRIM(text)` | Remove spaces/non-printables |
| FIND/SEARCH | `=FIND(find_text, within_text)` | Find position |
| SUBSTITUTE | `=SUBSTITUTE(text, old, new)` | Replace text |

---

## 8. MODERN EXCEL FUNCTIONS (Excel 365)

### Dynamic Arrays
**Use internally only - compatibility issues with older Excel**

| Function | Syntax | IB Application |
|----------|--------|----------------|
| **FILTER** | `=FILTER(array, include, [if_empty])` | Dynamic filtering |
| **SORT** | `=SORT(array, [sort_index], [order])` | Dynamic sorting |
| **UNIQUE** | `=UNIQUE(array)` | Extract unique values |
| **SEQUENCE** | `=SEQUENCE(rows, [cols], [start], [step])` | Generate period numbers |
| **VSTACK** | `=VSTACK(array1, array2, ...)` | Stack arrays vertically |
| **HSTACK** | `=HSTACK(array1, array2, ...)` | Stack arrays horizontally |
| TAKE/DROP | `=TAKE(array, rows, [cols])` | Extract first/last elements |
| CHOOSECOLS/CHOOSEROWS | `=CHOOSECOLS(array, col1, col2, ...)` | Select specific columns/rows |

### Advanced Functions
| Function | Syntax | IB Application |
|----------|--------|----------------|
| **LET** | `=LET(name1, value1, ..., calculation)` | **Readable formulas** - assign intermediate variables |
| **LAMBDA** | `=LAMBDA([params], calculation)` | Create custom reusable functions |

### LET Example (Improved Readability)
```
# Without LET - hard to read
=IF(B5/B6>0.5, B5/B6*1.1, B5/B6*0.9)

# With LET - clear and efficient
=LET(
    ratio, B5/B6,
    IF(ratio>0.5, ratio*1.1, ratio*0.9)
)
```

---

# PART 2: IB MODELING USE CASES

## DCF Valuation Model

### Unlevered Free Cash Flow Formula
```
UFCF = EBIT × (1 - Tax Rate) + D&A - ΔWorking Capital - CapEx
```

### Excel Implementation
```python
# UFCF calculation
ws['B15'] = '=B10*(1-$B$5)+B11-B12-B13'  # EBIT*(1-Tax)+D&A-ΔNWC-CapEx

# Terminal Value - Perpetuity Growth (Gordon Growth)
ws['G20'] = '=G15*(1+$B$7)/($B$6-$B$7)'  # FCF*(1+g)/(WACC-g)

# Terminal Value - Exit Multiple
ws['G21'] = '=G10*$B$8'  # EBITDA * Exit Multiple

# Present Value with XNPV (PREFERRED)
ws['B25'] = '=XNPV($B$6, B15:G15, B2:G2)'  # Discount FCFs at WACC

# Enterprise Value
ws['B30'] = '=B25+G22/(1+$B$6)^5'  # PV of FCFs + PV of Terminal Value
```

### WACC Calculation
```
=([Equity/EV]*[Cost_of_Equity])+([Debt/EV]*[Cost_of_Debt]*(1-[Tax_Rate]))

# Cost of Equity (CAPM)
=Risk_Free_Rate + Beta*(Market_Return - Risk_Free_Rate)

# Beta calculation using SLOPE
=SLOPE(stock_returns, market_returns)
```

---

## LBO Model - Circular Reference Handling

### The Circularity Problem
Interest expense → Net income → Cash flow → Debt repayment → Average debt → Interest expense

### Solution 1: Enable Iterative Calculations
```
File → Options → Formulas → Enable iterative calculation
- Maximum iterations: 100
- Maximum change: 0.001
```

### Solution 2: Circuit Breaker Toggle (CRITICAL)
```python
# Create a toggle cell (e.g., $B$1 named "CircuitBreaker")
# 0 = OFF (breaks circularity for debugging)
# 1 = ON (enables circularity)

# Interest expense formula with circuit breaker
ws['B20'] = '=IF($B$1=1, (B18+C18)/2*$B$5, B18*$B$5)'
# When ON: Average debt * interest rate
# When OFF: Beginning debt * interest rate (no circularity)
```

### LBO Returns Formulas
```python
# MOIC (Multiple on Invested Capital)
ws['B30'] = '=B25/B10'  # Exit Equity / Initial Equity

# IRR using XIRR (with dates)
ws['B31'] = '=XIRR(B35:G35, B36:G36)'  # Cash flows with dates

# Quick IRR approximation from MOIC
# 2.0x over 5 years ≈ 15% IRR
# 2.5x over 5 years ≈ 20% IRR
# 3.0x over 5 years ≈ 25% IRR
```

---

## M&A Accretion/Dilution Analysis

### Pro Forma EPS Calculation
```python
# Combined Net Income
ws['B10'] = '=Acquirer_NI + Target_NI + Synergies - Lost_Interest_Income - New_Interest_Expense'

# Pro Forma Shares Outstanding
ws['B11'] = '=Acquirer_Shares + New_Shares_Issued'  # For stock deals

# Pro Forma EPS
ws['B12'] = '=B10/B11'

# Accretion/Dilution %
ws['B15'] = '=B12/Standalone_Acquirer_EPS - 1'
# Positive = Accretive, Negative = Dilutive
```

### Deal Structure Scenarios with CHOOSE
```python
# Consideration mix scenarios
# 1 = All Cash, 2 = All Stock, 3 = 50/50 Mix
ws['B5'] = '=CHOOSE($B$1, Cash_Consideration, Stock_Consideration, Mixed_Consideration)'
```

### Purchase Price Allocation
```python
# Goodwill
ws['B20'] = '=Purchase_Price - Fair_Value_Net_Assets'
```

---

## Trading Comps / Comparable Company Analysis

### Enterprise Value Calculation
```
EV = Market Cap + Total Debt + Preferred Stock + Minority Interest - Cash
```

### Valuation Multiples
```python
# EV/EBITDA
ws['B15'] = '=B10/B5'  # Enterprise Value / EBITDA

# EV/Revenue
ws['B16'] = '=B10/B4'  # Enterprise Value / Revenue

# P/E Ratio
ws['B17'] = '=B8/B6'  # Share Price / EPS

# Use MEDIAN for peer summary (reduces outlier impact)
ws['B25'] = '=MEDIAN(B15:B22)'  # Median EV/EBITDA of peer group

# Percentile ranges for valuation
ws['B26'] = '=PERCENTILE.INC(B15:B22, 0.25)'  # 25th percentile
ws['B27'] = '=PERCENTILE.INC(B15:B22, 0.75)'  # 75th percentile

# Implied valuation
ws['B30'] = '=Target_EBITDA * B25'  # Target EBITDA × Peer Median Multiple
```

---

## Precedent Transactions

### Control Premium Calculation
```python
# Control Premium
ws['B10'] = '=Offer_Price/Unaffected_Price - 1'

# Unaffected price periods
ws['B11'] = '=Offer_Price/Price_1Day_Prior - 1'   # 1-day premium
ws['B12'] = '=Offer_Price/Price_1Week_Prior - 1'  # 1-week premium
ws['B13'] = '=Offer_Price/Price_1Month_Prior - 1' # 1-month premium
```

---

## Three-Statement Model Integration

### Working Capital Days Formulas
```python
# Accounts Receivable
ws['B20'] = '=Revenue/365*DSO_Days'  # Revenue ÷ 365 × DSO

# Inventory
ws['B21'] = '=COGS/365*DIO_Days'  # COGS ÷ 365 × DIO

# Accounts Payable
ws['B22'] = '=COGS/365*DPO_Days'  # COGS ÷ 365 × DPO

# Net Working Capital
ws['B23'] = '=B20+B21-B22'  # AR + Inventory - AP

# Change in NWC (for cash flow)
ws['B24'] = '=B23-A23'  # Current NWC - Prior NWC
```

### PP&E Roll-Forward
```
Beginning PP&E + CapEx - Depreciation = Ending PP&E
```

### Cash Flow Statement Links
```python
# Operating Activities
ws['B30'] = '=Net_Income'              # Start with NI
ws['B31'] = '=Depreciation'            # Add back D&A (non-cash)
ws['B32'] = '=-Change_in_NWC'          # Subtract increase in NWC

# Investing Activities
ws['B35'] = '=-CapEx'                  # Capital expenditures (negative)

# Financing Activities
ws['B40'] = '=Debt_Issuance'
ws['B41'] = '=-Debt_Repayment'
ws['B42'] = '=-Dividends'

# Ending Cash = Beginning Cash + Sum of all sections
ws['B50'] = '=A50+SUM(B30:B32)+B35+SUM(B40:B42)'
```

---

# PART 3: MODEL INTEGRITY CHECKS

## Dedicated Checks Tab Structure

```python
def create_model_checks_tab(ws):
    """
    Creates a dedicated checks tab with integrity validations.
    All checks should show "✓" when passing.
    """
    
    checks = [
        ("Balance Sheet Balances", "=ABS('Balance Sheet'!Assets-'Balance Sheet'!Liabilities-'Balance Sheet'!Equity)<0.01"),
        ("Cash Ties to CFS", "=ABS('Balance Sheet'!Cash-'Cash Flow'!Ending_Cash)<0.01"),
        ("Retained Earnings Ties", "=ABS(RE_Current-(RE_Prior+Net_Income-Dividends))<0.01"),
        ("Debt Schedule Ties to BS", "=ABS('Debt Schedule'!Total_Debt-'Balance Sheet'!Total_Debt)<0.01"),
        ("Sources = Uses (LBO)", "=ABS(Total_Sources-Total_Uses)<0.01"),
        ("No Circular Ref Errors", "=ISERROR(Interest_Expense)=FALSE"),
    ]
    
    ws['A1'] = "MODEL INTEGRITY CHECKS"
    ws['A1'].font = Font(bold=True, size=14)
    
    headers = ["Check Description", "Formula Result", "Status"]
    for i, h in enumerate(headers):
        ws.cell(row=3, column=i+1, value=h).font = Font(bold=True)
    
    for i, (description, formula) in enumerate(checks):
        row = 4 + i
        ws.cell(row=row, column=1, value=description)
        ws.cell(row=row, column=2, value=formula)
        ws.cell(row=row, column=3, value=f'=IF(B{row},"✓","✗")')
    
    # Master check
    last_row = 4 + len(checks)
    ws.cell(row=last_row+2, column=1, value="MASTER CHECK")
    ws.cell(row=last_row+2, column=1).font = Font(bold=True)
    ws.cell(row=last_row+2, column=3, value=f'=IF(COUNTIF(C4:C{last_row},"✗")=0,"ALL PASS","REVIEW REQUIRED")')
```

## Balance Sheet Check Formula
```
=IF(ABS(Total_Assets - Total_Liabilities - Total_Equity) < 0.01, "✓", "✗")
```

## Common Imbalance Sources
1. Retained earnings not linked to net income
2. Cash not matching cash flow statement ending balance
3. Depreciation mismatch between statements
4. Debt schedule not tied to balance sheet

---

# PART 4: ERROR DETECTION & REPAIR

## Excel Error Types Reference

| Error | Cause | Common Scenarios | Fix Strategy |
|-------|-------|------------------|--------------|
| `#REF!` | Invalid cell reference | Deleted rows/columns, broken links | Rebuild references |
| `#DIV/0!` | Division by zero | Empty cells, zero denominators | Add IFERROR or IF check |
| `#VALUE!` | Wrong data type | Text in numeric formula | Check input types |
| `#NAME?` | Unrecognized name | Typo in function/range name | Fix spelling |
| `#N/A` | Value not found | Failed lookup | Check lookup value exists |
| `#NUM!` | Invalid numeric value | Impossible math | Validate inputs |
| `#CALC!` | Calculation error | Empty array | Check array formula |
| `Circular` | Self-referencing formula | Debt/interest loop | Use circuit breaker |

## Automated Error Scanner

```python
from openpyxl import load_workbook
from collections import defaultdict
import json

def scan_workbook_for_errors(filepath):
    """
    Comprehensive workbook scanner for all error types.
    """
    ERROR_PATTERNS = {
        '#REF!': 'Broken cell reference',
        '#DIV/0!': 'Division by zero',
        '#VALUE!': 'Wrong data type',
        '#NAME?': 'Unrecognized function/name',
        '#N/A': 'Lookup value not found',
        '#NUM!': 'Invalid numeric result',
        '#NULL!': 'Invalid range intersection',
        '#CALC!': 'Calculation engine error',
    }
    
    wb = load_workbook(filepath, data_only=True)
    errors = defaultdict(list)
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for row in ws.iter_rows():
            for cell in row:
                if cell.value in ERROR_PATTERNS:
                    errors[cell.value].append(f"{sheet_name}!{cell.coordinate}")
    
    wb.close()
    
    return {
        'total_errors': sum(len(v) for v in errors.values()),
        'error_details': dict(errors)
    }


def find_circular_references(filepath):
    """
    Detects circular references by building dependency graph.
    """
    from openpyxl import load_workbook
    import re
    
    wb = load_workbook(filepath, data_only=False)
    dependencies = defaultdict(set)
    
    cell_ref_pattern = r"(?:'?([^'!]+)'?!)?\$?([A-Z]+)\$?(\d+)"
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for row in ws.iter_rows():
            for cell in row:
                if cell.value and str(cell.value).startswith('='):
                    formula = str(cell.value)
                    current_cell = f"{sheet_name}!{cell.coordinate}"
                    
                    for match in re.finditer(cell_ref_pattern, formula):
                        ref_sheet = match.group(1) or sheet_name
                        ref_col, ref_row = match.group(2), match.group(3)
                        ref_cell = f"{ref_sheet}!{ref_col}{ref_row}"
                        
                        if ref_cell != current_cell:
                            dependencies[current_cell].add(ref_cell)
    
    wb.close()
    
    # Detect cycles using DFS
    def find_cycle(start, current, visited, path):
        if current in path:
            return path[path.index(current):] + [current]
        if current in visited:
            return None
        visited.add(current)
        path.append(current)
        for neighbor in dependencies.get(current, []):
            cycle = find_cycle(start, neighbor, visited, path)
            if cycle:
                return cycle
        path.pop()
        return None
    
    circular_refs = []
    all_visited = set()
    
    for cell in dependencies:
        if cell not in all_visited:
            cycle = find_cycle(cell, cell, set(), [])
            if cycle:
                circular_refs.append(cycle)
            all_visited.update(set())
    
    return {
        'has_circular_refs': len(circular_refs) > 0,
        'circular_chains': circular_refs
    }


def add_error_protection(filepath, output_path=None):
    """
    Wraps division formulas with IFERROR and lookups with IFNA.
    """
    wb = load_workbook(filepath)
    output_path = output_path or filepath
    fixes = []
    
    lookup_functions = ['VLOOKUP', 'HLOOKUP', 'XLOOKUP', 'MATCH', 'INDEX']
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for row in ws.iter_rows():
            for cell in row:
                if cell.value and str(cell.value).startswith('='):
                    formula = str(cell.value)
                    formula_upper = formula.upper()
                    
                    if 'IFERROR' in formula_upper or 'IFNA' in formula_upper:
                        continue
                    
                    has_lookup = any(f in formula_upper for f in lookup_functions)
                    has_division = '/' in formula
                    
                    if has_lookup:
                        cell.value = f'=IFNA({formula[1:]},"—")'
                        fixes.append(f"{sheet_name}!{cell.coordinate}")
                    elif has_division:
                        cell.value = f'=IFERROR({formula[1:]},0)'
                        fixes.append(f"{sheet_name}!{cell.coordinate}")
    
    wb.save(output_path)
    wb.close()
    
    return {'fixes_made': len(fixes), 'cells_fixed': fixes}
```

## Safe Formula Patterns

```
# Safe division
=IFERROR(A1/B1, 0)
=IF(B1=0, 0, A1/B1)

# Safe lookup
=IFNA(VLOOKUP(A1, range, 2, 0), "Not Found")
=IFERROR(INDEX(range, MATCH(A1, lookup, 0)), "N/A")

# Display "NM" for not meaningful
=IFERROR(Revenue/EBITDA, "NM")
```

---

# PART 5: SENSITIVITY ANALYSIS

## Two-Way Data Table Structure

```python
def create_two_way_sensitivity(ws, start_row, start_col, row_input, col_input, 
                                output_cell, row_values, col_values, title):
    """
    WACC vs Terminal Growth sensitivity table.
    """
    from openpyxl.styles import Font, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    
    thin = Border(left=Side(style='thin'), right=Side(style='thin'),
                  top=Side(style='thin'), bottom=Side(style='thin'))
    header_fill = PatternFill(start_color="1F4E79", fill_type="solid")
    
    # Title
    ws.cell(row=start_row, column=start_col, value=title).font = Font(bold=True, size=12)
    ws.cell(row=start_row+1, column=start_col, value="WACC ↓ / Terminal Growth →").font = Font(italic=True, size=9)
    
    # Top-left corner: link to output
    corner = ws.cell(row=start_row+2, column=start_col, value=f"={output_cell}")
    corner.fill = header_fill
    corner.font = Font(bold=True, color="FFFFFF")
    
    # Column headers
    for j, val in enumerate(col_values):
        cell = ws.cell(row=start_row+2, column=start_col+1+j, value=val)
        cell.fill = header_fill
        cell.font = Font(bold=True, color="FFFFFF")
        cell.number_format = '0.0%'
    
    # Row headers and result cells
    for i, row_val in enumerate(row_values):
        ws.cell(row=start_row+3+i, column=start_col, value=row_val).font = Font(color="0000FF")
        ws.cell(row=start_row+3+i, column=start_col).number_format = '0.0%'
        
        for j in range(len(col_values)):
            ws.cell(row=start_row+3+i, column=start_col+1+j).number_format = '$#,##0.00'
```

## Performance Optimization for Data Tables

```
# Data tables are memory-intensive
# Change calculation mode:
File → Options → Formulas → "Automatic Except for Data Tables"

# Press F9 to manually recalculate when needed
```

---

# PART 6: FORMATTING STANDARDS

## Color Coding (Universal IB Standard)

```python
from openpyxl.styles import Font, PatternFill

# Text Colors
BLUE_INPUT = Font(color="0000FF")      # Hardcoded inputs/assumptions
BLACK_FORMULA = Font(color="000000")   # All formulas and calculations
GREEN_LINK = Font(color="008000")      # Links to other sheets in workbook
RED_EXTERNAL = Font(color="FF0000")    # Links to external files

# Background Colors
YELLOW_INPUT = PatternFill(start_color="FFFF00", fill_type="solid")   # Input cells
HEADER_BLUE = PatternFill(start_color="1F4E79", fill_type="solid")    # Headers
GRAY_ALT = PatternFill(start_color="D6DCE4", fill_type="solid")       # Alternating rows
```

## Number Formats

```python
NUMBER_FORMATS = {
    'currency': '$#,##0;($#,##0);"-"',        # Parentheses for negatives
    'currency_mm': '$#,##0,,"mm";($#,##0,,"mm");"-"',
    'percent': '0.0%;(0.0%);"-"',             # One decimal
    'multiple': '0.0x;(0.0x);"-"',            # Valuation multiples
    'number': '#,##0;(#,##0);"-"',            # General numbers
    'year': '0',                               # No commas for years
}
```

## Font & Layout Rules
- **One font only**: Arial or Calibri, 10-11pt
- **Bold**: Titles and total rows only
- **Alignment**: Right-align numbers, left-align text
- **Indent**: Subordinate line items
- **Never hide rows**: Use grouping instead (Alt+Shift+→)

---

# PART 7: KEYBOARD SHORTCUTS

## Essential IB Shortcuts

| Shortcut | Action | Context |
|----------|--------|---------|
| **F2** | Edit cell / Toggle reference mode | Formula editing |
| **F4** | Toggle absolute/relative reference ($) | Building formulas |
| **F9** | Recalculate / Evaluate formula part | Debugging |
| **Ctrl+[** | Go to precedent cells | Model auditing |
| **Ctrl+]** | Go to dependent cells | Model auditing |
| **Ctrl+`** | Show/hide formulas | Review mode |
| **Ctrl+Shift+U** | Expand formula bar | Long formulas |

## Navigation & Selection

| Shortcut | Action |
|----------|--------|
| **Ctrl+Arrow** | Jump to edge of data |
| **Ctrl+Shift+Arrow** | Select to edge of data |
| **Ctrl+Home** | Go to cell A1 |
| **Ctrl+End** | Go to last used cell |
| **Ctrl+Page Up/Down** | Switch worksheets |
| **Ctrl+Space** | Select entire column |
| **Shift+Space** | Select entire row |

## Formatting & Editing

| Shortcut | Action |
|----------|--------|
| **Ctrl+1** | Format Cells dialog |
| **Ctrl+Shift+1** | Number format |
| **Ctrl+Shift+4** | Currency format |
| **Ctrl+Shift+5** | Percentage format |
| **Alt+E+S+V** | Paste Values |
| **Alt+E+S+T** | Paste Formats |
| **Alt+H+O+I** | AutoFit column width |
| **Ctrl+;** | Insert current date |

## Data Tables & Analysis

| Shortcut | Action |
|----------|--------|
| **Alt+A+W+T** | Data Table dialog |
| **Alt+A+W+G** | Goal Seek |
| **Alt+A+W+S** | Solver |
| **Alt+Shift+→** | Group rows/columns |
| **Alt+Shift+←** | Ungroup rows/columns |

---

# PART 8: WORKFLOW CHECKLIST

## Before Building
- [ ] Define all assumptions in dedicated Assumptions tab
- [ ] Plan sheet structure: Cover → Assumptions → Schedules → Statements → Valuation → Output
- [ ] Establish naming conventions
- [ ] Set up circuit breaker for circular references if needed

## During Build
- [ ] Use formulas, NEVER hardcode calculations
- [ ] Apply color coding consistently (blue inputs, black formulas)
- [ ] Link everything to assumptions
- [ ] Wrap divisions with IFERROR
- [ ] Wrap lookups with IFNA
- [ ] Use MEDIAN not AVERAGE for comps

## After Build
- [ ] Run `recalc.py` to calculate all formulas
- [ ] Run error scan - fix any #REF!, #DIV/0!, etc.
- [ ] Verify no unintended circular references
- [ ] Check all model integrity tests pass
- [ ] Validate balance sheet balances
- [ ] Verify cash ties to cash flow statement
- [ ] Test sensitivity tables work correctly
- [ ] Review formulas with Ctrl+` (formula view)

## Before Delivery
- [ ] Remove any modern functions (XLOOKUP, FILTER) if sharing externally
- [ ] Test on target Excel version
- [ ] Protect input cells if needed
- [ ] Add documentation/instructions tab
