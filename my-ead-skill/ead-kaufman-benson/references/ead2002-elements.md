# EAD2002 Elements Quick Reference

This guide provides quick reference for commonly used EAD2002 elements in archival finding aids.

## Document Structure

### Root Elements

```xml
<ead>
  <eadheader>
    <!-- Metadata about the finding aid itself -->
  </eadheader>
  <archdesc level="collection">
    <!-- Main archival description -->
  </archdesc>
</ead>
```

## EAD Header Elements

### Basic Header Structure

```xml
<eadheader>
  <eadid>Unique identifier for this EAD</eadid>
  <filedesc>
    <titlestmt>
      <titleproper>Title of Finding Aid</titleproper>
      <author>Author name</author>
    </titlestmt>
    <publicationstmt>
      <publisher>Repository name</publisher>
      <date>Publication date</date>
    </publicationstmt>
  </filedesc>
  <profiledesc>
    <creation>Finding aid created <date>date</date></creation>
    <langusage>Finding aid written in <language>English</language></langusage>
  </profiledesc>
</eadheader>
```

## Archival Description Elements

### Required <did> Elements

The Descriptive Identification element contains essential metadata:

```xml
<did>
  <unittitle>Title of materials</unittitle>
  <unitid>Collection identifier</unitid>
  <unitdate normal="1950/2000">1950-2000</unitdate>
  <physdesc>
    <extent>5 linear feet (10 boxes)</extent>
  </physdesc>
  <repository>
    <corpname>Repository Name</corpname>
  </repository>
  <langmaterial>
    <language langcode="eng">English</language>
    <language langcode="spa">Spanish</language>
  </langmaterial>
  <origination label="Creator">
    <persname>Creator Name</persname>
  </origination>
  <abstract>Brief description of collection</abstract>
</did>
```

### Administrative Information

```xml
<descgrp type="admininfo">
  <head>Administrative Information</head>
  
  <accessrestrict>
    <head>Access Restrictions</head>
    <p>Collection is open for research.</p>
  </accessrestrict>
  
  <userestrict>
    <head>Use Restrictions</head>
    <p>Copyright restrictions may apply.</p>
  </userestrict>
  
  <prefercite>
    <head>Preferred Citation</head>
    <p>Proper citation format here</p>
  </prefercite>
  
  <acqinfo>
    <head>Acquisition Information</head>
    <p>Details about how materials were acquired</p>
  </acqinfo>
  
  <processinfo>
    <head>Processing Information</head>
    <p>Processing details and date</p>
  </processinfo>
</descgrp>
```

### Descriptive Elements

```xml
<bioghist>
  <head>Biographical Note</head>
  <p>Biographical or historical information about creator or materials</p>
</bioghist>

<scopecontent>
  <head>Scope and Content Note</head>
  <p>Description of what's in the collection and its significance</p>
</scopecontent>

<arrangement>
  <head>Arrangement</head>
  <p>How the materials are organized (series, chronological, etc.)</p>
</arrangement>

<relatedmaterial>
  <head>Related Material</head>
  <p>Information about related collections elsewhere</p>
</relatedmaterial>

<separatedmaterial>
  <head>Separated Material</head>
  <p>Information about materials removed from collection</p>
</separatedmaterial>
```

### Controlled Access Terms

```xml
<controlaccess>
  <head>Index Terms</head>
  
  <persname source="lcnaf">Personal name</persname>
  <corpname source="lcnaf">Corporate name</corpname>
  <geogname source="lcsh">Geographic name</geogname>
  <subject source="lcsh">Subject heading</subject>
  <genreform source="aat">Genre/form term</genreform>
  <occupation source="lcsh">Occupation</occupation>
</controlaccess>
```

## Description of Subordinate Components

### Container List Structure

```xml
<dsc type="combined">
  <head>Container List</head>
  
  <c01 level="series">
    <did>
      <unittitle>Series 1: Correspondence</unittitle>
      <unitdate normal="1960/1970">1960-1970</unitdate>
      <physdesc><extent>2 boxes</extent></physdesc>
    </did>
    <scopecontent>
      <p>Description of series contents</p>
    </scopecontent>
    
    <c02 level="file">
      <did>
        <container type="box">1</container>
        <container type="folder">1</container>
        <unittitle>Letters to family</unittitle>
        <unitdate>1960-1965</unitdate>
      </did>
    </c02>
    
    <c02 level="file">
      <did>
        <container type="box">1</container>
        <container type="folder">2</container>
        <unittitle>Professional correspondence</unittitle>
        <unitdate>1965-1970</unitdate>
      </did>
    </c02>
  </c01>
  
  <c01 level="series">
    <did>
      <unittitle>Series 2: Research Files</unittitle>
      <unitdate normal="1970/1980">1970-1980</unitdate>
    </did>
    <!-- Additional components -->
  </c01>
</dsc>
```

## Special Elements for Linguistic/Indigenous Materials

### Language Material Encoding

For multilingual collections (especially important for AILLA):

```xml
<langmaterial>
  <language langcode="eng">English</language>
  <language langcode="spa">Spanish</language>
  <language langcode="nah">Nahuatl</language>
  <language langcode="may">Mayan languages</language>
</langmaterial>
```

### Cultural Context Notes

```xml
<odd type="cultural">
  <head>Cultural Context</head>
  <p>Information about cultural sensitivity, indigenous community connections, 
     or special handling requirements</p>
</odd>
```

## Common Attributes

### Date Normalization

```xml
<!-- Single date -->
<unitdate normal="1965">1965</unitdate>

<!-- Date range -->
<unitdate normal="1960/1970">1960-1970</unitdate>

<!-- Approximate date -->
<unitdate normal="1965" certainty="approximate">circa 1965</unitdate>

<!-- Bulk dates -->
<unitdate normal="1950/2000">1950-2000</unitdate>
<unitdate type="bulk" normal="1960/1970">bulk 1960-1970</unitdate>
```

### Level Attributes

For `<archdesc>` and `<c>` elements:

- `level="collection"` - Entire collection
- `level="recordgrp"` - Record group
- `level="series"` - Major grouping
- `level="subseries"` - Subdivision of series
- `level="file"` - File folder
- `level="item"` - Individual item

### Audience Attribute

```xml
<!-- Internal use only -->
<processinfo audience="internal">
  <p>Internal processing notes</p>
</processinfo>

<!-- Public display -->
<scopecontent>
  <p>Public description</p>
</scopecontent>
```

## Tips for Clean EAD Markup

1. **Always close tags properly** - EAD must be well-formed XML
2. **Use semantic nesting** - Follow proper parent-child relationships
3. **Normalize dates** - Use `normal` attribute for machine-readable dates
4. **Include source attributes** - Cite authority files (lcnaf, lcsh, aat)
5. **Use meaningful IDs** - Make `unitid` values clear and consistent
6. **Paragraph tags** - Wrap narrative text in `<p>` tags
7. **Escape special characters** - Use entities: `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`

## Common Validation Errors

1. Missing required elements (`<unittitle>` in `<did>`)
2. Improper nesting (e.g., `<c02>` outside a `<c01>`)
3. Undefined attributes or values
4. Text content not wrapped in `<p>` tags where required
5. Unclosed or mismatched tags
6. Invalid language codes or source attributes
