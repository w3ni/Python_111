# Geeky_show

class Add:
    def result(self,x,y):
        print('Additon :',x+y)

class Multi:
    def result(self,a,b):
        super().result(10,20)
        print('Multiplication :',a*b)

m = Multi()
m.result(10,20)

# a = Add()
# a.result(10,20)