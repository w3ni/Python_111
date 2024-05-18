# def cube(x):
#     return x*x*x

# l = [1,2,3,4,5]
# newl = list(map(cube,l))
# print(newl)

# new = []
# for items in l:
#     new.append(cube(items))
# print(new)

# --------------------------------------------

# from functools import reduce

# number = [1,2,3,4]

# def mysum(x,y):
#     return x+y
# sum = reduce(mysum, number)
# print(sum)

# ---------------------------------------------

# double = lambda x: x*2
# print(double(5))    

# cube = lambda x:x*x*x
# print(cube(5))

# def appl(fx,value):
#     return 6 + fx(value)
# print(appl(cube,2))

# ----------------------------------------------

l = [1,2,3,5,6,8,9]
def filter_func(a):
    return a > 4

newl = list(filter(filter_func,l))
print(newl)