# Color Palette Reference

## Primary Colors

| Name | Hex | RGB | Use Case |
|------|-----|-----|----------|
| Navy | #1F3864 | rgb(31, 56, 100) | Headers, titles, table headers |
| Dark Navy | #0D1B2A | rgb(13, 27, 42) | Heavy emphasis |
| Black | #000000 | rgb(0, 0, 0) | Body text, data cells |
| Dark Gray | #404040 | rgb(64, 64, 64) | Secondary text |
| Medium Gray | #595959 | rgb(89, 89, 89) | Footnotes, tertiary text |
| Light Gray | #808080 | rgb(128, 128, 128) | NA/NM values, page numbers |
| Very Light Gray | #BFBFBF | rgb(191, 191, 191) | Hairline borders |
| White | #FFFFFF | rgb(255, 255, 255) | Backgrounds, reversed text |

---

## Table Shading

| Purpose | Hex | Use Case |
|---------|-----|----------|
| Header background | #1F3864 | Table header row |
| Sub-header background | #D6DCE5 | Category rows |
| Alternate row (even) | #F7F7F7 | Zebra striping |
| Alternate row (odd) | #FFFFFF | Zebra striping |
| Subtotal row | #F2F2F2 | Subtotal emphasis |
| Total row | #E6E6E6 | Total emphasis |
| Grand total row | #D9D9D9 | Grand total emphasis |

---

## Conditional Formatting

### Positive/Negative

| Condition | Text Color | Background |
|-----------|------------|------------|
| Positive | #375623 | #E2EFDA |
| Negative | #C00000 | #FFC7CE |
| Neutral | #000000 | — |

### Highlights

| Purpose | Text Color | Background |
|---------|------------|------------|
| Mean/Median | #806000 | #FFF2CC |
| Implied value | #375623 | #E2EFDA |
| Warning | #C00000 | #FFF0F0 |
| Info | #000000 | #F5F5F5 |
| Key highlight | #1F3864 | #E8F1F8 |

### Percentile Heat Map

| Percentile | Background |
|------------|------------|
| Top 10% | #C6EFCE |
| Top 25% | #E2EFDA |
| Middle 50% | #FFFFFF |
| Bottom 25% | #FFEB9C |
| Bottom 10% | #FFC7CE |

---

## Accent Colors

| Name | Hex | Use Case |
|------|-----|----------|
| Blue Accent | #4472C4 | Charts, hyperlinks |
| Green | #375623 | Positive values text |
| Green Light | #E2EFDA | Positive background |
| Green Medium | #C6EFCE | Top percentile |
| Red | #C00000 | Negative values text |
| Red Light | #FFC7CE | Negative background |
| Yellow/Gold | #806000 | Mean/median text |
| Yellow Light | #FFF2CC | Highlight background |
| Orange | #ED7D31 | Warnings |

---

## Border Colors

| Purpose | Hex |
|---------|-----|
| Hairline borders | #BFBFBF |
| Standard borders | #A6A6A6 |
| Header bottom | #808080 |
| Total top (heavy) | #404040 |
| Outer frame | #000000 |

---

## Usage in Code

```javascript
// Color constants
const colors = {
  // Primary
  navy: "1F3864",
  darkNavy: "0D1B2A",
  black: "000000",
  darkGray: "404040",
  mediumGray: "595959",
  lightGray: "808080",
  veryLightGray: "BFBFBF",
  white: "FFFFFF",
  
  // Table shading
  headerBg: "1F3864",
  subHeaderBg: "D6DCE5",
  alternateRow: "F7F7F7",
  subtotalRow: "F2F2F2",
  totalRow: "E6E6E6",
  grandTotalRow: "D9D9D9",
  
  // Conditional
  positiveText: "375623",
  positiveBg: "E2EFDA",
  negativeText: "C00000",
  negativeBg: "FFC7CE",
  highlightText: "806000",
  highlightBg: "FFF2CC",
  infoBg: "F5F5F5",
  keyHighlightBg: "E8F1F8",
  
  // Accent
  blueAccent: "4472C4",
  orange: "ED7D31"
};

// Apply to table cell
new TableCell({
  shading: { fill: colors.headerBg, type: ShadingType.CLEAR },
  children: [
    new Paragraph({
      children: [
        new TextRun({ text: "Header", color: colors.white, bold: true })
      ]
    })
  ]
});
```
