arr = [-15,8,-31,47,-2,19]
minimum = 0
maximum = 0

for i in range(0,len(arr)-1):
    if arr[i] < minimum:
        minimum = arr[i]
    else:
        continue

for i in range(0,len(arr)-1):
    if arr[i] > maximum:
        maximum = arr[i]
    else:
        continue

print(minimum)
print(maximum)
