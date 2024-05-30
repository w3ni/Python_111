import re

# pattern = r"[A-Z]+yclone"
# text = '''abhisehk kumar y clone '''
# matches = re.findall(pattern,text)
# # for match in matches:
# #     print(match)

# match = re.search(r"\.",b)
# print(match)

# --------------------------------------

a = "charlie chaplin 778898954 siya and the chocolate factory"
b = "abhishek.ve$rma@gmail.com"
c = "hello"
d = "xyz,xxyyzz,zxy,yxz,yzx,zyz, xxy,xxyyz,xyzz"

# match = re.search(r'\.',b)
# match = re.search(r"[@]",b)
# match = re.search(r"[l]",c)
# match = re.search(r'^abhi',c)
# match = re.search(r"com$",b)
# match = re.findall(r"C.a",a)
# match = re.findall(r"cha|and",a)
# match = re.findall(r"si?ya",a)
# match = re.findall(r"ch*a",a)
# match = re.findall(r"ch*a",a)
# match = re.findall(r"xy+z",d)
# match = re.findall(r"x{2,4}",d)
# match = re.findall(r"(x|z)yz",d)
# print(match)

# match = re.search(r"\Ahar",a)
# match = re.search(r"\bh",a)
# match = re.search(r"po\B",a)
# match = re.search("po\d",a)
# match = re.search(r'\D',a)
# match = re.search(r'\d',a)
# match = re.search(r'\s',a)
# match = re.search(r'\S',a)
# match = re.search(r'\w',a)
# match = re.search(r'\W',a)
# match = re.findall(r'@2\Z',a)
# print(match)

# match = re.findall(r'[atx]',a)
# match = re.findall(r'[^atx]',a)
# match = re.findall(r'[a-t]',a)
# match = re.findall(r'[1,2,3,4,5]',a)
# match = re.findall(r'[0-9]',a)
# match = re.findall(r'[0-7][0-9]',a)
# match = re.findall(r'[a-zA-Z]',b)
# match = re.findall(r'[$]',b)
# print(match)

# ------------------------------
phn = "222-334-5456"
if re.search("\d{3}-\d{3}-\d{4}",phn):
    print("it is a verified number")
else:
    print("incorrect number")
# -------------------------------

email = "john88@gmail.com"
print(re.findall("[\w.%]{0,20}@[\w-].[A-Za-z]{2,3}",email))