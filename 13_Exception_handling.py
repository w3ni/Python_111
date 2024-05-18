# a = input("Enter the number")
# print(f"Multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("Sorry")
# print("Some line fo code")
# print("End of programe")


# try:
#     num = int(input("enter an iteager"))
#     a = [66,44]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an inteager")
# except IndexError:
#     print("Index error")

# def func1():
#     try:
#         l = [1,2,3,4,5,6]
#         i = int(input("Enter your index"))
#         print(l[i])
#         return l
#     except:
#         print("Some error occured")
#         return 0
#     finally:
#         print("I am always executed")
#         print("I am always executed")
# x = func1()
# print(x)

# ----------------------------------

# a = int(input("Enter any value between 1 to 5 :"))
# if (a<5 or a>9):
#     raise ValueError("value should be between 5 and 9")