# class Person:
#     name = "Abhishek"
#     occupation = "Software Developer"
#     networth = 1000000
    
#     def info(self):
#         print(f'{self.name} is a {self.networth}')

# a = Person()
# b = Person()

# a.occupation = "Accoountant"
# a.networth = 1000
# a.info()

# ----------------------------------------------------

# class Library:
#     def __init__(self):
#         self.noBooks = 0
#         self.books = []

#     def addBook(self,b):
#         self.books.append(b)
#         self.noBooks = len(self.books)

#     def showInfo(self):
#         print(f"The library has {self.noBooks} books")
#         for b in self.books:
#             print(b)

# l1 = Library()
# l1.addBook("Harry potter")
# l1.showInfo()

# --------------------------------------------------------

# class Person:
#     def __init__(self,n,o):
#         self.name = n 
#         self.occ = o

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = Person("Harry" , "Developer")
# a.info()

# ---------------------------------------------------

class faculty:
    def __init__(self):
        self.id = int(input("enter faculty id : "))
        self.name = input("Enter name")
        self.salary = float(input("Enter faculty salary"))

    def display(self):
        print(f"faculty id is : {self.id}")
        print(f"faculty name :" , self.name)
        print(f"faculty salary :", self.salary)

a = faculty()
a.display()

# ---------------------------------------

# Constructor example 


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
