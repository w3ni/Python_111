# Creating Connection

import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='#MySql1899',
        host='localhost',
        port=3306)
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable to connect')
print('Before Close :', conn.is_connected())
conn.close()
print('After Close :', conn.is_connected())

# --------------------------------

# config = {
#     'user' : 'root',
#     'password' : '#MySql1899',
#     'port' : 3306
# }

# try:
#     conn = mysql.connector.connect(**config)
#     # print(conn.is_connected())
#     if(conn.is_connected()):
#         print('Connected')
# except:
#     print('Unable to connect')
