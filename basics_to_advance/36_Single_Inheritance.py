# class Parent:
#     def func1(self):
#         print("This function is in parent class")

# class Child(Parent):
#     def func2(self):
#         print("This function is in child class")

# object = Child()
# object.func1()
# object.func2()

# ---------------------------
# geeky_shows

class Father:
    money = 1000

    def show(self):
        print("Parent class instance method")

    @classmethod
    def showmoney(cls):
        print("Print class class method",cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent class static method:",a)

class Son(Father):
    def disp(self):
        print("Child class instance method")

s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()