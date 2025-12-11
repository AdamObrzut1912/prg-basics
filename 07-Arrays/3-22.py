import random
def random_el(arr, random):
    
    return arr[random]

arr1 = [2,5,34,2,5,7,4,2,43]

randomNum1 = random.randint(0,len(arr1))
randomNum2 = random.randint(0,len(arr1))
randomNum3 = random.randint(0,len(arr1))

print(random_el(arr1, randomNum1))
print(random_el(arr1, randomNum2))
print(random_el(arr1, randomNum3))