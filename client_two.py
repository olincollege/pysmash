# import socket,pickle

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server

# class NetworkDataPTwo:
#        position = 0
#        velocity = 0
#        jump = 0
#        knockback = 0
#        attack = 'true'
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     variable = NetworkDataPTwo()
#     data_string = pickle.dumps(variable)
#     s.send(data_string)
#     s.close

import socket,pickle

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server

class NetworkDataPTwo:
       position = 0
       velocity = 0
       jump = 0
       knockback = 0
       attack = 'true'
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     variable = NetworkDataPOne()
#     data_string = pickle.dumps(variable)
#     s.send(data_string)
#     s.close


# ClientMultiSocket = socket.socket()
# host = '127.0.0.1'
# port = 2004
# print('Waiting for connection response')
# try:
#     ClientMultiSocket.connect((host, port))
# except socket.error as e:
#     print(str(e))
# data = ClientMultiSocket.recv(1024)
# data_variable = pickle.loads(data)
# data_variable.process_id
# while True:
#     variable = NetworkDataPTwo()
#     data_string_two = pickle.dumps(variable)
#     ClientMultiSocket.send(data_string_two)
#     ClientMultiSocket.close()

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
data = ClientMultiSocket.recv(1024)
data_variable = pickle.loads(data)
print(data_variable)
data_variable.process_id
while True:
    variable = NetworkDataPTwo()
    data_string_two = pickle.dumps(variable)
    ClientMultiSocket.send(data_string_two)
    ClientMultiSocket.close()