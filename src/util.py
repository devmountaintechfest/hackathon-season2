import sqlite3
from functools import wraps
import time
from datetime import datetime
from datetime import date
from dateutil import relativedelta
import json

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

class DateUtility(object):
    def currentDate(self):
        return date.today()

    def toDate(self,dateStr):
        date = datetime.strptime(dateStr, '%d-%m-%Y')
        return date

    def diffYear(self,start,end):
        diff = relativedelta.relativedelta(end, start)
        return diff.years

    def diffYear2(self,startStr,endStr):
        testdate = '09-10-2020'

        # start = d.date()
        # end = date.today()
        # print(f'start {start} {end}')
        diff = relativedelta.relativedelta(end, start)
        return diff.years

class DataUtility(object):
    def __init__(self, DB_NAME):
        self.dbName=DB_NAME

    def getConnection(self):
        con = sqlite3.connect(self.dbName)
        return con
        
    def dbSetup(self):
        con=self.getConnection()
        cur = con.cursor()
        cur.execute("DROP TABLE emp_test;")
        cur.execute("CREATE TABLE emp_test(EMP_ID INTEGER,PASSPORT VARCHAR(100),FIRSTNAME VARCHAR(100),LASTNAME VARCHAR(100),GENDER INTEGER,BIRTHDAY VARCHAR(100),NATIONALITY VARCHAR(100),HIRED VARCHAR(100),DEPT VARCHAR(100),POSITION VARCHAR(100),STATUS INTEGER,REGION VARCHAR(100));")
        con.close
        print("setup completed.")

    def save(self,data):
        print("Save..")
        con=self.getConnection()
        con.executemany("INSERT INTO emp_test (EMP_ID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,POSITION,STATUS,REGION) VALUES(?,?,?,?,?,?,?,?,?,?,?,?);", data)
        con.commit()
        con.close

    def query(self,cond,value):
        print("query..")
        con=self.getConnection()
        cur = con.cursor()
        SQL=f'SELECT EMP_ID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,POSITION,STATUS,REGION FROM EMP_TEST  {cond}'
        if(cond==''):
            cur.execute(SQL)
        else:
            cur.execute(SQL,(value,))
        rows = cur.fetchall()
        con.close
        return rows

    

class FileUtility(object):
    def write(seft,fileName,data):
        print("Write..")
        with open(fileName, 'w') as f:
            f.write(data)