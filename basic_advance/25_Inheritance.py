
# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"the name of employee : {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLan(self):
#         print("the default language is python")

# a = Employee("Rohan", "400")
# a.showDetails()
# ------------------------------------

# Geeky_shows

class Employee:
    id = 1
    @classmethod
    def getid(cls):
        return cls.id 
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setsalary(self,salary):
        self.salary = salary
    def getsalary(self):
        return self.salary
    def setovertime(self,ot):
        self.ot = ot
    def getovertime(self):
        return self.ot
    
class Manager:
    def setsalary(self,salary):
        self.salary = salary
    def getsalary(self):
        return self.salary
    def getseniorname(self,sname):
        self.sname = sname
    def getseniorname(self):
        return self.sname
