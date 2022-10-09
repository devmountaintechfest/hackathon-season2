#-*-coding: utf-8 -*-
# Dev Mountain Tech Fest - Qualifiers Round
# [python] user query search by department
#
# v1.0.0 09/10/65
#   - Initial Release
#
# Author: Team MFEC


# ================== Import library ==================
import json     #json form
import pprint   #pretty print
import sqlite3  #sqlite
# import datetime #datetime
from time import perf_counter


# ============== defined variable ====================
static_sqlitedb_filepath     = 'devclub.db'
static_savejson_filepath     = 'lastestresult_userquery_searchby_dept.json'


# ================== Function ========================
# get user input
def GetUserInput():
    print("Script search employee by department")
    searchkeyword = input("Enter department name : ")
    return str(searchkeyword)

def SearchSQLiteDB(_searchfield="",_searchkeyword=""):
    #basic handle
    if not _searchkeyword:
        print("No Input search keyword")
        jsonfile_clear()
        return False, None #apistatus, result_json
    if not _searchkeyword.isalpha():
        print("Input search keyword is not valid")
        jsonfile_clear()
        return False, None #apistatus, result_json
    #create a connection to the database
    conn = None
    try:
        conn = sqlite3.connect(static_sqlitedb_filepath)
    except sqlite3.Error as e:
        print("cannot connect to database")
        jsonfile_clear()
        return False, None #apistatus, result_json
    #query databasecad
    myquery = "SELECT * " + \
        "FROM vEMPLOYEEBYDEPT WHERE " + _searchfield + " = '" +_searchkeyword + "'"
    mycursor = conn.cursor()
    mycursor.execute(myquery)
    rows = mycursor.fetchall()
    if not rows:
        print("SQL result : Not found record with department name : " + _searchkeyword)
        jsonfile_clear()
        return False, None #apistatus, result_json
    temp_result_list = []
    for row in rows:
        # row is a tuple
        this_record_dict = {
            'DEPT'            : row[0],
            'EMPID'           : row[1],
            'PASSPORT'        : row[2],
            'FIRSTNAME'       : row[3],
            'LASTNAME'        : row[4],
            'GENDER'          : row[5],
            'GENDER_TEXT'     : row[6],
            'BIRTHDAY'        : row[7],
            'AGE_of_EMPLOYEE' : row[8],
            'REGION'          : row[9],
            'NATIONALITY'     : row[10],
            'HIRED'           : row[11],
            'AGE_of_HIRED'    : row[12],
            'POSITION'        : row[13],
            'STATUS'          : row[14],
            'STATUS_TEXT'     : row[15]
        }
        temp_result_list.append(this_record_dict)
    # pprint.pprint(temp_result_list) #json form
    return True, temp_result_list #apistatus, result_json

# if no result clear json file
def jsonfile_clear():
    with open(static_savejson_filepath, 'w+') as stream:
        stream.truncate()
        stream.close()

# if found result record write to json file
def jsonfile_write(render_infile=""):
    with open(static_savejson_filepath, 'w+') as stream:
        stream.truncate()
        stream.write(render_infile)
        stream.close()


# ================== Main Sector =====================
def main():
    # STEP #1 GET USER INPUT
    searchkeyword = GetUserInput()

    # STEP #2 SEARCH
    time_then = perf_counter()
    apistatus, result_json = SearchSQLiteDB("DEPT",searchkeyword)

    # STEP #3 PRINT RESULT AS JSON
    time_now = perf_counter()
    print("Elapsed running time : " + str(time_now-time_then) + " seconds")
    if apistatus:
        print("SQL Result : found record with department name : " + searchkeyword + " , total record : " + str(len(result_json)))
        jsonfile_write(json.dumps(result_json))
        print("save result to json file : " + static_savejson_filepath)
        print("result as json format is shown below")
        print("==========================================================================")
        pprint.pprint(result_json)

if __name__ == "__main__":
    main()



# notes

# tested on python 3.10.4(CPU Apple Silicon)
# required library
# NO EXTERNAL LIBRARY IS REQUIRED

#very end