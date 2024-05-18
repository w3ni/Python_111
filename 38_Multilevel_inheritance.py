# class Employees():
#     def Name(self):
#         print("Employee name : Kush") 

# class Salary(Employees):
#     def salary(self):
#         print("salary is 100000000")

# class Designation(Salary):
#     def desig(self):
#         print("Designation : test engineer")

# call = Designation()
# call.Name()

# -------------------------------------------

# class GrandFather:
#     pass

# class Father(GrandFather):
#     pass

# class Son(Father):
#     pass

# ----------------------
# geeky_shows 

class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Son(Father):
    # def __init__(self):
    def __init__(self):
        super().__init__()
        print("Son class constructor")
    def showS(self):
        print("Son class method")
    
class GrandSon(Son):
    # def __init__(self):
    def __init__(self):
        super().__init__()
        print("Grandson constructor")
    def showG(self):
        print("Grandson class method")

g = GrandSon()
g.showF()
# g.showS()
# g.showG()