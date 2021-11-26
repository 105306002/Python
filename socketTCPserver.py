# -*- coding: utf-8 -*


import socket 
import datetime


HOST = '0.0.0.0'
PORT = 3434

#AF_INET 說明使用Ipv4 SOCK_STREAM指名TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr = s.accept() #接收TCP連接，並回傳新的socket物件
    addr = str(addr) #用戶端IP地址
    print('Clinet {} connected!'.format(addr))

    dt = datetime.datetime.now()
    message = "Current time is " + str(dt)
    conn.send(message)
    print("Sent", message)
    conn.close() 

