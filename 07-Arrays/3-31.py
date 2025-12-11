# array = [[-38, 19], [5,40],[-7,11],[29,16]]
# lista = []
# counter = 1
# highest_val = [0,0]
# for row in array:
#     if row[0]<row[1]:
#         row[0], row[1] = row[1], row[0]
#         maximum = max(row)
#         highest_val = [counter,2]
#     else:
#         highest_val = [counter,1]

    
#     counter +=1
#     if maximum < row[0]:
#         maximum = row[0]
#     elif maximum < row[1]:
#         maximum = row[1]

    

# print(array)
# print(maximum)
# print(highest_val)


array = [[-38, 19], [5,40],[-7,11],[29,16]]

max_row = 0
max_column = 0

min_row = 0
min_column = 0



for i in range(len(array)):
    for j in range(len(array[i])):

        if array[i][j] > array[max_row][max_column]:
            max_row = i
            max_column = j

print(array[max_row][max_column])
print(max_row+1,",",max_column+1)


for i in range(len(array)):
    for j in range(len(array[i])):

        if array[i][j] < array[min_row][min_column]:
            min_row = i
            min_column = j

print(array[min_row][min_column])
print(min_row+1,",",min_column+1)


