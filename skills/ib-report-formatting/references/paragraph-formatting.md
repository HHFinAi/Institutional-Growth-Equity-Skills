# Paragraph Formatting Reference (38 Properties)

## Alignment Types

| Type | Constant | Use Case |
|------|----------|----------|
| Left | `AlignmentType.LEFT` | Body text, labels, descriptions |
| Center | `AlignmentType.CENTER` | Titles, dates, tickers |
| Right | `AlignmentType.RIGHT` | Numbers, page numbers |
| Justified | `AlignmentType.JUSTIFIED` | Legal documents, formal text |
| Distributed | `AlignmentType.DISTRIBUTED` | Asian typography |

```javascript
new Paragraph({
  alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun("Legal disclaimer text...")]
})
```

---

## Indentation

### Indentation Types

| Type | Property | Use Case |
|------|----------|----------|
| Left | `indent.left` | Bullets, quotes, nested content |
| Right | `indent.right` | Pull quotes, annotations |
| First line | `indent.firstLine` | Traditional paragraphs |
| Hanging | `indent.hanging` | Numbered lists, bibliographies |

### Standard Indent Values (DXA)

| Level | DXA | Inches |
|-------|-----|--------|
| Level 1 | 360 | 0.25" |
| Level 2 | 720 | 0.5" |
| Level 3 | 1080 | 0.75" |
| Level 4 | 1440 | 1.0" |

```javascript
// Hanging indent for numbered paragraph
new Paragraph({
  indent: {
    left: 720,    // 0.5" total indent
    hanging: 360  // Number hangs 0.25"
  },
  children: [
    new TextRun({ text: "1.", bold: true }),
    new TextRun("  First item description")
  ]
})

// Block quote
new Paragraph({
  indent: {
    left: 720,
    right: 720
  },
  children: [new TextRun({ text: "Management believes...", italics: true })]
})
```

---

## Line Spacing

### Line Spacing Types

| Type | Value | Rule | Use Case |
|------|-------|------|----------|
| Single | 240 | AUTO | Dense tables |
| 1.15 | 276 | AUTO | Standard body |
| 1.5 | 360 | AUTO | Comfortable |
| Double | 480 | AUTO | Legal drafts |
| Exactly | Custom | EXACT | Precise control |
| At Least | Custom | AT_LEAST | Minimum height |

```javascript
// Standard body text (1.15 spacing)
new Paragraph({
  spacing: {
    line: 276,
    lineRule: LineRuleType.AUTO
  },
  children: [new TextRun("Body paragraph text...")]
})

// Exact 12pt line height
new Paragraph({
  spacing: {
    line: 240, // 12pt in twips
    lineRule: LineRuleType.EXACT
  },
  children: [new TextRun("Fixed height text")]
})
```

### Paragraph Spacing (Before/After)

| Element | Before (twips) | After (twips) |
|---------|----------------|---------------|
| Title | 0 | 480 |
| Heading 1 | 480 | 240 |
| Heading 2 | 360 | 180 |
| Heading 3 | 240 | 120 |
| Body | 0 | 160 |
| Bullet | 0 | 80 |
| Footnote | 120 | 60 |

```javascript
new Paragraph({
  spacing: {
    before: 480,
    after: 240
  },
  children: [new TextRun({ text: "Section Title", bold: true, size: 28 })]
})
```

---

## Tab Stops

### Tab Stop Types

| Type | Constant | Description |
|------|----------|-------------|
| Left | `TabStopType.LEFT` | Text starts at tab |
| Center | `TabStopType.CENTER` | Text centered on tab |
| Right | `TabStopType.RIGHT` | Text ends at tab |
| Decimal | `TabStopType.DECIMAL` | Aligns on decimal point |
| Bar | `TabStopType.BAR` | Vertical line |

### Tab Leaders

| Type | Constant | Appearance |
|------|----------|------------|
| None | `LeaderType.NONE` | (blank) |
| Dot | `LeaderType.DOT` | ........... |
| Hyphen | `LeaderType.HYPHEN` | ----------- |
| Underscore | `LeaderType.UNDERSCORE` | ___________ |

```javascript
// Table of contents style
new Paragraph({
  tabStops: [
    { type: TabStopType.RIGHT, position: 9360, leader: LeaderType.DOT }
  ],
  children: [
    new TextRun("Executive Summary"),
    new TextRun({ children: [new Tab()] }),
    new TextRun("3")
  ]
})

// Financial alignment
new Paragraph({
  tabStops: [
    { type: TabStopType.LEFT, position: 720 },
    { type: TabStopType.DECIMAL, position: 5760 },
    { type: TabStopType.DECIMAL, position: 7920 }
  ],
  children: [
    new TextRun("Revenue"),
    new TextRun({ children: [new Tab()] }),
    new TextRun("$1,234.5"),
    new TextRun({ children: [new Tab()] }),
    new TextRun("$1,456.7")
  ]
})
```

---

## Pagination Control

### Properties

| Property | Use Case | Implementation |
|----------|----------|----------------|
| Widow/Orphan | Prevent single lines | `widowControl: true` |
| Keep with next | Header + content | `keepNext: true` |
| Keep lines together | Small tables | `keepLines: true` |
| Page break before | New sections | `pageBreakBefore: true` |

```javascript
// Section header that stays with content
new Paragraph({
  keepNext: true,
  children: [new TextRun({ text: "Valuation Analysis", bold: true, size: 28 })]
})

// Force new page
new Paragraph({
  pageBreakBefore: true,
  children: [new TextRun({ text: "Appendix A", bold: true, size: 28 })]
})

// Keep paragraph together
new Paragraph({
  keepLines: true,
  children: [new TextRun("This entire paragraph must stay on one page...")]
})
```

---

## Paragraph Borders

### Border Positions

| Position | Property | Use Case |
|----------|----------|----------|
| Top | `border.top` | Section divider |
| Bottom | `border.bottom` | Underline effect |
| Left | `border.left` | Quote indicator |
| Right | `border.right` | Annotation |
| Between | `border.between` | Multi-para group |

### Border Styles

| Style | Constant | Appearance |
|-------|----------|------------|
| Single | `BorderStyle.SINGLE` | ─────── |
| Double | `BorderStyle.DOUBLE` | ═══════ |
| Dotted | `BorderStyle.DOTTED` | ······· |
| Dashed | `BorderStyle.DASHED` | - - - - |
| Thick | `BorderStyle.THICK` | ━━━━━━━ |

```javascript
// Callout with left border
new Paragraph({
  border: {
    left: { style: BorderStyle.SINGLE, size: 24, color: "1F3864", space: 10 }
  },
  indent: { left: 360 },
  shading: { fill: "E8F1F8", type: ShadingType.CLEAR },
  children: [new TextRun("Key investment thesis...")]
})

// Section divider
new Paragraph({
  border: {
    bottom: { style: BorderStyle.SINGLE, size: 12, color: "808080", space: 1 }
  },
  spacing: { after: 240 }
})
```

---

## Paragraph Shading

```javascript
new Paragraph({
  shading: {
    fill: "FFF2CC", // Yellow highlight
    type: ShadingType.CLEAR
  },
  children: [new TextRun({ text: "Key Assumption:", bold: true })]
})
```

### Common Shading Colors

| Purpose | Hex | Use |
|---------|-----|-----|
| Highlight | #FFF2CC | Key assumptions |
| Info | #E8F1F8 | Notes, context |
| Warning | #FFF0F0 | Risk factors |
| Success | #E2EFDA | Positive highlights |
| Neutral | #F5F5F5 | Background emphasis |

---

## Drop Caps

For chapter or section openings:

```javascript
// Note: Limited support in docx-js, requires XML manipulation
// Typical settings:
// - Type: DROP (in margin) or MARGIN (inline)
// - Lines: 2-3 (height in lines)
// - Distance: 0-720 DXA (space from following text)
```

---

## Outline Level

Required for Table of Contents generation:

```javascript
// Heading that appears in TOC
new Paragraph({
  heading: HeadingLevel.HEADING_1, // Sets outlineLevel automatically
  children: [new TextRun({ text: "Executive Summary", bold: true })]
})

// Or manually set outline level
new Paragraph({
  outlineLevel: 0, // Level 1 heading (0-indexed)
  children: [new TextRun({ text: "Custom Heading", bold: true })]
})
```

---

## Right-to-Left Text

For international documents:

```javascript
new Paragraph({
  bidirectional: true, // Enable RTL
  children: [new TextRun({ text: "Hebrew or Arabic text", rightToLeft: true })]
})
```

---

## Complete Example: IB Report Section

```javascript
const sectionContent = [
  // Section title
  new Paragraph({
    pageBreakBefore: true,
    keepNext: true,
    spacing: { after: 360 },
    children: [
      new TextRun({
        text: "VALUATION ANALYSIS",
        font: "Arial",
        size: 28,
        bold: true,
        color: "1F3864",
        allCaps: true
      })
    ]
  }),
  
  // Horizontal rule
  new Paragraph({
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 18, color: "1F3864", space: 1 }
    },
    spacing: { after: 360 }
  }),
  
  // Intro paragraph
  new Paragraph({
    spacing: { after: 200, line: 276, lineRule: LineRuleType.AUTO },
    alignment: AlignmentType.JUSTIFIED,
    children: [
      new TextRun({
        text: "We have performed a comprehensive valuation analysis using multiple methodologies including comparable company analysis, precedent transactions, and discounted cash flow analysis.",
        font: "Arial",
        size: 20
      })
    ]
  }),
  
  // Callout box
  new Paragraph({
    border: {
      left: { style: BorderStyle.SINGLE, size: 24, color: "1F3864", space: 10 }
    },
    shading: { fill: "E8F1F8", type: ShadingType.CLEAR },
    indent: { left: 360 },
    spacing: { before: 240, after: 240 },
    children: [
      new TextRun({
        text: "Implied Valuation Range: $45.00 - $55.00 per share",
        font: "Arial",
        size: 22,
        bold: true,
        color: "1F3864"
      })
    ]
  })
];
```
