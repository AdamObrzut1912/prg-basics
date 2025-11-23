car_speed = int(input("Enter the car speed"))
speed_limit_min = 40
speed_limit_max = 140

if car_speed > speed_limit_min and car_speed < speed_limit_max:
    print("Speed is valid")
else:
    print("Speed is invalid")