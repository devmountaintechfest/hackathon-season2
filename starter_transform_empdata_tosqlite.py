#-*-coding: utf-8 -*-
# Dev Mountain Tech Fest - Qualifiers Round
# [python] xml/sqlite employee tranform data
#
# v1.0.0 09/10/65
#   - Initial Release
#
# Author: Team MFEC


# ================== Import library ==================
import pprint   #pretty print
import sqlite3  #sqlite
import datetime #datetime
import xml.etree.ElementTree as ET #xml reader
from time import perf_counter #stopwatch
from dateutil.relativedelta import relativedelta #timedelta


# ============== defined variable ====================
static_employee_xml_filepath = 'data-devclub-1.xml'
static_sqlitedb_filepath     = 'devclub.db'


# ================== Function ========================
# the custom recursive fuction that convert xml to json
"""
NOTE! explain the xml element
xml to json using built-in python library "xml"
child.tag   << key
root.attrib << {} if not lowest level
root.text   << value / none if not lowest level
"""
def XMLtoJSON(_nesteddata):
    temp_data_dict = {}
    temp_data_list = []
    for child in _nesteddata:
        # check if level have child nest
        if isinstance(child.text, type(None)):
            # this level have child nest , store with list
            temp_data_list.append(XMLtoJSON(child)) #use RECURSIVE!!
        else:
            # this level have no child nest , store with dict
            temp_data_dict[child.tag] = child.text
    if temp_data_list:
        return {_nesteddata.tag:temp_data_list}
    return {_nesteddata.tag:temp_data_dict}

# read xml file and return table json
"""
NOTE! example xmldata_dict structure
{
    "records" : [
        {
            "record" : {
                "EMPID"    : "1234",
                "PASSPORT" : "A567",
                ...
                "REGION"   : "THAI"
            }
        },
        ....
    ] 
}
"""
def ReadXML(_xmlfilepath=""):
    # read raw file
    with open(_xmlfilepath, 'r') as f:
        rawfiledata = f.read()
    rawfiledata = rawfiledata.replace("\n","").replace("\t","")
    # custom parser xml
    xmldata_xml  = ET.fromstring(rawfiledata)
    xmldata_dict = XMLtoJSON(xmldata_xml)
    # pprint.pprint(xmldata_dict["records"][0]["record"])
    return xmldata_dict #employee_rawdata

# clean up employee data by BRUTE FORCE method and insert data to sqlite
"""
NOTE! filter out with conditions
- POSITION is in "Airhostess" or "Pilot" or "Steward"
- Remove Worked less than 3 years
- Remove duplicate data << what is this ???
- Ramove duplicate employeeId and passportNo and fullname
- Remove employess that have Resigned/Retired status
shown as 6 filter condition on below
"""
def ClearEmployeeData(_xmldata=[],_conn=None):
    # variable counter
    valid_employee_list = []
    temp_empid_list     = []
    temp_passport_list  = []
    temp_fullname_list  = []
    temp_time_current   = datetime.datetime.now()
    temp_time_3yearsago = temp_time_current - relativedelta(years=3)
    # loop for each record/row
    for this_employee in _xmldata:
        this_record = this_employee.get("record",{})
        # filter condition #1 : check Active status is not "Resigned" or "Retired"
        if (thisemp_status := this_record.get("STATUS","")) not in ["1"]:
            continue
        # filter condition #2 : check if position is in "Airhostess" or "Pilot" or "Steward"
        if (thisemp_position := this_record.get("POSITION","")) not in ["Airhostess","Pilot","Steward"]:
            continue
        # filter condition #3 : check if worked more than 3 years
        thisemp_hired_dt = datetime.datetime.strptime(this_record.get("HIRED",""), '%d-%m-%Y')
        if thisemp_hired_dt > temp_time_3yearsago:
            continue
        # filter condition #4 : check duplicate employeeId
        if (thisemp_empid    := this_record.get("EMPID",""))    in temp_empid_list:
            continue
        temp_empid_list.append(thisemp_empid)
        # filter condition #5 : check duplicate passportNo
        if (thisemp_passport := this_record.get("PASSPORT","")) in temp_passport_list:
            continue
        temp_passport_list.append(thisemp_passport)
        # filter condition #6 : check duplicate fullname
        thisemp_fullname = this_record.get("FIRSTNAME","") + this_record.get("LASTNAME","")
        if thisemp_fullname in temp_fullname_list:
            continue
        temp_fullname_list.append(thisemp_fullname)
        # this employee is valid condition
        thisemp_hired_float = datetime.datetime.timestamp(thisemp_hired_dt) #datetime to float
        thisemp_hired_str   = datetime.datetime.fromtimestamp(thisemp_hired_float).strftime('%Y-%m-%d')
        thisemp_birthday_dt    = datetime.datetime.strptime(this_record.get("BIRTHDAY",""), '%d-%m-%Y')
        thisemp_birthday_float = datetime.datetime.timestamp(thisemp_birthday_dt) #datetime to float
        thisemp_birthday_str   = datetime.datetime.fromtimestamp(thisemp_birthday_float).strftime('%Y-%m-%d')
        this_valid_employee = {
            "EMPID"       : int(thisemp_empid),
            "PASSPORT"    : thisemp_passport,
            "FIRSTNAME"   : this_record.get("FIRSTNAME",""),
            "LASTNAME"    : this_record.get("LASTNAME",""),
            "GENDER"      : int(this_record.get("GENDER","")),
            "BIRTHDAY"    : thisemp_birthday_str,
            "NATIONALITY" : this_record.get("NATIONALITY",""),
            "HIRED"       : thisemp_hired_str,
            "DEPT"        : this_record.get("DEPT",""),
            "POSITION"    : thisemp_position,
            "STATUS"      : int(thisemp_status),
            "REGION"      : this_record.get("REGION","")
        }
        # pprint.pprint(this_valid_employee) #test print valid employee record
        apistatus = db_create_employee(_conn,this_valid_employee)
        valid_employee_list.append(this_valid_employee)
    return valid_employee_list #employee_cleaned

# sqlite db create connection
def db_create_connection(_dbfilepath=""):
    """ create a database connection to the SQLite database
        specified by _dbfilepath
    :param _dbfilepath: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(_dbfilepath)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# sqlite db create table
def db_create_table(_conn=None):
    """ create a table from the create_table_sql statement
    :param _conn: Connection object
    :return: apistatus
    """
    try:
        mycursor = _conn.cursor()
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS employee(
                EMPID       INTEGER,
                PASSPORT    TEXT,
                FIRSTNAME   TEXT,
                LASTNAME    TEXT,
                GENDER      INTEGER,
                BIRTHDAY    NUMERIC,
                NATIONALITY TEXT,
                HIRED       NUMERIC,
                DEPT        TEXT,
                POSITION    TEXT,
                STATUS      INTEGER,
                REGION      TEXT
            );
        """
        mycursor.execute(create_table_sql)
        create_view1_dept_sql = """
            CREATE VIEW IF NOT EXISTS vEMPLOYEEBYDEPT AS SELECT
            DEPT,
            EMPID,
            PASSPORT,
            FIRSTNAME,
            LASTNAME,
            GENDER,
            CASE GENDER
            WHEN 0 THEN 'Male'
            WHEN 1 THEN 'Female'
            ELSE '-' END GENDER_TEXT,
            BIRTHDAY,
            CAST((((JulianDay('now')) - JulianDay(BIRTHDAY))/365.25) AS INTEGER) AS AGE_of_EMPLOYEE,
            REGION,
            NATIONALITY,
            HIRED,
            CAST((((JulianDay('now')) - JulianDay(HIRED))/365.25) AS INTEGER) AS AGE_of_HIRED,
            POSITION,
            STATUS,
            CASE STATUS
            WHEN 1 THEN 'Active'
            WHEN 2 THEN 'Resigned'
            WHEN 3 THEN 'Retired'
            ELSE 'anomaly information' END STATUS_TEXT
            FROM employee
            ORDER By DEPT ASC;
        """
        mycursor.execute(create_view1_dept_sql)
        create_view2_nationality_sql = """
            CREATE VIEW IF NOT EXISTS vEMPLOYEEBYNATIONALITY AS SELECT
            NATIONALITY, 
            REGION,
            EMPID,
            PASSPORT,
            FIRSTNAME,
            LASTNAME,
            GENDER,
            CASE GENDER
            WHEN 0 THEN 'Male'
            WHEN 1 THEN 'Female'
            ELSE '-' END GENDER_TEXT,
            BIRTHDAY,
            CAST((((JulianDay('now')) - JulianDay(BIRTHDAY))/365.25) AS INTEGER) AS AGE_of_EMPLOYEE,
            HIRED,
            CAST((((JulianDay('now')) - JulianDay(HIRED))/365.25) AS INTEGER) AS AGE_of_HIRED,
            DEPT,
            POSITION,
            STATUS,
            CASE STATUS
            WHEN 1 THEN 'Active'
            WHEN 2 THEN 'Resigned'
            WHEN 3 THEN 'Retired'
            ELSE 'anomaly information' END STATUS_TEXT
            FROM employee
            ORDER By NATIONALITY ASC;
        """
        mycursor.execute(create_view2_nationality_sql)
        create_view3_region_sql = """
            CREATE VIEW IF NOT EXISTS vEMPLOYEEBYREGION AS SELECT
            REGION,
            NATIONALITY, 
            EMPID,
            PASSPORT,
            FIRSTNAME,
            LASTNAME,
            GENDER,
            CASE GENDER
            WHEN 0 THEN 'Male'
            WHEN 1 THEN 'Female'
            ELSE '-' END GENDER_TEXT,
            BIRTHDAY,
            CAST((((JulianDay('now')) - JulianDay(BIRTHDAY))/365.25) AS INTEGER) AS AGE_of_EMPLOYEE,
            HIRED,
            CAST((((JulianDay('now')) - JulianDay(HIRED))/365.25) AS INTEGER) AS AGE_of_HIRED,
            DEPT,
            POSITION,
            STATUS,
            CASE STATUS
            WHEN 1 THEN 'Active'
            WHEN 2 THEN 'Resigned'
            WHEN 3 THEN 'Retired'
            ELSE 'anomaly information' END STATUS_TEXT
            FROM employee
            ORDER By REGION ASC;
        """
        mycursor.execute(create_view3_region_sql)
        
        return True #apistatus
    except sqlite3.Error as e:
        print(e)
        return False #apistatus

# sqlite db delete old on employee table
def db_delete_old(_conn=None):
    """ delete old data from employee table
    :param _conn: Connection object
    :return: apistatus
    """
    try:
        mycursor = _conn.cursor()
        delete_old_sql = """
            DELETE FROM employee;
        """
        mycursor.execute(delete_old_sql)
        return True #apistatus
    except sqlite3.Error as e:
        print(e)
        return False #apistatus

# sqlite create employee record on employee table
def db_create_employee(_conn=None, _employee={}):
    """ create a new employee record
    :param _conn:
    :param _employee:
    :return: apistatus
    """
    try:
        myquery = """INSERT INTO employee(EMPID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,POSITION,STATUS,REGION)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""
        myemployee = (
            _employee["EMPID"],
            _employee["PASSPORT"],
            _employee["FIRSTNAME"],
            _employee["LASTNAME"],
            _employee["GENDER"],
            _employee["BIRTHDAY"],
            _employee["NATIONALITY"],
            _employee["HIRED"],
            _employee["DEPT"],
            _employee["POSITION"],
            _employee["STATUS"],
            _employee["REGION"]
        )
        mycursor = _conn.cursor()
        mycursor.execute(myquery, myemployee)
        _conn.commit()
        return True #apistatus
    except sqlite3.Error as e:
        print("sql error", e)
        return False #apistatus
    # return mycursor.lastrowid
    return True #apistatus

# save csv by nationality
def SaveCSVByNationality(_employee_list=[]):
    temp_employee_nation_list = []
    temp_scaned_nation_list   = []
    # find all nationality and list to temp nation list
    for this_record in _employee_list:
        if this_record["NATIONALITY"] not in temp_scaned_nation_list:
            temp_scaned_nation_list.append(this_record["NATIONALITY"])
    # for each nationality, create csv file
    for this_nation in temp_scaned_nation_list:
        csv_filename      = "devclub_" + this_nation + ".csv"
        render_csv_infile = []
        render_csv_header = ['EMPID','PASSPORT','FIRSTNAME','LASTNAME','GENDER','BIRTHDAY','NATIONALITY','HIRED','DEPT','POSITION','STATUS','REGION']
        render_csv_infile.append(render_csv_header)
        for this_employee in _employee_list:
            if this_nation == this_employee["NATIONALITY"]:
                # this record is match with nationaity
                render_csv_infile.append([
                    str(this_employee["EMPID"]),
                    this_employee["PASSPORT"],
                    this_employee["FIRSTNAME"],
                    this_employee["LASTNAME"],
                    str(this_employee["GENDER"]),
                    this_employee["BIRTHDAY"],
                    this_employee["NATIONALITY"],
                    this_employee["HIRED"],
                    this_employee["DEPT"],
                    this_employee["POSITION"],
                    str(this_employee["STATUS"]),
                    this_employee["REGION"]
                ])
        #NOTE! now render_csv_infile is contain all employee record of this_nation
        # write to csv file
        with open(csv_filename, 'w+') as stream:
            stream.truncate()
            len_row = len(render_csv_infile)
            for i in range(len_row):
                strmid = "," #csv delimiter
                strrow = strmid.join(render_csv_infile[i])
                stream.write(strrow)
                if i < (len_row - 1) : #add new row while not end file
                    stream.write('\n')
            stream.close()
    return True #apistatus


# ================== Main Sector =====================
def main():
    # STEP #0 PREPARING
    time_then = perf_counter()

    # STEP #1 GET EMPLOYEE DATA FROM XML
    employee_rawdata = ReadXML(static_employee_xml_filepath)

    # STEP #2 CREATE SQLLITE DB
    conn = db_create_connection(static_sqlitedb_filepath)
    if conn is not None:
        apistatus = db_create_table(conn)
        if apistatus:
            # CLEAN OLD DATA
            apistatus = db_delete_old(conn)
    else:
        print("Error! cannot create the database connection.")

    # STEP #3 CLEAN UP EMPLOYEE DATA AND INSERT TO SQLLITE
    employee_cleaned = ClearEmployeeData(employee_rawdata.get("records",[]),conn)
    del employee_rawdata

    # STEP #4 SAVE CSV FILE GROUP BY NATIONALITY FIELD
    apistatus = SaveCSVByNationality(employee_cleaned)

    # FINALIZE
    time_now = perf_counter()
    print("Elapsed time : " + str(time_now-time_then) + " seconds")

if __name__ == "__main__":
    main()



# notes

# tested on python 3.10.4(CPU Apple Silicon)
# required library
# NO EXTERNAL LIBRARY IS REQUIRED

# REF sqlite built-in lib : https://www.sqlitetutorial.net/sqlite-python/
# REF xml etree built-in lib : https://docs.python.org/3/library/xml.etree.elementtree.html
# REF save file mode : https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/

#very end