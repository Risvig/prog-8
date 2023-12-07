from machine import TouchPad, Pin
from time import sleep, ticks_ms

RED_PIN = 26
led1=Pin(RED_PIN, Pin.OUT)

YELLOW_PIN = 12
led2=Pin(YELLOW_PIN, Pin.OUT)

GREEN_PIN = 13
led3=Pin(GREEN_PIN, Pin.OUT)

######

touch1 = TouchPad(Pin(0, Pin.IN))
start_time = ticks_ms()
led_blink = 500
led_blink2 = 1000

#####

while True:
    if touch1.read() < 170:
        if ticks_ms() - start_time > led_blink:
            led1.on()
            led2.off()
            led3.on()
            print("LED blinker")
            sleep(0.5)
            
        if ticks_ms() - start_time > led_blink2:
            led1.off()
            led2.on()
            led3.off()
            start_time = ticks_ms()
            print("LED slukker")


            
            
        
        
        