# class Employee:
#     Company_Name = "Apple"
#     No_Of_Employee = 0
#     def __init__(self,name):
#         self.name = name
#         self.raise_ammount = 0.2
#         Employee.No_Of_Employee +=1

#     def showDetails(self):
#         print(f"the naem of the employee is {self.name} the no employee {self.No_Of_Employee} and the raise ammount of {self.Company_Name} is {self.raise_ammount}")

# emp1 = Employee("harry")
# emp1.raise_ammount = 0.4
# emp1.Company_Name = "Apple India"
# emp1.showDetails()
# Employee.Company_Name = "GOOGLE"
# print(Employee.Company_Name)

# class Mobile:
#     def __init__(self):
#         self.model = "Realme X" #Instance Vriable

#     def show_model(self):
#         print(self.model) #Accessing Instance

# realme = Mobile()

# realme.model = "Poco M2 Pro"
# print(realme.model)

# ========== Class Variable / Static Variable ================================

# class Mobile:
#     fp = "yes "

#     @classmethod
#     def is_fp(cls):
#         print(cls.fp)

# realme = Mobile()
# print(Mobile.fp)
# Mobile.is_fp()

class Mobile:
    fp = "Yes" #class variable

    def __init__(self):
        self.model = 'Realme X' #Instance Variable

    def show_model(self): #Instance Method
        print("Model : ", self.model) #Accessing Instance method
 
    @classmethod #Classmethod
    def is_fp(cls):
        print("Finger Print :",cls.fp) #Aceessing  class variable

realme = Mobile()
realme.show_model()
Mobile.is_fp()
Mobile.fp = 'No'
Mobile.is_fp()