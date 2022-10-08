import sqlite3
from typing import List


def create_table(table_name: str):
    try:
        sqlite_connection = sqlite3.connect('sql_lite.db')
        cursor = sqlite_connection.cursor()
        print("connect success")
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                      (EMPID INT, PASSPORT TEXT, FIRSTNAME TEXT, LASTNAME TEXT, 
                      GENDER INT, BIRTHDAY TEXT, NATIONALITY TEXT, HIRED TEXT,
                      DEPT TEXT, POSITION TEXT, STATUS INT, REGION TEXT)''')
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("create failed", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("database.close")


def insert_data(table_name: str, data: List[dict]):
    try:
        sqlite_connection = sqlite3.connect('sql_lite.db')
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
