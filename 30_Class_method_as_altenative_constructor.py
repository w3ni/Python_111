# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def fromStr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
    
# e = Employee("Abhishek",18000)
# print(e.name)
# print(e.salary)

# string = "Harry-1200"
# e1 = Employee.fromStr(string)
# print(e1.name)
# print(e1.salary)

# --------------------------------------------

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_str(cls,str):
        name ,  age = str.split(",")
        return cls(name, int(age))
    
Person = Person.from_str("Abhi , 30")
print(Person.name , Person.age)