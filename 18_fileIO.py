# f = open("18_file.txt",'r')
# text = f.read()
# print(text)
# f.close()

# f = open('18_file.txt','w')
# f.write('hello world')
# f.close()

# with open('18_filse.txt','r') as a:
#     t = a.read()
#     print(t)

# with open('18_file.txt','a') as k:
#     k.write("Hey i am inside")

# h = open('18_file.txt','r')
# print(h.read())
# h.close()

# z = open('18_file.txt','w')
# lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
# z.writelines(lines)
# z.close()

# with open('18_file.txt','r') as z1:
#     print(z1.read())

# with open('18_file.txt' , 'r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data = f.read(5)
#     print(data)

with open('18_file.txt','a') as b:
    b.truncate(2)

f = open("18_file.txt", "r")
print(f.read())