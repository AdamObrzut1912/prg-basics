###
# a program that calculates the distance to the horizon from a height given in meters from the keyboard
#

import math

height = float(input("Give me a height in meters: "))

v = 3.57

d = v * math.sqrt(height)
print(d)

