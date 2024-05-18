import mysql.connector

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

    sql = 'insert into student(name,roll,fees) values (%s,%s,%s)'
    myc = conn.cursor()

    n = nm
    r = ro
    f = fe

    params = (n,r,f)

    try:
        myc.execute(sql,params)
        conn.commit()
    except:
        conn.rollback()
        print('Unable to insert data')

    myc.close()
    conn.close()

while True:
    nm = input('Enter Your Name :')
    ro = int(input('Enter roll :'))
    fe = float(input('Enter fees :'))
    student_data(nm,ro,fe)
    ans = input("Do you want to exit? (y/n)")
    if (ans=='y'):
        break

