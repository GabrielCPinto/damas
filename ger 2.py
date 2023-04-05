import socket
import random
import time

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 5000


print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    ClientMultiSocket.send(str.encode('message2'))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))

ClientMultiSocket.close()
