# Typography Reference

## Font Families

| Priority | Font | Fallback | Use Case |
|----------|------|----------|----------|
| Primary | Arial | Helvetica | Universal compatibility |
| Alternative | Calibri | Carlito | Modern Microsoft |
| Formal | Times New Roman | Liberation Serif | Legal documents |
| Monospace | Consolas | Courier New | Code references |

**Rule**: Use one font family throughout the entire document.

---

## Font Size Hierarchy

Note: docx-js uses **half-points** for font size (size 20 = 10pt).

| Element | Size (pt) | Size (half-pt) | Weight | Color |
|---------|-----------|----------------|--------|-------|
| Document title | 20 | 40 | Bold | #1F3864 |
| Section header (L1) | 14 | 28 | Bold | #1F3864 |
| Section header (L2) | 12 | 24 | Bold | #1F3864 |
| Section header (L3) | 11 | 22 | Bold | #000000 |
| Body text | 10 | 20 | Regular | #000000 |
| Table header | 9 | 18 | Bold | #FFFFFF |
| Table body | 9 | 18 | Regular | #000000 |
| Table footnote | 8 | 16 | Italic | #595959 |
| Page header/footer | 8 | 16 | Regular | #808080 |
| Disclaimer | 7 | 14 | Regular | #808080 |
| Watermark | 48 | 96 | Bold | #D9D9D9 |

---

## Color Palette

### Primary Colors

| Name | Hex | RGB | Use Case |
|------|-----|-----|----------|
| Navy | #1F3864 | 31, 56, 100 | Headers, titles |
| Dark Navy | #0D1B2A | 13, 27, 42 | Heavy emphasis |
| Black | #000000 | 0, 0, 0 | Body text |
| Dark Gray | #404040 | 64, 64, 64 | Secondary text |
| Medium Gray | #595959 | 89, 89, 89 | Footnotes |
| Light Gray | #808080 | 128, 128, 128 | NA values, disabled |
| White | #FFFFFF | 255, 255, 255 | Backgrounds |

### Accent Colors

| Name | Hex | Use Case |
|------|-----|----------|
| Blue Accent | #4472C4 | Charts, links |
| Green (text) | #375623 | Positive values |
| Green (fill) | #E2EFDA | Positive shading |
| Red (text) | #C00000 | Negative values |
| Red (fill) | #FFC7CE | Negative shading |
| Yellow (text) | #806000 | Mean/median |
| Yellow (fill) | #FFF2CC | Highlight shading |
| Orange | #ED7D31 | Warnings |

### Table Header Colors

| Style | Background | Text |
|-------|------------|------|
| Primary header | #1F3864 | #FFFFFF |
| Sub-header | #D6DCE5 | #1F3864 |
| Alternative header | #44546A | #FFFFFF |

---

## Font Weight Rules

| Element | Weight | Notes |
|---------|--------|-------|
| All headers | Bold | Hierarchy clarity |
| Table headers | Bold | Column identification |
| Row labels | Bold or Regular | Depends on density |
| Data cells | Regular | Always |
| Subtotal/total rows | Bold | Emphasis |
| Body paragraphs | Regular | Readability |
| Inline emphasis | Bold | Selective only |
| Footnotes | Regular | Subtle |

---

## Italic Usage

| Use Case | Style |
|----------|-------|
| Source citations | Italic |
| Notes and caveats | Italic |
| NA/NM values | Italic |
| Foreign terms | Italic |
| Estimates | Italic or "E" suffix |
| Publication titles | Italic |
| Body text | Never |
| Headers | Never |

---

## Text Decoration

| Decoration | Allowed Use | Never Use For |
|------------|-------------|---------------|
| Underline | Hyperlinks only | Headers, emphasis |
| Strikethrough | Track changes only | General text |
| All caps | Section headers, disclaimers | Body paragraphs |
| Small caps | Legal entity names | Body text |
| Superscript | Footnote markers | General emphasis |

---

## Implementation

```javascript
// Font configuration objects
const fonts = {
  title: { font: "Arial", size: 40, bold: true, color: "1F3864" },
  heading1: { font: "Arial", size: 28, bold: true, color: "1F3864" },
  heading2: { font: "Arial", size: 24, bold: true, color: "1F3864" },
  heading3: { font: "Arial", size: 22, bold: true, color: "000000" },
  body: { font: "Arial", size: 20, color: "000000" },
  tableHeader: { font: "Arial", size: 18, bold: true, color: "FFFFFF" },
  tableBody: { font: "Arial", size: 18, color: "000000" },
  footnote: { font: "Arial", size: 16, italics: true, color: "595959" },
  pageNumber: { font: "Arial", size: 16, color: "808080" }
};

// Document-wide styles
const documentStyles = {
  styles: {
    default: {
      document: {
        run: { font: "Arial", size: 20 } // 10pt default
      }
    },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "1F3864" },
        paragraph: { spacing: { before: 480, after: 240 }, outlineLevel: 0 }
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: "1F3864" },
        paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 1 }
      },
      {
        id: "Footnote",
        name: "Footnote",
        basedOn: "Normal",
        run: { size: 16, italics: true, font: "Arial", color: "595959" },
        paragraph: { spacing: { before: 120, after: 60 } }
      }
    ]
  }
};

// Helper function
function createStyledText(text, styleName) {
  return new TextRun({ text, ...fonts[styleName] });
}
```
