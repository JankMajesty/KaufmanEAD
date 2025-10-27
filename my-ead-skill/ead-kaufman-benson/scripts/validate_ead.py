#!/usr/bin/env python3
"""
EAD XML Validation and Analysis Tool

This script validates EAD XML files and provides analysis of their structure.
Useful for checking well-formedness and EAD2002 compliance.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import sys
from typing import Dict, List, Tuple


def validate_xml_wellformed(xml_file: str) -> Tuple[bool, str]:
    """
    Check if XML file is well-formed.
    
    Args:
        xml_file: Path to XML file
        
    Returns:
        Tuple of (is_valid, message)
    """
    try:
        ET.parse(xml_file)
        return True, "XML is well-formed"
    except ET.ParseError as e:
        return False, f"XML Parse Error: {str(e)}"
    except Exception as e:
        return False, f"Error reading file: {str(e)}"


def analyze_ead_structure(xml_file: str) -> Dict:
    """
    Analyze the structure of an EAD file.
    
    Args:
        xml_file: Path to EAD XML file
        
    Returns:
        Dictionary with structural analysis
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Remove namespace for easier processing
        # EAD typically uses xmlns="urn:isbn:1-931666-22-9"
        namespace = ''
        if root.tag.startswith('{'):
            namespace = root.tag.split('}')[0] + '}'
        
        analysis = {
            'root_element': root.tag.replace(namespace, ''),
            'has_eadheader': False,
            'has_archdesc': False,
            'archdesc_level': None,
            'collection_title': None,
            'series_count': 0,
            'total_components': 0,
            'required_elements': {},
        }
        
        # Find eadheader
        eadheader = root.find('.//' + namespace + 'eadheader')
        if eadheader is not None:
            analysis['has_eadheader'] = True
            
        # Find archdesc
        archdesc = root.find('.//' + namespace + 'archdesc')
        if archdesc is not None:
            analysis['has_archdesc'] = True
            analysis['archdesc_level'] = archdesc.get('level', 'Not specified')
            
            # Get collection title from archdesc/did/unittitle
            did = archdesc.find('.//' + namespace + 'did')
            if did is not None:
                unittitle = did.find('.//' + namespace + 'unittitle')
                if unittitle is not None:
                    analysis['collection_title'] = unittitle.text
                    
                # Check for required did elements
                analysis['required_elements'] = {
                    'unittitle': unittitle is not None,
                    'unitid': did.find('.//' + namespace + 'unitid') is not None,
                    'unitdate': did.find('.//' + namespace + 'unitdate') is not None,
                    'physdesc': did.find('.//' + namespace + 'physdesc') is not None,
                    'repository': did.find('.//' + namespace + 'repository') is not None,
                }
        
        # Count components
        for level in range(1, 13):
            components = root.findall('.//' + namespace + f'c{level:02d}[@level="series"]')
            analysis['series_count'] += len(components)
            
        # Count all c elements (any level)
        all_c = root.findall('.//' + namespace + 'c') 
        for level in range(1, 13):
            all_c.extend(root.findall('.//' + namespace + f'c{level:02d}'))
        analysis['total_components'] = len(all_c)
        
        return analysis
        
    except Exception as e:
        return {'error': str(e)}


def print_analysis(analysis: Dict):
    """Print analysis results in a readable format."""
    print("\n=== EAD Structure Analysis ===\n")
    
    if 'error' in analysis:
        print(f"Error analyzing file: {analysis['error']}")
        return
    
    print(f"Root Element: {analysis['root_element']}")
    print(f"Has EAD Header: {'✓' if analysis['has_eadheader'] else '✗'}")
    print(f"Has Archival Description: {'✓' if analysis['has_archdesc'] else '✗'}")
    print(f"Description Level: {analysis['archdesc_level']}")
    
    if analysis['collection_title']:
        print(f"Collection Title: {analysis['collection_title']}")
    
    print(f"\nSeries Count: {analysis['series_count']}")
    print(f"Total Components: {analysis['total_components']}")
    
    print("\n=== Required Elements in Collection <did> ===")
    for element, present in analysis['required_elements'].items():
        status = '✓' if present else '✗'
        print(f"{status} {element}")


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python validate_ead.py <path_to_ead.xml>")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    
    if not Path(xml_file).exists():
        print(f"Error: File not found: {xml_file}")
        sys.exit(1)
    
    print(f"Validating: {xml_file}")
    
    # Check well-formedness
    is_valid, message = validate_xml_wellformed(xml_file)
    print(f"\n{message}")
    
    if not is_valid:
        sys.exit(1)
    
    # Analyze structure
    analysis = analyze_ead_structure(xml_file)
    print_analysis(analysis)
    
    print("\n✓ Validation complete")


if __name__ == "__main__":
    main()
