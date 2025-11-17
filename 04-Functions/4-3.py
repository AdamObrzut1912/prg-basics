###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    
    p = ((a+b+c)/2)
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

side1 = int(input("Ente the lenght of first side: "))
side2 = int(input("Ente the lenght of second side: "))
side3 = int(input("Ente the lenght of third side: "))

t_area = triangle_area(side1, side2, side3)

print(f'The area of ​a triangle with sides {side1}, {side2}, {side3} is {t_area}')
