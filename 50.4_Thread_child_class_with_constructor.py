# thread child class with constructor
# Geeky_Show

from collections.abc import Callable
from threading import Thread
from typing import Any, Iterable, Mapping

class Mythread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("CHild thread constructor",a)

    def run(self):
        pass
    
t = Mythread(10)
t.start()
print("Main THread")