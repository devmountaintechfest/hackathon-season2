import csv
import json
import sys


def generate_json(path: str, json_file_name: str):
    with open(path) as csv_file:
        data = [{key: val for key, val in row.items()} for row in csv.DictReader(csv_file, skipinitialspace=True)]
        with open(json_file_name, "w") as json_file:
            json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        generate_json(path=sys.argv[1], json_file_name=sys.argv[2])
    else:
        print("Please insert param")
