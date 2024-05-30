import pickle,stu

# unpick.py
# Reading Object from the file

with open('Student.dat', mode='rb') as f:
    while True:
        try:
            obj1 = pickle.load(f)
            obj1.disp()
        except EOFError:
            print('Done')
            break

