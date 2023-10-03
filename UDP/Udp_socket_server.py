from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from sys import exit

server_port = 12000 # porten du sender til
server_socket = socket(AF_INET, SOCK_DGRAM) # vælg udp og ip

server_socket.bind(('',server_port))
print('server is ready to recive')

while True:
    try:
        message, client_address =server_socket.recvfrom(2048) #lyt efter en besked på port 2048 og lav den in til en variabel som heder message
        modified_message = message.decode() # lav beskeden du fik om til en string
        
        server_socket.sendto(modified_message.encode(),client_address) # send en besked til den ip og port hvor den siste besked kom fra
        if modified_message != '':
            print(modified_message)
            modified_message = ''
    except KeyboardInterrupt:
        client_socket.close()
        exit()