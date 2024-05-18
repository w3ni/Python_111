# Geeky_Shows

# from threading import Thread, current_thread

# def disp():
#     print("Default Child Thread Obj", current_thread().getName())
#     current_thread().setName('Doc THREAD')
#     print("New child thread name :",current_thread().getName())
          
# t = Thread(target=disp)
# t.start()

# print("Main Thread", current_thread().getName())
# current_thread().setName('Geeky Shows')
# print("New main thread name", current_thread().getName)

# ---------------------------------------------------------------

# def disp():
#     print("Defualt child name :", current_thread().name)
#     current_thread().name = "Flying Thread"
#     print("New child name",current_thread().name)

# t = Thread(target=disp)
# t.start()

# print("Default main name :", current_thread().name)
# current_thread().name = 'Geeky Thread'
# print("New main thread name :", current_thread().name)

# ---------------------------------------------------------------

# def disp():
#     pass

# t = Thread(target=disp)
# print("default :",t.getName())
# t.setName('Doc Thread')
# print("New :",t.getName())

# t = Thread(target=disp)
# print("Default :",t.name)
# t.name = 'flying thread'
# print('New :',t.name)

# t  = Thread(target=disp, name ="Abhishek Thread")
# print(t.name)