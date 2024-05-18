from typing import Any

class Employee:
    def __init__(self,name):
        self.name = name
    
    def __len__(self):
        i = 0
        for items in self.name:
            i = i+1
        return 1
    
    def __str__(self):
        return f"the name of is {self.name} str"
    
    def __repr__(self):
        return f"the name of the employee is {self.name} rpr"
    
    def __call__(self):
        return ("Hey i am good ")
    
# e = Employee("harry")
# print(e.name)
# print(len(e))
