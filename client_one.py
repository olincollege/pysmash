import socket,pickle

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server

class NetworkDataPOne:
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


ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
data = []
while True:
    packet = ClientMultiSocket.recv(4096)
    if not packet: break
    data.append(packet)
data_arr = pickle.loads(b"".join(data))
print (data_arr)
# data = ClientMultiSocket.recv(2048)
# if not data: 
#     break
# packet += data
# data_arr = pickle.loads(packet)
# print (data_arr)
# data_arr.process_id
while True:
    variable = NetworkDataPOne()
    data_string_one = pickle.dumps(variable)
    ClientMultiSocket.send(data_string_one)
    ClientMultiSocket.close()
