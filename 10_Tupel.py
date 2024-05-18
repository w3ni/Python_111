# tup = (1,2,3,4,5)
# tup2 = ("red","green","blue")

# print(tup[1],tup[-2],tup[1:2],tup[::2])

# temp = list(tup)
# print(temp , type(temp))

# print(temp.pop(3))

# temp[2] = "Finland"
# print(temp)

# ---------------- unpack tupel ----------------

# info = ("Abhishek", 22 , "BBDU")
# (name,age,university) = info
# print(name,age,university)

# # -------------------------------------

# # Nested tupel access using while loop

# a = (10,20, (30,40))
# n = len(a)
# i = 0
# while(i<n):
#     # checking a[i] is a tuple or not
#     if type(a[i]) is tuple:
#         if len(a[i]) > 1:
#             j = 0
#             m = len(a[j])
#             while j<m:
#                 print(i,j,a[i][j])
#                 j+=1
#             i += 1
#     else:
#         print(i, a[j])
#         i += 1

# ----------------------------------------
# a = ((1,2,3),(11,22,33))
# n = len(a)
# i = 0
# while(i<n):
#     j = 0
#     while j < len(a[i]):
#         print(i,j,a[i][j])
#         j+=1
#     i+=1

# ============================================

# Nested tuple access using For loop

# a = (10,20,30 , (50,60))
# n = len(a)
# for i in range(n):
#     if type(a[i]) is tuple:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j,a[i][j])
#     else:
#         print(i,a[i])

# -------------------------------------------

a = ((10,20,30),(40,50,60))
# Without index
# for r in a:
#     for c in r:
#         print(c)
#     print()

# With index

n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()