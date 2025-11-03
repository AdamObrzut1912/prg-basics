###
#Program that checks whether the speed is valid
#
speed = int(input("Enter the speed: "))
valid_speed = speed >= 40 and speed <= 140
print(f"Speed is valid: {valid_speed}")