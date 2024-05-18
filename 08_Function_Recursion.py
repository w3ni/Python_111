# def calgmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# calgmean(9,8)

# def func(name):
#     print("hello",name)
# func("Abhishek")

# def fun2(name1 = "Abhishek"):
#     print("hello",name1)

# fun2()

# -----------------------

# def func(a,b):
#     sum = a+b
#     return sum
# result = func(20,30)
# print(result)

# ------------------------------

# def com(e,d):
#     if e>d:
#         print("e is greater than")
#     else:
#         print("d is greater")

# com(1,2)

# -----------------------------

# def avg(a,b):
#     print("the average is", (a+b)/2)

# avg(1,2)

# ------------------------------

# def avg(*num):
#     sum = 0 
#     for i in num:
#         sum += 1
#         return sum/len(num)

# c = avg(4,4)
# print(c)

# ----------------------------------

# def name(**name):
#     print("Hello", name["fname"],
#         name["mname"],name["lname"])
# name(fname="Abhishek", mname="Kumar" , lname="Verma")

# ---------------------------------

# def factorial(n):
#     if (n==0 or n ==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# ---------------------------------------
# =======PASS Statement==================
# ---------------------------------------

if 5 > 2:
    pass
else:
    print("Else body")

print("Rest of the code")

if 5<2:
    pass
else:
    print("Body of else")
print("rest of code")

i = 1
while(i <= 10):
    if (i == 5):
        pass
    print(i)
    i +=1
print("rest of the code")