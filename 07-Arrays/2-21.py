def subset(arr1, arr2):
    counter = 0
    result = ""
    for el1 in arr1:
        if el1 in arr2:
            counter += 1

    if counter == len(arr1):
        result = f"{arr1} is a subset of {arr2}"

    return result

print(subset([0,1,2], [0,1,2,4,5,6,]))