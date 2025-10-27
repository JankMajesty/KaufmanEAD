# Implementing Archival Feedback Guide

This guide helps systematically implement feedback from archivists and supervisors on preliminary finding aids.

## Feedback Implementation Workflow

### 1. Document the Feedback

Create a clear record of all feedback received:

- **Source**: Who provided the feedback (name, role)
- **Date**: When feedback was received
- **Priority**: Critical / Important / Nice-to-have
- **Category**: Structural / Descriptive / Administrative / Technical
- **Specific Item**: Exact location in EAD (element, series, etc.)
- **Requested Change**: What needs to change
- **Rationale**: Why the change is needed (if provided)

### 2. Categorize Feedback Types

#### Structural Changes
- Reorganizing series or subseries
- Changing component hierarchy levels
- Adjusting arrangement of materials
- Modifying container numbering

#### Descriptive Improvements
- Enhancing scope and content notes
- Refining biographical/historical notes
- Clarifying titles and headings
- Improving folder-level descriptions
- Adding missing context

#### Administrative Updates
- Access restrictions revisions
- Use restrictions clarifications
- Processing information updates
- Preferred citation corrections
- Acquisition details

#### Technical Corrections
- XML syntax errors
- Element nesting issues
- Required elements missing
- Attribute corrections
- Schema validation errors

#### Metadata Enhancements
- Controlled vocabulary updates
- Subject heading additions
- Language code corrections
- Date normalization
- Name authority alignment

### 3. Prioritize Changes

**Critical (Do First)**
- Issues blocking publication or access
- Required elements missing
- Schema validation errors
- Factual inaccuracies
- Privacy/sensitivity concerns

**Important (Do Soon)**
- Significant description gaps
- Structural reorganization
- Access policy clarifications
- Major content improvements

**Enhancement (Do When Time Allows)**
- Additional detail in descriptions
- Formatting improvements
- Optional metadata enhancements
- Cross-reference additions

### 4. Implementation Process

For each feedback item:

1. **Locate**: Find the exact location in KaufmanEAD.xml
2. **Review**: Check reference EADs for similar examples
3. **Plan**: Determine exact changes needed
4. **Implement**: Make the changes in XML
5. **Validate**: Check XML well-formedness and schema compliance
6. **Document**: Note what was changed and why
7. **Review**: Compare with institutional standards

### 5. Common Feedback Scenarios

#### "Add more context to the scope and content note"

**Before:**
```xml
<scopecontent>
  <p>Papers of Terrence Kaufman.</p>
</scopecontent>
```

**After:**
```xml
<scopecontent>
  <head>Scope and Content</head>
  <p>The Terrence Kaufman Papers document his extensive research in 
  Mesoamerican linguistics, particularly his work on Mayan language 
  reconstruction and historical linguistics. The collection includes 
  field notes, manuscript drafts, correspondence with other linguists, 
  and unpublished research materials spanning his career from [dates]. 
  Materials are particularly strong in [specific areas].</p>
</scopecontent>
```

#### "Reorganize series to reflect creation/processing order"

May require restructuring entire `<dsc>` section with new series divisions.

#### "Add subject headings for better discovery"

```xml
<controlaccess>
  <head>Index Terms</head>
  <subject source="lcsh">Mayan languages--Grammar</subject>
  <subject source="lcsh">Historical linguistics--Methodology</subject>
  <subject source="lcsh">Indigenous languages--Mexico</subject>
  <geogname source="lcsh">Mesoamerica--Languages</geogname>
  <persname source="lcnaf">Kaufman, Terrence</persname>
</controlaccess>
```

#### "Specify access restrictions more clearly"

**Before:**
```xml
<accessrestrict>
  <p>Some restrictions may apply.</p>
</accessrestrict>
```

**After:**
```xml
<accessrestrict>
  <head>Access Restrictions</head>
  <p>Collection is open for research with the following exceptions: 
  materials containing personal information about living individuals 
  are restricted for 50 years from date of creation. Some materials 
  may be restricted at the request of indigenous communities. Contact 
  the repository for details.</p>
</accessrestrict>
```

#### "Include cultural sensitivity statement"

For indigenous language materials:

```xml
<odd type="cultural">
  <head>Cultural Sensitivity</head>
  <p>This collection contains materials documenting indigenous languages 
  and cultures. Researchers are expected to respect the cultural protocols 
  of the communities represented. Some materials may be culturally sensitive 
  or contain traditional knowledge that should be handled with appropriate care 
  and consultation with community members.</p>
</odd>
```

### 6. Quality Checks After Implementation

- [ ] All feedback items addressed or noted if not applicable
- [ ] Changes documented in processing information
- [ ] XML validates against schema
- [ ] Consistent with reference EAD examples
- [ ] No new validation errors introduced
- [ ] Descriptive text is clear and professional
- [ ] All required elements present
- [ ] Dates properly normalized
- [ ] Subject headings from controlled vocabularies
- [ ] Cultural sensitivity considerations addressed

### 7. Documentation

Update the processing information to reflect changes:

```xml
<processinfo>
  <head>Processing Information</head>
  <p>Collection processed by [name] in [date]. Preliminary finding aid 
  created [date]. Finding aid revised [date] incorporating feedback from 
  [name], [title]. Revisions included: [brief summary of major changes].</p>
</processinfo>
```

### 8. Communication

When returning revised finding aid:

- Summarize changes made
- Note any feedback items not implemented (with rationale)
- Highlight areas where clarification is needed
- Ask about any remaining questions
- Request final review

## Tips for Success

1. **Work methodically** - Address one category of feedback at a time
2. **Use reference EADs** - Match institutional style and standards
3. **Validate frequently** - Check XML after each major change
4. **Document as you go** - Keep track of what's been changed
5. **Seek clarification** - Ask questions about ambiguous feedback
6. **Maintain backup** - Keep version history of changes
7. **Think holistically** - Consider how changes affect the whole finding aid
8. **Stay organized** - Use a tracking system for feedback items
