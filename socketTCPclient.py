# -*- coding: utf-8 -*

import socket
HOST='127.0.0.1'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
print("Connect %s %d OK" % (HOST, PORT))
data = s.recv(1024) #接收資料，本次接收資料的最大長度為1024
print("Received:",data)
s.close()

#client 端得通訊port 由系統自動分配
