from lxml import etree as ET
from data import DevMountainData,ClubData
from util import DataUtility,FileUtility,DateUtility,usedtime
import json
import time
import sys
import os
import csv

@usedtime
class Executor(object):
    config={}
    total=int()
    valid=int()
    invalid=int()
    rawData=[]
    results=[]
    @usedtime
    def setup(self,config):
        self.config=config

    @usedtime
    def extract(self):
        print("Extract..")
        xmlData=self.config['datasource']
        parser = ET.XMLParser(remove_comments=False)
        xml = ET.parse(xmlData, parser=parser)
        alldata=xml.xpath("count(/records/record)")
        self.total=int(alldata)
        print("Raw Data Total:",self.total)
        self.rawData=xml.xpath("/records/record[STATUS/text()='1' and (POSITION/text()='Steward' or POSITION/text()='Pilot' or POSITION/text()='Airhostess') and EMPID/text()!=PASSPORT/text()]")
        
    @usedtime
    def transform(self):
        dateUtil=DateUtility()
        currentDate=dateUtil.currentDate()
        YEAR_EXP=3
        for element in self.rawData:
            data=DevMountainData(element)
            clubData=ClubData(data)
            
            diffYear=dateUtil.diffYear(dateUtil.toDate(clubData.hired),currentDate)
            # print(f'diff {dateUtil.toDate(clubData.hired)} {currentDate} : {diffYear} ')
            if(diffYear>YEAR_EXP):
                self.results.append(clubData.toSet())
        print("Raw Data Valid:",len(self.results))
        print("Raw Data InValid:",str(self.total-len(self.results)))

    @usedtime
    def generateCSVByNationality(self):
        nationIndex={}
        nationsResult=[[]]
        for i in range(500):
	        nationsResult.append([])
        index=0
        print(len(self.results))
        for data in self.results:
            nationality={}
            emp=data
            if(emp[6] not in nationIndex.keys()):
                nationIndex[emp[6]]=index
                currentIdex=nationIndex[emp[6]]
                nationsResult[currentIdex].append(emp)
                index=index+1
            else:
                currentIdex=nationIndex[emp[6]]
                nationsResult[currentIdex].append(emp)

        print(nationIndex)
        print(nationsResult)
        keyList = list(nationIndex.keys())
        valList = list(nationIndex.values())
        
        for idx in range(0,len(nationIndex)):
            position = valList.index(idx)
            print(f'{idx} : {keyList[position]} ')
            
            fileName=f'{self.config["csvPath"]}/data-devmountain-{keyList[position].lower()}.csv'
            print(fileName)
            with open(fileName, 'w') as f:
                f.write("EMP_ID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,POSITION,STATUS,REGION\n")
                for empNationData in nationsResult[idx]:
                    print(empNationData)
                    f.write(json.dumps(empNationData).replace('[','').replace(']','')+'\n')

    @usedtime
    def load(self):
        print("Load..")
        dataUtility=DataUtility(self.config['dbName'])
        dataUtility.dbSetup()
        dataUtility.save(self.results)
    def rep(self,data):
        return data.replace('"','').strip()
    @usedtime
    def loadFromCSV(self):
        csvPath=self.config["csvPath"]
        dataUtility=DataUtility(self.config['dbName'])
        dataUtility.dbSetup()
        print("Load fron csv..")
        for file in os.listdir(csvPath):
            if os.path.isfile(os.path.join(csvPath, file)):
                print(file)
                fileDatas=[]
                with open(os.path.join(csvPath, file), 'r') as f:
                    csvData = csv.reader(f, delimiter=',',quoting=csv.QUOTE_NONE)
                    next(csvData)
                    for row in csvData:
                        fileData=(row[0],self.rep(row[1]),self.rep(row[2]),self.rep(row[3]),row[4],self.rep(row[5]),self.rep(row[6]),self.rep(row[7]),self.rep(row[8]),self.rep(row[9]),row[10],self.rep(row[11]))
                        fileDatas.append(fileData)
                    dataUtility.save(fileDatas)

    @usedtime
    def generateSummary(self):
        print("Generate Summary..")
        results=[]
        for data in self.results:
            tmpData={
                "emp_id":data[0],
                "passport":data[1],
                "firstname":data[2],
                "lastname":data[3],
                "gender":data[4],
                "birthday":data[5],
                "nationality":data[6],
                "hired":data[7],
                "dept":data[8],
                "position":data[9],
                "status":data[10],
                "region":data[11]
            }
            results.append(tmpData)
        FileUtility().write(self.config['clubDataReport'],json.dumps(results))

    @usedtime
    def queryByRegion(self,region):
        print("queryByRegion..")
        dataUtility=DataUtility(self.config['dbName'])
        cond=''
        if(region!='' and region!='all'):
            cond='WHERE REGION=?'
        datas=dataUtility.query(cond,region.replace('"',''))
        print("####Result####")
        for data in datas:
            print(f'{data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11]}')

    @usedtime
    def queryByNationality(self,nationality):
        print("queryByNationality..")
        dataUtility=DataUtility(self.config['dbName'])
        cond=''
        if(nationality!='' and nationality!='all'):
            cond='WHERE NATIONALITY=?'
        datas=dataUtility.query(cond,nationality.replace('"',''))
        print("####Result####")
        for data in datas:
            print(f'{data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11]}')

    @usedtime
    def queryByDepartment(self,department):
        print("queryByDepartment..")
        dataUtility=DataUtility(self.config['dbName'])
        cond=''
        if(department!='' and department!='all'):
            cond='WHERE DEPT=?'
        datas=dataUtility.query(cond,department.replace('"',''))
        print("####Result####")
        for data in datas:
            print(f'{data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11]}')

def printInfo():
    print("- arg1 Execute type\n  - M Migrate\n- arg2 Datasource file\n- arg3 Target db\n- arg4 Report name")
    print("Example\n python runv2.py M ../data-devclub-1.xml ../database/devclub2022.db ../csv ../reports/data-devclub-report.json")
def printInfoQ():
    print("- arg1 Execute type\n  - M Migrate\n- arg2 Target db file\n- arg3 Search Type\n- arg4 Value Search")
    print("Example\n python run.py Q ../database/devclub2022.db region all")
    print('Example\n python run.py Q ../database/devclub2022.db region "Canada"')
    print("Example\n python run.py Q ../database/devclub2022.db dept all")
    print('Example\n python run.py Q ../database/devclub2022.db dept "Flight Planning"')
    print("Example\n python run.py Q ../database/devclub2022.db nationality all")
    print('Example\n python run.py Q ../database/devclub2022.db nationality "Germany"')
def main():
    try:

        print("#####start#####")
        print(f"{sys.argv}")
        if(len(sys.argv)>1):
            exeType = sys.argv[1]
            if (exeType=='M'):
                datasource = sys.argv[2]
                dbName = sys.argv[3]
                csvPath = sys.argv[4]
                reportName = sys.argv[5]
                config={
                    "datasource":datasource,
                    "dbName":dbName,
                    "csvPath":csvPath,
                    "clubDataReport":reportName
                }

                startTime = time.perf_counter()
                        
                exe=Executor()
                exe.setup(config)
                exe.extract()
                exe.transform()
                exe.generateCSVByNationality()
                # exe.load()
                exe.loadFromCSV()
                exe.generateSummary()
                

                endTime = time.perf_counter()
                totalTime = endTime - startTime
                print(f'##Total used time {totalTime:.4f} seconds##')
            elif (exeType=='Q'):
                dbName = sys.argv[2]
                searchType = sys.argv[3]
                valueSearch = sys.argv[4]
                if(searchType!='' or valueSearch!=''):
                    config={
                        "searchType":searchType,
                        "dbName":dbName,
                        "valueSearch":valueSearch
                    }
                    startTime = time.perf_counter()
                            
                    exe=Executor()
                    exe.setup(config)
                    if searchType=='region':
                        exe.queryByRegion(valueSearch)
                    elif searchType=='dept':
                        exe.queryByDepartment(valueSearch)
                    elif searchType=='nationality':
                        exe.queryByNationality(valueSearch)
                    else:
                        print("Invalid Parameter!")
                        printInfoQ()
                else:
                     print("Please enter Parameter!")
                     printInfoQ()
                endTime = time.perf_counter()
                totalTime = endTime - startTime
                print(f'##Total used time {totalTime:.4f} seconds##')
            else:
                print("Please enter Execute Type (M) Parameter!")
                printInfo()
                printInfoQ()
        else:
            print("Please enter Parameter!")
            printInfo()
            printInfoQ()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())