# class Person:

#     def __init__(self, n , o):
#         self.name = n
#         self.occ = o

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = Person("Harray", "Developere")
# b = Person("Abhishek", "Penetration tester")
# c = Person(1,2,3)

# a.info()
# b.info()

# class faculty:
#     def __init__(self):
#         self.id = int(input("enter facylty id"))
#         self.name = input("Enter name")
#         self.salary = float(input("Enter faculty salary"))

#     def display(self):
#         print("faculty id :", self.id)
#         print("faculty name :", self.name)
#         print("faculty salary :", self.salary)

# a = faculty()
# a.display()

# ----------- Geeky Shows ----------------------

# class Mobile:
#     def __init__(self):
#         print("Mobile constructor called ")
    
# realme = Mobile()

# ----------- without parameter ----------------

# class Mobile:
#     def __init__(self):
#         self.model = "Realme X"

#     def show_model(self):
#         print("Model :", self.model)
    
# realme = Mobile()
# realme.show_model()

# -------- With parameter ------------------

class Mobile:
    def __init__(self,m,v=90): #default value and formal argument 
        self.model = m
        self.volume = v
    
    def show_model(self,p):
        price = p #local variable
        print("Model : ", self.model, "And price :" , price )
        print("Volume :", self.volume)

realme = Mobile('Realme X') #object with acual argument

realme.show_model(10001)
