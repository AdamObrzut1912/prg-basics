###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temp_celcius = int(input("Enter the temperature in celcius")) #typing the temperature to calculate
temp_f = (temp_celcius * 1.8 +32)
temp_cal = (temp_celcius + 273.15)

print(f"{temp_celcius} in Fahrenheit is {temp_f}")
print(f"{temp_celcius} in Calvins is {temp_cal}")