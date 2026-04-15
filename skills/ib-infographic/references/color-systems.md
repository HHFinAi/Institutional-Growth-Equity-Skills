# IB Color Systems Reference

## Primary Palette (Goldman/MS Standard)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Primary Navy | #1F3864 | 31, 56, 100 | Headers, hero metrics, totals |
| Secondary Blue | #2E75B6 | 46, 117, 182 | Charts, links, secondary emphasis |
| Accent Gold | #C5A572 | 197, 165, 114 | Premium highlights, accents |
| Positive Green | #00B050 | 0, 176, 80 | Positive deltas, growth |
| Negative Red | #C00000 | 192, 0, 0 | Negative deltas, decline, warnings |
| Neutral Gray | #7F7F7F | 127, 127, 127 | Body text, labels, axis |
| Light Gray | #D0D0D0 | 208, 208, 208 | Borders, gridlines |
| Very Light Gray | #E8E8E8 | 232, 232, 232 | Dotted gridlines |
| Light Fill | #E8F1F8 | 232, 241, 248 | Background highlights, cards |

## Extended Palette

| Name | Hex | Use Case |
|------|-----|----------|
| Teal | #008080 | Third data series |
| Orange | #ED7D31 | Attention, alternate accent |
| Purple | #7030A0 | Fourth data series |
| Dark Green | #006400 | Strong positive |
| Light Blue | #5B9BD5 | Softer data series |
| Dark Red | #8B0000 | Strong negative |

## Firm-Specific Palettes

### Goldman Sachs
- Primary: #003865 (Goldman Blue)
- Secondary: #B0B7BC (Silver)
- Accent: #D3BC8D (Gold)

### Morgan Stanley
- Primary: #00467F (MS Blue)
- Secondary: #7C878E (Slate)
- Accent: #C4B67C (Gold)

### JP Morgan
- Primary: #004C6D (JPM Blue)
- Secondary: #6D6E71 (Gray)
- Accent: #B58B00 (Gold)

## Usage Rules

### Data Visualization
1. Use navy for totals/key figures
2. Use blue for general data series
3. Reserve green/red for directional indicators only
4. Use gray for labels and non-data elements
5. Maximum 5 colors per chart

### Positive/Negative Convention
- Always green for positive
- Always red for negative
- Never invert (even for costs where down is good)
- Use neutral gray for unchanged/NA

### Background Colors
- White (#FFFFFF) for main background
- Light Fill (#E8F1F8) for callout boxes
- Very Light Gray (#E8E8E8) for table alternating rows

### Text Colors
- Navy for headers
- Black (#000000) for body text
- Gray (#7F7F7F) for labels, captions, secondary text
- White for text on dark backgrounds

## Accessibility

All color combinations should meet WCAG AA contrast standards:
- Navy on white: ✓ 10.5:1
- Gray on white: ✓ 4.5:1
- White on navy: ✓ 10.5:1
- Green on white: ✗ 3.2:1 (use for indicators only, not text)
- Red on white: ✓ 5.1:1

## Financial Model Convention

| Color | Hex | Meaning |
|-------|-----|---------|
| Blue | #0000FF | Hard-coded inputs, historical |
| Black | #000000 | Formulas, same-sheet |
| Green | #008000 | Links to other sheets |
| Red | #FF0000 | External links, errors |
| Yellow BG | #FFFF00 | Key assumptions (highlight) |
