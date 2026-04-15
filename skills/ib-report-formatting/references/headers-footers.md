# Headers & Footers Reference (18 Properties)

## Header/Footer Types

| Type | Property | Use Case |
|------|----------|----------|
| Default | `headers.default` | All pages (unless overridden) |
| First Page | `headers.first` | Title/cover page |
| Even Pages | `headers.even` | Left-hand pages in books |

---

## Basic Implementation

```javascript
const { Header, Footer, Paragraph, TextRun, PageNumber, AlignmentType } = require('docx');

const doc = new Document({
  sections: [{
    properties: {
      page: { /* page settings */ }
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [
              new TextRun({ text: "Project Alpha", font: "Arial", size: 18 }),
              new TextRun({ text: "  |  Strictly Confidential", font: "Arial", size: 16, italics: true, color: "808080" })
            ]
          })
        ]
      })
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: "Page ", font: "Arial", size: 16, color: "808080" }),
              new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: "808080" }),
              new TextRun({ text: " of ", font: "Arial", size: 16, color: "808080" }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: "808080" })
            ]
          })
        ]
      })
    },
    children: [/* document content */]
  }]
});
```

---

## Different First Page

For cover pages without headers/footers:

```javascript
sections: [{
  properties: {
    titlePage: true // Enable different first page
  },
  headers: {
    default: createHeader("Project Alpha"),
    first: new Header({ children: [] }) // Empty header for first page
  },
  footers: {
    default: createFooter(),
    first: new Footer({ children: [] }) // Empty footer for first page
  },
  children: [/* content */]
}]
```

---

## Different Odd/Even Pages

For book-style layouts:

```javascript
sections: [{
  properties: {
    evenAndOddHeaders: true
  },
  headers: {
    default: new Header({ // Odd pages (right-hand)
      children: [
        new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun("Project Alpha")]
        })
      ]
    }),
    even: new Header({ // Even pages (left-hand)
      children: [
        new Paragraph({
          alignment: AlignmentType.LEFT,
          children: [new TextRun("Confidential Information Memorandum")]
        })
      ]
    })
  },
  children: [/* content */]
}]
```

---

## Section-Specific Headers

Different headers for different document sections:

```javascript
sections: [
  // Section 1: Front matter
  {
    properties: {
      titlePage: true,
      page: { /* page settings */ }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({ children: [new TextRun("Table of Contents")] })]
      }),
      first: new Header({ children: [] })
    },
    children: [/* TOC content */]
  },
  // Section 2: Main content
  {
    properties: {
      page: { /* page settings */ }
      // Note: By default, links to previous section's header
    },
    headers: {
      default: new Header({
        children: [new Paragraph({ children: [new TextRun("Executive Summary")] })]
      })
    },
    children: [/* main content */]
  },
  // Section 3: Appendix
  {
    headers: {
      default: new Header({
        children: [new Paragraph({ children: [new TextRun("Appendix")] })]
      })
    },
    children: [/* appendix content */]
  }
]
```

---

## Page Number Formats

### Using PageNumber Class

```javascript
const { PageNumber } = require('docx');

// Current page number
new TextRun({ children: [PageNumber.CURRENT] })

// Total pages
new TextRun({ children: [PageNumber.TOTAL_PAGES] })
```

### Using SimpleField for More Control

```javascript
const { SimpleField } = require('docx');

// Arabic numerals (1, 2, 3)
new SimpleField({ instruction: "PAGE" })

// Roman numerals lowercase (i, ii, iii)
new SimpleField({ instruction: "PAGE \\* roman" })

// Roman numerals uppercase (I, II, III)
new SimpleField({ instruction: "PAGE \\* Roman" })

// Letters lowercase (a, b, c)
new SimpleField({ instruction: "PAGE \\* alphabetic" })
```

### Page Number Styles by Document Section

| Section | Format | Example |
|---------|--------|---------|
| Cover page | None | — |
| Front matter (TOC) | Roman lowercase | i, ii, iii |
| Main content | Arabic | 1, 2, 3 |
| Appendix | Arabic or A-1, A-2 | 25 or A-1 |

---

## IB Header Patterns

### Pitch Book Header

```javascript
function createPitchbookHeader(projectName) {
  return new Header({
    children: [
      new Paragraph({
        children: [
          // Left: Logo placeholder
          new TextRun({ text: "[LOGO]", font: "Arial", size: 16, color: "808080" }),
          // Use tabs or table for positioning
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [
          new TextRun({ text: projectName, font: "Arial", size: 18 }),
          new TextRun({ text: "  |  ", font: "Arial", size: 16, color: "808080" }),
          new TextRun({ text: "Strictly Confidential", font: "Arial", size: 16, italics: true, color: "808080" })
        ]
      })
    ]
  });
}
```

### CIM Header

```javascript
function createCIMHeader(companyName) {
  return new Header({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: companyName, font: "Arial", size: 20, bold: true, color: "1F3864" })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Confidential Information Memorandum", font: "Arial", size: 16, italics: true, color: "595959" })
        ]
      })
    ]
  });
}
```

### Research Report Header

```javascript
function createResearchHeader(companyName, ticker, date) {
  return new Header({
    children: [
      new Paragraph({
        children: [
          new TextRun({ text: `${companyName} (${ticker})`, font: "Arial", size: 18, bold: true }),
          new TextRun({ text: `  |  ${date}`, font: "Arial", size: 16, color: "595959" })
        ]
      })
    ]
  });
}
```

---

## IB Footer Patterns

### Standard Footer

```javascript
function createStandardFooter() {
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Page ", font: "Arial", size: 16, color: "808080" }),
          new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: "808080" }),
          new TextRun({ text: " of ", font: "Arial", size: 16, color: "808080" }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: "808080" })
        ]
      })
    ]
  });
}
```

### Footer with Firm Name

```javascript
function createFirmFooter(firmName) {
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: firmName, font: "Arial", size: 16, color: "808080" }),
          new TextRun({ text: "  |  Page ", font: "Arial", size: 16, color: "808080" }),
          new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: "808080" }),
          new TextRun({ text: " of ", font: "Arial", size: 16, color: "808080" }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: "808080" })
        ]
      })
    ]
  });
}
```

### Footer with Section Name (Using STYLEREF)

```javascript
function createSectionFooter() {
  return new Footer({
    children: [
      new Paragraph({
        children: [
          // Current section name from Heading 1
          new SimpleField({ instruction: 'STYLEREF "Heading 1" \\* MERGEFORMAT' }),
          new TextRun({ text: "  |  Page ", font: "Arial", size: 16, color: "808080" }),
          new SimpleField({ instruction: "PAGE" }),
          new TextRun({ text: " of ", font: "Arial", size: 16, color: "808080" }),
          new SimpleField({ instruction: "NUMPAGES" })
        ]
      })
    ]
  });
}
```

### Three-Column Footer (Left/Center/Right)

```javascript
function createThreeColumnFooter(leftText, centerText, rightText) {
  return new Footer({
    children: [
      new Paragraph({
        tabStops: [
          { type: TabStopType.CENTER, position: 4680 }, // Center of page
          { type: TabStopType.RIGHT, position: 9360 }   // Right margin
        ],
        children: [
          new TextRun({ text: leftText, font: "Arial", size: 16, color: "808080" }),
          new TextRun({ children: [new Tab()] }),
          new TextRun({ text: centerText, font: "Arial", size: 16, color: "808080" }),
          new TextRun({ children: [new Tab()] }),
          new TextRun({ text: rightText, font: "Arial", size: 16, color: "808080" })
        ]
      })
    ]
  });
}
```

---

## Header/Footer Spacing

```javascript
properties: {
  page: {
    margin: {
      top: 1440,    // 1" from page edge
      bottom: 1440,
      header: 720,  // 0.5" from page edge to header
      footer: 720   // 0.5" from page edge to footer
    }
  }
}
```

---

## Draft Watermark in Header

```javascript
function createDraftHeader(projectName) {
  return new Header({
    children: [
      // Watermark (positioned behind content)
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({
            text: "DRAFT",
            font: "Arial",
            size: 144, // 72pt
            color: "E0E0E0",
            bold: true
          })
        ]
      }),
      // Regular header content
      new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [
          new TextRun({ text: projectName, font: "Arial", size: 18 }),
          new TextRun({ text: "  |  ", color: "808080" }),
          new TextRun({ text: "DRAFT", font: "Arial", size: 16, bold: true, color: "C00000" })
        ]
      })
    ]
  });
}
```
