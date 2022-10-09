import argparse
import csv
import xml.etree.ElementTree as ET

from datetime import datetime

attribute_list = (
    'EMPID', 'PASSPORT', 'FIRSTNAME', 'LASTNAME', 'GENDER', 'BIRTHDAY', 'NATIONALITY', 'HIRED', 'DEPT', 'POSITION',
    'STATUS', 'REGION')

current_datetime = datetime.now()  # Acceptable edge case

def ensure_years_experiences(date_str, years=3):
    leap_days = 0
    target_date = datetime(int(date_str[6:]), int(date_str[3:5]), int(date_str[:2]))
    for year in range(target_date.year, current_datetime.year+2):
        if year & 0b11: # mod 4
            leap_days += 1
    return (current_datetime - target_date).days > years * 365 + leap_days


def xml2csv_converter_helper(records, convert_default):
    existed_EMPID_set = set()
    existed_PASSPORT = set()
    for record in records:
        if convert_default and \
                (record[10].text != '1' or \
                record[9].text not in ('Airhostess', 'Pilot', 'Steward') or \
                record[0].text == record[1].text or \
                record[0].text in existed_EMPID_set or \
                record[1].text in existed_PASSPORT or \
                not ensure_years_experiences(record[7].text, years=3)):
            continue
        existed_EMPID_set.add(record[0].text)
        existed_PASSPORT.add(record[1].text)
        yield list(map(lambda attibute: record.find(attibute).text, attribute_list))


def xml2csv_converter(xml_file, csv_file, convert_default):
    tree = ET.parse(xml_file)
    records = tree.getroot()
    csv_by_nationality = dict()
    with open(csv_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',')
        csv_writer.writerow(attribute_list)
        for record in xml2csv_converter_helper(records, convert_default):
            nationality = record[6]
            if nationality not in csv_by_nationality:
                csv_by_nationality_file = f'{csv_file[:-4]}-{nationality}.csv' if csv_file[-4:] == '.csv' else csv_file
                csv_by_nationality[nationality] = csv.writer(open(csv_by_nationality_file, 'w', newline=''),
                                                             delimiter=',')
                csv_by_nationality[nationality].writerow(attribute_list)
            csv_writer.writerow(record)
            csv_by_nationality[nationality].writerow(record)


def main():
    try:
        xml_file = args.xml
        csv_file = args.csv
        convert_default = args.convert_default
        xml2csv_converter(xml_file=xml_file, csv_file=csv_file, convert_default=convert_default)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--xml",
        default='data-devclub-1.xml',
        help="Specify a xml file."
    )

    parser.add_argument(
        "--csv",
        default='data-devclub-1.csv',
        help="Specify the name of a csv file to write to."
    )

    parser.add_argument(
        "--convert-default",
        action='store_false',
        help="Only convert actives 3 years experiences+ Airhostess, Pilot, Steward to csv file without duplicate ID and passport number"
    )

    args = parser.parse_args()

    if not args.xml:
        print("[-] Please specify a xml file.")
        exit()

    if not args.csv:
        print("[-] Please specify the name of a csv file to write to.")
        exit()

    main()
