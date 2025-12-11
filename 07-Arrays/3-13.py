def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
userNum = int(input("Podaj numer"))
arr = [15,38,7,23,14]
if occurs(userNum, arr) == True:
    print(f"Number {userNum} in the array: {arr}")