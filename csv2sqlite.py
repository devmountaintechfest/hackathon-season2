import csv
import sqlite3

from contextlib import closing

CSV_FILE = 'data-devclub-1.csv'
DATABASE = 'data-devclub-1.db'
TABLE_NAME = 'DEVCLUB'
HEADERS = 'employeeId, passportNo, firstname, lastname, gender, birthDate, nationality, hiredDate, department, position, status, workRegion'
CSV_HEADER_MAP = {'employeeId': 'EMPID',
                  'passportNo': 'PASSPORT',
                  'firstname': 'FIRSTNAME',
                  'lastname': 'LASTNAME',
                  'gender': 'GENDER',
                  'birthDate': 'BIRTHDAY',
                  'nationality': 'NATIONALITY',
                  'hiredDate': 'HIRED',
                  'department': 'DEPT',
                  'position': 'POSITION',
                  'status': 'STATUS',
                  'workRegion': 'REGION',
                  }

TABLE_SCHEMA = {
    'EMPID': 'INTEGER PRIMARY KEY',
    'PASSPORT': 'CHAR(11) NOT NULL UNIQUE',
    'FIRSTNAME': 'VARCHAR(255)',
    'LASTNAME': 'VARCHAR(255)',
    'GENDER': 'INT2',
    'BIRTHDAY': 'CHAR(10)',
    'NATIONALITY': 'VARCHAR(56)',
    'HIRED': 'CHAR(10)',
    'DEPT': 'VARCHAR(56)',
    'POSITION': 'VARCHAR(56)',
    'STATUS': 'TINYINT',
    'REGION': 'VARCHAR(85)',
}

JOINED_TABLE_SCHEMA = ',\n'.join((f'{struct} {domain}' for struct, domain in TABLE_SCHEMA.items()))
CREATE_TABLE_STATEMENT = f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}({JOINED_TABLE_SCHEMA})'

with closing(sqlite3.connect(DATABASE)) as conn, open(CSV_FILE, 'r') as infile:
    csv_dict_reader = csv.DictReader(infile)
    payload = (list(map(lambda struct: record[struct], TABLE_SCHEMA)) for record in csv_dict_reader)

    with conn as cur:
        cur.execute(CREATE_TABLE_STATEMENT)
        cur.executemany(f'INSERT INTO {TABLE_NAME}({", ".join(TABLE_SCHEMA)}) VALUES (?{", ?" * (len(TABLE_SCHEMA) - 1)})', payload)
