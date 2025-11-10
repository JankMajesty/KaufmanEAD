# Kaufman EAD Preliminary Finding Aid Project

## Project Overview

This is a preliminary finding aid for the **Terrence Kaufman Papers** at the Archive of Indigenous Languages of Latin America (AILLA), housed at the Benson Latin American Studies and Collections, University of Texas at Austin.

**Collection Details:**
- **Extent**: 62 linear feet (62 boxes)
- **Status**: Unprocessed collection - preliminary inventory only
- **Subtitle**: "Preliminary Inventory"
- **Finding Aid Type**: Container list (box-level description, no folder-level detail)

This is a **pre-processing snapshot** that describes materials as physically stored, not intellectually arranged into traditional archival series. The structure may change once the collection undergoes full archival processing.

## Terrence Kaufman Collection Context

**Terrence Kaufman (1937-2022)** was a linguistic anthropologist who conducted 50 years of research on indigenous languages of the Americas, with primary focus on Mesoamerica (Mexico and Guatemala).

**Key Research Projects:**
- **Proyecto Lingüístico Francisco Marroquín (PLFM)**: Guatemala, 1970s
- **Project for the Documentation of the Languages of MesoAmerica (PDLMA)**: Mexico, 1993-2010

**Materials Types:**
- Lexical file slips (unpublished dictionary drafts in dozens of boxes)
- Audio recordings (cassettes, open-reels, MiniDiscs, CDs)
- Video recordings (Hi-8, miniDV)
- Field notes and research papers
- Administrative documents and worklogs

**Languages Documented** (extensive multilingual collection):
- Mayan language family (multiple languages and dialects)
- Mixe-Zoquean languages
- Zapotecan languages
- Nahuatl varieties
- Otomanguean languages
- North American languages (Hokan, Pomoan, etc.)

## EAD Structure and Formatting Standards

### File Information
- **Main file**: `kaufmanEAD.xml`
- **Schema**: EAD 2002 DTD (NOT EAD3)
- **Validation**: Must validate against EAD 2002 DTD (`schema2.xsl`)
- **Template base**: BLAC_EADSchemaTemplate.xml
- **Integration**: TARO (Texas Archival Resources Online) compliant

### Unique Preliminary Inventory Structure

Unlike fully processed finding aids with multiple series and folder-level description, this preliminary finding aid uses:

#### FLAT HIERARCHY
- **Single series only**: One `<c01 level="series">` element titled "Terrence Kaufman Papers"
- **All boxes as direct children**: 62 `<c02 level="file">` elements under the single series
- **No subseries divisions**: No traditional series organization (correspondence, research files, etc.)
- **Box-level description only**: No `<c03>` folder-level components

#### Consistent Box Entry Structure
```xml
<c02 level="file">
  <did>
    <container type="box">1</container>
    <unittitle>Language Materials</unittitle>
  </did>
  <scopecontent>
    <!-- See formatting rules below -->
  </scopecontent>
</c02>
```

**Key conventions:**
- Every box uses `<unittitle>Language Materials</unittitle>` (consistent across all 62 boxes)
- Container numbers 1-62
- Structured scopecontent with specific field order (see below)

### CRITICAL: Scopecontent Formatting Standards

Based on archivist feedback, the `<scopecontent>` element follows this exact structure:

```xml
<scopecontent>
  <p>Content: [item 1]; [item 2]; [item 3]; [item n]</p>
  <p>Language Name: [standardized language name]</p>
  <p>Country: [geographic location]</p>
  <p>Digital collection: <archref>[AILLA collection link]</archref></p>
  <p>AILLA Notes: [additional context]</p>  <!-- only when applicable -->
</scopecontent>
```

#### Field-by-Field Rules:

**1. Content Field**
- **Single `<p>` tag** containing all physical inventory items
- **Semicolon separation**: Multiple items separated by `; ` (semicolon + space)
- **Format**: `Content: [item 1]; [item 2]; [item 3]`
- **Inventory notation**:
  - Counts and descriptions of file slip boxes
  - Audio/video media with formats (CDs, cassettes, MiniDiscs, etc.)
  - Dates when relevant
  - Example: `Content: 1 fileslip box 2002, 2009; 2 fileslip boxes 2002; 1 fileslip box 2004 with 0.5" fileslips, 7 CDs, 1 audio cassette`

**2. Language Name Field**
- **Separate `<p>` tag**: `<p>Language Name: [name]</p>`
- Use standardized language names (proper linguistic terminology)
- Multiple languages separated by appropriate punctuation

**3. Country Field**
- **Separate `<p>` tag**: `<p>Country: [location]</p>`
- Geographic locations where language is/was spoken
- Multiple countries separated by commas if applicable

**4. Digital Collection Field**
- **Separate `<p>` tag** with embedded `<archref>` element
- Format: `<p>Digital collection: <archref>[AILLA URL]</archref></p>`
- Links to corresponding AILLA digital collection materials

**5. AILLA Notes Field (optional)**
- **Separate `<p>` tag**: `<p>AILLA Notes: [notes]</p>`
- Only include when there is additional contextual information
- Use for clarifications, special conditions, or important context

#### IMPORTANT: What Changed
- **OLD FORMAT** (boxes 1-48 prior to archivist feedback): Multiple `<p>` tags for each content item
- **NEW FORMAT** (all boxes now): Content items consolidated in single `<p>` tag with semicolon separation
- **Other fields unchanged**: Language Name, Country, Digital collection, AILLA Notes remain in separate `<p>` tags

## AILLA Integration Standards

### Digital Collection Links
- Every box links to corresponding AILLA digital collection via `<archref>` element
- AILLA serves as primary access point for digitized materials
- Finding aid documents physical materials; digital access through AILLA

### Indigenous Language Documentation Practices
- Respectful representation of indigenous languages and communities
- Proper language name standardization
- Cultural sensitivity and intellectual property awareness
- Research access considerations (materials stored remotely, advance notice required)

## Institutional Context: AILLA and Benson

**AILLA (Archive of Indigenous Languages of Latin America)**
- Specialized archive for endangered indigenous language documentation
- Focus on Latin American indigenous languages
- Digital preservation and access mission
- Integration with physical collections at Benson

**Benson Latin American Studies and Collections**
- Part of University of Texas at Austin Libraries
- Major research collection for Latin American materials
- TARO (Texas Archival Resources Online) participant
- EAD 2002 standards for finding aids

## Reference Materials in Project

### Institutional Template
- `BLAC_EADSchemaTemplate.xml`: Benson's standard EAD structure

### Example Finding Aids (for reference)
- `carlosMorton.xml`: Carlos Morton Papers (processed, multiple series, findaidstatus="edited-full-draft")
- `ailla.xml`: AILLA Collection (findaidstatus="unverified-partial-draft")
- `noraEnglandEAD.xml`: Nora England Papers (linguist collection, similar content)
- `pirapirana.xml`: Another AILLA-related collection

### Validation Tools
- `schema2.xsl`: EAD 2002 validation schema

## Current Project Status

### Work Completed
- 62 box entries created with structured scopecontent
- AILLA digital collection links integrated
- Language names and geographic data documented
- Physical inventory documented for all boxes

### Current Task
- Applying formatting changes across all 62 boxes based on archivist feedback
- Consolidating Content field items with semicolon separation (instead of multiple `<p>` tags)
- Additional formatting refinements to follow

### Future Work
- Additional archivist feedback items to address
- Ongoing validation against EAD 2002 DTD
- Potential structure changes when collection undergoes full processing
- Additional materials expected: `<accruals>` note indicates "Additional materials will be added to this collection once digitization work is complete."

## Quality Control and Validation

### EAD 2002 Compliance
- Validate against EAD 2002 DTD using `schema2.xsl`
- Ensure proper namespace declarations
- Use correct encoding analogs (MARC21 where applicable)
- Maintain TARO requirements

### Consistency Checks
- All 62 boxes follow identical formatting structure
- Consistent use of `<unittitle>Language Materials</unittitle>`
- Scopecontent fields in correct order
- Proper semicolon separation in Content field
- All AILLA `<archref>` links properly formatted

### Content Accuracy
- Verify language names use standardized terminology
- Confirm geographic locations are accurate
- Ensure physical inventory counts are correct
- Check AILLA collection URLs are valid

## Working Guidelines

### When Editing kaufmanEAD.xml

1. **Preserve EAD 2002 structure**: Never introduce EAD3 elements
2. **Maintain flat hierarchy**: Single series, all boxes as `<c02>` elements
3. **Follow scopecontent formatting exactly**: Content field with semicolons; other fields in separate `<p>` tags
4. **Validate after changes**: Ensure XML remains valid against EAD 2002 DTD
5. **Consistency is critical**: All 62 boxes must follow identical formatting

### Archival Principles for This Project

- **Preliminary inventory purpose**: Provide access to unprocessed materials
- **Physical description focus**: Document what exists and where it's located
- **Digital access integration**: Connect researchers to AILLA digital collections
- **Future processing expected**: This structure is temporary; full processing will create traditional series/subseries organization
- **Transparency about status**: Finding aid clearly marked as "Preliminary Inventory" and collection noted as "not processed"

## Additional Notes

### Processing Information
From the finding aid's `<processinfo>`:
> "This collection is not processed."

This preliminary finding aid provides:
- Basic intellectual control (box-level description)
- Physical location information
- Connection to digital surrogates (AILLA)
- Access point for researchers while awaiting full processing

### Access Considerations
- Materials stored remotely (note in `<accessrestrict>`)
- Advance notice required for access
- Intellectual property rights and indigenous community rights must be respected
- Some materials may have access restrictions pending community consultation

### Relationship to AILLA Digital Collections
- Physical materials (described in this finding aid) complement digital collections
- AILLA digital collections are primary access point for many materials
- Some physical materials may not yet be digitized
- Finding aid serves as bridge between physical and digital access
