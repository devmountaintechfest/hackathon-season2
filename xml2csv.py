import argparse
import csv
import xml.etree.ElementTree as ET


attibute_list = ('EMPID', 'PASSPORT', 'FIRSTNAME', 'LASTNAME', 'GENDER', 'BIRTHDAY', 'NATIONALITY', 'HIRED', 'DEPT', 'POSITION', 'STATUS', 'REGION')


def xml2csv_converter_helper(records):
    for record in records:
        yield list(map(lambda attibute: record.find(attibute).text, attibute_list))


def xml2csv_converter(xml_file, csv_file):
    tree = ET.parse(xml_file)
    records = tree.getroot()
    csv_by_nationality = dict()
    with open(csv_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',')
        csv_writer.writerow(attibute_list)
        for record in xml2csv_converter_helper(records):
            nationality = record[6]
            if nationality not in csv_by_nationality:
                csv_by_nationality_file = f'{csv_file[:-4]}-{nationality}.csv' if csv_file[-4:] == '.csv' else csv_file
                csv_by_nationality[nationality] = csv.writer(open(csv_by_nationality_file, 'w', newline=''), delimiter=',')
                csv_by_nationality[nationality].writerow(attibute_list)
            csv_writer.writerow(record)
            csv_by_nationality[nationality].writerow(record)


def main():
    try:
        xml_file = args.xml
        csv_file = args.csv
        xml2csv_converter(xml_file=xml_file, csv_file=csv_file)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-xml",
        default='data-devclub-1.xml',
        help="Specify a xml file."
    )

    parser.add_argument(
        "-csv",
        default='data-devclub-1.csv',
        help="Specify the name of a csv file to write to."
    )
    
    args = parser.parse_args()

    if not args.xml:
        print("[-] Please specify a xml file."
              "\nUse -xml <file.xml> to specify the file.")
        exit()
        
    if not args.csv:
        print("[-] Please specify the name of a csv file to write to. "
              "\nUse -csv <file.csv> to specify the file")
        exit()

    main()
