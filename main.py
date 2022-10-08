import json

from src.insert_sqlite import insert_data
from src.xml_file_handle import read_file

if __name__ == "__main__":
    data = read_file('resources/data-devclub-1.xml')
    print(json.dumps(data))
    # insert_data(100, "WIN16ELU8GN")
