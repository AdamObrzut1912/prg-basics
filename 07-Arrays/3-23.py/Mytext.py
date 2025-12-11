def numWords(text):
    text_splited = text.split(" ")
    
    return len(text_splited)

def order_arr_num(arr):
    arr_splited = arr.split(" ")
    sorted_arr = sorted(arr_splited, key=len, reverse = True)
    result = ",".join(sorted_arr)

    return result

def order_arr_alph(arr):
    arr_splited = arr.split(" ")
    sorted_arr = sorted(arr_splited)
    result = ",".join(sorted_arr)
    return result



