# Visual Hierarchy Reference

## Section Dividers

| Type | Thickness | Color | Width | Use Case |
|------|-----------|-------|-------|----------|
| Heavy rule | 2–3pt (40–60) | #1F3864 | 100% | Major section break |
| Medium rule | 1–1.5pt (20–30) | #808080 | 100% | Minor section break |
| Light rule | 0.5pt (10) | #BFBFBF | 100% | Subtle separation |
| Partial rule | 1pt (20) | #808080 | 33% centered | Visual pause |

```javascript
function createHorizontalRule(type = "medium") {
  const configs = {
    heavy: { size: 48, color: "1F3864" },
    medium: { size: 24, color: "808080" },
    light: { size: 10, color: "BFBFBF" }
  };
  
  const config = configs[type];
  return new Paragraph({
    border: {
      bottom: { style: BorderStyle.SINGLE, size: config.size, color: config.color }
    },
    spacing: { before: 240, after: 240 }
  });
}
```

---

## Callout Boxes

### Style Definitions

| Style | Border | Background | Text Color | Use Case |
|-------|--------|------------|------------|----------|
| Highlight | #1F3864 1.5pt | #E8F1F8 | #1F3864 | Key takeaways |
| Warning | #C00000 1.5pt | #FFF0F0 | #C00000 | Risk factors |
| Info | #808080 1pt | #F5F5F5 | #000000 | Notes, context |
| Success | #375623 1pt | #F0F8F0 | #375623 | Positive outcomes |
| Executive | #1F3864 2pt | #FFFFFF | #000000 | Executive summary |

### Callout Box Specifications

| Element | Value |
|---------|-------|
| Border width | 1–2pt (20–40 DXA) |
| Corner radius | 0 (square) |
| Internal padding | 144–216 DXA (10–15pt) |
| External margin | 240–360 DXA (12–18pt) |

```javascript
function createCalloutBox(content, style = "highlight") {
  const styles = {
    highlight: { border: "1F3864", fill: "E8F1F8", text: "1F3864" },
    warning: { border: "C00000", fill: "FFF0F0", text: "C00000" },
    info: { border: "808080", fill: "F5F5F5", text: "000000" },
    success: { border: "375623", fill: "F0F8F0", text: "375623" },
    executive: { border: "1F3864", fill: "FFFFFF", text: "000000" }
  };
  
  const s = styles[style];
  const border = { style: BorderStyle.SINGLE, size: 24, color: s.border };
  
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: { top: border, bottom: border, left: border, right: border },
            shading: { fill: s.fill, type: ShadingType.CLEAR },
            margins: { top: 173, bottom: 173, left: 216, right: 216 },
            children: [
              new Paragraph({
                children: [new TextRun({ text: content, font: "Arial", size: 20, color: s.text })]
              })
            ]
          })
        ]
      })
    ]
  });
}
```

---

## Spacing Standards

### Paragraph Spacing (in twentieths of a point / DXA)

| Element | Before | After |
|---------|--------|-------|
| Document title | 0 | 480 |
| Section header (L1) | 480 | 240 |
| Section header (L2) | 360 | 180 |
| Section header (L3) | 240 | 120 |
| Body paragraph | 0 | 160 |
| Bullet item | 0 | 80 |
| Table caption | 240 | 120 |
| Footnote | 120 | 60 |

### Section Transitions

| Transition | Spacing |
|------------|---------|
| Title → First section | 480 twips |
| Major section → Major section | Page break or 480 twips |
| Section → Subsection | 360 twips |
| Text → Table | 240 twips |
| Table → Text | 240 twips |
| Table → Table | 360 twips |
| Text → Bullets | 120 twips |
| Bullets → Text | 200 twips |

```javascript
const spacing = {
  title: { before: 0, after: 480 },
  heading1: { before: 480, after: 240 },
  heading2: { before: 360, after: 180 },
  heading3: { before: 240, after: 120 },
  body: { before: 0, after: 160 },
  bullet: { before: 0, after: 80 },
  tableCaption: { before: 240, after: 120 },
  footnote: { before: 120, after: 60 }
};
```

---

## Bullet & List Formatting

### Bullet Hierarchy

| Level | Character | Unicode | Indent | Hanging |
|-------|-----------|---------|--------|---------|
| Primary | • | U+2022 | 720 | 360 |
| Secondary | – | U+2013 | 1080 | 360 |
| Tertiary | ○ | U+25CB | 1440 | 360 |

### Numbered List Hierarchy

| Level | Format | Indent | Hanging |
|-------|--------|--------|---------|
| Primary | 1., 2., 3. | 720 | 360 |
| Secondary | a., b., c. | 1080 | 360 |
| Tertiary | i., ii., iii. | 1440 | 360 |

**Important**: Never use unicode bullets directly. Always use `LevelFormat.BULLET` with numbering config.

```javascript
const { LevelFormat } = require('docx');

const bulletConfig = {
  config: [
    {
      reference: "ibBullets",
      levels: [
        {
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        },
        {
          level: 1,
          format: LevelFormat.BULLET,
          text: "–",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1080, hanging: 360 } } }
        },
        {
          level: 2,
          format: LevelFormat.BULLET,
          text: "○",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1440, hanging: 360 } } }
        }
      ]
    }
  ]
};

// Usage
new Paragraph({
  numbering: { reference: "ibBullets", level: 0 },
  children: [new TextRun("First bullet point")]
})
```

---

## Indent Hierarchy

| Level | Indent (DXA) | Use Case |
|-------|--------------|----------|
| Level 0 | 0 | Primary content |
| Level 1 | 360 | First sub-level |
| Level 2 | 720 | Second sub-level |
| Level 3 | 1080 | Third sub-level |
| Level 4 | 1440 | Deep nesting |

```javascript
function createIndentedParagraph(text, level = 0) {
  return new Paragraph({
    indent: { left: level * 360 },
    children: [new TextRun({ text, font: "Arial", size: 20 })]
  });
}
```

---

## Key Metrics Box

For highlighting 3-4 key metrics at the top of a page:

```javascript
function createMetricsBox(metrics) {
  // metrics = [{label: "EV", value: "$5.2bn"}, ...]
  const cells = metrics.map(m => 
    new TableCell({
      borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
      shading: { fill: "E8F1F8", type: ShadingType.CLEAR },
      margins: { top: 115, bottom: 115, left: 144, right: 144 },
      verticalAlign: VerticalAlign.CENTER,
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: m.label, font: "Arial", size: 16, color: "595959" }),
          ]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 60 },
          children: [
            new TextRun({ text: m.value, font: "Arial", size: 24, bold: true, color: "1F3864" }),
          ]
        })
      ]
    })
  );
  
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [new TableRow({ children: cells })]
  });
}

// Usage
createMetricsBox([
  { label: "Enterprise Value", value: "$5.2bn" },
  { label: "LTM Revenue", value: "$1.8bn" },
  { label: "LTM EBITDA", value: "$425mm" },
  { label: "EV/EBITDA", value: "12.3x" }
]);
```
