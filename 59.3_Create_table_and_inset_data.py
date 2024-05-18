# Create insert or delete rowcount() , lastrowid()
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

# sql = 'create table student(stuid int auto_increment primary key, name varchar(20) , roll int , fees float)'
# myc = conn.cursor()
# myc.execute(sql)
# myc.close()
# conn.close()

# ------------- show tables ------------

# sql = 'show tables'
# myc = conn.cursor()
# myc.execute(sql)
# for d in myc:
#     print(d)
# myc.close()
# conn.close()

# ---------- Insert data in tables and rowcount() --------

# sql = 'insert into student(name,roll,fees) values ("Vaibhav",15,8890)'
# myc = conn.cursor()
# try:
#     myc.execute(sql)
#     conn.commit()
#     # rowcount()
#     # print(myc.rowcount, 'Row inserted')
#     # lastrowid()
#     # print(myc.lastrowid)
# except:
#     conn.rollback()
#     print('Unable to insert data')

# myc.close()
# conn.close()

# --------------------- Delete Row from table --------------

# sql = 'delete from student where stuid=4'
# myc = conn.cursor()
# try:
#     myc.execute(sql)
#     conn.commit()
#     print(myc.rowcount, 'Row Deleted')
# except:
#     conn.rollback()
#     print('Unable to delete data')

# myc.close()
# conn.close()

# ---------------- Update data ----------------


# sql = 'update student set fees=20000 where stuid=3'
# myc = conn.cursor()
# try:
#     myc.execute(sql)
#     conn.commit()
#     print(myc.rowcount, 'Update')
# except:
#     conn.rollback()
#     print('Unable to Update data')

# myc.close()
# conn.close()

# --------------- fetchon() method --------------


# sql = 'select * from student'
# sql = 'select name,roll from student'
# myc = conn.cursor()
# try:
#     myc.execute(sql)
#     row = myc.fetchone()
#     while row is not None:
        # stuid = row[0]
        # name = row[1]
        # roll = row[2]
        # fess = row[3]
        # print(row)
        # print(f'Stuid : {stuid} Name : {name} Roll : {roll} Fees : {fess}')
#         row = myc.fetchone()
#     print(myc.rowcount, 'Total rows')
# except:
#     conn.rollback()
#     print('Unable to show data')
# myc.close()
# conn.close()

# ---------------------- fetchall() ------------------------



# sql = 'select * from student'
# myc = conn.cursor()
# try:
#     myc.execute(sql)
#     rows = myc.fetchall()
#     for r in rows:
#         print(r)
#     print('Total rows :',myc.rowcount)
# except:
#     conn.rollback()
#     print('Unable to show data')

# myc.close()
# conn.close()

# ------------------- Fetchmany() -------------------------

# sql = 'select * from student'
# myc = conn.cursor(buffered=True)
# try:
#     myc.execute(sql)
#     rows = myc.fetchmany(size=3)
#     for r in rows:
#         print(r)
#     print('Total rows :',myc.rowcount)
# except:
#     conn.rollback()
#     print('Unable to show data')

# myc.close()
# conn.close()

# --------------- Where Clause -------------------------


sql = 'select * from student where stuid=5'
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print('Total rows :',myc.rowcount)
except:
    conn.rollback()
    print('Unable to show data')

myc.close()
conn.close()

