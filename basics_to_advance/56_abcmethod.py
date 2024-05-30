from abc import ABC , abstractmethod

# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass

#     def show(self):
#         print("Concrete method")

# class Child(Father):
#     def disp(self):
#         print("child clss")
#         print("Defining abstract method")

# c = Child()
# c.disp()
# c.show

# ----------------------------------

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK47")

class Army(DefenceForce):
    def area(self):
        print("Area = Land")

class Airforce(DefenceForce):
    def area(self):
        print("Area = Sky")

class Navy(DefenceForce):
    def area(self):
        print("Area = Sea")
0
a = Army()
af = Airforce()
n = Navy()

a.gun()
a.area()