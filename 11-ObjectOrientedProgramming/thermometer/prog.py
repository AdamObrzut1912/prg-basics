class Thermometer():
    def __init__(self):
        self.state = False


    def turn_on(self):
        self.state = True
        print("Thermometer tured on")
    
    def turn_off(self):
        self.state = False
        print("Thermometer tured off")

    
    def temp_measure(self, temp):
        self.temp = temp

    def display_temp(self):
        if self.temp > 41:
            print(f"Temperature {self.temp} CRITICAL TEMPERATURE")
        elif self.temp > 37:
            print(f"Temperature {self.temp} (fever)")
        else:
            print(f"Temperature {self.temp}")
        
    