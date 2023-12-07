from machine import Pin
import time

class BlinkLED():
    def __init__(self, pin, period):
        self.led = Pin(26, Pin.OUT)
        self.period = period
        self.start_timer = time.ticks_ms()

    def blink_led(self):
        current_time = time.ticks_ms()
        if current_time - self.start_timer >= self.period:
            self.led.value(not self.led.value())
            self.start_timer = current_time

led_blinker = BlinkLED(2, 300)

while True:
    led_blinker.blink_led()
    time.sleep(2)
