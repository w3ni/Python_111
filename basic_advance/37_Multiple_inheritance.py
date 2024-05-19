# class ClassA:
#     def m1(self):
#         print("In class1")

# class ClassB(ClassA):
#     def m2(self):
#         print("In class2")

# class ClassC(ClassA):
#     def m3(self):
#         print("in class 3")

# class ClassD(ClassB,ClassC):
#     pass

# obj = ClassD()

# -------------------------
# Geeky_Shows

# class Father:
#     def __init__(self):
#         super().__init__()
#         print("Father class constructor")
#     def showF(self):
#         print("Father class method")

# class Mother:
#     def __init__(self):
#         super().__init__()
#         print("Mother class constructor")
#     def showM(self):
#         print("Mother class constructor")

# class Son(Father,Mother):
#     def __init__(self):
#         super().__init__() #Parent class constructor
#         print("Son class constructor")

#     def showS(self):
#         print("Son class constructor")

# s = Son()

# --------------------------

# Method Resolution Order (MRO)