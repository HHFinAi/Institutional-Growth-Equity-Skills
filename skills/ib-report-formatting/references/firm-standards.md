# Investment Bank Firm Standards Reference

## Goldman Sachs

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Goldman Sans (proprietary) |
| Fallback font | Arial |
| Body size | 10-11pt |
| Table size | 9-10pt |

### Terminology & Style

| Term | Correct Usage |
|------|---------------|
| Firm reference | "the firm" (lowercase) |
| Possessive | "Goldman Sachs'" |
| Compound | "firmwide" (one word, lowercase) |
| Spelling | US spellings globally |
| Date format | "January 1, 2018" |

### Document Guidelines

- Use approved templates only
- Limited emphasis (sparingly colored text, boldface, all caps, italics)
- Active voice preferred
- Descriptive hyperlink text (never "click here")
- White space valued for readability

### Color Palette

| Use | Color |
|-----|-------|
| Primary brand | #10478A (Goldman Blue) |
| Headers | Navy or Goldman Blue |
| Body text | Black |
| Accents | Gold sparingly |

---

## Morgan Stanley

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Helvetica |
| Fallback font | Arial |
| Body size | 10pt |
| Table size | 9pt |

### Document Standards

- Precise alignment to page borders
- Meticulous spacing measurement
- Clean, modern aesthetic
- Consistent visual hierarchy
- Professional restraint in design

### Pitchbook Standards

| Element | Specification |
|---------|---------------|
| Slide count | 40-60 slides |
| Appendix | 60+ pages |
| Orientation | Landscape |
| Margins | 0.5" minimum |

### Color Palette

| Use | Color |
|-----|-------|
| Primary | #002D72 (MS Blue) |
| Secondary | #6E6E6E (Gray) |
| Accent | #00B2A9 (Teal) |

---

## JP Morgan

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Arial |
| Fallback font | Helvetica |
| Body size | 10pt |
| Table size | 9pt |
| Excel models | Arial 10pt, 80-90% zoom |

### Document Standards

- Conservative, professional appearance
- Emphasis on clarity over design
- Structured document hierarchy
- Consistent numbering systems
- Clear section breaks

### Color Palette

| Use | Color |
|-----|-------|
| Primary | #003D6A (JPM Blue) |
| Headers | Navy |
| Tables | Blue headers, minimal color |

---

## Bank of America / Merrill Lynch

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Arial |
| Body size | 10pt |
| Table size | 9pt |

### Color Palette

| Use | Color |
|-----|-------|
| Primary | #012169 (BofA Blue) |
| Secondary | #C8102E (Red accent) |

---

## Citi

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Calibri |
| Fallback font | Arial |
| Body size | 10pt |

### Color Palette

| Use | Color |
|-----|-------|
| Primary | #003B70 (Citi Blue) |
| Secondary | #00BDF2 (Light Blue) |

---

## UBS / Barclays

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Helvetica |
| Body size | 10pt |

### UBS Colors

| Use | Color |
|-----|-------|
| Primary | #E60000 (UBS Red) |
| Secondary | #000000 (Black) |

### Barclays Colors

| Use | Color |
|-----|-------|
| Primary | #00AEEF (Barclays Blue) |

---

## Lazard / Evercore (Boutiques)

### Typography

| Element | Standard |
|---------|----------|
| Primary font | Garamond |
| Fallback font | Times New Roman |
| Body size | 11pt |

More traditional, elegant appearance appropriate for M&A advisory focus.

---

## Financial Model Color Coding (Industry Standard)

### Cell Color Conventions

| Color | Hex | Use |
|-------|-----|-----|
| Blue (text) | #0000FF | Hard-coded inputs, historical data |
| Black (text) | #000000 | Formulas, same-sheet references |
| Green (text) | #008000 | Links to other worksheets |
| Red (text) | #FF0000 | External file links, errors |
| Yellow (fill) | #FFFF00 | Key assumptions, sensitivity inputs |

### Implementation

```javascript
// Input cell (blue text)
new TextRun({ text: "1,500", color: "0000FF" })

// Formula cell (black text)
new TextRun({ text: "2,250", color: "000000" })

// Cross-reference (green text)
new TextRun({ text: "3,750", color: "008000" })

// Key assumption (yellow background)
new TableCell({
  shading: { fill: "FFFF00", type: ShadingType.CLEAR },
  children: [/* content */]
})
```

---

## McKinsey & Consulting Firm Standards

### Presentation Structure

| Principle | Description |
|-----------|-------------|
| Pyramid Principle | Conclusion first, then supporting points |
| MECE | Mutually Exclusive, Collectively Exhaustive |
| SCR | Situation-Complication-Resolution storyline |

### Typography

| Element | Standard |
|---------|----------|
| Body font | Arial |
| Title font | Georgia |
| Max fonts | 2 families per document |

### Slide Standards

- Action titles (readable as standalone storyline)
- Slide numbers on every page
- Source citations in every footer
- Clean, minimal design
- Data-driven visualizations

---

## Big 4 Accounting Firms

### PCAOB Audit Report Standards

- Standardized opinion letter format
- Clear section headers (Opinion, Basis for Opinion, Critical Audit Matters)
- Consistent date formatting
- Signature blocks with engagement partner identification

### Report Formatting

| Element | Standard |
|---------|----------|
| Font | Times New Roman or Arial |
| Body size | 11-12pt |
| Margins | 1" minimum |
| Line spacing | 1.5 for drafts, single for finals |

---

## Common Cross-Firm Standards

### Numbers

| Format | Example | Use |
|--------|---------|-----|
| Currency | $1,234.5 | Financial values |
| Multiples | 12.5x | Valuation multiples |
| Percentages | 25.5% | Margins, growth rates |
| Negatives | (1,234) | Losses, decreases |

### Tables

| Element | Standard |
|---------|----------|
| Header background | Navy or dark blue |
| Header text | White, bold |
| Borders | Minimal vertical, horizontal emphasis |
| Alignment | Left for text, right for numbers |
| Alternating rows | Subtle gray shading |

### Document Elements

| Element | Standard |
|---------|----------|
| Confidentiality | Header or footer on every page |
| Page numbers | "Page X of Y" format |
| Dates | Spelled out month (January 17, 2026) |
| Source citations | Italic footnotes |
| Disclaimers | End of document or dedicated page |

---

## Implementation Template

```javascript
// Firm-agnostic professional styling
const firmStyles = {
  // Conservative defaults work across all banks
  fonts: {
    primary: "Arial",
    body: { size: 20, color: "000000" },      // 10pt
    table: { size: 18, color: "000000" },     // 9pt
    header: { size: 18, bold: true, color: "FFFFFF" }
  },
  colors: {
    navy: "1F3864",      // Universal header color
    black: "000000",
    gray: "595959",
    lightGray: "F7F7F7",
    highlight: "FFF2CC"
  },
  // Model color coding
  modelColors: {
    input: "0000FF",
    formula: "000000",
    crossRef: "008000",
    error: "FF0000",
    assumption: "FFFF00"
  }
};
```
