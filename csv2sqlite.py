import csv, sqlite3

csv_file = 'data-devclub-1.csv'
sqlite_file = 'data-devclub-1.db'
table_name = 'devclub'
headers = 'employeeId, passportNo, firstname, lastname, gender, birthDate, nationality, hiredDate, department, position, status, workRegion'
csv_header_map = {'employeeId': 'EMPID',
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

con = sqlite3.connect(sqlite_file)
cur = con.cursor()

cur.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
if cur.fetchone()[0]==1 : 
	print('Table exists.')
else :
	cur.execute(f'CREATE TABLE {table_name} ({headers});')

with open(csv_file,'r') as infile:
    csv_dict_reader = csv.DictReader(infile)
    to_sqlite = [list(map(lambda header: record[csv_header_map[header]], headers.split(', '))) for record in csv_dict_reader]

cur.executemany(f'INSERT INTO devclub ({headers}) VALUES (?{", ?" * headers.count(",")});', to_sqlite)
con.commit()
con.close()
