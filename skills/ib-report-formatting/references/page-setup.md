# Page Setup Reference

## Page Dimensions (DXA)

| Paper | Width | Height | Content Width (1" margins) |
|-------|-------|--------|---------------------------|
| US Letter | 12,240 | 15,840 | 9,360 |
| US Letter Landscape | 15,840 | 12,240 | 13,680 |
| A4 | 11,906 | 16,838 | 9,026 |
| A4 Landscape | 16,838 | 11,906 | 14,558 |
| US Legal | 12,240 | 20,160 | 9,360 |

**Note**: docx-js defaults to A4. Always set page size explicitly for US documents.

---

## Margin Standards

### By Document Type

| Document Type | Top | Bottom | Left | Right | Content Width |
|---------------|-----|--------|------|-------|---------------|
| Pitch Book (landscape) | 720 | 720 | 1080 | 1080 | 13,680 |
| Memo (portrait) | 1440 | 1440 | 1440 | 1440 | 9,360 |
| CIM (portrait) | 1440 | 1440 | 1440 | 1440 | 9,360 |
| Bound Report | 1440 | 1440 | 1800 | 1080 | 8,640 |
| Dense Analysis | 1080 | 1080 | 1080 | 1080 | 10,080 |
| Board Deck (landscape) | 720 | 720 | 1080 | 1080 | 13,680 |

### Conversion Reference

| Inches | DXA |
|--------|-----|
| 0.5" | 720 |
| 0.75" | 1080 |
| 1.0" | 1440 |
| 1.25" | 1800 |

---

## Headers & Footers

### Header Content Options

| Element | Position | Font | Size |
|---------|----------|------|------|
| Document title | Center or Left | Arial | 9pt |
| Project name | Left | Arial | 9pt |
| Confidentiality | Right | Arial Italic | 8pt |
| Draft status | Right | Arial Bold | 8pt |
| Company logo | Left | — | — |
| Date | Right | Arial | 8pt |

### Footer Content Options

| Element | Position | Font | Size |
|---------|----------|------|------|
| Firm name | Left | Arial | 8pt |
| Page number (simple) | Center | Arial | 9pt |
| Page number (full) | Center | Arial | 9pt |
| Section indicator | Right | Arial | 8pt |
| Disclaimer | Center | Arial | 7pt |

### Header/Footer Spacing

| Element | From Edge | From Body |
|---------|-----------|-----------|
| Header | 432–720 DXA | 288–432 DXA |
| Footer | 432–720 DXA | 288–432 DXA |

---

## Implementation

### Portrait Document (Memo)

```javascript
const memoSetup = {
  page: {
    size: {
      width: 12240,   // 8.5"
      height: 15840   // 11"
    },
    margin: {
      top: 1440,      // 1"
      bottom: 1440,
      left: 1440,
      right: 1440
    }
  }
};
```

### Landscape Document (Pitch Book)

```javascript
const pitchbookSetup = {
  page: {
    size: {
      width: 15840,   // 11"
      height: 12240,  // 8.5"
      orientation: "landscape"
    },
    margin: {
      top: 720,       // 0.5"
      bottom: 720,
      left: 1080,     // 0.75"
      right: 1080
    }
  }
};
```

### Dense Analysis (Tighter Margins)

```javascript
const denseSetup = {
  page: {
    size: {
      width: 12240,
      height: 15840
    },
    margin: {
      top: 1080,      // 0.75"
      bottom: 1080,
      left: 1080,
      right: 1080
    }
  }
};
```

### Header Implementation

```javascript
const { Header, Footer, PageNumber, Paragraph, TextRun, AlignmentType } = require('docx');

function createHeader(title, confidential = true) {
  return new Header({
    children: [
      new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 0 },
        children: [
          new TextRun({ text: title, font: "Arial", size: 18 }),
          confidential ? new TextRun({
            text: "  |  Strictly Confidential",
            font: "Arial",
            size: 16,
            italics: true,
            color: "808080"
          }) : null
        ].filter(Boolean)
      })
    ]
  });
}
```

### Footer Implementation

```javascript
function createFooter(firmName = null) {
  const children = [];
  
  if (firmName) {
    children.push(new TextRun({ text: firmName + "  |  ", font: "Arial", size: 16, color: "808080" }));
  }
  
  children.push(
    new TextRun({ text: "Page ", font: "Arial", size: 16, color: "808080" }),
    new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: "808080" }),
    new TextRun({ text: " of ", font: "Arial", size: 16, color: "808080" }),
    new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: "808080" })
  );
  
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: children
      })
    ]
  });
}
```

### Complete Section Setup

```javascript
const section = {
  properties: pitchbookSetup.page,
  headers: {
    default: createHeader("Project Alpha")
  },
  footers: {
    default: createFooter("Investment Bank LLC")
  },
  children: [
    // Document content here
  ]
};

const doc = new Document({
  sections: [section]
});
```

---

## Keep-Together Rules

| Element | Setting | Notes |
|---------|---------|-------|
| Heading + first paragraph | keepNext: true | Never orphan headers |
| Small tables (< 15 rows) | keepLines: true | Avoid mid-break |
| Callout boxes | keepLines: true | Never break |
| Image + caption | keepNext: true | Visual integrity |

```javascript
// Heading that stays with following content
new Paragraph({
  keepNext: true,
  children: [new TextRun({ text: "Section Title", bold: true, size: 28 })]
})
```

---

## Orphan/Widow Control

```javascript
// Paragraph with widow/orphan control
new Paragraph({
  widowControl: true,  // Prevent single lines at page top/bottom
  children: [/* content */]
})
```
