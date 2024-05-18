# Geeky_Show

from datetime import datetime

dt = datetime.today()
print(dt)
print()

new1 = dt.strftime("%B , %d , %Y")
print(new1)
print()

new2 = dt.strftime("%d/%b/%Y")
print(new2)
print()

new3 = dt.strftime("%d-%m-%Y")
print(new3)
print()

new4 = dt.strftime("%H:%M:%S")
print(new4)
print()

new5 = dt.strftime("%I:%M:%S")
print(new5)
print()