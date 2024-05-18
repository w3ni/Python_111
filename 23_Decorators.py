# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thans for using it")
#     return mfx

# @greet
# def hello():
#     print("Hello taiba...........")

# # hello()
# greet(hello)()

# --------------------------------------------

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("good morning")
#         fx(*args, **kwargs)
#         print("Thanks for using it")
#     return mfx

# @greet
# def add(a,b):
#     print(a+b)

# # greet(hello)()
# # greet(add)(1,2)
# add(1,2)

# ----------------------------------------------------

# def deco(func):
#     def wrapper():
#         print("Transuction initiated")
#         func()
#         print("Transuction completed")
#     return wrapper

# def hello():
#     print(".....Executing all steps of transuction.....")

# hello1 = deco(hello)
# hello1()

# --------------------------------------------------






