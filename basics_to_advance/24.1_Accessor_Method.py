#Geeky_shows

#getter method 
# class Mobile:
#     def __init__(self):
#         self.model = " Realme X " #Instance variable

#     def get_model(self): #Accessor Method
#         return self.model
    
# realme = Mobile()
# m = realme.get_model() #Calling Accessor Method
# print(m)

# -------------------------------
#Setter method

# class Mobile:
#     def __init__(self):
#         self.model = "realme x" #Instance variable

#     def set_model(self):
#         self.model = 'Realme 2' #Mutator method

# realme = Mobile()
# #Before setting
# print(realme.model)
# #After setting
# realme.set_model()
# print(realme.model)

# -----------------------------

class Mobile():
    def set_model(self,m):
        self.model = m # Mutator method
        
realme = Mobile()
realme.set_model('Realme X') #Calling mutator method
print(realme.model)