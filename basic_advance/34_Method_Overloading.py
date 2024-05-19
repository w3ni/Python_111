# class Add:
#     def result(self, x, y):
#         print('Addition', x+y)

# class Multi(Add):
#     def result(self, a, b):
#         super().result(10,20)
#         print('Multiplication',a*b)

# m = Multi()
# m.result(10,2)

# a = Add()
# a.result(10,20)

# ---------------------------------------

class Add:
    def result(self,a,b):
        print('Addition',a+b)
    
class Multi:
    def result(self,a,b):
        print("Multiplication",a*b)

a = Multi()
a.result(1,2)

# --------------------------------------

# class example:
#     def add(self,a,b):
#         x = a+b
#         return x
    
#     def add(self,a,b,c):
#         x = a+b+c
#         return x
    
# obj = example()

# print(obj.add(10,20,30))
# print(obj.add(10,20))

# ----------------------------

# Geeky_Shows

class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a*b
        else:
            s = 'Provide at least two numbers'
        return s
obj = Myclass()
print(obj.sum(10,2,2))
