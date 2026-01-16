def f(arr):
    arr.sort()

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            return arr[i]

print(f([7,7,7,7,7,7,5]))