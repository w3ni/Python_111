from threading import Thread, current_thread
from time import sleep

# def disp():
#     print("d thread")

# t1 = Thread(target=disp)
# print(t1.isDaemon())
# # t1.start()
# # t1.daemon = True
# t1.setDaemon(True)
# print(t1.isDaemon())

# -------------------------------

# mt = current_thread()
# print(mt.getName())
# print(mt.daemon)


# ----------------------------------

# def disp():
#     print('Disp function')
#     t2 = Thread(target=show)
#     print(t2.isDaemon())
#     t2.start()


# def show():
#     print('Show function')


# mt = current_thread()
# print(mt.getName())
# print(mt.isDaemon())

# t1 = Thread(target=disp)

# print('Before', t1.isDaemon())
# t1.setDaemon(True)
# print('after', t1.isDaemon())
# t1.start()
# t1.join()
# print('main thread')

# if parrent deamon then child will be also deamon . if parent non deamon then child is also non deamonṇ

# -----------------------------------------------

def teacher():
    for i in range(1,11):
        print('Teaching session',i)
        sleep(1)

t1 = Thread(target=teacher)
t1.setDaemon(True)
t1.start()
sleep(6)
t1.join()
print("Exam finished",current_thread().name)