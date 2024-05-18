# Exception Handling , Assert


# a = int(input('Enter your first Num : '))
# b = int(input('Enter your second Num : '))

# try:
#     d = a/b
#     print(d)


#     # print('Inside try')

# # except ZeroDivisionError:
# #     print('Division by zero not allowed')
# # else:
# #     print('Inside else')
# # finally:
# #     print('Inside finally')

# # print('Rest of the code')

# except ZeroDivisionError as obj:
#     print(obj)

# except NameError as ob:
#     print(ob)

# print('Rest of the code')

# try:
#     d =a/b
#     print(d)

# except (NameError, ZeroDivisionError) as obj:
#     # print('Exception Handler')
#     print(obj)

# print('Rest of the code')

#----- all exception -------------

# except:
#     print('Exception Handler')
# print('Rest of the code')

# ----------------------------------------------------
# -------- Assert Statement ------------------

a = 35
assert a <= 10 , 'Invalid Number'