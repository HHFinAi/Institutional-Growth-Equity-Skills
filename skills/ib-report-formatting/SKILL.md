---
name: ib-report-formatting
description: "Comprehensive professional formatting for investment banking documents. Use when creating pitch books, CIMs, fairness opinions, valuation reports, offering memoranda, or any financial document requiring institutional-quality formatting. Covers 200+ Word formatting capabilities including text/paragraph formatting, advanced table features, styles/themes, track changes, TOC/references, fields/automation, watermarks, and SEC compliance. Follows Goldman/Morgan Stanley/JP Morgan conventions. Produces polished Word documents via docx-js."
---

# Investment Banking Report Formatting Skill

Comprehensive formatting for institutional-quality financial documents covering all 200+ Word formatting capabilities across 11 categories.

## When to Use This Skill

Trigger on requests involving:
- "Format this table professionally"
- "Create an IB-style report / pitch book / CIM"
- "Format comps table / precedent transactions / DCF / football field"
- "Goldman/Morgan Stanley/JP Morgan style"
- "Add track changes / comments / watermark"
- "Create table of contents / cross-references"
- "SEC filing format / EDGAR compliance"
- "Fairness opinion / offering memorandum format"

## Workflow Overview

1. **Identify document type** – Pitch book, CIM, fairness opinion, valuation report, offering memo
2. **Set page layout** – Orientation, margins, sections, columns, watermarks
3. **Apply styles/themes** – Document-wide consistency, heading hierarchy
4. **Configure headers/footers** – Different first page, odd/even, section-specific
5. **Apply typography** – Font hierarchy, character spacing, text effects
6. **Format paragraphs** – Spacing, indentation, tabs, pagination control
7. **Format tables** – Advanced borders, formulas, nested tables, header repeat
8. **Style numbers** – Decimals, currencies, multiples, conditional formatting
9. **Add references** – TOC, cross-references, footnotes, citations
10. **Insert fields** – Page numbers, dates, document properties, automation
11. **Enable collaboration** – Track changes, comments, document comparison
12. **Output document** – Generate .docx via docx-js

---

## Document Types & Requirements

| Type | Pages | Orientation | Margins | Key Features |
|------|-------|-------------|---------|--------------|
| Pitch Book | 40-60 | Landscape | 0.5"/0.75" | Visual tables, charts, tombstones |
| CIM | 50-150 | Portrait | 1.0" | Watermark, TOC, sections, appendices |
| Fairness Opinion | 2-3 | Portrait | 1.0" | Letter format, numbered paragraphs |
| Valuation Report | 20-50 | Portrait | 0.75" | DCF tables, sensitivity matrices |
| Offering Memo | 100+ | Portrait | 1.0" | SEC compliance, legal formatting |
| Board Deck | 15-30 | Landscape | 0.5" | Executive summary focus |
| Research Report | 10-30 | Portrait | 1.0" | FINRA disclosures, rating charts |

---

## Category 1: Text Formatting (42 Properties)

Read: `references/text-formatting.md`

### Font Properties

| Property | IB Standard | Implementation |
|----------|-------------|----------------|
| Font family | Arial (JP Morgan, BofA), Calibri (Citi), Helvetica (UBS) | `font: "Arial"` |
| Size | 9-10pt tables, 10-11pt body, 14-20pt headers | `size: 20` (half-points) |
| Bold | Headers, totals, labels only | `bold: true` |
| Italic | Footnotes, estimates, NA/NM | `italics: true` |
| Color | See color palette | `color: "1F3864"` |

### Character Spacing

| Property | Use Case | Implementation |
|----------|----------|----------------|
| Kerning | Dense headers | `characterSpacing: -10` (twips) |
| Scaling | Fit text in cells | `scale: 90` (percentage) |
| Position | Superscript refs | `position: 6` (half-points up) |

### Text Effects

| Effect | Use Case | Implementation |
|--------|----------|----------------|
| Small caps | Legal entity names | `smallCaps: true` |
| All caps | Section headers, disclaimers | `allCaps: true` |
| Strikethrough | Track changes | `strike: true` |
| Double strikethrough | Rejected edits | `doubleStrike: true` |
| Hidden | Draft comments | `hidden: true` |

### Underline Styles (10 Types)

| Style | Use Case | Value |
|-------|----------|-------|
| Single | Hyperlinks | `UnderlineType.SINGLE` |
| Double | Total lines | `UnderlineType.DOUBLE` |
| Dotted | Pending items | `UnderlineType.DOTTED` |
| Dash | Cross-references | `UnderlineType.DASH` |
| Wave | Errors | `UnderlineType.WAVE` |

### Highlight Colors (15 Options)

| Color | Hex | Use Case |
|-------|-----|----------|
| Yellow | #FFFF00 | Key assumptions |
| Green | #00FF00 | Approved items |
| Cyan | #00FFFF | Questions |
| Magenta | #FF00FF | Attention needed |
| Red | #FF0000 | Critical issues |

---

## Category 2: Paragraph Formatting (38 Properties)

Read: `references/paragraph-formatting.md`

### Alignment Types

| Type | Use Case | Implementation |
|------|----------|----------------|
| Left | Body text, labels | `AlignmentType.LEFT` |
| Center | Titles, dates | `AlignmentType.CENTER` |
| Right | Numbers, page numbers | `AlignmentType.RIGHT` |
| Justified | Legal documents | `AlignmentType.JUSTIFIED` |
| Distributed | Asian typography | `AlignmentType.DISTRIBUTED` |

### Indentation

| Type | Use Case | Implementation (DXA) |
|------|----------|----------------------|
| Left | Bullets, quotes | `indent: { left: 720 }` |
| Right | Pull quotes | `indent: { right: 720 }` |
| First line | Traditional paragraphs | `indent: { firstLine: 360 }` |
| Hanging | Numbered lists | `indent: { hanging: 360 }` |

### Line Spacing

| Type | Value | Use Case |
|------|-------|----------|
| Single | 240 | Dense tables |
| 1.15 | 276 | Standard body |
| 1.5 | 360 | Comfortable reading |
| Double | 480 | Legal drafts |
| Exactly | Custom | Precise control |
| At least | Minimum | Mixed content |

### Tab Stops (5 Types)

| Type | Use Case | Implementation |
|------|----------|----------------|
| Left | Standard tabs | `TabStopType.LEFT` |
| Center | Centered headings | `TabStopType.CENTER` |
| Right | Right-aligned numbers | `TabStopType.RIGHT` |
| Decimal | Financial columns | `TabStopType.DECIMAL` |
| Bar | Vertical separators | `TabStopType.BAR` |

**Tab Leaders** (4 Types): None, Dots, Hyphens, Underline

### Pagination Control

| Property | Use Case | Implementation |
|----------|----------|----------------|
| Widow/orphan control | Prevent single lines | `widowControl: true` |
| Keep with next | Header + first para | `keepNext: true` |
| Keep lines together | Small tables | `keepLines: true` |
| Page break before | New sections | `pageBreakBefore: true` |

### Paragraph Borders & Shading

```javascript
new Paragraph({
  border: {
    top: { style: BorderStyle.SINGLE, size: 12, color: "1F3864" },
    bottom: { style: BorderStyle.SINGLE, size: 12, color: "1F3864" }
  },
  shading: { fill: "E8F1F8", type: ShadingType.CLEAR }
})
```

### Drop Caps

| Property | Value | Use Case |
|----------|-------|----------|
| Type | DROP or MARGIN | Chapter openings |
| Lines | 2-3 | Height in lines |
| Distance | 0-720 DXA | Space from text |

---

## Category 3: Table Formatting (47 Properties)

Read: `references/table-formatting.md`

### Cell Properties

| Property | Options | Implementation |
|----------|---------|----------------|
| Margins (padding) | top/bottom/left/right | `margins: { top: 72, bottom: 72, left: 72, right: 72 }` |
| Vertical alignment | Top/Center/Bottom | `verticalAlign: VerticalAlign.CENTER` |
| Text direction | Horizontal/Vertical/Rotated | `textDirection: TextDirection.BOTTOM_TO_TOP` |
| Width | Exact/Percentage/Auto | `width: { size: 1440, type: WidthType.DXA }` |

### Row Properties

| Property | Use Case | Implementation |
|----------|----------|----------------|
| Height (exact) | Uniform rows | `height: { value: 360, rule: HeightRule.EXACT }` |
| Height (minimum) | Variable content | `height: { value: 288, rule: HeightRule.ATLEAST }` |
| Header row repeat | Multi-page tables | `tableHeader: true` |
| Prevent row break | Keep rows together | `cantSplit: true` |

### Border Styles (15+ Types)

| Style | Size | Use Case |
|-------|------|----------|
| SINGLE | 4 (hairline) | Internal borders |
| SINGLE | 8 (light) | Standard borders |
| SINGLE | 12 (medium) | Header bottom |
| SINGLE | 18 (heavy) | Total row top |
| DOUBLE | 4 | Grand total |
| DOTTED | 4 | Draft indicators |
| DASHED | 4 | Projections |
| NIL | 0 | No border |

### Table Formulas (IB Critical)

```javascript
// Sum column above
new TableCell({
  children: [new Paragraph({
    children: [new SimpleField({ instruction: "=SUM(ABOVE) \\# \"$#,##0.0\"" })]
  })]
})

// Available functions: SUM, AVERAGE, COUNT, MAX, MIN, PRODUCT
// Positional: ABOVE, BELOW, LEFT, RIGHT
// Cell references: =SUM(B2:B5), =A1*B1
```

### Table Positioning

| Property | Options | Use Case |
|----------|---------|----------|
| Horizontal | Left/Center/Right/Inside/Outside | Page alignment |
| Vertical | Top/Center/Bottom | Vertical position |
| Text wrapping | Around/None | Inline vs floating |
| Distance from text | top/bottom/left/right | Wrapped spacing |

### Nested Tables

```javascript
new TableCell({
  children: [
    new Table({
      // Inner table definition
      rows: [/* nested rows */]
    })
  ]
})
```

### IB Table Templates

**Comparable Companies**
```
| Company | Ticker | Mkt Cap | EV | Revenue | EBITDA | EV/Rev | EV/EBITDA |
| 22%     | 8%     | 12%     | 12%| 11%     | 11%    | 12%    | 12%       |
```

**Precedent Transactions**
```
| Date | Acquirer | Target | EV ($mm) | EV/Revenue | EV/EBITDA |
| 10%  | 20%      | 20%    | 15%      | 17.5%      | 17.5%     |
```

**DCF Sensitivity (WACC vs Terminal Growth)**
```
| WACC↓ \ TG→ | 1.5% | 2.0% | 2.5% | 3.0% | 3.5% |
| 20%         | 16%  | 16%  | 16%  | 16%  | 16%  |
```

**Sources & Uses**
```
| Sources        | $mm  | %    |    | Uses           | $mm  | %    |
| 50%            | 25%  | 25%  |    | 50%            | 25%  | 25%  |
```

**Football Field (Valuation Range)**
```
| Methodology          | Low    | High   | Bar Representation |
| 30%                  | 15%    | 15%    | 40% (visual bar)   |
```

---

## Category 4: Page Layout (31 Properties)

Read: `references/page-setup.md`

### Page Size

| Size | Width (DXA) | Height (DXA) | Use Case |
|------|-------------|--------------|----------|
| US Letter | 12,240 | 15,840 | Standard IB |
| US Letter Landscape | 15,840 | 12,240 | Pitch books |
| US Legal | 12,240 | 20,160 | Legal documents |
| A4 | 11,906 | 16,838 | International |

### Margins

| Document Type | Top | Bottom | Left | Right | Gutter |
|---------------|-----|--------|------|-------|--------|
| Pitch book | 720 | 720 | 1080 | 1080 | 0 |
| Memo | 1440 | 1440 | 1440 | 1440 | 0 |
| CIM | 1440 | 1440 | 1440 | 1440 | 0 |
| Bound report | 1440 | 1440 | 1800 | 1080 | 360 |
| SEC filing | 1440 | 1440 | 1440 | 1440 | 0 |

### Section Breaks (4 Types)

| Type | Use Case | Implementation |
|------|----------|----------------|
| Next Page | New chapters | `SectionType.NEXT_PAGE` |
| Continuous | Column changes | `SectionType.CONTINUOUS` |
| Even Page | Book layout | `SectionType.EVEN_PAGE` |
| Odd Page | Book layout | `SectionType.ODD_PAGE` |

### Columns

```javascript
properties: {
  column: {
    count: 2,
    space: 720, // 0.5" between columns
    equalWidth: true,
    // Or custom widths:
    // children: [{ width: 4320, space: 720 }, { width: 4320 }]
  }
}
```

### Line Numbers

```javascript
properties: {
  lineNumbers: {
    countBy: 1,
    start: 1,
    restart: LineNumberRestartType.NEW_PAGE
  }
}
```

### Watermarks

```javascript
// Text watermark
new TextRun({
  text: "CONFIDENTIAL",
  font: "Arial",
  size: 144, // 72pt
  color: "D9D9D9",
  bold: true
})
// Position in header with rotation
```

### Page Borders

```javascript
properties: {
  pageBorders: {
    display: PageBorderDisplay.ALL_PAGES,
    offsetFrom: PageBorderOffsetFrom.PAGE,
    pageBorderTop: { style: BorderStyle.SINGLE, size: 24, color: "1F3864" },
    // ... other sides
  }
}
```

---

## Category 5: Headers & Footers (18 Properties)

Read: `references/headers-footers.md`

### Header/Footer Types

| Type | Use Case | Implementation |
|------|----------|----------------|
| Default | All pages | `headers: { default: new Header({...}) }` |
| First page | Cover page (no header) | `headers: { first: new Header({...}) }` |
| Even pages | Book layout | `headers: { even: new Header({...}) }` |

### Section-Specific Headers

```javascript
sections: [
  {
    properties: {
      titlePage: true, // Enable different first page
      evenAndOddHeaders: true // Enable odd/even
    },
    headers: {
      default: createHeader("Section 1"),
      first: new Header({ children: [] }), // Empty for first page
    }
  },
  {
    properties: {
      // Link to previous = false for new header
    },
    headers: {
      default: createHeader("Section 2")
    }
  }
]
```

### IB Header Patterns

**Pitch Book**
```
[Logo]                    Project [Name]  |  Strictly Confidential
```

**CIM**
```
[Company Name]            Confidential Information Memorandum
```

**Fairness Opinion**
```
[Firm Letterhead]
```

### IB Footer Patterns

**Standard**
```
                          Page X of Y
```

**With Firm Name**
```
[Firm Name]               Page X of Y                    [Date]
```

**With Section**
```
Section II – Valuation    Page X of Y
```

### Page Number Formats

| Format | Example | Implementation |
|--------|---------|----------------|
| Arabic | 1, 2, 3 | `PageNumberFormat.DECIMAL` |
| Roman lower | i, ii, iii | `PageNumberFormat.LOWER_ROMAN` |
| Roman upper | I, II, III | `PageNumberFormat.UPPER_ROMAN` |
| Letter lower | a, b, c | `PageNumberFormat.LOWER_LETTER` |

---

## Category 6: Styles & Themes (35 Properties)

Read: `references/styles-themes.md`

### Style Types

| Type | Scope | Use Case |
|------|-------|----------|
| Paragraph | Entire paragraph | Headings, body |
| Character | Selected text | Bold terms, emphasis |
| Linked | Context-dependent | Flexible application |
| Table | Table formatting | Consistent tables |
| List | Numbered/bulleted | Consistent lists |

### IB Heading Hierarchy

```javascript
styles: {
  paragraphStyles: [
    {
      id: "Heading1",
      name: "Heading 1",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { font: "Arial", size: 28, bold: true, color: "1F3864" },
      paragraph: { spacing: { before: 480, after: 240 }, outlineLevel: 0 }
    },
    {
      id: "Heading2",
      name: "Heading 2",
      basedOn: "Normal",
      next: "Normal",
      run: { font: "Arial", size: 24, bold: true, color: "1F3864" },
      paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 1 }
    },
    {
      id: "Heading3",
      name: "Heading 3",
      basedOn: "Normal",
      next: "Normal",
      run: { font: "Arial", size: 22, bold: true, color: "000000" },
      paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 }
    }
  ]
}
```

### Document Theme

```javascript
theme: {
  colors: {
    dark1: "000000",
    light1: "FFFFFF",
    dark2: "1F3864",
    light2: "E8F1F8",
    accent1: "4472C4",
    accent2: "ED7D31",
    accent3: "A5A5A5",
    accent4: "FFC000",
    accent5: "5B9BD5",
    accent6: "70AD47"
  },
  fonts: {
    major: { latin: "Arial" },
    minor: { latin: "Arial" }
  }
}
```

### Multilevel Lists (IB Numbering)

```javascript
numbering: {
  config: [{
    reference: "legal-numbering",
    levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
      { level: 1, format: LevelFormat.LOWER_LETTER, text: "%2.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 1080, hanging: 360 } } } },
      { level: 2, format: LevelFormat.LOWER_ROMAN, text: "%3.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 1440, hanging: 360 } } } }
    ]
  }]
}
```

---

## Category 7: Track Changes & Comments (22 Properties)

Read: `references/track-changes.md`

### Track Changes

```javascript
// Enable tracking
const doc = new Document({
  settings: {
    trackRevisions: true,
    revisionView: RevisionView.FINAL // or ORIGINAL, FINAL_MARKUP
  }
});

// Insert with revision
new InsertedTextRun({
  text: "new text",
  id: 1,
  author: "Analyst",
  date: "2026-01-17T10:00:00Z"
})

// Delete with revision
new DeletedTextRun({
  text: "old text",
  id: 2,
  author: "Analyst",
  date: "2026-01-17T10:00:00Z"
})
```

### Comments

```javascript
// Add comment
const commentId = "comment-1";
new CommentRangeStart({ id: commentId });
new TextRun({ text: "commented text" });
new CommentRangeEnd({ id: commentId });
new CommentReference({ id: commentId });

// Comment content in separate section
comments: {
  children: [
    new Comment({
      id: commentId,
      author: "Senior Analyst",
      date: new Date(),
      children: [new Paragraph({ children: [new TextRun("Please verify this figure")] })]
    })
  ]
}
```

### Document Comparison

```javascript
// Compare two documents (requires post-processing or VBA)
// docx-js creates documents; comparison done in Word or via OpenXML SDK
```

---

## Category 8: References (41 Properties)

Read: `references/references-toc.md`

### Table of Contents

```javascript
new TableOfContents("Table of Contents", {
  hyperlink: true,
  headingStyleRange: "1-3",
  stylesWithLevels: [
    { styleName: "Heading1", level: 1 },
    { styleName: "Heading2", level: 2 },
    { styleName: "Heading3", level: 3 }
  ]
})

// TOC requires headings with outlineLevel set
// Update TOC in Word: Ctrl+A, F9
```

### Cross-References

```javascript
// Bookmark target
new Bookmark({
  id: "valuation-section",
  children: [new TextRun("Valuation Analysis")]
})

// Reference to bookmark
new InternalHyperlink({
  anchor: "valuation-section",
  children: [new TextRun({ text: "See Valuation Analysis", style: "Hyperlink" })]
})
```

### Footnotes & Endnotes

```javascript
new TextRun({ text: "revenue" });
new FootnoteReferenceRun({
  id: 1,
  style: FootnoteReferenceStyle.SUPERSCRIPT
});

// In document settings
footnotes: {
  1: {
    children: [
      new Paragraph({
        children: [new TextRun({ text: "Source: Company filings.", size: 16, italics: true })]
      })
    ]
  }
}
```

### Citations & Bibliography

```javascript
// For research reports and offering memoranda
// Requires custom implementation or XML manipulation
// Standard styles: APA, Chicago, Harvard
```

### Index

```javascript
// Mark index entry
new SimpleField({ instruction: 'XE "Investment Banking"' })

// Insert index
new SimpleField({ instruction: 'INDEX \\c "2" \\h "A"' })
```

---

## Category 9: Fields & Automation (68 Field Types)

Read: `references/fields-automation.md`

### Document Information Fields

| Field | Output | Implementation |
|-------|--------|----------------|
| FILENAME | "Report.docx" | `new SimpleField({ instruction: "FILENAME" })` |
| FILESIZE | "1,234 KB" | `new SimpleField({ instruction: "FILESIZE \\# \"#,##0 KB\"" })` |
| AUTHOR | "John Smith" | `new SimpleField({ instruction: "AUTHOR" })` |
| TITLE | Document title | `new SimpleField({ instruction: "TITLE" })` |
| SUBJECT | Document subject | `new SimpleField({ instruction: "SUBJECT" })` |

### Date/Time Fields

| Field | Output | Format |
|-------|--------|--------|
| DATE | "January 17, 2026" | `\\@ "MMMM d, yyyy"` |
| TIME | "3:45 PM" | `\\@ "h:mm AM/PM"` |
| CREATEDATE | Creation date | Same format switches |
| SAVEDATE | Last saved | Same format switches |
| PRINTDATE | Last printed | Same format switches |

### Page Number Fields

```javascript
// Current page
new SimpleField({ instruction: "PAGE" })

// Total pages
new SimpleField({ instruction: "NUMPAGES" })

// Section pages
new SimpleField({ instruction: "SECTIONPAGES" })

// "Page X of Y"
children: [
  new TextRun({ text: "Page " }),
  new SimpleField({ instruction: "PAGE" }),
  new TextRun({ text: " of " }),
  new SimpleField({ instruction: "NUMPAGES" })
]
```

### Calculated Fields

```javascript
// Expression
new SimpleField({ instruction: "= 1234.5678 \\# \"$#,##0.00\"" })

// Reference calculation
new SimpleField({ instruction: "= revenue * 0.25 \\# \"$#,##0\"" })
```

### Conditional Fields

```javascript
// IF field
new SimpleField({
  instruction: 'IF { MERGEFIELD Status } = "Approved" "✓" "Pending"'
})
```

### Sequence Fields (Auto-Numbering)

```javascript
// Table numbering
new SimpleField({ instruction: "SEQ Table \\* ARABIC" })
// Result: 1, 2, 3...

// Figure numbering
new SimpleField({ instruction: "SEQ Figure \\* ARABIC" })
```

---

## Category 10: Graphics (52 Properties)

Read: `references/graphics.md`

### Images

```javascript
new ImageRun({
  type: "png", // Required: png, jpg, jpeg, gif, bmp, svg
  data: fs.readFileSync("chart.png"),
  transformation: {
    width: convertInchesToTwip(6),
    height: convertInchesToTwip(4)
  },
  altText: {
    title: "Valuation Chart",
    description: "Football field chart showing valuation ranges",
    name: "ValuationChart"
  }
})
```

### Drawing Positioning

```javascript
new ImageRun({
  // ... image data
  floating: {
    horizontalPosition: {
      relative: HorizontalPositionRelativeFrom.PAGE,
      align: HorizontalPositionAlign.CENTER
    },
    verticalPosition: {
      relative: VerticalPositionRelativeFrom.PARAGRAPH,
      offset: 914400 // 1 inch in EMUs
    },
    wrap: {
      type: TextWrappingType.SQUARE,
      side: TextWrappingSide.BOTH_SIDES
    }
  }
})
```

### Shapes & Lines

```javascript
// Horizontal line
new Paragraph({
  border: {
    bottom: { style: BorderStyle.SINGLE, size: 24, color: "1F3864", space: 1 }
  }
})
```

---

## Category 11: Advanced Features (28 Capabilities)

Read: `references/advanced-features.md`

### Document Protection

```javascript
const doc = new Document({
  settings: {
    protection: {
      type: ProtectionType.READ_ONLY,
      password: "optional-password"
    }
  }
})
```

### Custom Document Properties

```javascript
customProperties: {
  "Project Name": "Project Alpha",
  "Deal Value": "$500mm",
  "Client": "TechCo Inc.",
  "Confidentiality": "Strictly Confidential"
}
```

### Content Controls (Form Fields)

```javascript
// Plain text control
new PlainTextContentControl({
  children: [new Paragraph({ children: [new TextRun("[Enter value]")] })],
  title: "Revenue Input",
  tag: "revenue"
})

// Drop-down control
new DropDownListContentControl({
  children: [new Paragraph({ children: [new TextRun("Select...")] })],
  listItems: [
    { displayText: "Option A", value: "a" },
    { displayText: "Option B", value: "b" }
  ]
})
```

### Compatibility Settings

```javascript
settings: {
  compatibility: {
    doNotExpandShiftReturn: true,
    useSingleBorderForContiguousCells: true
  }
}
```

---

## Firm-Specific Standards

### Goldman Sachs

| Element | Standard |
|---------|----------|
| Font | Goldman Sans (proprietary), Arial fallback |
| Possessive | "Goldman Sachs'" |
| Terminology | "the firm" (lowercase), "firmwide" (one word) |
| Dates | "January 1, 2018" format |
| Emphasis | Minimal colored text, bold, italics |

### Morgan Stanley / JP Morgan

| Element | Standard |
|---------|----------|
| Font | Arial (JP Morgan), Helvetica (Morgan Stanley) |
| Alignment | Precise measurement to page borders |
| Pitchbooks | 40-60 slides + 60+ appendix pages |
| Red herring | Perfect alignment of legal text |

### Financial Model Color Coding

| Color | Hex | Use |
|-------|-----|-----|
| Blue | #0000FF | Hard-coded inputs, historical data |
| Black | #000000 | Formulas, same-sheet references |
| Green | #008000 | Links to other worksheets |
| Red | #FF0000 | External links, errors |
| Yellow BG | #FFFF00 | Key assumptions |

---

## SEC/EDGAR Compliance

Read: `references/sec-compliance.md`

### Filing Requirements

| Format | Requirements |
|--------|--------------|
| ASCII | Courier 12pt, 80 char max line, 1" margins |
| HTML | Version 3.2, Times New Roman/Arial/Verdana |
| Invalid chars | No ¥, £, ©, ®, ™, smart quotes |
| File size | 200 MB max (600 MB certain forms) |
| Graphics | GIF/JPG only |

### Form-Specific

| Form | Timing | Key Elements |
|------|--------|--------------|
| 10-K | 60-90 days after FY | 4 parts, 16 items |
| 10-Q | 40-45 days after Q | Condensed financials |
| 8-K | 4 business days | Material events |
| S-1 | Registration | One-page cover requirements |

### FINRA Rule 2241 (Research Reports)

- Disclosure on front page or clear reference
- Ownership > 1% disclosure
- Market making disclosure
- IB compensation (past 12 months, next 3 months)
- Rating distribution charts required

---

## Implementation

### Dependencies

```bash
npm install -g docx
```

### Complete Import

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, PageNumber, HeadingLevel,
  WidthType, BorderStyle, ShadingType, AlignmentType, VerticalAlign,
  TableOfContents, Bookmark, InternalHyperlink, ExternalHyperlink,
  FootnoteReferenceRun, SimpleField,
  ImageRun, PageBreak, SectionType, Tab, TabStopType, TabStopPosition,
  LevelFormat, NumberFormat, LineRuleType, HeightRule,
  Comment, CommentRangeStart, CommentRangeEnd, CommentReference,
  InsertedTextRun, DeletedTextRun
} = require('docx');
const fs = require('fs');
```

### Critical Rules

1. **Always set page size explicitly** – Default is A4, not US Letter
2. **Set both `columnWidths` AND cell `width`** – Both required for tables
3. **Use `ShadingType.CLEAR`** – Never SOLID (causes black backgrounds)
4. **Use `LevelFormat.BULLET`** – Never unicode bullets directly
5. **Never use `\n`** – Create separate Paragraph elements
6. **Set `outlineLevel` for TOC** – Required for heading detection
7. **Use half-points for font size** – `size: 20` = 10pt
8. **Match `tableHeader: true` on header rows** – For multi-page repeat

---

## References

See `references/` folder:
- `text-formatting.md` – Character properties, effects, underlines
- `paragraph-formatting.md` – Spacing, tabs, pagination, borders
- `table-formatting.md` – Advanced tables, formulas, nested tables
- `page-setup.md` – Sections, columns, watermarks, page borders
- `headers-footers.md` – Multi-section, odd/even, page numbers
- `styles-themes.md` – Document themes, multilevel lists
- `track-changes.md` – Revisions, comments, comparison
- `references-toc.md` – TOC, cross-references, footnotes, citations
- `fields-automation.md` – 68 field types, switches, calculations
- `graphics.md` – Images, positioning, shapes
- `advanced-features.md` – Protection, content controls, compatibility
- `sec-compliance.md` – EDGAR requirements, form specifications
- `firm-standards.md` – Goldman, Morgan Stanley, JP Morgan conventions
- `templates.js` – Complete code templates
- `color-palette.md` – Full color specifications
