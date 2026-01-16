def f(array):
    row_num = 0
    col_num = 0
    min_val = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < min_val:
                min_val = array[i][j]
                row_num = i
                col_num = j
    if row_num == col_num:
        return True
    else:
        return False
                
print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))
                