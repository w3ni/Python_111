
import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         user='root',
#         password='#MySql1899',
#         host='localhost',
#         database = 'pdb',
#         port=3306)
#     if(conn.is_connected()):
#         print('Connected')
# except:
#     print('Unable to connect')


# --------- inset single rows in dict ------------------
# sql = 'insert into student(name,roll,fees) values (%(name)s,%(roll)s,%(fees)s)'
# myc = conn.cursor()
# params = {'name' : 'Ada' , 'roll' : 988 , 'fees' : 65445}
# try:
#     myc.execute(sql,params)
#     # myc.execute(sql, {'name' : 'Sameer' , 'roll' : 777 , 'fees' : 561254})
#     conn.commit()
#     print(myc.rowcount, 'Row inserted')
#     print(f'StuID : {myc.lastrowid} Inserted')
# except:
#     conn.rollback()
#     print('Unable to insert data')

# myc.close()
# conn.close()

# ----------- insert multiple rows in dict ------------

# sql = 'insert into student(name,roll,fees) values (%(name)s,%(roll)s,%(fees)s)'
# myc = conn.cursor()

# nm = input('Enter name : ')
# ro = int(input('Enter your roll no :'))
# fe = float(input("Enter your fees :"))

# params = {'name':nm , 'roll':ro , 'fees':fe}
# try:
#     myc.execute(sql,params)
#     conn.commit()
#     print(myc.rowcount, 'Row inserted')
#     print(f'StuID : {myc.lastrowid} Inserted')
# except:
#     conn.rollback()
#     print('Unable to insert data')

# myc.close()
# conn.close()

# ------------ continue adding data ---------------------

def student_data(nm,ro,fe):
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
    sql = 'insert into student(name,roll,fees) values (%(name)s,%(roll)s,%(fees)s)'
    myc = conn.cursor()

    n = nm
    r = ro
    f = fe

    params = {'name':n , 'roll':r , 'fees':f}
    try:
        myc.execute(sql,params)
        conn.commit()
        print(myc.rowcount, 'Row inserted')
        print(f'StuID : {myc.lastrowid} Inserted')
    except:
        conn.rollback()
        print('Unable to insert data')

    myc.close()
    conn.close()

while True:
    nm = input('Enter name : ')
    ro = int(input('Enter your roll no :'))
    fe = float(input("Enter your fees :"))
    student_data(nm,ro,fe)
    ans = input("Do you want to exit (y/n)")
    if (ans=='y'):
        break