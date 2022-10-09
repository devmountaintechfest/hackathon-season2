import csv
import argparse
import collections
import json
import sqlite3

from contextlib import closing


def _json_dumps(objects):
    output = {}
    for i, obj in enumerate(objects):
        output[i] = []
        for emp in map(EMPLOYEE_RECORD._make, iter(obj)):
            output[i].append(emp._asdict())
    return json.dumps(output, indent=2)


def main():
    with closing(sqlite3.connect(DATABASE)) as conn, open(
        CSV_FILE, "r"
    ) as infile, open(JSON_FILE, "w") as outfile:
        csv_dict_reader = csv.DictReader(infile)
        payload = (
            list(map(lambda struct: record[struct], TABLE_SCHEMA))
            for record in csv_dict_reader
        )

        with conn as cur:
            cur.execute(
                f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}({JOINED_TABLE_SCHEMA})"
            )
            cur.execute(
                f"CREATE VIEW IF NOT EXISTS `VIEW_EMP_REGION` AS SELECT * FROM {TABLE_NAME} ORDER BY REGION"
            )
            cur.execute(
                f"CREATE VIEW IF NOT EXISTS `VIEW_EMP_DEPARTMENT` AS SELECT * FROM {TABLE_NAME} ORDER BY DEPT"
            )
            cur.execute(
                f"CREATE VIEW IF NOT EXISTS `VIEW_EMP_NATIONALITY` AS SELECT * FROM {TABLE_NAME} ORDER BY NATIONALITY"
            )

            try:
                cur.executemany(
                    f'INSERT INTO {TABLE_NAME} VALUES (?{", ?" * (len(TABLE_SCHEMA) - 1)})',
                    payload,
                )
            except sqlite3.IntegrityError:
                pass

            result_sets = [
                cur.execute(
                    "SELECT * FROM `VIEW_EMP_REGION` WHERE REGION = ?",
                    (args.region_param,),
                ),
                cur.execute(
                    "SELECT * FROM `VIEW_EMP_DEPARTMENT` WHERE DEPT = ?",
                    (args.dept_param,),
                ),
                cur.execute(
                    "SELECT * FROM `VIEW_EMP_NATIONALITY` WHERE NATIONALITY = ?",
                    (args.nation_param,),
                ),
            ]
            outfile.write(_json_dumps(result_sets))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--csv",
        default="data-devclub-1.csv",
        help="Specify a csv file."
    )
    parser.add_argument(
        "--json",
        default="data-devclub-1.json",
        help="Specify a json outfile."
    )
    parser.add_argument(
        "--database",
        default="data-devclub-1.db",
        help="Specify the name of a database file to write to.",
    )
    parser.add_argument(
        "--table-name",
        default="DEVCLUB",
        help="Specify the name of a table"
    )
    parser.add_argument(
        "--region-param",
        default="Europe",
        help="Specify parameter for SQLite View region-based query",
    )
    parser.add_argument(
        "--dept-param",
        default="Flight Planning",
        help="Specify parameter for SQLite View department-based query",
    )
    parser.add_argument(
        "--nation-param",
        default="Ukraine",
        help="Specify parameter for SQLite View nationality-based query",
    )

    args = parser.parse_args()

    if not args.csv:
        print("[-] Please specify a csv file.")
        exit(1)

    if not args.database:
        print("[-] Please specify the name of a database file to write to.")
        exit(1)

    if not args.table_name:
        print("[-] Please specify the name of a table.")
        exit(1)

    CSV_FILE = args.csv
    JSON_FILE = args.json
    DATABASE = args.database
    TABLE_NAME = args.table_name
    TABLE_SCHEMA = {
        "EMPID": "INTEGER PRIMARY KEY",
        "PASSPORT": "CHAR(11) NOT NULL UNIQUE",
        "FIRSTNAME": "VARCHAR(255)",
        "LASTNAME": "VARCHAR(255)",
        "GENDER": "INT2",
        "BIRTHDAY": "CHAR(10)",
        "NATIONALITY": "VARCHAR(56)",
        "HIRED": "CHAR(10)",
        "DEPT": "VARCHAR(56)",
        "POSITION": "VARCHAR(56)",
        "STATUS": "TINYINT",
        "REGION": "VARCHAR(85)",
    }

    JOINED_TABLE_SCHEMA = ",\n".join(
        (f"{struct} {domain}" for struct, domain in TABLE_SCHEMA.items())
    )

    EMPLOYEE_RECORD = collections.namedtuple("EmployeeRecord", ",".join(TABLE_SCHEMA))

    main()
