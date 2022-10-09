from lxml import etree as ET
from data import DevMountainData, ClubData
from util import DataUtility, FileUtility, usedtime
import time
import sys
from datetime import datetime, date
from dateutil import relativedelta


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
