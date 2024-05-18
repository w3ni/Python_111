x = int(input("enter your num"))
match x:
    case 0:
        print("num is 0")
    case 1:
        print("num is 1")
    case _ if x!=90:
        print(x,"is not 90")
    case _:
        print(x)