from threading import Thread
from time import sleep

class MyExam:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Question 1 solve")
        sleep(3)
    def q2(self):
        print("Question 2 solve")
        sleep(2)
    def q3(self):
        print("Question 3 solve")
        sleep(2)
        print("Thank You")

mye = MyExam()
t = Thread(target=mye.solve_question)
t.start()