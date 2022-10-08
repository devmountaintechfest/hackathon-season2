from lxml import etree as ET
from data import DevMountainData,ClubData
from util import DataUtility,FileUtility,usedtime
import json
import time
import sys

@usedtime
class Executor(object):
    config={}
    total=int()
    valid=int()
    invalid=int()
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
        datasource=xml.xpath("/records/record[STATUS/text()='1' and (POSITION/text()='Steward' or POSITION/text()='Pilot' or POSITION/text()='Airhostess') and EMPID/text()!=PASSPORT/text()]")
        print("Raw Data Valid:",len(datasource))
        print("Raw Data InValid:",str(self.total-len(datasource)))
        
        for element in list(datasource):
            data=DevMountainData(element)
            clubData=ClubData(data)
            self.results.append(clubData.toSet())

    @usedtime
    def load(self):
        print("Load..")
        dataUtility=DataUtility(self.config['dbName'])
        dataUtility.dbSetup()
        dataUtility.save(self.results)

    @usedtime
    def generateSummary(self):
        print("Generate Summary..")
        FileUtility().write(self.config['clubDataReport'],json.dumps(self.results))




def main():
    try:
        print("#####start#####")
        config={
            "datasource":"../data-devclub-1.xml",
            "clubDataReport":"../reports/data-devclub-report.json",
            "dbName":"../database/devclub2022.db"
        }

        startTime = time.perf_counter()
                
        exe=Executor()
        exe.setup(config)
        exe.extract()
        exe.load()
        exe.generateSummary()

        endTime = time.perf_counter()
        totalTime = endTime - startTime
        print(f'##Total used time {totalTime:.4f} seconds##')
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())