import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.10.11.5', 5000)
sock.bind(server_address)
sock.listen(1)
while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.sendall(data)
    connection.close()
