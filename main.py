from datetime import datetime

from src.insert_sqlite import insert_data, create_table
from src.xml_file_handle import read_file

if __name__ == "__main__":
    data = read_file('resources/data-devclub-1.xml')
    for idx, elm in enumerate(data):
        data[idx]["BIRTHDAY"] = datetime.strptime(elm["BIRTHDAY"], "%d-%m-%Y").strftime("%Y-%m-%d")
        data[idx]["HIRED"] = datetime.strptime(elm["HIRED"], "%d-%m-%Y").strftime("%Y-%m-%d")
    create_table("master")
    insert_data("master", data)
