# Devmountain Tech Fest
> Hackathon Season2
> 
> Qualifiers Round  
> Transform xml employee data to sqlite with view and on-demand user query db - python3

## Team members
> We Are `mVATOR`
> - Mr.Theerawat [@sajarudth](https://github.com/sajarudth)
> - Mr.Paphavich [@thaiversion](https://github.com/thaiversion)
> - Mr.Thongrit  [@badoss](https://github.com/badoss)

## Data Visualization Demo Dashboard

> - hosted website (cloudflare)
>     - url[https://hackathon-season2-data-analysis.pages.dev]
> - github
>     - url[https://github.com/badoss/hackathon-season2-data-analysis.git]


## Required Environment 
- python 3.10.4 

## How to Implement

1. clone this repository
```
git clone https://github.com/thaiversion/hackathon-season2_devmountaintechfest.git
```

2. change directory to project path  
for example
```
cd hackathon-season2_devmountaintechfest
```

3. start program
description of each program is shown on below section 


#### program #1 starter_transform_empdata_tosqlite.py
functionality >> convert xml file (data-devclub-1.xml) and filter data then add to sqlite db table "employee" with 3 following sqlite views  
and the final save .csv which each file contain employee record group by same nationality > file format devclub_\<Nationality\>.csv
```
list of sqlite view that focus on user query perspective
1. vEMPLOYEEBYDEPT
2. vEMPLOYEEBYNATIONALITY
3. vEMPLOYEEBYREGION
```  
  
  
How to run file 
```
python starter_transform_empdata_tosqlite.py
```
\*sqlite db store in filename "devclub.db"  
\*example screenshot db on file "./screenshot/ss_example_sqlitedb_viewnotincluded.png"  
\*example screenshot script on file "./screenshot/ss_starter_transform_empdata_tosqlite.py_importxml_tosqlite.png"  


#### program #2 userquery_searchby_region.py
functionality >> user ondemand script to query database, ask user for input region name on python cmd 
and get retrive employee record(s) with 'REGION' field condition then display json format to user on python cmd 
and save json format string to file "lastestresult_userquery_searchby_region.json"  
  

How to run file 
```
python userquery_searchby_region.py
```  
then user must input some charecters to python cmd  
\*valid charecter is A-Z and a-z , must not input number or any special charecter  
\*result json file maybe empty cuz lastest user input is invalid then clear any result remain on .json  
\*example screenshot script case found record on file "./screenshot/ss_userquery_case_found.png"  
\*example screenshot script case no record return on file "./screenshot/ss_userquery_case_notfound.png"  
\*example screenshot script case user input invalid charecter on file "./screenshot/ss_userquery_case_notfound.png"  


#### program #3 userquery_searchby_dept.py
functionality >> user ondemand script to query database, ask user for input department name on python cmd 
and get retrive employee record(s) with 'DEPT' field condition then display json format to user on python cmd 
and save json format string to file "lastestresult_userquery_searchby_dept.json"  
  

How to run file 
```
python userquery_searchby_dept.py
```  
then user must input some charecters to python cmd  
\*valid charecter is A-Z and a-z , must not input number or any special charecter  
\*result json file maybe empty cuz lastest user input is invalid then clear any result remain on .json  
\*example screenshot script case found record on file "./screenshot/ss_userquery_case_found.png"  
\*example screenshot script case no record return on file "./screenshot/ss_userquery_case_notfound.png"  
\*example screenshot script case user input invalid charecter on file "./screenshot/ss_userquery_case_notfound.png"  


#### program #4 userquery_searchby_nationality.py
functionality >> user ondemand script to query database, ask user for input nationality name on python cmd 
and get retrive employee record(s) with 'NATIONALITY' field condition then display json format to user on python cmd 
and save json format string to file "lastestresult_userquery_searchby_nationality.json"  
  

How to run file 
```
python userquery_searchby_nationality.py
```  
then user must input some charecters to python cmd  
\*valid charecter is A-Z and a-z , must not input number or any special charecter  
\*result json file maybe empty cuz lastest user input is invalid then clear any result remain on .json  
\*example screenshot script case found record on file "./screenshot/ss_userquery_case_found.png"  
\*example screenshot script case no record return on file "./screenshot/ss_userquery_case_notfound.png"  
\*example screenshot script case user input invalid charecter on file "./screenshot/ss_userquery_case_notfound.png"  


## Once Again
Data Visualization Demo Dashboard is displayed on website [https://hackathon-season2-data-analysis.pages.dev]


> ..
---
Syntex Guide on GitHub [GitHub Help](https://help.github.com/articles/basic-writing-and-formatting-syntax/).
