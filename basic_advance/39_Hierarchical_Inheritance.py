# class Parent:
#     def func1(self):
#         print("This function is in parent class")

# class Child1(Parent):
#     def func2(self):
#         print("this function is in child 1")

# class Child2(Parent):
#     def func3(self):
#         print("this function is in child 2")

# object1 = Child1()
# object2 = Child2()
# object1.func1()

# -----------------------------------------

# Son - Daughter can't access each other

class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class Method")
    
class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class constructor")
    def showS(self):
        print("Son class method")
    
class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter class constructor")
    def showD(self):
        print("Daughter class method")

d = Daughter()
# s = Son()
# d.showD()
d.showS()
# d.showF()