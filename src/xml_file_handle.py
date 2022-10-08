import xml.etree.ElementTree as ET
from typing import List


def read_file(path: str) -> List[dict]:
    tree = ET.parse('resources/data-devclub-1.xml')
    root = tree.getroot()
    for child in root.iter():
        print(child.tag, child.attrib)

    return [{
        "x": "y"
    }]
