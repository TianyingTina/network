import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.10.11.5', 5000)
sock.connect(server_address)

while True:
    #Send data
    message = "This is the message from client."
    sock.sendall(message)
    
    #Look for response
    rsp = sock.recv(1024)
    print(rsp)

sock.close()
