from machine import Pin
from dht import DHT11
from time import sleep

dht11 = DHT11(Pin(0, Pin.IN))
dht11.measure()

temperature = dht11.temperature()
humidity = dht11.humidity()

while True:
    print("temp is", temperature)
    print("humidity is", humidity)
    sleep(10)