#Geeky_Shows

class Mobile:
    fp = "yes"

    @classmethod
    def is_fp(cls):
        print("Finger print :",cls.fp)

Realme = Mobile()
redmi = Mobile()
poco = Mobile()

# print("class fp :", Mobile.fp)
# print("realme :",redmi.fp)
# print("poco", poco.fp)

# print()

# Mobile.fp = "No"

# print("class fp :", Mobile.fp)
# print("realme :",redmi.fp)
# print("poco", poco.fp)

print()

poco.fp = "Not working"
Realme.fp = "both avaialble"

print("class fp :", Mobile.fp)
print("realme :",redmi.fp)
print("poco", poco.fp)
print("realme", Realme.fp)