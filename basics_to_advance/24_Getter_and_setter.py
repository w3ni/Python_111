# class Mobile:
#     def __init__(self):
#         self.model = 'realme X'

#     def get_modle(self):
#         return self.model
    
#     def set_model(self):
#         self.model = "realme gt 20"

# realme = Mobile()
# m = realme.get_modle()
# # m = realme.set_model()
# # print(realme.model)
# print(m)

# # ------------------------------------------

# class Employee:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first,self.last)
    
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
    
#     @fullname.setter
#     def fullname(self,name):
#         first , last = name.split(' ')
#         self.first = first
#         self.last = last
    
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name')
#         self.first = None
#         self.last = None

# emp1 = Employee('john','smith')
# emp1.fullname = 'cary schafer'

# print(emp1.fullname)
# print(emp1.email)

# del emp1.fullname
# print(emp1.fullname)

# -----------------------------------------------

# class Employee:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def explain(self):
#         return f"this emp is {self.fname} {self.lname}"
    
#     @property
#     def email(self):
#         if self.fname == None or self.lname == None:
#             return "Email is not set please set it using setter"
#         return f"{self.fname} {self.lname} @gmail.com"
    
#     @email.setter
#     def email(self,string):
#         print("Sitting Now")
#         name = string.split("@")[0]
#         self.fname = name.split(".") [0]
#         self.lname = name.split(".") [1]

#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
    
# Abhishek = Employee("Student" , "18")
# # Abhishek.fname = "Weni"
# Abhishek.email = "the.the@abhishek.com"
# print(Abhishek.email, "\n" , Abhishek.lname)
    
# del Abhishek.email
# print(Abhishek.email)

# ----------------------------------------------------

class myClass:
    def __init__(self,value):
        self.value = value
    
    def show(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

obj = myClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()