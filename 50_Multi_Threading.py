# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor


# def func(seconds):
#     print(f"sleeping for {seconds} seconds")
#     time.sleep(seconds)


# def main():
#     time1 = time.perf_counter()
#     func(4)
#     func(2)
#     func(1)

#     t1 = threading.Thread(target=func, args=[4])
#     t2 = threading.Thread(target=func, args=[2])
#     t3 = threading.Thread(target=func, args=[1])
#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()

#     time2 = time.perf_counter()
#     print(time2 - time1)


# def poolinedemo():
#     with ThreadPoolExecutor() as executer:
#         future1 = executer.submit(func,3)
#         future2 = executer.submit(func,2)
#         future3 = executer.submit(func,1)
#         print(future1.result())
#         print(future2.result())
#         print(future3.result())
# poolinedemo()
#

# -----------------------------
# Geeky_Shows

# Main Thread

import threading

t = threading.current_thread().getName()

print("Geeky shows")

print(t)