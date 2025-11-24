###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
arr1 = ""

print(arr)
print(0, len(arr))# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print(0, len(arr))
print(arr[0])
print(arr[len(arr)-1])
...
...
print(arr[0] + arr[len(arr)-2])

print(len(arr)//2)

for i in range(0, len(arr)):
    arr1 = arr1 + " " + str(arr[i])

print(arr1)