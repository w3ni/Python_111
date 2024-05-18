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

    sql = 'insert into student (name,roll,fees) values (%s, %s, %s)'
    myc = conn.cursor(prepared=True)
    # params = ('RRR', 111, 49455.45)
    # seq_of_params = [

    #     ("Nidhi",333,353.5),
    #     ("Rony",434,667.355)
    # ]
    # nm = input('Enter your name :')
    # ro = int(input('Enter your roll :'))
    # fe = float(input('Enter fee'))

    n = nm
    r = ro
    f = fe
    params = (n,r,f)
    try:
        # myc.executemany(sql,seq_of_params)
        myc.execute(sql,params)
        conn.commit()
        print(myc.rowcount, ' Row Insertd')
        print(f'Stu ID :, {myc.lastrowid} Inserted')

    except:
        conn.rollback()
        print('Unable to insert data')
    myc.close()
    conn.close()

while True:
    nm = input('Enter your name :')
    ro = int(input('Enter your roll :'))
    fe = float(input('Enter fee'))
    student_data(nm,ro,fe)
    ans = input('do you want to exit y/n')
    if (ans=='y'):
        break