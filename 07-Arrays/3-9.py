def compare(array1, array2):
    counter = 0
    for i in array1:
        for y in array2:
            if i == y:
                counter += 1
    if len(array1) == len(array2) and counter == len(array1):
        return True
    else:
        return False
    
    
print(compare(["water", "book", "sky"], ["water", "book", "sky"]))
print(compare([5,3,1], [5,3,1]))
print(compare([3,2,1], [3,2]))
print(compare([True, False], [True, False, True]))