# Geeky_Shows 
# Passing member of one class to another class in python

class Student:
    #Constructor
    def __init__(self,n,r):
        self.name = n
        self.roll = r

    # Instance Method
    def disp(self):
        print("Student Name :",self.name)
        print("Student roll :", self.roll)

class User:
    @staticmethod
    def show(s):
        print("User name",s.name)
        print("User roll", s.roll)
        s.disp()

# Creating Object of student class
stu = Student('Rahul', 101)
User.show(stu)
