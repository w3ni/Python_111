# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Abhishek")
#         super().parent_method()

#     def child_method(self):
#         print("this is the child method")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

# -------------------------------------

# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

# class Programmer(Employee):
#     def __init__(self,name,id,lang):
#         super().__init__(name,id)
#         self.lang = lang

# rohan = Employee('rohan das','320')
# harry = Programmer("harry","2301" , "python")

# print(rohan.name)
# print(harry.lang)
