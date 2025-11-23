#A program that convers 24-hour format into 12-hour format
time_24 = (input("Enter time (24-hour format):"))
char = time_24.find(":")
hour = time_24[:char]
minutes = time_24[char+1:]

hour_change = {
    13:1,
    14:2,
    15:3,
    16:4,
    17:5,
    18:6,
    19:7,
    20:8,
    21:9,
    22:10,
    23:11,
}
if int(hour) <= 12:
    print(f"Time in 12-hour format:{hour}:{minutes}pm")
elif int(hour) > 12 or int(hour) <= 24:
    print(f"Time in 12-hour format:{hour_change[int(hour)]}:{minutes}am")
