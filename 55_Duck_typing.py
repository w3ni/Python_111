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
    obj.walk()

c = Cat()
myfunction(c)

