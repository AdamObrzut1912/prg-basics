# Program that determinates in which quadrant is are the entered coordinates
x = int(input(f"Enter a first coordinate: "))
y = int(input(f"Enter a second coordinate: "))

if x == 0 or y == 0:
    print(f"Point({x},{y}) is in one of the axes")
elif x > 0 and y > 0:
    print(f"Point({x},{y}) is in first quadrant of the coordinate system: ")
elif x < 0 and y > 0:
    print(f"Point({x},{y}) is in second quadrant of the coordinate system: ")
elif x < 0 and y < 0:
    print(f"Point({x},{y}) is in third quadrant of the coordinate system: ")
elif x > 0 and y < 0:
    print(f"Point({x},{y}) is in fourth quadrant of the coordinate system: ")
else:
    print("You did something wrong")