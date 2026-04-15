# Number Formatting Reference

## Alignment Rules

| Data Type | Alignment | Vertical |
|-----------|-----------|----------|
| Text labels | Left | Center |
| Company names | Left | Center |
| Descriptions | Left | Top |
| Integers | Right | Center |
| Decimals | Right | Center |
| Currencies | Right | Center |
| Percentages | Right | Center |
| Multiples | Right | Center |
| Dates | Center | Center |
| Tickers | Center | Center |
| NA/NM values | Center | Center |
| Checkmarks | Center | Center |

---

## Decimal Place Standards

| Data Type | Decimals | Example |
|-----------|----------|---------|
| Revenue/EBITDA ($mm) | 1 | 1,234.5 |
| Revenue/EBITDA ($bn) | 2 | 12.34 |
| Enterprise Value ($mm) | 1 | 5,678.9 |
| Market Cap ($mm) | 1 | 2,345.6 |
| Share price | 2 | 145.67 |
| EV/Revenue multiple | 2 | 3.45x |
| EV/EBITDA multiple | 1 | 12.5x |
| P/E multiple | 1 | 18.5x |
| Gross margin | 1 | 45.5% |
| EBITDA margin | 1 | 25.5% |
| Growth rates | 1 | 12.3% |
| Discount rate/WACC | 2 | 9.50% |
| Terminal growth | 2 | 2.50% |
| Interest rate | 3 | 5.375% |
| Basis points | 0 | 150 bps |

---

## Currency Formatting

| Format | Pattern | Example | Use Case |
|--------|---------|---------|----------|
| Full with symbol | $#,##0.0 | $1,234.5 | Standalone values |
| Negative (parens) | ($#,##0.0) | ($1,234.5) | Financial statements |
| Header-indicated | #,##0.0 | 1,234.5 | When unit in header |
| Millions | $#,##0.0mm | $1,234.5mm | Large values |
| Billions | $#,##0.00bn | $1.23bn | Very large values |

---

## Multiple Formatting

| Type | Format | Example |
|------|--------|---------|
| Standard | #,##0.0x | 12.5x |
| High precision | #,##0.00x | 12.45x |
| Range | #,##0.0x – #,##0.0x | 10.5x – 14.5x |

Always use lowercase "x" for multiples.

---

## Negative Number Handling

| Style | Format | Example | Use Case |
|-------|--------|---------|----------|
| Parentheses | (#,##0.0) | (1,234.5) | IB standard |
| Parentheses red | (#,##0.0) in red | (1,234.5) | Emphasis |
| Minus sign | -#,##0.0 | -1,234.5 | Mathematical |

**IB Standard**: Always use parentheses for negative numbers, optionally in red (#C00000).

---

## Special Value Handling

| Condition | Display | Alignment | Color | Style |
|-----------|---------|-----------|-------|-------|
| Not Available | NA | Center | #808080 | Italic |
| Not Meaningful | NM | Center | #808080 | Italic |
| Not Applicable | N/A | Center | #808080 | Italic |
| Zero | — | Center | #808080 | Regular |
| Confidential | Conf. | Center | #808080 | Italic |
| To Be Determined | TBD | Center | #808080 | Italic |
| Estimate | 1,234.5E | Right | #000000 | Italic |
| Preliminary | 1,234.5 (P) | Right | #000000 | Regular |
| Restated | 1,234.5 (R) | Right | #000000 | Regular |

---

## Implementation

```javascript
// Format currency
function formatCurrency(value, decimals = 1, showSymbol = false) {
  if (value === null || value === undefined) return "NA";
  if (!isFinite(value)) return "NM";
  
  const formatted = Math.abs(value).toLocaleString('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  });
  
  const prefix = showSymbol ? "$" : "";
  return value < 0 ? `(${prefix}${formatted})` : `${prefix}${formatted}`;
}

// Format multiple with "x" suffix
function formatMultiple(value, decimals = 1) {
  if (value === null || value === undefined) return "NA";
  if (!isFinite(value) || value <= 0) return "NM";
  
  return value.toLocaleString('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  }) + "x";
}

// Format percentage
function formatPercentage(value, decimals = 1) {
  if (value === null || value === undefined) return "NA";
  if (!isFinite(value)) return "NM";
  
  const pct = (value * 100).toFixed(decimals);
  return value < 0 ? `(${Math.abs(pct)}%)` : `${pct}%`;
}

// Format with conditional styling
function getNumberStyle(value, text) {
  // Default style
  let style = { color: "000000", italics: false, alignment: AlignmentType.RIGHT };
  
  // Special values
  if (text === "NA" || text === "NM" || text === "—") {
    style.color = "808080";
    style.italics = true;
    style.alignment = AlignmentType.CENTER;
  }
  // Negative values
  else if (text.startsWith("(") || value < 0) {
    style.color = "C00000";
  }
  
  return style;
}

// Create formatted number cell
function createNumberCell(value, format, width) {
  let text;
  switch (format) {
    case "currency": text = formatCurrency(value); break;
    case "currencySymbol": text = formatCurrency(value, 1, true); break;
    case "multiple": text = formatMultiple(value); break;
    case "multiplePrecise": text = formatMultiple(value, 2); break;
    case "percentage": text = formatPercentage(value); break;
    default: text = String(value);
  }
  
  const style = getNumberStyle(value, text);
  
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    margins: { top: 43, bottom: 43, left: 72, right: 72 },
    verticalAlign: VerticalAlign.CENTER,
    children: [
      new Paragraph({
        alignment: style.alignment,
        children: [
          new TextRun({
            text: text,
            font: "Arial",
            size: 18,
            color: style.color,
            italics: style.italics
          })
        ]
      })
    ]
  });
}
```

---

## Conditional Formatting

### Value-Based Colors

| Condition | Text Color | Background |
|-----------|------------|------------|
| Positive | #375623 | #E2EFDA (optional) |
| Negative | #C00000 | #FFC7CE (optional) |
| Neutral | #000000 | None |

### Percentile Highlighting

| Percentile | Background |
|------------|------------|
| Top 10% | #C6EFCE |
| Top 25% | #E2EFDA |
| Middle 50% | None |
| Bottom 25% | #FFEB9C |
| Bottom 10% | #FFC7CE |

### Change Indicators

| Change | Symbol | Color |
|--------|--------|-------|
| Increase | ▲ | #375623 |
| Decrease | ▼ | #C00000 |
| No change | ◆ | #808080 |

```javascript
function getConditionalFormat(value, baseline = 0) {
  if (value > baseline) {
    return { color: "375623", fill: "E2EFDA" };
  } else if (value < baseline) {
    return { color: "C00000", fill: "FFC7CE" };
  }
  return { color: "000000", fill: null };
}
```
