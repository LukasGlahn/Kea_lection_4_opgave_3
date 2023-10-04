from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from machine import PWM
from sys import exit
from machine import Pin
import random

BUZZ_PIN = 26
buzzer_pin = Pin (BUZZ_PIN, Pin.OUT)
pwm_buzz = PWM (buzzer_pin)


def buzzer (buzzer_PWM_object, frequency, sound_duration, silence_duration):
    buzzer_PWM_object.duty(512)
    buzzer_PWM_object.freq(frequency)
    sleep(sound_duration)
    buzzer_PWM_object.duty(0)
    sleep(silence_duration)

buzzer(pwm_buzz, 100, 0.2, 0.01)

noter = (262, 294, 330, 349, 392, 440, 494)

server_port = 12000 # porten du sender til
server_socket = socket(AF_INET, SOCK_DGRAM) # vælg udp og ip

server_socket.bind(('',server_port))
print('server is ready to recive')

while True:
    try:
        message, client_address =server_socket.recvfrom(2048) #lyt efter en besked på port 2048 og lav den in til en variabel som heder message
        modified_message = message.decode() # lav beskeden du fik om til en string
        
        server_socket.sendto(modified_message.encode(),client_address) # send en besked til den ip og port hvor den siste besked kom fra
        if modified_message == 'spil random toner':
            print(modified_message)
            for i in range (3):
                tone = random.choice(noter)
                buzzer(pwm_buzz, tone, 0.2, 0.2)
            modified_message = ''
    except KeyboardInterrupt:
        client_socket.close()
        exit()