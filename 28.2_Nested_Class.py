class Army:
    def __init__(self) : #outer class
        self.name = 'Rahul'
        self.gn = self.Gun() #creating inner class obj

    def show(self):
        print("Name", self.name)

    class Gun:
        def __init__(self):
            self.name = 'Ak47'
            self.capacity = '75 round'
            self.length = '2.3 meter'

        def disp(self):
            print('Gun Name', self.name)
            print("Capicity", self.capacity)
            print("Length", self.length)
a = Army()
print(a.name)
a.show()
print(a.gn.name)

# g = a.gn

g = Army().Gun()
print()
print(g.name)
print(g.capacity)
print(g.length)
g.disp()

