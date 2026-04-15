# Text Formatting Reference (42 Properties)

## Font Properties

### Font Family Selection by Firm

| Firm | Primary Font | Fallback |
|------|--------------|----------|
| Goldman Sachs | Goldman Sans | Arial |
| JP Morgan | Arial | Helvetica |
| Morgan Stanley | Helvetica | Arial |
| Bank of America | Arial | Calibri |
| Citi | Calibri | Arial |
| UBS | Helvetica | Arial |
| Barclays | Helvetica | Arial |
| Deutsche Bank | Calibri | Arial |
| Lazard | Garamond | Times New Roman |
| Evercore | Garamond | Times New Roman |

### Font Size (Half-Points in docx-js)

| Element | Points | Half-Points | Use |
|---------|--------|-------------|-----|
| Document title | 20 | 40 | Cover page |
| Section header (L1) | 14 | 28 | Major sections |
| Section header (L2) | 12 | 24 | Subsections |
| Section header (L3) | 11 | 22 | Minor sections |
| Body text | 10 | 20 | Paragraphs |
| Table header | 9 | 18 | Column headers |
| Table body | 9 | 18 | Data cells |
| Footnote | 8 | 16 | Source citations |
| Disclaimer | 7 | 14 | Legal text |

### Implementation

```javascript
const textStyles = {
  title: { font: "Arial", size: 40, bold: true, color: "1F3864" },
  heading1: { font: "Arial", size: 28, bold: true, color: "1F3864" },
  heading2: { font: "Arial", size: 24, bold: true, color: "1F3864" },
  heading3: { font: "Arial", size: 22, bold: true, color: "000000" },
  body: { font: "Arial", size: 20, color: "000000" },
  tableHeader: { font: "Arial", size: 18, bold: true, color: "FFFFFF" },
  tableBody: { font: "Arial", size: 18, color: "000000" },
  footnote: { font: "Arial", size: 16, italics: true, color: "595959" },
  disclaimer: { font: "Arial", size: 14, color: "808080" }
};
```

---

## Character Spacing

### Kerning

Adjusts space between specific character pairs for professional typography.

```javascript
new TextRun({
  text: "VALUATION",
  font: "Arial",
  size: 40,
  bold: true,
  kern: 28 // Enable kerning for fonts >= 14pt
})
```

### Character Spacing (Tracking)

| Value | Effect | Use Case |
|-------|--------|----------|
| -20 | Condensed | Dense headers |
| 0 | Normal | Standard text |
| +20 | Expanded | Emphasis |

```javascript
new TextRun({
  text: "Executive Summary",
  characterSpacing: -10 // Twips (1/20 point)
})
```

### Scaling (Horizontal Stretch)

| Percentage | Effect | Use Case |
|------------|--------|----------|
| 80% | Condensed | Fit long text |
| 100% | Normal | Standard |
| 120% | Expanded | Emphasis |

```javascript
new TextRun({
  text: "Confidential",
  scale: 90 // 90% width
})
```

### Position (Raised/Lowered)

| Value | Effect | Use Case |
|-------|--------|----------|
| Positive | Raised | Superscript-like |
| 0 | Normal | Standard |
| Negative | Lowered | Subscript-like |

```javascript
new TextRun({
  text: "1",
  position: 6 // Raised 3pt (half-points)
})
```

---

## Text Effects

### Basic Effects

| Effect | Property | Use Case |
|--------|----------|----------|
| Bold | `bold: true` | Headers, totals |
| Italic | `italics: true` | Footnotes, estimates |
| Underline | `underline: {}` | Links, emphasis |
| Strikethrough | `strike: true` | Deleted text |
| Double strike | `doubleStrike: true` | Strongly rejected |

### Case Transformations

| Effect | Property | Result |
|--------|----------|--------|
| Small caps | `smallCaps: true` | SMALL CAPS |
| All caps | `allCaps: true` | ALL CAPS |

```javascript
// Legal entity name
new TextRun({
  text: "Goldman Sachs & Co. LLC",
  smallCaps: true
})

// Section header
new TextRun({
  text: "Executive Summary",
  allCaps: true,
  bold: true
})
```

### Advanced Effects (Limited in docx-js)

| Effect | Support | Notes |
|--------|---------|-------|
| Shadow | Partial | Via XML manipulation |
| Outline | Partial | Via XML manipulation |
| Emboss | No | Requires Word |
| Engrave | No | Requires Word |
| Reflection | No | Requires Word |
| Glow | No | Requires Word |

---

## Underline Styles

| Style | Constant | Use Case |
|-------|----------|----------|
| Single | `UnderlineType.SINGLE` | Standard links |
| Double | `UnderlineType.DOUBLE` | Total emphasis |
| Thick | `UnderlineType.THICK` | Strong emphasis |
| Dotted | `UnderlineType.DOTTED` | Pending items |
| Dash | `UnderlineType.DASH` | Soft emphasis |
| Dot-dash | `UnderlineType.DOT_DASH` | Mixed |
| Dot-dot-dash | `UnderlineType.DOT_DOT_DASH` | Pattern |
| Wave | `UnderlineType.WAVE` | Errors, warnings |
| Words only | `UnderlineType.WORDS` | Titles |
| None | `UnderlineType.NONE` | Remove underline |

```javascript
new TextRun({
  text: "See Appendix A",
  underline: {
    type: UnderlineType.SINGLE,
    color: "4472C4" // Optional: separate underline color
  }
})
```

---

## Highlight Colors

| Color | Constant | Hex Equivalent |
|-------|----------|----------------|
| Yellow | `HighlightColor.YELLOW` | #FFFF00 |
| Green | `HighlightColor.GREEN` | #00FF00 |
| Cyan | `HighlightColor.CYAN` | #00FFFF |
| Magenta | `HighlightColor.MAGENTA` | #FF00FF |
| Blue | `HighlightColor.BLUE` | #0000FF |
| Red | `HighlightColor.RED` | #FF0000 |
| Dark Blue | `HighlightColor.DARK_BLUE` | #000080 |
| Dark Cyan | `HighlightColor.DARK_CYAN` | #008080 |
| Dark Green | `HighlightColor.DARK_GREEN` | #008000 |
| Dark Magenta | `HighlightColor.DARK_MAGENTA` | #800080 |
| Dark Red | `HighlightColor.DARK_RED` | #800000 |
| Dark Yellow | `HighlightColor.DARK_YELLOW` | #808000 |
| Light Gray | `HighlightColor.LIGHT_GRAY` | #C0C0C0 |
| Dark Gray | `HighlightColor.DARK_GRAY` | #808080 |
| Black | `HighlightColor.BLACK` | #000000 |

```javascript
new TextRun({
  text: "Key Assumption",
  highlight: "yellow"
})
```

---

## Special Characters

### Smart Quotes (XML Entities)

| Character | Entity | Description |
|-----------|--------|-------------|
| ' | `&#x2018;` | Left single quote |
| ' | `&#x2019;` | Right single/apostrophe |
| " | `&#x201C;` | Left double quote |
| " | `&#x201D;` | Right double quote |
| – | `&#x2013;` | En dash |
| — | `&#x2014;` | Em dash |
| … | `&#x2026;` | Ellipsis |
| • | `&#x2022;` | Bullet |

### Symbols for Financial Documents

| Symbol | Unicode | Use |
|--------|---------|-----|
| $ | U+0024 | Dollar |
| € | U+20AC | Euro |
| £ | U+00A3 | Pound |
| ¥ | U+00A5 | Yen |
| % | U+0025 | Percent |
| ‰ | U+2030 | Per mille |
| × | U+00D7 | Multiplication |
| ÷ | U+00F7 | Division |
| ± | U+00B1 | Plus-minus |
| ≈ | U+2248 | Approximately |
| ≤ | U+2264 | Less than or equal |
| ≥ | U+2265 | Greater than or equal |
| ∆ | U+0394 | Delta (change) |

---

## Hidden Text

For draft comments or internal notes that don't print:

```javascript
new TextRun({
  text: "[INTERNAL: Verify with CFO]",
  hidden: true,
  color: "FF0000"
})
```

---

## Complete Example

```javascript
// Professional IB paragraph with mixed formatting
new Paragraph({
  children: [
    new TextRun({
      text: "Investment Highlights",
      font: "Arial",
      size: 28,
      bold: true,
      color: "1F3864",
      allCaps: true
    })
  ],
  spacing: { after: 240 }
}),

new Paragraph({
  children: [
    new TextRun({
      text: "The Company",
      font: "Arial",
      size: 20,
      bold: true
    }),
    new TextRun({
      text: " represents a compelling acquisition opportunity with ",
      font: "Arial",
      size: 20
    }),
    new TextRun({
      text: "strong recurring revenue",
      font: "Arial",
      size: 20,
      bold: true,
      color: "375623"
    }),
    new TextRun({
      text: " and significant margin expansion potential.",
      font: "Arial",
      size: 20
    }),
    new FootnoteReferenceRun({ id: 1 })
  ]
})
```
