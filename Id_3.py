from machine import Pin, ADC
from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

PB1_PIN = 4
pb1 = Pin(PB1_PIN, Pin.IN)
pot = ADC(Pin(34, Pin.IN),atten=3)
pot.width(11)

n = 12 #number of pixels
p = 26 #pin acchachet to ring 
np = NeoPixel(Pin(p, Pin.OUT), n)
light_nr = -1

def led_step(r,g,b):
    global light_nr
    for i in range (n):
        np[i] = (0,0,0)
    np.write()
    if light_nr > 10:
            light_nr = -1
    light_nr = light_nr + 1
    np[light_nr] = (r,g,b)
    np.write()

while True:
    pot_val = pot.read()
    led_step(80,0,0)
    sleep_ms(pot_val)