import math
def secondLargest(arr):
    sorted_array = sorted(arr)

    return sorted_array[-2]

def diff_larg_low(arr):
    minimum = min(arr)
    maximum = max(arr)

    diff = maximum - minimum
    return diff

def median(arr):
    sorted_arr = sorted(arr)
    mediana = sorted_arr[math.floor(len(arr)/2)]
    return mediana

def larg_lowe(arr):
    minimum = min(arr)
    maximum = max(arr)

    return [minimum,maximum]

def str_arr(arr):
    string = ""

    for i in arr:
        string = string + str(i)

    expression = ("-".join(string))
    return expression


