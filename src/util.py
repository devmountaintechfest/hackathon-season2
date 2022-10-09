import sqlite3
from functools import wraps
import time
import csv,json


def usedtime(func):
    @wraps(func)
    def usedtimeWrapper(*args, **kwargs):
        startTime = time.perf_counter()
        result = func(*args, **kwargs)
        endTime = time.perf_counter()
        totalTime = endTime - startTime
        print(f'{func.__name__} used time {totalTime:.4f} seconds')
        return result

    return usedtimeWrapper


class DataUtility(object):
    def __init__(self, DB_NAME):
        self.dbName = DB_NAME

    def getConnection(self):
        con = sqlite3.connect(self.dbName)
        return con

    def dbSetup(self):
        con = self.getConnection()
        cur = con.cursor()
        try:
            cur.execute("DROP TABLE employee;")
        except:
            pass
        cur.execute(
            "CREATE TABLE employee(EMP_ID INTEGER,PASSPORT VARCHAR(100),FIRSTNAME VARCHAR(100),LASTNAME VARCHAR(100),"
            "GENDER INTEGER,BIRTHDAY VARCHAR(100),NATIONALITY VARCHAR(100),HIRED VARCHAR(100),DEPT VARCHAR(100),"
            "POSITION VARCHAR(100),STATUS INTEGER,REGION VARCHAR(100));")
        con.close()
        print("setup completed.")

    def view(self):
        con = self.getConnection()
        cur = con.cursor()
        try:
            cur.execute("DROP VIEW employee_country_view;")
        except:
            pass
        try:
            cur.execute("DROP VIEW employee_department_view;")
        except:
            pass
        try:
            cur.execute("DROP VIEW employee_nation_view;")
        except:
            pass
        cur.execute("""CREATE VIEW employee_country_view AS SELECT "EMP_ID","PASSPORT","FIRSTNAME","LASTNAME",
        "REGION" FROM employee;""")
        cur.execute("""CREATE VIEW employee_department_view AS SELECT "EMP_ID","PASSPORT","FIRSTNAME","LASTNAME",
        "DEPT" FROM employee;""")
        cur.execute("""CREATE VIEW employee_nation_view AS SELECT "EMP_ID","PASSPORT","FIRSTNAME","LASTNAME",
        "NATIONALITY" FROM employee;""")
        con.close()
        print("setup completed.")

    def save(self, data):
        print("Save..")
        con = self.getConnection()
        con.executemany(
            "INSERT INTO employee (EMP_ID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,"
            "POSITION,STATUS,REGION) VALUES(?,?,?,?,?,?,?,?,?,?,?,?);",
            data)
        con.commit()
        con.close()


class FileUtility(object):
    def write(seft, fileName, data):
        print("Write..")
        nation = data[0][6]
        print(nation)
        with open("{}_{}.csv".format(fileName.replace(".csv", ""), nation), 'w', newline="") as f:
            write = csv.writer(f)
            write.writerows(data)

    def json(seft, fileName, data):
        print("Write json..")
        with open("{}.json".format(fileName.replace(".json", "")), "w") as final:
            json.dump(data, final)
