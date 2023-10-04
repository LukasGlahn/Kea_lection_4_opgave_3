from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from time import ticks_ms
from machine import PWM
from gpio_lcd import GpioLcd
from sys import exit
from machine import Pin

lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
              d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20)

pb1 = Pin(4, Pin.IN)

server_port = 12000 # porten du sender til
server_socket = socket(AF_INET, SOCK_DGRAM) # vælg udp og ip

server_socket.bind(('',server_port))
beskeder_sent = 0
print('server is ready to recive')

while True:
    try:
        if beskeder_sent < 4:
            message, client_address =server_socket.recvfrom(2048) #lyt efter en besked på port 2048 og lav den in til en variabel som heder message
            modified_message = message.decode() # lav beskeden du fik om til en string
            
            server_socket.sendto(modified_message.encode(),client_address) # send en besked til den ip og port hvor den siste besked kom fra
        if beskeder_sent >= 4 and pb1.value() == 0:
            beskeder_sent = 0
            print('beskeder kommer igen')
        if modified_message != '':
            print(modified_message)
            lcd.clear() #clear den siste besked fra lcdet
            lcd.putstr(modified_message)
            modified_message = ''
            beskeder_sent = beskeder_sent + 1
    except KeyboardInterrupt:
        client_socket.close()
        exit()