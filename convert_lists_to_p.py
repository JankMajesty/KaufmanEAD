#!/usr/bin/env python3
"""
Convert EAD list elements to paragraph elements according to Benson feedback.
Converts multi-item lists to single paragraphs with inline content.
"""

import re
import sys

def convert_list_to_p(list_content):
    """
    Convert a list structure to a p element.
    Takes the items and combines them appropriately.
    """
    # Extract all items from the list
    items = re.findall(r'<item>(.*?)</item>', list_content, re.DOTALL)

    if not items:
        return list_content

    # First item is typically the label (e.g., "Content:", "Language Name:")
    label = items[0].strip()

    if len(items) == 1:
        # Just a label, no content
        return f"<p>{label}</p>"
    elif len(items) == 2:
        # Label and single value
        content_items = items[1:]
        combined = ' '.join(item.strip() for item in content_items)
        return f"<p>{label} {combined}</p>"
    else:
        # Label and multiple values - combine with brackets for sub-items
        content_items = items[1:]
        # Join the content items
        combined = ' '.join(item.strip() for item in content_items)
        # If the first content item doesn't start with a dash, wrap sub-items in brackets
        if content_items and not content_items[0].strip().startswith('-'):
            # First item is the main content, rest are details
            main_content = content_items[0].strip()
            details = ' '.join(item.strip() for item in content_items[1:])
            if details:
                return f"<p>{label} {main_content} [{details}]</p>"
            else:
                return f"<p>{label} {main_content}</p>"
        else:
            # All items are details, combine them
            return f"<p>{label} [{combined}]</p>"

def process_file(input_file, output_file):
    """Process the EAD file and convert all list elements to p elements."""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match entire list elements including nested content
    # This will match from <list to </list> including everything in between
    list_pattern = r'<list type="simple">\s*(.*?)\s*</list>'

    def replace_list(match):
        list_content = match.group(0)
        return convert_list_to_p(list_content)

    # Replace all lists with paragraphs
    new_content = re.sub(list_pattern, replace_list, content, flags=re.DOTALL)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Count changes
    original_count = len(re.findall(list_pattern, content, re.DOTALL))
    new_count = len(re.findall(list_pattern, new_content, re.DOTALL))

    print(f"Converted {original_count - new_count} list elements to p elements")
    print(f"Remaining list elements: {new_count}")

if __name__ == "__main__":
    input_file = "/Users/jankmajesty/Desktop/ailla/EAD/kaufmanEAD.xml"
    output_file = "/Users/jankmajesty/Desktop/ailla/EAD/kaufmanEAD.xml.new"

    process_file(input_file, output_file)
    print(f"\nOutput written to: {output_file}")
    print("Review the changes, then run: mv kaufmanEAD.xml.new kaufmanEAD.xml")
