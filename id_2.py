from neopixel import NeoPixel
from machine import Pin
from time import sleep

PB1_PIN = 4
pb1 = Pin(PB1_PIN, Pin.IN)

n = 12 #number of pixels
p = 26 #pin acchachet to ring 
np = NeoPixel(Pin(p, Pin.OUT), n)
light_nr = -1

def led_step(r,g,b):# for hver gang fungtionen er kallet flyt den tænde led en gang
    global light_nr
    for i in range (n):
        np[i] = (0,0,0) # sluk alle lederne for at gøre klar til den næste bliver tænt
    np.write()
    if light_nr > n-2: #hvis numerd bliver højer end mænkten af leder i index sæt den til -1 som bliver til 0 på indxset nå koden køre frem
            light_nr = -1
    light_nr = light_nr + 1
    np[light_nr] = (r,g,b) # set den led vi nåde til faven som var valdt nå fungtionen er kallet
    np.write()

while True:
    first = pb1.value()
    sleep(0.05)
    second = pb1.value()
    
    if first > second: #hvis knappen er trykket kør vores led_step fungtion 1 gang
        led_step(80,0,0)