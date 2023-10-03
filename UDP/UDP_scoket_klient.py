from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from sys import exit

server_name = input('input IP addresse of ESP32\n')
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    try:
        message = input('Write a mesege to send\n')
        
        client_socket.sendto(message.encode(), (server_name, server_port)) #brug den her til at sende en besked ud til en port beskeden er den der heder message og .encode gør den klar
        
        modified_message, server_address = client_socket.recvfrom(2048) #modtag en besked på port 2048 og lav en variabel som heder modified_message med beskeden i binær brug .decode() til at lave det om til en nomal besked
        print(modified_message.decode())
    except KeyboardInterrupt:
        client_socket.close()
        exit()
