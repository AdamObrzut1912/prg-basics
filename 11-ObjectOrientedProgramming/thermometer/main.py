import prog
import random
import math

def main():
    temp = round(random.uniform(34.0,42.0),1)
    thermometer1 = prog.Thermometer()
    thermometer1.turn_on()
    thermometer1.temp_measure(temp)
    thermometer1.display_temp()
    thermometer1.turn_off()

if __name__ == "__main__":
   main() 