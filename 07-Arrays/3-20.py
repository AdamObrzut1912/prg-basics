arr = [7,9,2,4,5,6]
even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()

arr.clear()
arr.extend(even)
arr.extend(odd)

print(arr)