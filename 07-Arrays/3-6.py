arr = [15,8,31,47,2,19]
arr_len = len(arr)
sum = 0
i = 0
while True:
    sum += arr[i]
    i += 1
    if i == arr_len:
        break

arithmetic_mean = sum / arr_len
print(arr)
print(arithmetic_mean)