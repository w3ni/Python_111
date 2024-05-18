#Geeky_Show

# def decor(fun):
#     def inner():
#         print("If : before enhcancing function")
#         fun()
#         print("If : After enhancing function")
#     return inner

# def num():
#     print("We will use this function")
#     print("and will enchance this in decorator")

# result = decor(num)
# result()

# -------------------------

# def decor(fun):
#     def inner():
#         print("If : before enhancing")
#         fun()
#         print("If : after enhancing")
#     return inner

# @decor
# def num():
#     print("We will use this fun")
#     print("and will enhance")

# num()

# -----------------------------

# def decor(fun):
#     def inner():
#         a = fun()
#         add = a + 5
#         return add
#     return inner

# def num():
#     return 20

# result = decor(num)
# print(result())

# -------------------------

# def decor(num):
#     def inner():
#         a = num()
#         add = a + 5
#         return add
#     return inner
# @decor
# def num():
#     return 10
# print(num())

# ---------------------------

# def decor(num):
#     def inner():
#         b = num()
#         multi = b * 5
#         return multi
#     return inner

# def num():
#     return 10

# num = decor(num)
# print(num())


# -------------------------


def decor1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi
    return inner

def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner


def num():
    return 10

num = decor(decor1(num))
print(num())

