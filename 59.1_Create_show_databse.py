# # import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         user='root',
#         password='#MySql1899',
#         host='localhost',
#         port=3306)
#     if(conn.is_connected()):
#         print('Connected')
# except:
#     print('Unable to connect')
# # print('Before Close :', conn.is_connected())
# # conn.close()
# # print('After Close :', conn.is_connected())

# sql = 'show databases'
# myc = conn.cursor()
# myc.execute(sql)
# for d in myc:
#     print(d)

# myc.close()
# conn.close()

# # -------------------------------------------------

