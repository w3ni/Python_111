# class Employee:
#     def __init__(self):
#         self.__name = "Harry"

# a = Employee()
# print(a._Employee__name)
# print(a.__dir__())

# ------------------------------

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funcName(self):
        return "CodeWithHarry"
    
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))