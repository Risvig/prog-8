from machine import ADC, Pin
from time import sleep

class LMT84:
    #Class to measure in celsius, fahrenheit and kelvin units
    def __init__(self,pin_number=35, ADC2_mV = 2048 / 4095, alpha = -5.5, beta = 1035, average = 128,):
        self.pin_number = pin_number
        self.lmt84_ADC = ADC(Pin(pin_number))
        self.ADC2_mV = ADC2_mV
        self.lmt84_ADC.atten(ADC.ATTN_6DB)
        self.alpha = alpha
        self.beta = beta
        self.average = average
        #Temp unit attributes
        self.temperature_celsius = None
        self.temperature_fahrenheit = None
        self.temperature_kelvin = None
 
    def set_temperature_celsius(self):
        ADC_value = 0
        if self.average > 1:
            for i in range (self.average):
                ADC_value += self.lmt84_ADC.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.lmt84_ADC.read()
            sleep(1)

        mV = self.ADC2_mV * ADC_value
        temp = (mV - self.beta) / self.alpha
        return temp
    
    def set_temperature_fahrenheit(self):
        self.set_temperature_celsius()
        self.celsius_to_fahrenheit = self.set_temperature_celsius() * (9/5) + 32
        return self.celsius_to_fahrenheit
 
 
    def celsius_to_kelvin(self):
        self.set_temperature_celsius()
        self.celsius_to_kelvin = self.set_temperature_celsius() + 273.15
        return self.celsius_to_kelvin
 
lmt84 = LMT84()
lmt84.set_temperature_celsius()
print()
print(lmt84.set_temperature_celsius())
print(lmt84.set_temperature_fahrenheit())
print(lmt84.celsius_to_kelvin())
