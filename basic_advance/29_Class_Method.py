# class Employee:
#     Company = "Apple"
    
#     def show(self):
#         print(f"the name is {self.name} and company is {self.Company}")

#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.Company = newCompany

# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.Company)

# -----------------------------------

# Geeky_shows

# class Mobile:
#     @classmethod #Decorator
#     def show_model(cls): #Class method
#         print("Realme X")

# realme = Mobile()
# Mobile.show_model() #Calling class method

# ---------------------------------------  

class Mobile:
    fp = "Yes" #class variable

    @classmethod
    def show_model(cls , r):
        cls.ram = r
        print("Fingerprint :", cls.fp)
        print("RAM :",cls.ram)

realme = Mobile()
Mobile.show_model('4GB')