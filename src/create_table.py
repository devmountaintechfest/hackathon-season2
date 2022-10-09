import sqlite3
import sys


def create_table(database_name: str, table_name: str):
    try:
        sqlite_connection = sqlite3.connect(database_name)
        cursor = sqlite_connection.cursor()
        print("connect success")
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                      (EMPID INT, PASSPORT TEXT, FIRSTNAME TEXT, LASTNAME TEXT, 
                      GENDER INT, BIRTHDAY TEXT, NATIONALITY TEXT, HIRED TEXT,
                      DEPT TEXT, POSITION TEXT, STATUS INT, REGION TEXT)''')
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("create table failed", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("database.close")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        create_table(database_name=sys.argv[1], table_name=sys.argv[2])
    else:
        print("Please insert param")

