import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

while True:
    m = input('enter message: ')
    if m == 'exit':
        break
    clientsocket.send(m.encode())