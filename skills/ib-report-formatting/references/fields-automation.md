# Fields & Automation Reference (68 Field Types)

## Overview

Word fields are dynamic placeholders that automatically update content. Essential for IB documents with page numbers, dates, document properties, and calculated values.

---

## Field Syntax

```javascript
const { SimpleField } = require('docx');

// Basic field
new SimpleField({ instruction: "FIELD_NAME" })

// Field with switches
new SimpleField({ instruction: 'FIELD_NAME \\* Switch \\# "Format"' })
```

### Common Field Switches

| Switch | Type | Description | Example |
|--------|------|-------------|---------|
| `\\*` | Format | Text formatting | `\\* Upper` |
| `\\#` | Numeric | Number format | `\\# "$#,##0"` |
| `\\@` | Date | Date format | `\\@ "MMMM d, yyyy"` |

---

## Document Information Fields

### Filename & Path

```javascript
// Filename only
new SimpleField({ instruction: "FILENAME" })
// Result: "Report.docx"

// Filename with path
new SimpleField({ instruction: "FILENAME \\p" })
// Result: "C:\Documents\Report.docx"

// File size
new SimpleField({ instruction: 'FILESIZE \\# "#,##0 KB"' })
// Result: "1,205 KB"
```

### Document Properties

```javascript
// Author
new SimpleField({ instruction: "AUTHOR" })

// Title
new SimpleField({ instruction: "TITLE" })

// Subject
new SimpleField({ instruction: "SUBJECT" })

// Last saved by
new SimpleField({ instruction: "LASTSAVEDBY" })

// Revision number
new SimpleField({ instruction: "REVNUM" })
```

### Custom Document Properties

```javascript
// Define custom properties in document
const doc = new Document({
  customProperties: [
    { name: "Project Name", value: "Project Alpha" },
    { name: "Deal Value", value: "$500mm" },
    { name: "Client", value: "TechCo Inc." },
    { name: "Confidentiality", value: "Strictly Confidential" }
  ]
});

// Reference in document
new SimpleField({ instruction: 'DOCPROPERTY "Project Name"' })
// Result: "Project Alpha"
```

---

## Date & Time Fields

### Current Date/Time

```javascript
// Formatted date
new SimpleField({ instruction: 'DATE \\@ "MMMM d, yyyy"' })
// Result: "January 17, 2026"

// Formatted time
new SimpleField({ instruction: 'TIME \\@ "h:mm AM/PM"' })
// Result: "3:45 PM"
```

### Document Dates

| Field | Description |
|-------|-------------|
| CREATEDATE | Document creation date |
| SAVEDATE | Last saved date |
| PRINTDATE | Last printed date |
| EDITTIME | Total editing time (minutes) |

### Date Format Codes

| Code | Result | Example |
|------|--------|---------|
| M | Month (1-12) | 1 |
| MM | Month (01-12) | 01 |
| MMM | Month abbrev | Jan |
| MMMM | Month full | January |
| d | Day (1-31) | 7 |
| dd | Day (01-31) | 07 |
| yy | Year (2 digit) | 26 |
| yyyy | Year (4 digit) | 2026 |
| h | Hour (1-12) | 3 |
| H | Hour (0-23) | 15 |
| mm | Minute (00-59) | 05 |
| AM/PM | AM or PM | PM |

---

## Page Number Fields

### Basic Page Numbers

```javascript
// Current page
new SimpleField({ instruction: "PAGE" })

// Total pages
new SimpleField({ instruction: "NUMPAGES" })

// Section pages
new SimpleField({ instruction: "SECTIONPAGES" })
```

### "Page X of Y" Pattern

```javascript
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "Page ", font: "Arial", size: 16, color: "808080" }),
    new SimpleField({ instruction: "PAGE" }),
    new TextRun({ text: " of ", font: "Arial", size: 16, color: "808080" }),
    new SimpleField({ instruction: "NUMPAGES" })
  ]
})
```

### Page Number Formatting

| Switch | Format | Example |
|--------|--------|---------|
| `\\* Arabic` | 1, 2, 3 | 5 |
| `\\* Roman` | I, II, III | V |
| `\\* roman` | i, ii, iii | v |
| `\\* Alphabetic` | A, B, C | E |

---

## Sequence Fields (Auto-Numbering)

### Basic Sequences

```javascript
// Table numbering
new Paragraph({
  children: [
    new TextRun("Table "),
    new SimpleField({ instruction: "SEQ Table \\* ARABIC" }),
    new TextRun(": Comparable Companies Analysis")
  ]
})
// Result: "Table 1: Comparable Companies Analysis"

// Figure numbering
new Paragraph({
  children: [
    new TextRun("Figure "),
    new SimpleField({ instruction: "SEQ Figure \\* ARABIC" }),
    new TextRun(": Valuation Football Field")
  ]
})
```

### Sequence Switches

| Switch | Effect | Example |
|--------|--------|---------|
| `\\r N` | Reset to N | `\\r 1` starts at 1 |
| `\\c` | Repeat current | Shows same number |
| `\\n` | Next number | Increments (default) |

---

## Calculated Fields

### Basic Expressions

```javascript
// Simple calculation
new SimpleField({ instruction: "= 100 + 50" })
// Result: 150

// With formatting
new SimpleField({ instruction: '= 1234567 \\# "$#,##0"' })
// Result: "$1,234,567"
```

### Table Calculations

```javascript
// Sum column above current cell
new SimpleField({ instruction: '= SUM(ABOVE) \\# "#,##0.0"' })

// Sum row to the left
new SimpleField({ instruction: '= SUM(LEFT) \\# "#,##0.0"' })

// Average
new SimpleField({ instruction: '= AVERAGE(ABOVE) \\# "#,##0.0"' })

// Max/Min
new SimpleField({ instruction: '= MAX(ABOVE) \\# "#,##0.0"' })
new SimpleField({ instruction: '= MIN(ABOVE) \\# "#,##0.0"' })
```

### Number Format Codes

| Code | Description | Example |
|------|-------------|---------|
| `#` | Optional digit | 1234 |
| `0` | Required digit | 001234 |
| `,` | Thousands separator | 1,234 |
| `.` | Decimal point | 1234.56 |
| `$` | Currency symbol | $1,234 |
| `%` | Percentage | 12.34% |
| `()` | Negative in parens | (1,234) |

```javascript
// Currency with 2 decimals
new SimpleField({ instruction: '= value \\# "$#,##0.00"' })

// Percentage
new SimpleField({ instruction: '= value \\# "0.0%"' })

// Negative in parentheses
new SimpleField({ instruction: '= value \\# "#,##0;(#,##0)"' })
```

---

## Reference Fields

### REF (Bookmark Reference)

```javascript
// Reference bookmark content
new SimpleField({ instruction: "REF company-name" })

// Reference with formatting preserved
new SimpleField({ instruction: "REF company-name \\* MERGEFORMAT" })
```

### PAGEREF (Page Number of Bookmark)

```javascript
// Get page number where bookmark is located
new SimpleField({ instruction: "PAGEREF valuation-section" })

// "See page X"
new Paragraph({
  children: [
    new TextRun("(See page "),
    new SimpleField({ instruction: "PAGEREF valuation-section" }),
    new TextRun(")")
  ]
})
```

### STYLEREF (Content from Style)

```javascript
// Get text of nearest Heading 1
new SimpleField({ instruction: 'STYLEREF "Heading 1"' })

// Useful in headers to show current section name
```

---

## IB-Specific Field Patterns

### Cover Page

```javascript
// Project name from custom property
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "PROJECT ", size: 48, bold: true, color: "1F3864" }),
    new SimpleField({ instruction: 'DOCPROPERTY "Project Name" \\* UPPER' })
  ]
})
```

### Footer with Section & Page

```javascript
new Footer({
  children: [
    new Paragraph({
      children: [
        new SimpleField({ instruction: 'STYLEREF "Heading 1" \\* MERGEFORMAT' }),
        new TextRun("  |  Page "),
        new SimpleField({ instruction: "PAGE" }),
        new TextRun(" of "),
        new SimpleField({ instruction: "NUMPAGES" })
      ]
    })
  ]
})
```

### Auto-Numbered Tables

```javascript
new Paragraph({
  children: [
    new TextRun({ text: "Table ", bold: true }),
    new SimpleField({ instruction: "SEQ Table \\* ARABIC" }),
    new TextRun({ text: ": ", bold: true }),
    new TextRun("Comparable Companies Analysis")
  ]
})
```

---

## Field Reference Table

| Field | Description | Example Output |
|-------|-------------|----------------|
| PAGE | Current page | 5 |
| NUMPAGES | Total pages | 25 |
| DATE | Current date | January 17, 2026 |
| TIME | Current time | 3:45 PM |
| AUTHOR | Document author | John Smith |
| FILENAME | File name | Report.docx |
| TITLE | Document title | Project Alpha |
| CREATEDATE | Creation date | January 10, 2026 |
| SAVEDATE | Last saved | January 17, 2026 |
| SEQ | Sequence number | 1, 2, 3... |
| REF | Bookmark content | (varies) |
| PAGEREF | Page of bookmark | 12 |
| STYLEREF | Text from style | Section Title |
| DOCPROPERTY | Custom property | (varies) |

---

## Best Practices for IB Documents

1. **Use DOCPROPERTY** for project name, client name, confidentiality level
2. **Use SEQ** for table and figure numbering
3. **Use STYLEREF** in headers for running section names
4. **Use PAGE/NUMPAGES** in footers
5. **Use DATE** with consistent formatting
6. **Bookmark key values** for cross-referencing
7. **Test field updates** before finalizing document
