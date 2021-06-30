import socket

def server(addr, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((addr, port))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        print(client_socket, addr)


def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)

print('Outside inner while loop')
client_socket.close()


server('localhost', 5000)