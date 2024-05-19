import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",5551))

conn=True
while conn:
    msg = input("Enter Your Message : ")
    client.send(msg.encode('utf-8'))
    if msg=='no':
        conn=False
        client.close()