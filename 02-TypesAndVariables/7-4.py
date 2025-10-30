###
#Program that checks if the tree can be cutted down
#
import math
circumference = int(input("Enter the circumference of the tree: "))
can_be_cutted = (circumference/math.pi) > 50
print(f"Tree can be cut down {can_be_cutted}")