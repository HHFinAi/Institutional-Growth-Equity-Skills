# References, TOC & Citations Reference (41 Properties)

## Table of Contents

### Basic TOC

```javascript
const { TableOfContents, HeadingLevel } = require('docx');

// Insert TOC
new TableOfContents("Table of Contents", {
  hyperlink: true,
  headingStyleRange: "1-3" // Include Heading 1, 2, 3
})
```

### TOC Options

| Property | Type | Description |
|----------|------|-------------|
| hyperlink | boolean | Make entries clickable |
| headingStyleRange | string | "1-3" includes H1-H3 |
| stylesWithLevels | array | Custom style mapping |
| captionLabel | string | Include figure/table captions |
| entriesFromBookmark | string | Include bookmarked content |

### Custom Style Mapping

```javascript
new TableOfContents("Contents", {
  hyperlink: true,
  stylesWithLevels: [
    { styleName: "Heading1", level: 1 },
    { styleName: "Heading2", level: 2 },
    { styleName: "Heading3", level: 3 },
    { styleName: "AppendixHeading", level: 1 } // Custom style
  ]
})
```

### Required: Heading Styles with OutlineLevel

```javascript
// For TOC to work, headings must have outlineLevel set
styles: {
  paragraphStyles: [
    {
      id: "Heading1",
      name: "Heading 1",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { font: "Arial", size: 28, bold: true, color: "1F3864" },
      paragraph: {
        spacing: { before: 480, after: 240 },
        outlineLevel: 0  // REQUIRED for TOC - Level 1
      }
    },
    {
      id: "Heading2",
      name: "Heading 2",
      basedOn: "Normal",
      next: "Normal",
      run: { font: "Arial", size: 24, bold: true, color: "1F3864" },
      paragraph: {
        spacing: { before: 360, after: 180 },
        outlineLevel: 1  // Level 2
      }
    }
  ]
}
```

### Using HeadingLevel Enum

```javascript
// Simpler approach using built-in heading levels
new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun("Executive Summary")]
})
```

### TOC Formatting

```javascript
// Custom TOC styles
styles: {
  paragraphStyles: [
    {
      id: "TOC1",
      name: "toc 1",
      basedOn: "Normal",
      run: { font: "Arial", size: 22, bold: true },
      paragraph: {
        spacing: { before: 240, after: 120 },
        tabStops: [{ type: TabStopType.RIGHT, position: 9360, leader: LeaderType.DOT }]
      }
    },
    {
      id: "TOC2",
      name: "toc 2",
      basedOn: "Normal",
      run: { font: "Arial", size: 20 },
      paragraph: {
        indent: { left: 360 },
        spacing: { after: 60 },
        tabStops: [{ type: TabStopType.RIGHT, position: 9360, leader: LeaderType.DOT }]
      }
    }
  ]
}
```

### Updating TOC

**Note:** docx-js creates a TOC placeholder. To populate page numbers:
1. Open document in Word
2. Click inside TOC
3. Press F9 or right-click → "Update Field"
4. Choose "Update entire table"

---

## Bookmarks

### Creating Bookmarks

```javascript
const { Bookmark } = require('docx');

new Paragraph({
  children: [
    new Bookmark({
      id: "valuation-section",
      children: [
        new TextRun({ text: "Valuation Analysis", bold: true, size: 28 })
      ]
    })
  ]
})
```

### Bookmark Naming Conventions

| Pattern | Example | Use Case |
|---------|---------|----------|
| section-name | `exec-summary` | Section references |
| table-number | `table-1` | Table references |
| figure-number | `figure-3` | Figure references |
| page-marker | `appendix-start` | Page references |

---

## Cross-References

### Internal Hyperlinks (to Bookmarks)

```javascript
const { InternalHyperlink } = require('docx');

new Paragraph({
  children: [
    new TextRun("For valuation details, see "),
    new InternalHyperlink({
      anchor: "valuation-section",
      children: [
        new TextRun({
          text: "Section III - Valuation Analysis",
          style: "Hyperlink"
        })
      ]
    }),
    new TextRun(".")
  ]
})
```

### External Hyperlinks

```javascript
const { ExternalHyperlink } = require('docx');

new Paragraph({
  children: [
    new TextRun("Source: "),
    new ExternalHyperlink({
      link: "https://www.sec.gov/cgi-bin/browse-edgar",
      children: [
        new TextRun({
          text: "SEC EDGAR",
          style: "Hyperlink"
        })
      ]
    })
  ]
})
```

### Hyperlink Style

```javascript
styles: {
  characterStyles: [
    {
      id: "Hyperlink",
      name: "Hyperlink",
      run: {
        color: "4472C4",
        underline: { type: UnderlineType.SINGLE }
      }
    }
  ]
}
```

---

## Footnotes

### Creating Footnotes

```javascript
const { FootnoteReferenceRun } = require('docx');

// In document text
new Paragraph({
  children: [
    new TextRun("The company reported revenue of $1.5 billion"),
    new FootnoteReferenceRun({ id: 1 }),
    new TextRun(" for the fiscal year.")
  ]
})

// Define footnote content in document settings
const doc = new Document({
  footnotes: {
    1: {
      children: [
        new Paragraph({
          children: [
            new TextRun({
              text: "Source: Company 10-K filing dated March 15, 2025.",
              font: "Arial",
              size: 16,
              italics: true
            })
          ]
        })
      ]
    }
  }
});
```

### Footnote Numbering Options

| Format | Example | Implementation |
|--------|---------|----------------|
| Arabic | 1, 2, 3 | Default |
| Roman lower | i, ii, iii | Custom XML |
| Roman upper | I, II, III | Custom XML |
| Letter lower | a, b, c | Custom XML |
| Symbols | *, †, ‡ | Custom XML |

### Footnote Restart Options

| Option | Behavior |
|--------|----------|
| Continuous | Numbers continue throughout document |
| Each Section | Restart at each section break |
| Each Page | Restart on each page |

### IB Footnote Conventions

| Type | Format | Example |
|------|--------|---------|
| Data source | Italic | *Source: Capital IQ* |
| Company filing | Italic with date | *Source: 10-K (2025)* |
| Management | Italic | *Source: Management* |
| Estimate | Italic with qualifier | *Note: Analyst estimate* |
| Assumption | Italic | *Assumes 10% growth rate* |

---

## Endnotes

### Creating Endnotes

```javascript
const { EndnoteReferenceRun } = require('docx');

new Paragraph({
  children: [
    new TextRun("Subject to customary closing conditions"),
    new EndnoteReferenceRun({ id: 1 }),
    new TextRun(".")
  ]
})

// Define in document settings
const doc = new Document({
  endnotes: {
    1: {
      children: [
        new Paragraph({
          children: [
            new TextRun({
              text: "Closing conditions include regulatory approvals, shareholder approval, and absence of material adverse change.",
              font: "Arial",
              size: 18
            })
          ]
        })
      ]
    }
  }
});
```

### Footnotes vs Endnotes

| Aspect | Footnotes | Endnotes |
|--------|-----------|----------|
| Location | Bottom of page | End of document/section |
| Use Case | Quick references, sources | Detailed explanations |
| IB Usage | Data sources, brief notes | Legal disclaimers, definitions |

---

## Citations & Bibliography

### Manual Citation Format

For IB documents, citations are typically formatted manually:

```javascript
// In-text citation
new Paragraph({
  children: [
    new TextRun("According to industry research (Bloomberg, 2025), the sector is expected to grow...")
  ]
})

// Bibliography entry
new Paragraph({
  indent: { left: 720, hanging: 720 },
  spacing: { after: 120 },
  children: [
    new TextRun("Bloomberg. (2025). "),
    new TextRun({ text: "Global M&A Report Q4 2025", italics: true }),
    new TextRun(". Bloomberg Intelligence.")
  ]
})
```

### Common Citation Styles for IB

| Style | Use Case | Example |
|-------|----------|---------|
| Inline | Quick reference | (Source: Capital IQ) |
| Footnote | Detailed source | ¹ Bloomberg, January 2026 |
| Table note | Data tables | Source: Company filings |

---

## Index

### Marking Index Entries

```javascript
const { SimpleField } = require('docx');

new Paragraph({
  children: [
    new SimpleField({ instruction: 'XE "Valuation:DCF Analysis"' }),
    new TextRun("The DCF analysis indicates...")
  ]
})
```

### Index Entry Syntax

| Syntax | Result | Use |
|--------|--------|-----|
| `XE "Term"` | Term.....5 | Simple entry |
| `XE "Main:Sub"` | Main → Sub.....5 | Hierarchical |
| `XE "Term" \\t "See also X"` | Term. See also X | Cross-reference |
| `XE "Term" \\r BookmarkName` | Term.....5-10 | Page range |

### Inserting Index

```javascript
// Insert index at end of document
new Paragraph({
  children: [
    new SimpleField({ instruction: 'INDEX \\c "2" \\h "A"' })
    // \\c "2" = two columns
    // \\h "A" = alphabetic headings
  ]
})
```

---

## Table of Figures / Tables

### Marking Captions

```javascript
// Figure caption
new Paragraph({
  style: "Caption",
  children: [
    new TextRun("Figure "),
    new SimpleField({ instruction: "SEQ Figure \\* ARABIC" }),
    new TextRun(": Valuation Football Field")
  ]
})

// Table caption
new Paragraph({
  style: "Caption",
  children: [
    new TextRun("Table "),
    new SimpleField({ instruction: "SEQ Table \\* ARABIC" }),
    new TextRun(": Comparable Companies Analysis")
  ]
})
```

### Inserting Table of Figures

```javascript
new TableOfContents("List of Figures", {
  captionLabel: "Figure",
  captionLabelIncludesNumbers: true
})
```

---

## Complete Example: CIM Front Matter

```javascript
const doc = new Document({
  footnotes: {
    1: {
      children: [
        new Paragraph({
          children: [new TextRun({
            text: "Unless otherwise indicated, financial data represents fiscal year ended December 31, 2025.",
            size: 16, italics: true
          })]
        })
      ]
    }
  },
  styles: {
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        run: { font: "Arial", size: 28, bold: true, color: "1F3864" },
        paragraph: { spacing: { before: 480, after: 240 }, outlineLevel: 0 }
      },
      {
        id: "TOCHeading",
        name: "TOC Heading",
        basedOn: "Heading1",
        paragraph: { spacing: { after: 360 } }
      }
    ]
  },
  sections: [{
    children: [
      // Title page content...
      new Paragraph({ children: [new PageBreak()] }),
      
      // Table of Contents
      new Paragraph({
        style: "TOCHeading",
        children: [new TextRun("TABLE OF CONTENTS")]
      }),
      new TableOfContents("", {
        hyperlink: true,
        headingStyleRange: "1-3"
      }),
      new Paragraph({ children: [new PageBreak()] }),
      
      // First section with bookmark
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [
          new Bookmark({
            id: "executive-summary",
            children: [new TextRun("I. EXECUTIVE SUMMARY")]
          })
        ]
      }),
      
      new Paragraph({
        children: [
          new TextRun("The Company"),
          new FootnoteReferenceRun({ id: 1 }),
          new TextRun(" is a leading provider of enterprise software solutions...")
        ]
      }),
      
      // Cross-reference
      new Paragraph({
        children: [
          new TextRun("For detailed financial information, see "),
          new InternalHyperlink({
            anchor: "financial-overview",
            children: [new TextRun({ text: "Section IV", style: "Hyperlink" })]
          }),
          new TextRun(".")
        ]
      })
    ]
  }]
});
```
