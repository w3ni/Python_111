applePrice = int(input("Enter Apple Prices"))
budget = int(input("Enter Your Budeg"))

if (budget - applePrice > 150) and (budget-applePrice < 170):
    print("add 1kg apple in my cart")
elif (budget - applePrice > 170):
    print("It's okay you can buy hurry!")
else:
    print("Do not add apples i my cart")

# --------------------------------------------

num = int(input("Enter your number"))
if num < 0:
    print("num is negative")
elif num == 0:
    print("num is zero")
elif num > 0:
    print("num is positive")
else:
    print("enter integer")

    
# -------- Short Hand If Else -----------------
    
a = 20
b = 10
print(a) if a > b else print(b)
c = 9 if a > b else 0
print(c)