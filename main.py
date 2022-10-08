from src.insert_sqlite import insert_data, create_table
from src.xml_file_handle import read_file

if __name__ == "__main__":
    data = read_file('resources/data-devclub-1.xml')
    create_table("master")
    insert_data("master", data)
