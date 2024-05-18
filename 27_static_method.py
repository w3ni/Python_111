# class Math:
#     def __init__(self,num):
#         self.num = num

#     def addtonum(self, n):
#         self.num = self.num + n

#     @staticmethod
#     def add(a,b):
#         return a + b

# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)
# print(Math.add(7,2))

# ----------------------------------

# Geeky_shows

class Mobile:
    fp = 'yes'

    @staticmethod #Decorator
    def show_model(m,p): #Static method
        model = m
        price = p
        print('Model', model , 'price' , price)

realme = Mobile()
Mobile.show_model('Poco x' , 29999) #calling static method


