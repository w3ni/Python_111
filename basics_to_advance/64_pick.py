# pick.py 
# Storing obj in the file

import pickle,stu

n = int(input('Enter number of student'))
with open('Student.dat', mode='wb') as f:
    for i in range(n):
        name = input('Enter student name :')
        roll = int(input('Enter your roll :'))
        address = input('Enter address :')
        stu1 = stu.Student(name,roll,address)
        pickle.dump(stu1,f)

print('Pickling Done!!')