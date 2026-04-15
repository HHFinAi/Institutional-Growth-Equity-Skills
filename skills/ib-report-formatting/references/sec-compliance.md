# SEC & Regulatory Compliance Reference

## SEC EDGAR Filing Requirements

### Format Requirements

| Format | Requirements |
|--------|--------------|
| ASCII | Courier/Courier New 12pt, 80 char max line, 1" min margins |
| HTML | Version 3.2, Times New Roman/Arial/Verdana recommended |
| PDF | Unofficial only, must accompany HTML/ASCII |
| Graphics | GIF/JPG only |
| File Size | 200 MB max (600 MB for certain forms) |

### Invalid ASCII Characters

Do not use these characters in EDGAR filings:
- ¥ (Yen)
- £ (Pound)
- © (Copyright)
- ® (Registered)
- ™ (Trademark)
- Smart quotes (" " ' ')
- Em/En dashes (— –)

Use ASCII equivalents:
- `(C)` for ©
- `(R)` for ®
- `(TM)` for ™
- Straight quotes (" ')
- Double hyphen (--) for em dash

---

## Common SEC Forms

### Form 10-K (Annual Report)

| Requirement | Specification |
|-------------|---------------|
| Filing deadline | 60 days (large accelerated), 75 days (accelerated), 90 days (others) |
| Parts | 4 parts, 16 items |
| Financial statements | Audited, 2-3 years comparative |
| Signatures | CEO, CFO, majority of directors |

**Required Sections:**
1. Business description
2. Risk factors
3. Selected financial data
4. MD&A
5. Financial statements
6. Controls and procedures

### Form 10-Q (Quarterly Report)

| Requirement | Specification |
|-------------|---------------|
| Filing deadline | 40 days (large accelerated/accelerated), 45 days (others) |
| Parts | 2 parts |
| Financial statements | Unaudited, condensed |

### Form 8-K (Current Report)

| Requirement | Specification |
|-------------|---------------|
| Filing deadline | 4 business days |
| Triggers | Material events (acquisition, officer change, etc.) |

### Form S-1 (Registration Statement)

**Cover Page Requirements:**
- Company name prominently displayed
- Type and amount of securities
- Offering price range (or "To be determined")
- Underwriting discount
- Proceeds to company
- Exchange listing (if applicable)
- Risk factor cross-reference (prominently highlighted)
- SEC legend
- "Subject to completion" legend (red herring)

---

## XBRL/Inline XBRL Requirements

### Required Tagging Levels

| Level | Requirement |
|-------|-------------|
| Level 1 | Face of financial statements |
| Level 2 | Footnotes - text blocks |
| Level 3 | Footnotes - table tagging |
| Level 4 | Footnotes - detail tagging |

### Applicability

All operating company filings:
- Form 10-K
- Form 10-Q
- Form 8-K (with financial statements)
- Registration statements

---

## FINRA Rule 2241 (Research Reports)

### Required Disclosures

Must appear on front page or be clearly referenced:

| Disclosure | Requirement |
|------------|-------------|
| Firm/affiliate ownership | > 1% of equity securities |
| Market making | If firm is market maker |
| IB compensation | Received in past 12 months |
| Expected IB compensation | Next 3 months |
| Analyst interests | Financial interests in subject |
| Material conflicts | Any other conflicts |

### Rating Distribution

- Required chart showing firm's rating distribution
- Line graph of daily closing prices
- Period: Since rating assigned or 3 years

### Format

```
DISCLOSURES

Ownership: [Firm] and/or its affiliates beneficially own 1% or more 
of the common stock of [Company].

Investment Banking: [Firm] has received compensation for investment 
banking services from [Company] in the past 12 months.

Market Making: [Firm] makes a market in the securities of [Company].

Rating Distribution:
Buy: 45%
Hold: 40%
Sell: 15%
```

---

## Prospectus Requirements

### Red Herring (Preliminary Prospectus)

Required elements:
- "Subject to Completion" legend in red
- Preliminary price range
- All material information except final pricing
- "Red herring" legend on cover

```
SUBJECT TO COMPLETION, DATED [DATE]

The information in this preliminary prospectus is not complete 
and may be changed. These securities may not be sold until the 
registration statement filed with the Securities and Exchange 
Commission is effective.
```

### Final Prospectus

Required elements:
- Final offering price
- Final proceeds
- Final underwriting discount
- Use of proceeds
- Risk factors prominently placed

---

## Offering Memorandum (Private Placements)

### Standard Sections

1. **Cover Page**
   - Company name
   - Securities offered
   - Offering amount
   - Confidentiality legend
   
2. **Disclaimer/Legends**
   - Not registered with SEC
   - Accredited investor requirement
   - Forward-looking statement legend
   
3. **Executive Summary**
4. **Risk Factors**
5. **Use of Proceeds**
6. **Business Description**
7. **Management**
8. **Financial Information**
9. **Terms of Securities**

### Required Legends

```
CONFIDENTIAL

This Confidential Offering Memorandum (this "Memorandum") is being 
furnished on a confidential basis to a limited number of sophisticated 
investors for the sole purpose of evaluating a potential investment 
in [Company Name] (the "Company").

This Memorandum does not constitute an offer to sell or a solicitation 
of an offer to buy any securities in any jurisdiction where such offer 
or sale would be unlawful.

The securities offered hereby have not been registered under the 
Securities Act of 1933, as amended (the "Securities Act"), or any 
state securities laws and may not be offered or sold in the United 
States absent registration or an applicable exemption from registration.
```

---

## Document Formatting for SEC Filings

### Margins

| Element | Minimum |
|---------|---------|
| Top | 1 inch |
| Bottom | 1 inch |
| Left | 1 inch |
| Right | 1 inch |

### Fonts

| Format | Recommended Fonts |
|--------|-------------------|
| ASCII | Courier, Courier New |
| HTML | Times New Roman, Arial, Verdana |
| Size | 10pt minimum for body text |

### Tables

- Clear column headers
- Consistent alignment (right for numbers)
- Thousands separator for large numbers
- Parentheses for negative values
- Currency symbols where appropriate
- "nm" or "n/a" for non-meaningful values

### Financial Statement Presentation

```
                                    Year Ended December 31,
                                  2025        2024        2023
                                  ----        ----        ----
                                      (in thousands)

Net revenues                   $1,234,567  $1,123,456  $1,012,345
Cost of revenues                  617,284     561,728     506,173
                               ----------  ----------  ----------
Gross profit                      617,283     561,728     506,172

Operating expenses:
  Research and development        185,185     168,518     151,852
  Sales and marketing             246,913     224,691     202,469
  General and administrative       61,728      56,173      50,617
                               ----------  ----------  ----------
    Total operating expenses      493,826     449,382     404,938
                               ----------  ----------  ----------

Operating income                  123,457     112,346     101,234
```

---

## Compliance Checklist

### Before Filing

- [ ] All required sections present
- [ ] Signatures obtained
- [ ] Financial statements audited (10-K) or reviewed (10-Q)
- [ ] Risk factors comprehensive and current
- [ ] Forward-looking statement legend included
- [ ] XBRL tags applied
- [ ] File size under limit
- [ ] No invalid characters
- [ ] Cross-references accurate
- [ ] Page numbers correct

### Document Review

- [ ] Consistent formatting throughout
- [ ] Numbers foot and cross-foot
- [ ] Dates accurate
- [ ] Names spelled correctly
- [ ] Defined terms used consistently
- [ ] No tracked changes or comments remaining
- [ ] Headers/footers appropriate

---

## Implementation Notes

When generating SEC-compliant documents with docx-js:

1. **Use basic formatting** - Avoid complex styles
2. **Stick to standard fonts** - Arial, Times New Roman
3. **Test character encoding** - Ensure ASCII compatibility
4. **Verify table alignment** - Numbers right-aligned
5. **Check file output** - Validate before submission
