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

# sql = 'delete from student where stuid = %s'
# myc = conn.cursor(prepared=True)
# n = int(input('Enter your id :'))
# del_value = (n,)
# try: 
#     myc.execute(sql,del_value)
#     conn.commit()
#     print(myc.rowcount, ' Row Deleted ')
# except:
#     conn.rollback()
#     print('Unable to delete data')
# myc.close()
# conn.close()

# ---------- update -----------------


# sql = 'update student set fees=? where stuid=?'
# sql = 'update student set name=%s , roll=%s , fees=%s where stuid=%s'
# myc = conn.cursor(prepared=True)

# id = int(input('Enter student id to upgrade :'))
# nm = input("Enter your name :")
# ro = int(input('Enter roll no :'))
# fe = float(input('Enter fees:'))
# # update_value=(55000,112)
# update_value = (nm,ro,fe,id)
# try: 
#     myc.execute(sql,update_value)
#     conn.commit()
#     print(myc.rowcount, ' Row Updated ')
# except:
#     conn.rollback()
#     print('Unable to update data')
# myc.close()
# conn.close()

# ---------- Retrive Data ----------------

# sql = 'select * from student where stuid=%s'
sql = 'select * from student where roll=%s'
myc = conn.cursor(prepared=True)
# n = int(input('Enter your id to display data :'))
disp_value = (112,)
# disp_value = (n,)
try: 
    myc.execute(sql,disp_value)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
except:
    conn.rollback()
    print('Unable to Retrive data')
myc.close()
conn.close()