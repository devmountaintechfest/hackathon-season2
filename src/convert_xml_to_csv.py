import csv
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List


def check_leap_year(year: int):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False


def check_hired_greater_than_3year(hired_str: str):
    hired = datetime.strptime(hired_str, "%Y-%m-%d")
    current = datetime.now()
    diff_year = current.year - hired.year
    if diff_year >= 3:
        return True

    days_per_month = 366 / 12 if check_leap_year(hired.year) else 365 / 12
    current_days = (days_per_month * current.month) + current.day
    hired_days = (days_per_month * hired.month) + hired.day
    if current_days - hired_days == 0:
        return True

    return False


def read_xml_to_list_of_dict(path: str) -> tuple[List[dict], List[dict]]:
    tree = ET.parse(path)
    root = tree.getroot()
    dev_mountain = []
    dev_club = []
    for child in root.iter('record'):
        row = {}
        for elem in child.iter():
            if elem.tag == "record":
                continue

            if elem.tag == "BIRTHDAY" or elem.tag == "HIRED":
                row[elem.tag] = datetime.strptime(elem.text, "%d-%m-%Y").strftime("%Y-%m-%d")
                continue

            row[elem.tag] = elem.text
        if check_hired_greater_than_3year(row["HIRED"]) \
                and row["POSITION"] in ["Airhostess", "Pilot", "Steward"] \
                and row["STATUS"] == "1":
            dev_club.append(row)
        else:
            dev_mountain.append(row)
    return dev_mountain, dev_club


def convert_xml_to_csv(input_file_path: str, output_folder: str):
    dev_mountain, dev_club = read_xml_to_list_of_dict(input_file_path)
    columns = dev_mountain[0].keys()
    with open(f'{output_folder}/dev_mountain.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, columns)
        dict_writer.writeheader()
        dict_writer.writerows(dev_mountain)

    columns = dev_club[0].keys()
    with open(f'{output_folder}/dev_club.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, columns)
        dict_writer.writeheader()
        dict_writer.writerows(dev_club)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        convert_xml_to_csv(input_file_path=sys.argv[1], output_folder=sys.argv[2])
    else:
        print("Please insert param")
