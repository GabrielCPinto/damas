import socket
import os
import random
from _thread import *
from queue import Queue
import time
from datetime import datetime


ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 49996
q_pi = []
retorno1 = 0
retorno2 = 0


def attack():
    if (retorno1 == retorno2):
        return 1
    return 0


try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening...')
ServerSideSocket.listen()


def multi_threaded_client(connection, address):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(1024)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break

        connection.sendall(str.encode(response))
    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    chance = random.randint(0, 10)
    if (chance <= 2):
        print('confirmado')
    if (retorno1+retorno2 >= 180):
        print('sucesso')
    else:
        print('falhou')

    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, address))
    print()

ServerSideSocket.close()
