# Setup Instructions for EAD Kaufman-Benson Skill

## Overview

This skill helps you work on the Terrence Kaufman Papers EAD finding aid with Claude's assistance. It provides specialized knowledge about EAD2002, AILLA standards, and Benson institutional practices.

## Quick Setup

### 1. Add Your Files to the Skill

Place your working files in the `references/` directory:

**Required files:**
- `KaufmanEAD.xml` - Your working EAD finding aid
- `schema2.xsl` - The EAD2002 schema for validation

**Reference files (examples from your institution):**
- `carlosmorton.xml` - Carlos Morton Papers EAD
- `ailla.xml` - AILLA collection EAD
- `pirapirana.xml` - Pirapirana collection EAD

### 2. Package the Skill

Once you've added your files, package the skill:

```bash
python3 /mnt/skills/examples/skill-creator/scripts/package_skill.py ead-kaufman-benson
```

This creates a `ead-kaufman-benson.skill` file.

### 3. Install the Skill

Upload the `.skill` file to Claude through the Skills interface.

## How to Use This Skill

Once installed, you can ask Claude things like:

### Working on Your Finding Aid

- "Review my KaufmanEAD.xml file and identify any structural issues"
- "Help me implement this feedback: [paste feedback]"
- "Compare my finding aid structure to the carlosmorton example"
- "Add a scope and content note that follows AILLA standards"
- "Validate my EAD file against the schema"

### Understanding Feedback

- "Explain what this feedback means: [paste feedback]"
- "Show me how to implement this change in my EAD"
- "What's the best way to reorganize Series 2 based on this feedback?"

### Getting EAD Guidance

- "What elements should I include in the biographical note?"
- "How do I properly encode multiple languages in langmaterial?"
- "Show me the correct way to structure series and subseries"
- "What subject headings should I use for linguistic materials?"

### Quality Checks

- "Check if all required EAD2002 elements are present"
- "Validate my component hierarchy"
- "Review my controlled access terms"
- "Compare my description style to the reference EADs"

## Available Tools

### Python Scripts

**validate_ead.py**
Checks XML well-formedness and analyzes EAD structure:
```bash
python scripts/validate_ead.py references/KaufmanEAD.xml
```

**compare_ead.py**
Compares your EAD structure with reference examples:
```bash
python scripts/compare_ead.py references/KaufmanEAD.xml references/carlosmorton.xml
```

Or extract specific sections:
```bash
python scripts/compare_ead.py references/KaufmanEAD.xml --section scopecontent
```

### Reference Documents

- **ead2002-elements.md** - Quick reference for EAD elements
- **feedback-implementation.md** - Guide for implementing archival feedback
- **README.md** - Overview of reference files

## Workflow Example

Here's a typical workflow for implementing feedback:

1. **Upload feedback**: Share the feedback you received
2. **Review together**: "Help me understand this feedback and prioritize the changes"
3. **Implement changes**: "Let's work through these changes one at a time"
4. **Validate**: "Check that my changes are valid EAD2002"
5. **Compare**: "Compare my revised sections to the reference EADs"
6. **Document**: "Help me update the processing information to reflect these changes"

## Tips for Best Results

1. **Be specific**: Share the exact feedback or section you're working on
2. **Reference examples**: Ask Claude to check reference EADs for similar patterns
3. **Validate often**: Check your XML after making changes
4. **Ask questions**: If feedback is unclear, ask Claude to help interpret it
5. **Iterate**: Work on one section or series at a time

## File Structure

```
ead-kaufman-benson/
├── SKILL.md                              # Main skill instructions
├── scripts/
│   ├── validate_ead.py                  # XML validation tool
│   └── compare_ead.py                   # Structure comparison tool
├── references/
│   ├── ead2002-elements.md              # EAD element reference
│   ├── feedback-implementation.md       # Feedback workflow guide
│   ├── README.md                        # This file
│   ├── KaufmanEAD.xml                   # Your working file (add this)
│   ├── schema2.xsl                      # EAD schema (add this)
│   ├── carlosmorton.xml                 # Reference EAD (add this)
│   ├── ailla.xml                        # Reference EAD (add this)
│   └── pirapirana.xml                   # Reference EAD (add this)
└── assets/                               # (empty - not needed for this skill)
```

## Troubleshooting

**"Claude isn't using the skill"**
- Make sure you mention key terms like "EAD", "finding aid", "Kaufman", or "KaufmanEAD.xml"
- Try: "Using my EAD skill, help me with..."

**"Can't find my reference files"**
- Check that files are in the `references/` directory before packaging
- Repackage the skill after adding files

**"Validation errors"**
- Run the validate_ead.py script to identify specific issues
- Ask Claude: "Help me fix this validation error: [error message]"

**"Not sure how to implement feedback"**
- Share the exact feedback text with Claude
- Ask: "How should I implement this feedback in my EAD?"
- Reference the feedback-implementation.md guide

## Getting Help

When asking Claude for help:

1. Mention which file you're working on (e.g., "in my KaufmanEAD.xml file")
2. Share specific feedback or error messages
3. Ask Claude to reference the institutional examples
4. Request validation after changes

Example: "In my KaufmanEAD.xml file, I need to add more detail to the biographical note. Can you check the carlosmorton example and help me write something similar that follows AILLA standards?"
