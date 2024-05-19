# Chai_Aur_code

import time


# ------------------------------------------------------

# General difination
# def timer(func): #write difination - timer 
#     def wrapper(*args,**kwargs): #wrapper here - like toll booth
#         start = time.time()
#         result = func(*args,**kwargs) #execute func and give acess of argument
#         end = time.time()
#         print(f'{func.__name__} ran in {end-start}')
#         return result
#     return wrapper 

# @timer
# def example_func(n):
#     time.sleep(n)

# example_func(2)


# ----------------------------------------------------------

# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value = ', '.join(str(args) for arg in args ) #reverse loop also calle list compherihension
#         kwargs_value = ','.join(f"{k}={v}" for k,v in kwargs.items())
#         print(f'calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}')
#         return func(*args,**kwargs)
#     return wrapper

# @debug
# def hello():
#     print("Hello")

# @debug
# def greet(name, greeting="Hello"):
#     print(f'{greeting}, {name}')

# # hello()
# greet("Chai", greeting="HanJi")

# ------------------------------------------------------------

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

# long_running_function(2,3)
print(long_running_function(3,4))


