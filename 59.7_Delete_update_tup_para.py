# Delete row from table using parameterize query
import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='#MySql1899',
        host='localhost',
        database = 'pdb',
        port=3306)
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable to connect')

# use for tuple : -
# sql = 'delete from student where stuid = %s'

# Use for dictonary : -
# sql = 'delete from student where=%(id)s'

# myc = conn.cursor()
# del_value = (5,)

# del_value = {'id':5} ----- for dict
# del_value = {'id':n} ---- user input

# n = int(input('Enter ID to delete :'))
# del_value = (n,)
# try:
    # use for tuple - 
    # myc.execute(sql,del_value)

    # use for dict -
#     myc.execute(sql,{'id':4})

#     conn.commit()
#     print(myc.rowcount, ' Row Deleted ')
# except:
#     conn.rollback()
#     print('Unable to delete data')
# myc.close()
# conn.close()

# ----------------- Update data ---------------


# use for tuple : -
# sql = 'update student set fees=%s where stuid=%s'
# sql = 'update student set name=%s, roll=%s, fees=%s where stuid=%s'
# myc = conn.cursor()

# id = int(input('Enter student id to update :'))
# nm = input('Enter Name :')
# ro = int(input('Enter roll :'))
# fe = float(input('Enter your fees :'))

# # update_value = (400,6)
# # update_value = ('jack',123,55555,6)
# update_value = (nm,ro,fe,id)

# try:
#     myc.execute(sql, update_value)
#     conn.commit()
#     print(myc.rowcount, ' Row updated ')
# except:
#     conn.rollback()
#     print('Unable to delete data')
# myc.close()
# conn.close()

# ---------- update in dict ---------------------

# sql = 'update student set fees=%(fee)s where stuid=%(id)s'
# sql = 'update student set name=%(name)s , roll=%(roll)s , fees=%(fee)s where stuid=%(id)s'
# myc = conn.cursor()

# id = int(input('Enter your id :'))
# nm = input('ENter your name :')
# ro = int(input('Enter roll :'))
# fe = float(input('Enter fess :'))

# update_value = {'fee':400000 , 'id':6}
# update_value = {'name':'Ramu','roll':6564 , 'fee':545897856 , 'id':6}
# update_value = {'name':nm , 'roll':ro , 'fee':fe , 'id':id}

# try:
#     myc.execute(sql, update_value)
#     conn.commit()
#     print(myc.rowcount, ' Row updated ')
# except:
#     conn.rollback()
#     print('Unable to delete data')
# myc.close()
# conn.close()

# -------------------Retrive single / Multi row with where clause in tuple ------------

# sql = 'select * from student where roll=%s'
# myc = conn.cursor()
# n = int(input("Enter your Roll :"))

# disp_value = (n,)
# # disp_value = (7,)
# try:
#     myc.execute(sql, disp_value)
#     row = myc.fetchone()
#     while row is not None:
#         print(row)
#         row = myc.fetchone()
#     print('Total rows :', myc.rowcount)
# except:
#     conn.rollback()
#     print('Unable to Retrive data')
# myc.close()
# conn.close()

# ------------- Retrive single/multi row data in dict -----------------


# sql = 'select * from student where stuid=%(id)s'
sql = 'select * from student where fees=%(fees)s'
myc = conn.cursor()
n = int(input('Enter your fees :'))
disp_value =  {'fees':n}

try:
    myc.execute(sql,disp_value)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print('Total rows :', myc.rowcount)
except:
    conn.rollback()
    print('Unable to Retrive data')
myc.close()
conn.close()