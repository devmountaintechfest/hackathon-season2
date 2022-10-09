import csv
import sqlite3
import sys
from typing import List


def insert_data(database_name: str, table_name: str, data: List[dict]):
    try:
        sqlite_connection = sqlite3.connect(database_name)
        cursor = sqlite_connection.cursor()
        print("connect success")
        for val in data:
            sqlite_insert_query = f"""INSERT INTO {table_name} 
                (EMPID, PASSPORT, FIRSTNAME, LASTNAME, GENDER, BIRTHDAY, 
                NATIONALITY, HIRED, DEPT, POSITION, STATUS, REGION) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            count = cursor.execute(sqlite_insert_query, tuple(val.values()))
            sqlite_connection.commit()
            print("insert success", count)
        cursor.close()
    except sqlite3.Error as error:
        print("insert failed", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("database.close")


def csv_to_sqlite(database_name: str, table_name: str, path: str):
    with open(path) as f:
        data = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
        insert_data(database_name, table_name, data)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        csv_to_sqlite(database_name=sys.argv[1], table_name=sys.argv[2], path=sys.argv[3])
    else:
        print("Please insert param")
