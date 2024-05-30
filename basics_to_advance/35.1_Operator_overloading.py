# Geeky_shows

# MAGIC METHODS ..........

# int._add_(self,other)
# __sub__(self,other)
# __mul__(self,other)

# 10+20 int.__add__(10,20)
# 'a'+'b' str.__add__('a'+'b')

# print(int.__add__(20,20))
# print(20+20)

# print('Hello' + 'Geekyshows')
# print(str.__add__('Hello','Geekyshows'))
# ---------------------------------------------
class A:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return self.x + other.x

class B:
    def __init__(self,x):
        self.x = x
        
a = A(100)
b = B(200)

print(a+b)

print(a+b) 