# Parameterize query single row insert

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


# sql = 'insert into student(name,roll,fees) values (%s,%s,%s)'
# myc = conn.cursor()
# params = ("Veeru",33,964587)
# try:
#     myc.execute(sql,params)
#     # myc.execute(sql,[()])
#     conn.commit()
#     print(myc.rowcount, 'Row inserted')
#     print(f'StuID : {myc.lastrowid} Inserted')
# except:
#     conn.rollback()
#     print('Unable to insert data')

# myc.close()
# conn.close()

# ------------------ Multiple rows insert : Executemany()-----------


# sql = 'insert into student(name,roll,fees) values (%s,%s,%s)'
# myc = conn.cursor()
# params = [("jai",11,30000),("Veeru",33,964587)]
# try:
#     myc.executemany(sql,params)
#     conn.commit()
# except:
#     conn.rollback()
#     print('Unable to insert data')

# myc.close()
# conn.close()

# --------------- Take input from User -------------------------

sql = 'insert into student(name,roll,fees) values (%s,%s,%s)'
myc = conn.cursor()

nm = input('Enter Your Name :')
ro = int(input('Enter roll :'))
fe = float(input('Enter fees :'))

params = (nm,ro,fe)

try:
    myc.execute(sql,params)
    conn.commit()
except:
    conn.rollback()
    print('Unable to insert data')

myc.close()
conn.close()

