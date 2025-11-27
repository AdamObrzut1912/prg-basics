def time_string(hours, minutes, time_format):
    
    if time_format == '24':
        time = f"The time is {hours}:{minutes}"
    elif time_format == '12':
        if hours < 12:
            time = f"The time is {hours}:{minutes}am"
        elif hours <= 23: 
            time = f"The time is {hours-12}:{minutes}pm"
        elif hours == 0:
            time = f"The time is 12:{minutes}am"
    return time

print(time_string(15, 38, '12'))
print(time_string(8, 3, '24'))
print(time_string(00, 5 ,'24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))
