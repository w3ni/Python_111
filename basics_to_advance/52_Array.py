# import array

# std_roll = array.array('i',[101,102,103,104,105])
# print(std_roll[0])

# -----------------------------

from array import *

std_roll = array('i',[101,102,103,104,105])
# for el in std_roll:
#     print(el)

n = len(std_roll)
for i in range(n):
    print(i,std_roll[i])
