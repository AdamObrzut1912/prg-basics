###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
print("Podaj długości prostopadłościanu")
a = float(input('Podaj wysokość: a= '))
b = float(input("Podaj 1 z długości  podstawy b= "))
c = float(input("Podaj 2 z długości podstawy c= "))

cuboid_volume = a*b*c
cuboid_surface_area = 2*a*b + 2*a*c + 2*b*c
print(f'objętość prostopadłościanu dla wartości {a}, {b}, {c} to {cuboid_volume}')
print(f'pole powierzchni bocznej prostopadłościanu dla wartości {a}, {b}, {c} to {cuboid_surface_area}')