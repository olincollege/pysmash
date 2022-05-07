#one client method
import socket, pickle

class NetworkDataPOne:
       position = 0
       velocity = 0
       jump = 0
       knockback = 0
       attack = '' 

class NetworkDataPTwo:
       position = 0
       velocity = 0
       jump = 0
       knockback = 0
       attack = '' 

# HOST = '27.0.1.0'
# PORT = 62301
# BUFFER = 2048
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(BUFFER)
#             data_variable = pickle.loads(data)
#             if not data:
#                 break
#             conn.sendall(data)
#     s.close()


## multithread method


import socket
import os
from _thread import *


ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
buffer = 2048
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen()
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(buffer)
        data_variable = pickle.loads(data)
        data_variable.process_id
        response = 'Server message: ' + data.decode('utf-8')
        variable = NetworkDataPTwo()
        data_string = pickle.dumps(variable)
        ServerSideSocket.send(data_string)
        connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()




