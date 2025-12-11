arr1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

def inc(arr):
    counter = 0
    for i in range(len(arr)):
        counter = (i+1)
        for j in range(len(arr[i])):
            counter = (i+1)*(j+1)
            arr[i][j] = counter
            
            
    for row in arr:
        for item in row:
            print(item, end=" ")
        print()
          
inc(arr1)