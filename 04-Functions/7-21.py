
def f(number1,number2,number3):
    minimal = min(number1,number2,number3)
    maximum = max(number1,number2,number3)

    diff = minimal - maximum
    return abs(diff)

print(f(7,4,9))
print(f(2,12,8))
