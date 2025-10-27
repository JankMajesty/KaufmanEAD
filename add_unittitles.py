#!/usr/bin/env python3
"""
Add <unittitle>[Language files]</unittitle> after each <container type="box"> element
that doesn't already have a unittitle.
"""

import re

def add_unittitles(input_file, output_file):
    """Add unittitle elements after container elements where missing."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]
        modified_lines.append(line)

        # Check if this line contains a container element
        if '<container type="box">' in line and '</container>' in line:
            # Check if the next line (after whitespace) contains a unittitle
            # Look ahead to see if there's already a unittitle
            has_unittitle = False
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('<unittitle>'):
                    has_unittitle = True

            # If no unittitle found, add one
            if not has_unittitle:
                # Get the indentation from the container line
                indent = len(line) - len(line.lstrip())
                unittitle_line = ' ' * indent + '<unittitle>[Language files]</unittitle>\n'
                modified_lines.append(unittitle_line)

        i += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)

    # Count changes
    original_content = ''.join(lines)
    new_content = ''.join(modified_lines)

    original_containers = len(re.findall(r'<container type="box">', original_content))
    existing_unittitles = original_content.count('<unittitle>')
    new_unittitles = new_content.count('<unittitle>')
    added = new_unittitles - existing_unittitles

    print(f"Found {original_containers} container elements")
    print(f"Existing unittitles: {existing_unittitles}")
    print(f"Added {added} new unittitle elements")
    print(f"Total unittitles now: {new_unittitles}")

if __name__ == "__main__":
    input_file = "/Users/jankmajesty/Desktop/ailla/EAD/kaufmanEAD.xml"
    output_file = "/Users/jankmajesty/Desktop/ailla/EAD/kaufmanEAD.xml.new"

    add_unittitles(input_file, output_file)
    print(f"\nOutput written to: {output_file}")
    print("Review the changes, then run: mv kaufmanEAD.xml.new kaufmanEAD.xml")
