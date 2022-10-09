import csv
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from itertools import groupby
from typing import List


def read_xml_to_list_of_dict(path: str) -> List[dict]:
    tree = ET.parse(path)
    root = tree.getroot()
    data = []
    for child in root.iter('record'):
        row = {}
        for elem in child.iter():
            if elem.tag == "record":
                continue

            if elem.tag == "BIRTHDAY" or elem.tag == "HIRED":
                row[elem.tag] = datetime.strptime(elem.text, "%d-%m-%Y").strftime("%Y-%m-%d")
                continue

            row[elem.tag] = elem.text

        if row["STATUS"] not in ["1", "2", "3"] and row["GENDER"] not in ["0", "1"]:
            continue

        data.append(row)
    return data


def generate_csv_by_nationality(input_file_path: str, output_folder: str):
    obj = read_xml_to_list_of_dict(input_file_path)
    obj.sort(key=lambda x: x['NATIONALITY'])

    for key, val in groupby(obj, key=lambda x: x['NATIONALITY']):
        contents = list(val)

        columns = contents[0].keys()
        with open(f'{output_folder}/{key}.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, columns)
            dict_writer.writeheader()
            dict_writer.writerows(contents)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        generate_csv_by_nationality(input_file_path=sys.argv[1], output_folder=sys.argv[2])
    else:
        print("Please insert param")
