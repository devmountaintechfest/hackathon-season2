convert_xml_to_csv:
	python src/convert_xml_to_csv.py "resources/data-devclub-1.xml" "resources"

create_table:
	python src/create_table.py "./sql_lite.db" "dev_club"

clean_table:
	python src/clean_table.py "./sql_lite.db" "dev_club"

csv_to_db:
	python src/csv_to_db.py  "./sql_lite.db" "dev_club" "resources/dev_club.csv"

generate_json:
	python src/generate_json.py "resources/dev_club.csv" "resources/dev_club.json"

generate_csv_by_nationality:
	python src/generate_csv_by_nationality.py "resources/data-devclub-1.xml" "resources/by_nationality"