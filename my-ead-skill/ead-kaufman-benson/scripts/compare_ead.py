#!/usr/bin/env python3
"""
EAD Structure Comparison Tool

Compare the structure of your working EAD against reference examples
to ensure consistency with institutional standards.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import sys
from typing import List, Dict


def get_element_path(element, namespace=''):
    """Get a simplified path representation of an element."""
    tag = element.tag.replace(namespace, '')
    attribs = []
    
    if 'level' in element.attrib:
        attribs.append(f"level={element.attrib['level']}")
    if 'type' in element.attrib:
        attribs.append(f"type={element.attrib['type']}")
    
    if attribs:
        return f"{tag}[{', '.join(attribs)}]"
    return tag


def extract_structure(xml_file: str, max_depth: int = 5) -> List[str]:
    """
    Extract the hierarchical structure of an EAD file.
    
    Args:
        xml_file: Path to EAD XML file
        max_depth: Maximum depth to traverse
        
    Returns:
        List of structure strings
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Detect namespace
        namespace = ''
        if root.tag.startswith('{'):
            namespace = root.tag.split('}')[0] + '}'
        
        structure = []
        
        def traverse(element, depth=0, path=''):
            if depth > max_depth:
                return
            
            current_path = get_element_path(element, namespace)
            full_path = f"{path}/{current_path}" if path else current_path
            
            # Add to structure with indentation
            indent = '  ' * depth
            structure.append(f"{indent}{current_path}")
            
            # Process children
            for child in element:
                traverse(child, depth + 1, full_path)
        
        traverse(root)
        return structure
        
    except Exception as e:
        return [f"Error: {str(e)}"]


def compare_structures(file1: str, file2: str):
    """Compare structures of two EAD files."""
    print(f"\nComparing:")
    print(f"  File 1: {Path(file1).name}")
    print(f"  File 2: {Path(file2).name}")
    print("\n" + "="*60)
    
    structure1 = extract_structure(file1)
    structure2 = extract_structure(file2)
    
    print(f"\n{Path(file1).name} structure:")
    print("-" * 60)
    for line in structure1[:50]:  # Limit to first 50 lines
        print(line)
    
    if len(structure1) > 50:
        print(f"\n... and {len(structure1) - 50} more lines")
    
    print(f"\n\n{Path(file2).name} structure:")
    print("-" * 60)
    for line in structure2[:50]:
        print(line)
    
    if len(structure2) > 50:
        print(f"\n... and {len(structure2) - 50} more lines")


def extract_section(xml_file: str, section: str) -> str:
    """
    Extract a specific section from an EAD file.
    
    Args:
        xml_file: Path to EAD file
        section: Section to extract (e.g., 'bioghist', 'scopecontent', 'controlaccess')
    
    Returns:
        String representation of the section
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Detect namespace
        namespace = ''
        if root.tag.startswith('{'):
            namespace = root.tag.split('}')[0] + '}'
        
        # Find the requested section
        element = root.find('.//' + namespace + section)
        
        if element is not None:
            return ET.tostring(element, encoding='unicode', method='xml')
        else:
            return f"Section '{section}' not found in {xml_file}"
            
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Compare structures: python compare_ead.py <file1.xml> <file2.xml>")
        print("  Extract section: python compare_ead.py <file.xml> --section <section_name>")
        sys.exit(1)
    
    if '--section' in sys.argv:
        xml_file = sys.argv[1]
        section = sys.argv[3]
        print(extract_section(xml_file, section))
    elif len(sys.argv) == 3:
        compare_structures(sys.argv[1], sys.argv[2])
    else:
        # Just show structure of one file
        structure = extract_structure(sys.argv[1])
        print(f"\nStructure of {Path(sys.argv[1]).name}:")
        print("="*60)
        for line in structure:
            print(line)


if __name__ == "__main__":
    main()
