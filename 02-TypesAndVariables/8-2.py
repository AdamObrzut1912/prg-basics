###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results
import math

radius = int(input("enter a radius: "))
pi = math.pi
area = round(pi*(radius**2),2)
circumference = round((2*pi*radius),2)


print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")