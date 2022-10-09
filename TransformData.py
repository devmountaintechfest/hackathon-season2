from lxml import etree as ET
from model import DevMountainData,ClubData
from Util import DataUtility,FileUtility,DateUtility
import json
import time
import sys
from collections import Counter

import matplotlib.pyplot as plt

class Execute(object):
    config={}
    total=int()
    valid=int()
    invalid=int()
    ListAllresult=[]
    results=[]

    def setup(resource,config):
        resource.config=config

    def readfile(resource):
        print("readfile..")
        xmlData=resource.config['datasource']
        print(xmlData)
        parser = ET.XMLParser(remove_comments=False)
        xml = ET.parse(xmlData, parser=parser)
        alldata=xml.xpath("count(/records/record)")
        resource.total=int(alldata)
        print("Raw Data Total:",resource.total)
        resource.rawData=xml.xpath("/records/record[STATUS/text()='1' and (POSITION/text()='Steward' or POSITION/text()='Pilot' or POSITION/text()='Airhostess') and EMPID/text()!=PASSPORT/text()]")
        # print("Raw Data Total:",resource.rawData)

    def transform(resource):
        print("transform Data..")
        dateUtil=DateUtility()
        print(dateUtil)
        print("rawData in condition ..", len(resource.rawData))
        currentDate=dateUtil.currentDate()
        YEAR_EXP=3
        for element in resource.rawData:
            data=DevMountainData(element)
            clubData=ClubData(data)
            checkdupEmp = True
            # print(f'clubData {clubData.toSet()}')
            diffYear=dateUtil.diffYear(dateUtil.toDate(clubData.hired),currentDate)


            ## check grater year
            if(diffYear>YEAR_EXP):
                if resource.ListAllresult:
                    for checkEmp in resource.ListAllresult:

                        if checkEmp[0] == clubData.emp_id:
                            checkdupEmp = False
                    if checkdupEmp: resource.ListAllresult.append((clubData.toSet()))
                else:
                    resource.ListAllresult.append((clubData.toSet()))

        ## for drop duplicate data
        resource.results = set(resource.ListAllresult)

        print("Raw Data :",len(resource.results))
        print("Raw Data Duplicate:",str(len(resource.ListAllresult)-len(resource.results)))
        print("Raw Data InValid:",str(resource.total-len(resource.ListAllresult)))


    def generateJson(resource):
        print("Generate Json..")
        results=[]
        for data in resource.results:
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
            # print(data)
            results.append(tmpData)

        FileUtility().write(resource.config['clubDataReport'],json.dumps(results))

    def loadDb(resource):
        print("loadDb..")
        dataUtility=DataUtility(resource.config['dbName'])
        dataUtility.dbSetup()
        dataUtility.save(resource.results)


    def generateGraph(resource):
        print("generate Graph..")

        Pilot = 0
        Airhostess = 0
        Steward = 0

        for countPosition in resource.results:
            if "Airhostess" == countPosition[9]:
                Airhostess = Airhostess + 1
            if "Pilot" == countPosition[9]:
                Pilot = Pilot + 1
            if "Steward" == countPosition[9]:
                Steward = Steward + 1

        left = [1, 2, 3]

        # heights of bars
        height = [Pilot, Airhostess, Steward]

        # labels for bars
        tick_label = ['Pilot', 'Airhostess', 'Steward']

        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.8, color = ['red', 'green', 'blue'])

        # plot title
        plt.title('Summary Position Chart')

        # function to show the plot
        plt.show()

def main():

        print("#####start#####")

        config={
            "datasource":"data-devclub-1.xml",
            "dbName":"Hackaton.db",
            "clubDataReport":"empClubData"
        }

        startTime = time.perf_counter()


        exe=Execute()
        exe.setup(config)
        exe.readfile()
        exe.transform()
        exe.loadDb()
        exe.generateJson()
        exe.generateGraph()

        endTime = time.perf_counter()
        totalTime = endTime - startTime
        print(f'##Total used time {totalTime:.4f} seconds##')

if __name__ == "__main__":
    sys.exit(main())