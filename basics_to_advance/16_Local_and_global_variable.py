# Global variable
x = 10
def my_function():
    # Local variable modify info globle
    global x
    x = 20
    y = 5
    print(y)

my_function()
print(x)