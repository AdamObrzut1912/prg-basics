def f(arr2D):
    column_sum = 0
    row_sum = 0
    is_true = True
    for i in range(len(arr2D)):
        
        for j in range(len(arr2D[i])):
            column_sum += arr2D[j][i]
            row_sum += arr2D[i][j]

        if column_sum == row_sum:
            row_sum = 0
            column_sum = 0
        else:
            is_true = False
            return is_true
    return is_true


print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))

