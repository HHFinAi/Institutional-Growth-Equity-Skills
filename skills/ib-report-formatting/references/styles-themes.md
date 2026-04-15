# Styles & Themes Reference (35 Properties)

## Overview

Styles ensure consistent formatting throughout IB documents. Define once, apply everywhere.

---

## Style Types

| Type | Scope | Use Case |
|------|-------|----------|
| Paragraph | Entire paragraph | Headings, body text |
| Character | Selected text | Emphasis, terms |
| Linked | Context-dependent | Flexible application |
| Table | Table formatting | Consistent tables |
| List | Numbered/bulleted | Consistent lists |

---

## Document Styles Definition

```javascript
const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: "Arial",
          size: 20 // 10pt
        },
        paragraph: {
          spacing: { after: 160 }
        }
      }
    },
    paragraphStyles: [
      // Heading styles
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: {
          font: "Arial",
          size: 28,
          bold: true,
          color: "1F3864"
        },
        paragraph: {
          spacing: { before: 480, after: 240 },
          outlineLevel: 0 // Required for TOC
        }
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: {
          font: "Arial",
          size: 24,
          bold: true,
          color: "1F3864"
        },
        paragraph: {
          spacing: { before: 360, after: 180 },
          outlineLevel: 1
        }
      },
      {
        id: "Heading3",
        name: "Heading 3",
        basedOn: "Normal",
        next: "Normal",
        run: {
          font: "Arial",
          size: 22,
          bold: true,
          color: "000000"
        },
        paragraph: {
          spacing: { before: 240, after: 120 },
          outlineLevel: 2
        }
      },
      // Body styles
      {
        id: "BodyText",
        name: "Body Text",
        basedOn: "Normal",
        run: {
          font: "Arial",
          size: 20
        },
        paragraph: {
          spacing: { after: 160, line: 276, lineRule: LineRuleType.AUTO }
        }
      },
      // Special styles
      {
        id: "Footnote",
        name: "Footnote",
        basedOn: "Normal",
        run: {
          font: "Arial",
          size: 16,
          italics: true,
          color: "595959"
        },
        paragraph: {
          spacing: { after: 60 }
        }
      },
      {
        id: "TableCaption",
        name: "Table Caption",
        basedOn: "Normal",
        next: "Normal",
        run: {
          font: "Arial",
          size: 18,
          bold: true
        },
        paragraph: {
          spacing: { before: 240, after: 120 }
        }
      },
      {
        id: "Disclaimer",
        name: "Disclaimer",
        basedOn: "Normal",
        run: {
          font: "Arial",
          size: 14,
          color: "808080"
        },
        paragraph: {
          spacing: { after: 80 }
        }
      }
    ],
    characterStyles: [
      {
        id: "Emphasis",
        name: "Emphasis",
        run: {
          italics: true
        }
      },
      {
        id: "Strong",
        name: "Strong",
        run: {
          bold: true
        }
      },
      {
        id: "Hyperlink",
        name: "Hyperlink",
        run: {
          color: "4472C4",
          underline: { type: UnderlineType.SINGLE }
        }
      },
      {
        id: "PositiveValue",
        name: "Positive Value",
        run: {
          color: "375623"
        }
      },
      {
        id: "NegativeValue",
        name: "Negative Value",
        run: {
          color: "C00000"
        }
      }
    ]
  }
});
```

---

## Using Styles

### Paragraph Styles

```javascript
// Using heading level
new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun("Executive Summary")]
})

// Using style ID
new Paragraph({
  style: "Footnote",
  children: [new TextRun("Source: Company filings")]
})
```

### Character Styles

```javascript
new Paragraph({
  children: [
    new TextRun("Revenue increased by "),
    new TextRun({ text: "25%", style: "PositiveValue" }),
    new TextRun(" year-over-year.")
  ]
})
```

---

## Document Themes

Themes coordinate colors, fonts, and effects across the document.

```javascript
const doc = new Document({
  theme: {
    colors: {
      dark1: "000000",      // Text/background dark
      light1: "FFFFFF",     // Text/background light
      dark2: "1F3864",      // Accent dark (Navy)
      light2: "E8F1F8",     // Accent light
      accent1: "4472C4",    // Blue
      accent2: "ED7D31",    // Orange
      accent3: "A5A5A5",    // Gray
      accent4: "FFC000",    // Gold
      accent5: "5B9BD5",    // Light blue
      accent6: "70AD47",    // Green
      hyperlink: "4472C4",
      followedHyperlink: "954F72"
    },
    fonts: {
      major: {
        latin: "Arial",
        eastAsia: "MS Gothic",
        complexScript: "Arial"
      },
      minor: {
        latin: "Arial",
        eastAsia: "MS Gothic",
        complexScript: "Arial"
      }
    }
  }
});
```

---

## Multilevel Lists (Numbering)

### IB Legal Numbering (1. → a. → i.)

```javascript
numbering: {
  config: [
    {
      reference: "legal-numbering",
      levels: [
        {
          level: 0,
          format: LevelFormat.DECIMAL,
          text: "%1.",
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 720, hanging: 360 }
            },
            run: {
              bold: true
            }
          }
        },
        {
          level: 1,
          format: LevelFormat.LOWER_LETTER,
          text: "%2.",
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 1080, hanging: 360 }
            }
          }
        },
        {
          level: 2,
          format: LevelFormat.LOWER_ROMAN,
          text: "%3.",
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 1440, hanging: 360 }
            }
          }
        }
      ]
    }
  ]
}

// Usage
new Paragraph({
  numbering: { reference: "legal-numbering", level: 0 },
  children: [new TextRun("First main point")]
})

new Paragraph({
  numbering: { reference: "legal-numbering", level: 1 },
  children: [new TextRun("Sub-point a")]
})
```

### IB Bullet Points

```javascript
numbering: {
  config: [
    {
      reference: "ib-bullets",
      levels: [
        {
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 720, hanging: 360 }
            }
          }
        },
        {
          level: 1,
          format: LevelFormat.BULLET,
          text: "–", // En-dash
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 1080, hanging: 360 }
            }
          }
        },
        {
          level: 2,
          format: LevelFormat.BULLET,
          text: "○", // Circle
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 1440, hanging: 360 }
            }
          }
        }
      ]
    }
  ]
}
```

### Outline Numbering (I. → A. → 1. → a.)

```javascript
numbering: {
  config: [
    {
      reference: "outline-numbering",
      levels: [
        {
          level: 0,
          format: LevelFormat.UPPER_ROMAN,
          text: "%1.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 720 } } }
        },
        {
          level: 1,
          format: LevelFormat.UPPER_LETTER,
          text: "%2.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1440, hanging: 720 } } }
        },
        {
          level: 2,
          format: LevelFormat.DECIMAL,
          text: "%3.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 2160, hanging: 720 } } }
        },
        {
          level: 3,
          format: LevelFormat.LOWER_LETTER,
          text: "%4.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 2880, hanging: 720 } } }
        }
      ]
    }
  ]
}
```

---

## Level Format Options

| Format | Output | Constant |
|--------|--------|----------|
| 1, 2, 3 | Arabic | `LevelFormat.DECIMAL` |
| A, B, C | Uppercase letter | `LevelFormat.UPPER_LETTER` |
| a, b, c | Lowercase letter | `LevelFormat.LOWER_LETTER` |
| I, II, III | Uppercase Roman | `LevelFormat.UPPER_ROMAN` |
| i, ii, iii | Lowercase Roman | `LevelFormat.LOWER_ROMAN` |
| • | Bullet | `LevelFormat.BULLET` |
| 01, 02, 03 | Zero-padded | `LevelFormat.DECIMAL_ZERO` |

---

## IB Style Guide Summary

### Typography Hierarchy

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Title | Arial | 20pt | Bold | #1F3864 |
| Heading 1 | Arial | 14pt | Bold | #1F3864 |
| Heading 2 | Arial | 12pt | Bold | #1F3864 |
| Heading 3 | Arial | 11pt | Bold | #000000 |
| Body | Arial | 10pt | Regular | #000000 |
| Table Header | Arial | 9pt | Bold | #FFFFFF |
| Table Body | Arial | 9pt | Regular | #000000 |
| Footnote | Arial | 8pt | Italic | #595959 |
| Disclaimer | Arial | 7pt | Regular | #808080 |

### Color Usage

| Purpose | Color | Hex |
|---------|-------|-----|
| Headers | Navy | #1F3864 |
| Body text | Black | #000000 |
| Secondary | Gray | #595959 |
| Positive | Green | #375623 |
| Negative | Red | #C00000 |
| Highlight | Yellow | #FFF2CC |
| Links | Blue | #4472C4 |

---

## Best Practices

1. **Define styles once** at document creation
2. **Use built-in heading levels** for TOC compatibility
3. **Set outlineLevel** for headings to appear in TOC
4. **Create character styles** for emphasis, not ad-hoc formatting
5. **Use numbering configs** for consistent lists
6. **Apply theme colors** for easy global updates
7. **Test styles** before bulk content creation
