import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections

while True:
    print('server start')
    connection, address = serversocket.accept()
    print('client connected')
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf)
        # breakimport socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send(b'hello')