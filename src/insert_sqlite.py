import sqlite3


def insert_data(emp_id: int, passport: str):
    try:
        sqlite_connection = sqlite3.connect('sql_lite.db')
        cursor = sqlite_connection.cursor()
        print("connect success")
        data_tuple = (emp_id, passport)
        sqlite_insert_query = "INSERT INTO xxx (EMPID, PASSPORT) VALUES (?, ?);"
        count = cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        print("insert success", count)
        cursor.close()
    except sqlite3.Error as error:
        print("insert failed", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("database.close")
