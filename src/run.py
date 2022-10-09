from lxml import etree as ET
from data import DevMountainData, ClubData
from util import DataUtility, FileUtility, usedtime
import time,sys,os,csv
import sys
from datetime import datetime, date
from dateutil import relativedelta
import matplotlib.pyplot as plt


@usedtime
class Executor(object):
    config = {}
    total = int()
    valid = int()
    invalid = int()
    results = []

    @usedtime
    def setup(self, config):
        self.config = config

    @usedtime
    def extract(self):
        global clubData
        print("Extract..")
        today = date.today().strftime("%d-%m-%Y")
        xmlData = self.config['datasource']
        parser = ET.XMLParser(remove_comments=False)
        xml = ET.parse(xmlData, parser=parser)
        alldata = xml.xpath("count(/records/record)")
        self.total = int(alldata)
        print("Raw Data Total:", self.total)
        datasource = xml.xpath(
            "/records/record[STATUS/text()='1' and (POSITION/text()='Steward' or POSITION/text()='Pilot' or "
            "POSITION/text()='Airhostess') and EMPID/text()!=PASSPORT/text()]")

        for element in list(datasource):
            data = DevMountainData(element)
            birthday = data.birthday
            d1 = datetime.strptime(today, "%d-%m-%Y")
            d2 = datetime.strptime(birthday, "%d-%m-%Y")
            datediff = relativedelta.relativedelta(d1, d2)
            print(datediff.days)
            if datediff.days > 3:
                clubData = ClubData(data)
                self.results.append(clubData.toSet())

        print("Raw Data Valid:", len(self.results))
        print("Raw Data InValid:", str(self.total - len(self.results)))

    @usedtime
    def load(self):
        print("Load..")
        dataUtility = DataUtility(self.config['dbName'])
        dataUtility.dbSetup()
        dataUtility.view()
        dataUtility.save(self.results)

    @usedtime
    def generateSummary(self):
        print("Generate Summary..")
        nation_group = []
        for nat in self.results:
            if nat[6] not in nation_group:
                nation_group.append(nat[6])
        for ds in nation_group:
            data = [i for i in self.results if i[6] == ds]
            FileUtility().write(self.config['clubDataReport'], [list(dat) for dat in data])

        if not os.path.exists("../csv"):
            os.makedirs("../csv")

        with open("../csv/devclub.csv", 'w', newline="") as f:
            write = csv.writer(f)
            write.writerow(["EMP_ID","PASSPORT","FIRSTNAME","LASTNAME","GENDER","BIRTHDAY","NATIONALITY","HIRED","DEPT","POSITION","STATUS","REGION"])
            write.writerows([list(dat) for dat in self.results])

    @usedtime
    def visualize(self):
        print("Generate visualize..")
        if not os.path.exists("../visualize"):
            os.makedirs("../visualize")
        # gender
        male = 0
        female = 0
        for data in self.results:
            gender = data[4]
            if gender == 0:
                male += 1
            elif gender == 1:
                female += 1
            else:
                pass
        gender_data = [male, female]
        gender_data_label = ["Male", "Female"]
        print(gender_data)
        plt.pie(gender_data, labels=gender_data_label)
        plt.legend()
        plt.title("summary gender")
        plt.savefig('../visualize/gender.png')
        # import numpy as np
        # import pandas as pd
        # import matplotlib.pyplot as plt
        # df1 = pd.read_csv("../csv/devclub.csv")
        # df2 = df1[['GENDER', 'EMP_ID']]
        # df2 = df2.groupby(['GENDER'])['EMP_ID']
        # print(df2.plot.pie())

def main():
    try:
        print("#####start#####")
        print(f"{sys.argv}")
        if len(sys.argv) > 1:
            exeType = sys.argv[1]
            print(f'{exeType}')
            if exeType == 'M':
                datasource = sys.argv[2]
                dbName = sys.argv[3]
                reportName = sys.argv[4]
                config = {
                    "datasource": datasource,
                    "dbName": dbName,
                    "clubDataReport": reportName
                }
                startTime = time.perf_counter()
                exe = Executor()
                exe.setup(config)
                exe.extract()
                exe.load()
                exe.generateSummary()
                exe.visualize()
                endTime = time.perf_counter()
                totalTime = endTime - startTime
                print(f'##Total used time {totalTime:.4f} seconds##')
            else:
                print("Please enter Execute Type (M) Parameter!")
        else:
            print("Please enter Parameter!")
    except ValueError as ve:
        return str(ve)


if __name__ == "__main__":
    sys.exit(main())
