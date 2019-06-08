
class Employee:  #user defined datatype.. structure to hold emp info

    def __init__(self,eid,enm,eag,esal,eadr,edeg):
        self.empId=eid
        self.empName=enm
        self.empAge=eag
        self.empSalary=esal
        self.empAddress=eadr
        self.empDegignation=edeg

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)
