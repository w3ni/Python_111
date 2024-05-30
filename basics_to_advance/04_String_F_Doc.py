# --------- String Example ---------------

# name = "Abhishek kumar verma"
# print(name[0:5] , name[0:-3] , name[-4:-2])
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.rstrip("ma"))
# print(name.replace("Abhishek" , "Weni"))
# print(name.split(" "))
# print(name.capitalize())
# print(len(name.center(50)))
# print(name.count("A"))
# print(name.endswith("k"))
# print(name.startswith("A"))
# print(name.find("k"))
# print(name.index("v"))
# print(name.isalnum())
# print(name.isalpha())
# print(name.islower())
# print(name.isprintable())
# print(name.isspace())
# print(name.swapcase())
# print(name.title())

# --------- F String ----------------

# letter = "hey {}"
# country = " India "
# name = "AK"
# print(letter.format(country,name))
# print(f"name {name} country {country}")

# price = 10.98765
# txt = f"for only {{price}} {price:2f} dollers!"
# print(txt)

# print(f"{2+3}")

# ----------- Doc String ---------------

# def squar(n):
#     '''Take in a number n , return '''
#     print(n**2)

# squar(5)
# print(squar.__doc__)

# --------------------------------------

# For loop without Index

str1 = "Anjali Abhishek Kr"
# for c in str1:
#     print(c)

n = len(str1)
# for i in range(n):
#     print(i,str1[i])

i = 0
while(i<n):
    print(i,str1[i])
    i += 1