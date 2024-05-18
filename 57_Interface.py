from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("child clss")
        print("Disp 1 abstract method")

class Grandchil(Child):
    def disp2(self):
        print("Grandchild class")
        print("Disp 1 abstract method")


c = Child()
c.disp1()
