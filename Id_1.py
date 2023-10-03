from neopixel import NeoPixel
from machine import Pin
from time import sleep
import umqtt_robust2 as mqtt

n = 12 #number of pixels
p = 26 #pin acchachet to ring 
np = NeoPixel(Pin(p, Pin.OUT), n)

def set_led(r ,g ,b):  #set alle led'er til den samme fave som angivet med rød, grøn og blå
    for light in range (n):
        np[light] = (r, g, b) #coler in 8 bit range 0 til 255
        np.write()

rød = 0
grøn = 0
blå = 0
styrke = 1
nr_list = ('1','2','3','4','5','6','7','8','9','0')


while True:
    if len(mqtt.besked) > 1:
        if mqtt.besked[0] == '#': #set en fave med adafrute
            rød = (int(mqtt.besked[1:3],16)/100)
            grøn =(int(mqtt.besked[3:5],16)/100)
            blå = (int(mqtt.besked[5:7],16)/100)
            set_led(int(rød*styrke),int(grøn*styrke),int(blå*styrke))
    
    if len(mqtt.besked) > 0: #sæt styreken med adafrute
        if mqtt.besked[0] in nr_list:
            styrke = int(mqtt.besked)
            set_led(int(rød*styrke),int(grøn*styrke),int(blå*styrke))
    
    if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
        mqtt.besked = ""
         
    mqtt.sync_with_adafruitIO() 