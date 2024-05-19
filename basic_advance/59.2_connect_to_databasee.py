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

conn.close()