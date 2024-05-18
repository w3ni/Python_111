from threading import Thread

# def disp(a,b):
#     print("Thread Running",a,b)

# # t = Thread(target=disp , args=(20,30))
# # t.start()

# for i in range(5):
#     t = Thread(target=disp,args=(10,20))
#     t.start()

# -----------------------------

def disp():
    for i in range(5):
        print("Publish video C")

t = Thread(target=disp)

t.start()

for i in range(5):
    print("Publish video M")

for i in range(10):
    print("Publish VIdeo")