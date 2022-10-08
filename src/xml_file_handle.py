import xml.etree.ElementTree as ET
from typing import List


def read_file(path: str) -> List[dict]:
    tree = ET.parse(path)
    root = tree.getroot()
    data = []
    for child in root.iter('record'):
        d = {}
        for x in child.iter():
            if x.tag == "record":
                continue
            d[x.tag] = x.text
        data.append(d)
    return data
