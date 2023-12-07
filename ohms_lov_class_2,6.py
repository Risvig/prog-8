from math import sqrt

class OhmsLov:
    
    def __init__(self, current=None, power=None, resistance=None, voltage=None):
        self.current = current
        self.power = power
        self.voltage = voltage
        self.resistance = resistance
        
     # current   
    def current_calc(self):
        current = self.voltage / self.resistance
        print(current)
    
    def current_calc1(self):
        current = sqrt(self.power / self.resistance)
        print(current)
    
    def current_calc2(self):
        current = self.power / self.voltage
        print(current)
    
    # resistance
    def resistance_calc(self):
        resistance = self.voltage / self.current
        print(resistance)
    
    def resistance_calc1(self):
        resistance = self.power / self.current**2
        print(resistance)
    
    def resistance_calc2(self):
        resistance = self.voltage**2 / self.power
        print(resistance)
    
    # voltage
    def voltage_calc(self):
        voltage = self.power / self.current
        print(voltage)
    
    def voltage_calc1(self):
        voltage = sqrt(self.power / self.resistance)
        print(voltage)
    
    def voltage_calc2(self):
        voltage = self.voltage / self.resistance
        print(voltage)
    
    # power
    def power_calc(self):
        power = self.voltage * self.current
        print(power)
        
    def power_calc1(self):
        power = self.voltage**2 / self.resistance
        print(power)
    
    def power_calc2(self):
        power = self.resistance * self.current**2
        print(power)


# Define values
power = 10
resistance = 2000
voltage = 5
current = 2

calc = OhmsLov(power, resistance, voltage, current)

# Uncomment and run the desired calculation
# calc.current_calc()
# calc.current_calc1()
# calc.current_calc2()
calc.resistance_calc()
# calc.resistance_calc1()
# calc.resistance_calc2()
# calc.voltage_calc()
# calc.voltage_calc1()
# calc.voltage_calc2()
# calc.power_calc()
# calc.power_calc1()
# calc.power_calc2()