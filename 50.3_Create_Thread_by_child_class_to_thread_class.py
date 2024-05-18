# Creating a thread by creating child class to thread class
# Geeky_Shows

from threading import Thread

# class Mythread(Thread):
#     pass

# t = Mythread()
# print(t.name)):

# class Mythread(Thread):
#     def run(self):
#         print("Run Method")

# t = Mythread()
# t.start()

# ---------------------

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")

t = Mythread()
t.start()
t.join()

for i in range(5):
    print("Main thread")