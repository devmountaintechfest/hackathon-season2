from lxml import etree as ET
from data import DevMountainData,ClubData
from util import DataUtility,FileUtility,DateUtility,usedtime
import json
import time
import sys

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
        for i in range(50):
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

def printInfo():
    print("- arg1 Execute type\n  - M Migrate\n- arg2 Datasource file\n- arg3 Target db\n- arg4 Report name")
    print("Example\n python runv2.py M ../data-devclub-1.xml ../database/devclub2022.db ../csv ../reports/data-devclub-report.json")

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
                exe.load()
                exe.generateSummary()
                

                endTime = time.perf_counter()
                totalTime = endTime - startTime
                print(f'##Total used time {totalTime:.4f} seconds##')
            else:
                print("Please enter Execute Type (M) Parameter!")
                printInfo()
        else:
            print("Please enter Parameter!")
            printInfo()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())