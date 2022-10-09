import sqlite3
import sys


def clean_table(database_name: str, table_name: str):
    try:
        sqlite_connection = sqlite3.connect(database_name)
        cursor = sqlite_connection.cursor()
        print("connect success")
        cursor.execute(f'''DELETE FROM {table_name}''')
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("delete data failed", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("database.close")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        clean_table(database_name=sys.argv[1], table_name=sys.argv[2])
    else:
        print("Please insert param")
