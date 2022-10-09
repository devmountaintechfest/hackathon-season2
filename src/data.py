import json

class DevMountainData(object):
    def __init__(self, data):
        self.emp_id=int(data[0].text)
        self.passport=data[1].text
        self.firstname=data[2].text
        self.lastname=data[3].text
        self.gender=int(data[4].text)
        self.birthday=data[5].text
        self.nationality=data[6].text
        self.hired=data[7].text
        self.dept=data[8].text
        self.position=data[9].text
        self.status=int(data[10].text)
        self.region=data[11].text

class ClubData(object):
    def __init__(self, data):
        self.emp_id=data.emp_id
        self.passport=data.passport
        self.firstname=data.firstname
        self.lastname=data.lastname
        self.gender=data.gender
        self.birthday=data.birthday
        self.nationality=data.nationality
        self.hired=data.hired
        self.dept=data.dept
        self.position=data.position
        self.status=data.status
        self.region=data.region

    def toSet(self):
        return (self.emp_id,self.passport,self.firstname,self.lastname,self.gender,self.birthday,self.nationality,self.hired,self.dept,self.position,self.status,self.region)

    def toJson(self):
        return json.dumps(self.__dict__)