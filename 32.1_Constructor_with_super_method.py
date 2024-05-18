class Father:
    def __init__(self,m):
        self.money = m
        print("Father class constructor")

    def show(self):
        print("Father class constructor")

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)
        self.job = j
        print("Son class constructor")

    def disp(self):
        print("Son class instance method", self.money, self.job)

s = Son(45094535646, ' Python ')
s.disp()