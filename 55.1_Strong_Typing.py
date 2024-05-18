# Geeky_shows

class Duck:
    def walk(self):
        print("Thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")


def myfunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,"talk"):
        obj.talk()
        
d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

c = Cat()
myfunction(c)