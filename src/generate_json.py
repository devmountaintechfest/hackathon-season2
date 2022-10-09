import csv
import json
import sys


def generate_json(path: str, json_file_name: str):
    with open(path) as f:
        data = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
        with open(json_file_name, "w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        generate_json(path=sys.argv[1], json_file_name=sys.argv[2])
    else:
        print("Please insert param")
