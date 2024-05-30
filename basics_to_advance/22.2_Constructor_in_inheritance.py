# Geeky_shows

class Father:
    def __init__(self,m):
        self.money = m
        print("Father class constructor", self.money)

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class instance method")

s = Son(45000)
print(s.money)
s.show()
s.disp()