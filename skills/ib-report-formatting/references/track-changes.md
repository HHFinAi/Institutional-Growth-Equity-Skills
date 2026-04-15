# Track Changes & Comments Reference (22 Properties)

## Track Changes Overview

Essential for IB deal teams collaborating on transaction documents, offering memoranda, and legal agreements.

---

## Enabling Track Changes

```javascript
const doc = new Document({
  settings: {
    trackRevisions: true
  },
  // ... rest of document
});
```

---

## Revision Types

### Insertions

```javascript
const { InsertedTextRun } = require('docx');

new Paragraph({
  children: [
    new TextRun({ text: "The purchase price is " }),
    new InsertedTextRun({
      text: "$500 million",
      id: 1,
      author: "John Smith",
      date: "2026-01-17T10:00:00Z"
    }),
    new TextRun({ text: " subject to adjustment." })
  ]
})
```

### Deletions

```javascript
const { DeletedTextRun } = require('docx');

new Paragraph({
  children: [
    new TextRun({ text: "The purchase price is " }),
    new DeletedTextRun({
      text: "$450 million",
      id: 2,
      author: "John Smith",
      date: "2026-01-17T10:00:00Z"
    }),
    new InsertedTextRun({
      text: "$500 million",
      id: 3,
      author: "John Smith",
      date: "2026-01-17T10:00:00Z"
    }),
    new TextRun({ text: " subject to adjustment." })
  ]
})
```

### Formatting Changes

```javascript
// Formatting changes tracked via revision properties
new TextRun({
  text: "Important term",
  bold: true,
  revision: {
    id: 4,
    author: "Jane Doe",
    date: "2026-01-17T11:00:00Z"
  }
})
```

---

## Revision Properties

| Property | Type | Description |
|----------|------|-------------|
| id | number | Unique revision identifier |
| author | string | Name of person making change |
| date | string | ISO 8601 timestamp |

### Best Practices for IB Documents

| Author Format | Example | Use Case |
|---------------|---------|----------|
| Full name | "John Smith" | External documents |
| Initials | "JS" | Internal drafts |
| Role | "Analyst" | Anonymous review |
| Team | "Deal Team" | Collaborative edits |

---

## Revision View Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| FINAL | Shows document as if all changes accepted | Client presentation |
| ORIGINAL | Shows document before changes | Comparison |
| FINAL_MARKUP | Shows final with visible markup | Review |
| ORIGINAL_MARKUP | Shows original with visible markup | Detailed review |

```javascript
const doc = new Document({
  settings: {
    trackRevisions: true,
    revisionView: RevisionView.FINAL_MARKUP
  }
});
```

---

## Comments

### Adding Comments

```javascript
const { Comment, CommentRangeStart, CommentRangeEnd, CommentReference } = require('docx');

// Step 1: Define comment in document settings
const doc = new Document({
  comments: {
    children: [
      new Comment({
        id: 0,
        author: "Senior Analyst",
        initials: "SA",
        date: new Date("2026-01-17T14:30:00Z"),
        children: [
          new Paragraph({
            children: [new TextRun("Please verify this revenue figure against 10-K filing.")]
          })
        ]
      })
    ]
  },
  sections: [/* ... */]
});

// Step 2: Mark commented text in document
new Paragraph({
  children: [
    new TextRun("Revenue of "),
    new CommentRangeStart({ id: 0 }),
    new TextRun("$1.5 billion"),
    new CommentRangeEnd({ id: 0 }),
    new CommentReference({ id: 0 }),
    new TextRun(" was reported.")
  ]
})
```

### Comment Properties

| Property | Type | Description |
|----------|------|-------------|
| id | number | Unique comment identifier |
| author | string | Comment author name |
| initials | string | Author initials (for balloon display) |
| date | Date | Comment timestamp |
| children | Paragraph[] | Comment content |

### Comment Threading (Replies)

```javascript
// Parent comment
new Comment({
  id: 0,
  author: "Analyst",
  date: new Date(),
  children: [
    new Paragraph({ children: [new TextRun("Need to verify this figure.")] })
  ]
})

// Reply to comment
new Comment({
  id: 1,
  author: "VP",
  date: new Date(),
  children: [
    new Paragraph({ children: [new TextRun("Confirmed with CFO - figure is correct.")] })
  ]
  // Note: Threading requires additional XML attributes not fully supported in docx-js
})
```

---

## IB Comment Conventions

### Standard Comment Tags

| Tag | Meaning | Example |
|-----|---------|---------|
| [VERIFY] | Needs fact-check | "[VERIFY] Confirm market cap" |
| [SOURCE] | Needs citation | "[SOURCE] Add data source" |
| [LEGAL] | Legal review needed | "[LEGAL] Review disclosure" |
| [CLIENT] | Client input needed | "[CLIENT] Confirm company name" |
| [INTERNAL] | Internal note only | "[INTERNAL] Discuss with MD" |
| [TODO] | Action required | "[TODO] Update projections" |
| [QUESTION] | Clarification needed | "[QUESTION] Which fiscal year?" |

### Comment Workflow

1. **Draft Review**
   - Analyst adds [VERIFY] and [SOURCE] comments
   - Associate reviews and resolves

2. **Legal Review**
   - Counsel adds [LEGAL] comments
   - Deal team addresses and marks resolved

3. **Client Review**
   - Client adds [CLIENT] comments via tracked document
   - Team incorporates feedback

4. **Final Review**
   - VP/MD adds final comments
   - All comments resolved before printing

---

## Document Comparison

### Comparing Two Documents

```javascript
// Note: Full document comparison requires Word or OpenXML SDK
// docx-js creates documents; comparison is done externally

// Approach 1: Use Word's built-in Compare feature
// File → Compare → Compare Documents

// Approach 2: Use OpenXML SDK for programmatic comparison
// Microsoft.Office.Interop.Word.Document.Compare()

// Approach 3: Export both to text and use diff tools
```

### Combining Revisions from Multiple Authors

```javascript
// Note: Combining requires Word or advanced XML manipulation
// File → Compare → Combine Documents
```

---

## Revision Color Coding

Word automatically assigns colors to different authors. Common conventions:

| Author Role | Typical Color | Use |
|-------------|---------------|-----|
| Original author | Red | Base changes |
| Legal counsel | Blue | Legal edits |
| Client | Green | Client feedback |
| Senior reviewer | Purple | Final edits |

---

## Lock Tracking

Prevent users from turning off track changes:

```javascript
const doc = new Document({
  settings: {
    trackRevisions: true,
    // Lock tracking requires document protection
    protection: {
      type: ProtectionType.TRACKED_CHANGES,
      password: "optional"
    }
  }
});
```

---

## Complete Example: Tracked M&A Agreement Edit

```javascript
const { Document, Paragraph, TextRun, InsertedTextRun, DeletedTextRun,
        Comment, CommentRangeStart, CommentRangeEnd, CommentReference } = require('docx');

const doc = new Document({
  settings: {
    trackRevisions: true
  },
  comments: {
    children: [
      new Comment({
        id: 0,
        author: "Legal Counsel",
        initials: "LC",
        date: new Date("2026-01-17T09:00:00Z"),
        children: [
          new Paragraph({
            children: [new TextRun("[LEGAL] Confirm earnout structure complies with GAAP.")]
          })
        ]
      })
    ]
  },
  sections: [{
    children: [
      new Paragraph({
        children: [
          new TextRun({ text: "ARTICLE II", bold: true }),
        ]
      }),
      new Paragraph({
        children: [
          new TextRun({ text: "PURCHASE PRICE", bold: true }),
        ],
        spacing: { after: 240 }
      }),
      new Paragraph({
        children: [
          new TextRun("2.1  "),
          new TextRun({ text: "Purchase Price.", bold: true }),
          new TextRun("  The aggregate purchase price for the Shares shall be "),
          new DeletedTextRun({
            text: "Four Hundred Fifty Million Dollars ($450,000,000)",
            id: 1,
            author: "Deal Team",
            date: "2026-01-16T15:00:00Z"
          }),
          new InsertedTextRun({
            text: "Five Hundred Million Dollars ($500,000,000)",
            id: 2,
            author: "Deal Team",
            date: "2026-01-16T15:00:00Z"
          }),
          new TextRun(" (the \""),
          new TextRun({ text: "Purchase Price", bold: true }),
          new TextRun("\"), subject to adjustment as set forth in Section 2.2.")
        ]
      }),
      new Paragraph({
        spacing: { before: 240 },
        children: [
          new TextRun("2.2  "),
          new TextRun({ text: "Earnout.", bold: true }),
          new TextRun("  In addition to the Purchase Price, Buyer shall pay to Seller "),
          new CommentRangeStart({ id: 0 }),
          new TextRun("an earnout payment of up to Twenty-Five Million Dollars ($25,000,000)"),
          new CommentRangeEnd({ id: 0 }),
          new CommentReference({ id: 0 }),
          new TextRun(" based on achievement of the performance targets set forth in Exhibit A.")
        ]
      })
    ]
  }]
});
```

---

## Best Practices

### For IB Documents

1. **Always track changes** on legal documents, term sheets, and client-facing materials
2. **Use consistent author names** across the deal team
3. **Date all revisions** for audit trail
4. **Resolve comments** before final version
5. **Accept all changes** before printing/sending final version
6. **Keep revision history** for deal records

### Performance Considerations

- Large documents with many revisions can slow Word
- Consider accepting changes periodically during long editing sessions
- Archive revision history before accepting all changes
