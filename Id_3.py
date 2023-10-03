from machine import Pin, ADC
from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms, sleep

PB1_PIN = 4
pb1 = Pin(PB1_PIN, Pin.IN)
pot = ADC(Pin(34, Pin.IN),atten=3)
pot.width(10)

n = 12 #number of pixels
p = 26 #pin acchachet to ring 
np = NeoPixel(Pin(p, Pin.OUT), n)
light_nr = -1
pb1_pushed = 1
off = 0

def led_step(r,g,b): # for hver gang fungtionen er kallet flyt den tænde led en gang
    global light_nr
    for i in range (n):
        np[i] = (0,0,0)
    np.write()
    if light_nr > n-2:
            light_nr = -1
    light_nr = light_nr + 1
    np[light_nr] = (r,g,b)
    np.write()


while True:
    first = pb1.value()
    sleep(0.05)
    second = pb1.value()
    
    if first > second: # hvis knappen er trykket forbered værdiger der skal buges i looped og så start looped
        loop_full_start = 0
        pb1_pushed = 0
        while True:
            pot_val = pot.read()
            led_step(80,0,0) 
            #sov i den tid som potentiometerts værdi er og chek hvet 20 ms om kbappen er blevet trykket
            for time in range (0, pot_val, 20):
                if pb1.value() == 0 and loop_full_start == 1: # hvis knappen er blevet trykket stop looped og giv off en værdig af 1 for at ende det ydre loop
                    off = 1
                    break
                sleep_ms(20)
            #stop koden vis knapen er trykket
            if off == 1: # hvis knappen er tryket i for looped oven over stop looped
                off = 0
                break
            if pb1.value() == 0 and loop_full_start == 1: #stop looped hvis knappen er slukket 
                break
            
            if pb1.value() == 0 and pb1_pushed == 0: # sør for at knappen har været sluppet før den kan lave noget input i fungtionen der stopper looped
                ...
            else:
                loop_full_start = 1
                pb1_pushed = 0
  