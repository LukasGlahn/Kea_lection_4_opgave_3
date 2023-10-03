from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from sys import exit

server_port = 1200
server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('',server_port))
print('server is ready to recive')

while True:
    try:
        message, client_address =server_socket.recvfrom(2048)
        modified_message = message.decode()
        
        server_socket.sendto(modified_message.encode(),client_address)
        if modified_message != '':
            print(modified_message)
            odified_message = ''
    except KeyboardInterrupt:
        client_socket.close()
        exit()