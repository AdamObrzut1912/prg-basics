arr1 = [1,56,3,43,32,2,9]
arr2 = [3,5645,3,2,657,322]
arr3 = [32,654,234,2,78,31243,21]

def sort_bubble(arr):
    len_arr = len(arr)
    for i in range(len_arr-1):
        for y in range(len_arr-1-i):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1],arr[y]

    return arr

print(sort_bubble(arr1))