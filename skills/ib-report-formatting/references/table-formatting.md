# Table Formatting Reference

## DXA Unit Reference

All measurements in docx-js use DXA (twentieths of a point):
- **1 inch = 1440 DXA**
- **1 point = 20 DXA**
- **1 cm ≈ 567 DXA**

| Inches | DXA | Common Use |
|--------|-----|------------|
| 0.25" | 360 | Small indent |
| 0.5" | 720 | Standard indent |
| 0.75" | 1080 | Large indent |
| 1.0" | 1440 | Margin |
| 8.5" | 12240 | Letter width |
| 11.0" | 15840 | Letter height |

---

## Column Width Standards

### By Content Type

| Column Type | Width (DXA) | Width (inches) |
|-------------|-------------|----------------|
| Ticker | 720–900 | 0.5–0.625" |
| Date | 1080–1296 | 0.75–0.9" |
| Company Name | 2160–2880 | 1.5–2.0" |
| Currency | 1296–1584 | 0.9–1.1" |
| Multiple | 1080–1296 | 0.75–0.9" |
| Percentage | 1008–1296 | 0.7–0.9" |
| Description | 2880–4320 | 2.0–3.0" |
| Flag/Check | 576–720 | 0.4–0.5" |

### Comparable Companies Table (9360 DXA = full width, 1" margins)

| Column | Ratio | DXA |
|--------|-------|-----|
| Company Name | 22% | 2059 |
| Ticker | 8% | 749 |
| Market Cap | 12% | 1123 |
| EV | 12% | 1123 |
| LTM Revenue | 11% | 1030 |
| LTM EBITDA | 11% | 1030 |
| EV/Revenue | 12% | 1123 |
| EV/EBITDA | 12% | 1123 |

```javascript
const compsColumnWidths = [2059, 749, 1123, 1123, 1030, 1030, 1123, 1123];
```

### Precedent Transactions Table (9360 DXA)

| Column | Ratio | DXA |
|--------|-------|-----|
| Date | 10% | 936 |
| Acquirer | 20% | 1872 |
| Target | 20% | 1872 |
| EV ($mm) | 15% | 1404 |
| EV/Revenue | 17.5% | 1638 |
| EV/EBITDA | 17.5% | 1638 |

```javascript
const precedentColumnWidths = [936, 1872, 1872, 1404, 1638, 1638];
```

### DCF Sensitivity Matrix (7020 DXA = 75% width, centered)

| Column | Ratio | DXA |
|--------|-------|-----|
| Row Label (WACC) | 20% | 1404 |
| TG Column (×6) | ~13.3% each | 936 |

```javascript
const dcfColumnWidths = [1404, 936, 936, 936, 936, 936, 936];
```

---

## Row Height Standards

| Row Type | Height (DXA) | Height (pt) |
|----------|--------------|-------------|
| Header row | 432–576 | 21.6–28.8 |
| Data row (standard) | 288–360 | 14.4–18 |
| Data row (dense) | 252–288 | 12.6–14.4 |
| Subtotal row | 324–396 | 16.2–19.8 |
| Total row | 396–504 | 19.8–25.2 |
| Section header | 504–648 | 25.2–32.4 |

---

## Cell Padding Standards

| Mode | Top/Bottom (DXA) | Left/Right (DXA) | Use Case |
|------|------------------|------------------|----------|
| Tight | 29–43 | 43–72 | Dense financial tables |
| Standard | 43–72 | 72–115 | General tables |
| Comfortable | 72–115 | 115–144 | Summary tables |
| Generous | 115–173 | 144–216 | Callout boxes |

---

## Border Specifications

### Border Styles

| Type | BorderStyle | Size | Color | Use |
|------|-------------|------|-------|-----|
| Hairline | SINGLE | 4 | BFBFBF | Internal |
| Light | SINGLE | 8 | A6A6A6 | Standard |
| Medium | SINGLE | 12 | 808080 | Header bottom |
| Heavy | SINGLE | 18 | 404040 | Total top |
| Double | DOUBLE | 4 | 000000 | Grand total |
| None | NIL | 0 | — | Clean look |

### IB Standard Pattern (Minimal)

Goldman/Morgan Stanley style:
- **No vertical borders**
- **Header bottom**: Medium (size 12, #808080)
- **Total row top**: Heavy (size 18, #404040)
- **No outer frame**

```javascript
const noBorder = { style: BorderStyle.NIL };
const headerBottom = { style: BorderStyle.SINGLE, size: 12, color: "808080" };
const totalTop = { style: BorderStyle.SINGLE, size: 18, color: "404040" };

// Header cell borders
const headerBorders = {
  top: noBorder,
  bottom: headerBottom,
  left: noBorder,
  right: noBorder
};

// Data cell borders
const dataBorders = {
  top: noBorder,
  bottom: noBorder,
  left: noBorder,
  right: noBorder
};

// Total row borders
const totalBorders = {
  top: totalTop,
  bottom: noBorder,
  left: noBorder,
  right: noBorder
};
```

---

## Row Shading

| Row Type | Fill Color | Text Color | Font Weight |
|----------|------------|------------|-------------|
| Header | 1F3864 | FFFFFF | Bold |
| Sub-header | D6DCE5 | 1F3864 | Bold |
| Data (odd) | FFFFFF | 000000 | Regular |
| Data (even) | F7F7F7 | 000000 | Regular |
| Subtotal | F2F2F2 | 000000 | Bold |
| Total | E6E6E6 | 000000 | Bold |
| Grand Total | D9D9D9 | 000000 | Bold |
| Mean/Median | FFF2CC | 806000 | Bold Italic |
| Implied Value | E2EFDA | 375623 | Bold |

```javascript
// Alternating row shading
function getRowShading(rowIndex) {
  return rowIndex % 2 === 0 
    ? { fill: "F7F7F7", type: ShadingType.CLEAR }
    : undefined; // White (default)
}
```

---

## Implementation Template

```javascript
const { Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
        AlignmentType, VerticalAlign, Paragraph, TextRun } = require('docx');

// Complete table creation
function createCompsTable(data) {
  const colWidths = [2059, 749, 1123, 1123, 1030, 1030, 1123, 1123];
  const noBorder = { style: BorderStyle.NIL };
  const headerBottom = { style: BorderStyle.SINGLE, size: 12, color: "808080" };
  
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    columnWidths: colWidths,
    rows: [
      // Header row
      new TableRow({
        tableHeader: true,
        height: { value: 504, rule: "atLeast" },
        children: [
          createHeaderCell("Company", colWidths[0]),
          createHeaderCell("Ticker", colWidths[1]),
          createHeaderCell("Mkt Cap", colWidths[2]),
          createHeaderCell("EV", colWidths[3]),
          createHeaderCell("Revenue", colWidths[4]),
          createHeaderCell("EBITDA", colWidths[5]),
          createHeaderCell("EV/Rev", colWidths[6]),
          createHeaderCell("EV/EBITDA", colWidths[7]),
        ]
      }),
      // Data rows
      ...data.map((row, i) => createDataRow(row, i, colWidths))
    ]
  });
}

function createHeaderCell(text, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { fill: "1F3864", type: ShadingType.CLEAR },
    borders: {
      top: { style: BorderStyle.NIL },
      bottom: { style: BorderStyle.SINGLE, size: 12, color: "808080" },
      left: { style: BorderStyle.NIL },
      right: { style: BorderStyle.NIL }
    },
    margins: { top: 72, bottom: 72, left: 72, right: 72 },
    verticalAlign: VerticalAlign.CENTER,
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text, bold: true, color: "FFFFFF", font: "Arial", size: 18 })
        ]
      })
    ]
  });
}

function createDataCell(text, width, alignment, rowIndex) {
  const isEven = rowIndex % 2 === 0;
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: isEven ? { fill: "F7F7F7", type: ShadingType.CLEAR } : undefined,
    borders: {
      top: { style: BorderStyle.NIL },
      bottom: { style: BorderStyle.NIL },
      left: { style: BorderStyle.NIL },
      right: { style: BorderStyle.NIL }
    },
    margins: { top: 43, bottom: 43, left: 72, right: 72 },
    verticalAlign: VerticalAlign.CENTER,
    children: [
      new Paragraph({
        alignment: alignment,
        children: [
          new TextRun({ text, font: "Arial", size: 18 })
        ]
      })
    ]
  });
}
```

---

## Advanced Table Features

### Header Row Repeat (Multi-Page Tables)

For tables spanning multiple pages, repeat headers:

```javascript
new TableRow({
  tableHeader: true, // This row repeats on each page
  children: [/* header cells */]
})
```

### Prevent Row Breaking Across Pages

```javascript
new TableRow({
  cantSplit: true, // Keep entire row on same page
  children: [/* cells */]
})
```

### Row Height Control

```javascript
const { HeightRule } = require('docx');

// Exact height (fixed)
new TableRow({
  height: { value: 360, rule: HeightRule.EXACT },
  children: [/* cells */]
})

// Minimum height (can expand)
new TableRow({
  height: { value: 288, rule: HeightRule.ATLEAST },
  children: [/* cells */]
})
```

---

## Table Formulas

Calculate values directly in table cells:

```javascript
const { SimpleField } = require('docx');

// Sum column above
new TableCell({
  children: [
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      children: [
        new SimpleField({ instruction: '= SUM(ABOVE) \\# "$#,##0.0"' })
      ]
    })
  ]
})

// Available functions
// SUM(ABOVE), SUM(LEFT), SUM(BELOW), SUM(RIGHT)
// AVERAGE(ABOVE), COUNT(ABOVE), MAX(ABOVE), MIN(ABOVE), PRODUCT(ABOVE)

// Cell references (A1 notation)
new SimpleField({ instruction: '= B2 + B3 + B4 \\# "#,##0"' })

// Range sum
new SimpleField({ instruction: '= SUM(B2:B10) \\# "$#,##0"' })
```

---

## Nested Tables

Tables within table cells:

```javascript
new TableCell({
  children: [
    new Table({
      width: { size: 100, type: WidthType.PERCENTAGE },
      rows: [
        new TableRow({
          children: [
            new TableCell({
              children: [new Paragraph({ children: [new TextRun("Nested content")] })]
            })
          ]
        })
      ]
    })
  ]
})
```

---

## Cell Merging

### Horizontal Merge (Column Span)

```javascript
new TableRow({
  children: [
    new TableCell({
      columnSpan: 3, // Span 3 columns
      children: [new Paragraph({ children: [new TextRun("Merged across 3 columns")] })]
    }),
    new TableCell({
      children: [new Paragraph({ children: [new TextRun("Regular cell")] })]
    })
  ]
})
```

### Vertical Merge (Row Span)

```javascript
// First row - start of merge
new TableRow({
  children: [
    new TableCell({
      rowSpan: 3, // Span 3 rows
      verticalAlign: VerticalAlign.CENTER,
      children: [new Paragraph({ children: [new TextRun("Spans 3 rows")] })]
    }),
    new TableCell({ children: [/* content */] })
  ]
})

// Subsequent rows - merged cells are omitted
new TableRow({
  children: [
    // No cell here - it's merged from above
    new TableCell({ children: [/* content */] })
  ]
})
```

---

## Text Direction in Cells

```javascript
const { TextDirection } = require('docx');

new TableCell({
  textDirection: TextDirection.BOTTOM_TO_TOP_LEFT_TO_RIGHT,
  // Options:
  // LEFT_TO_RIGHT_TOP_TO_BOTTOM (default)
  // TOP_TO_BOTTOM_RIGHT_TO_LEFT (vertical)
  // BOTTOM_TO_TOP_LEFT_TO_RIGHT (vertical, rotated)
  children: [/* content */]
})
```

---

## Table Positioning

### Floating Table

```javascript
new Table({
  float: {
    horizontalAnchor: TableAnchorType.PAGE,
    verticalAnchor: TableAnchorType.PAGE,
    relativeHorizontalPosition: RelativeHorizontalPosition.CENTER,
    relativeVerticalPosition: RelativeVerticalPosition.TOP,
    overlap: OverlapType.NEVER,
    topFromText: 720,
    bottomFromText: 720
  },
  rows: [/* rows */]
})
```

---

## Additional IB Table Templates

### Sources & Uses Table

```javascript
const sourcesUsesWidths = [2340, 1170, 1170, 360, 2340, 1170, 1170];
// Sources (50%) | $mm | % | spacer | Uses (50%) | $mm | %
```

### LBO Returns Table

```javascript
const lboWidths = [1872, 936, 936, 936, 936, 936, 936, 936];
// Metric | Entry | Y1 | Y2 | Y3 | Y4 | Y5 | Exit
```

### Pro Forma Capitalization

```javascript
const capTableWidths = [2808, 1404, 1404, 1404, 1404, 936];
// Description | Pre-Transaction | Adjustments | Pro Forma | % of Total | Notes
```

### Football Field (Valuation Summary)

```javascript
// This is typically a visual chart, but can be approximated with:
const footballWidths = [2340, 1170, 1170, 4680];
// Methodology | Low | High | Bar (use shading to show range)
```
