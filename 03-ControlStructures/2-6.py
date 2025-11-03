###
# Program checking wether the number is positive or negative
#
num = int(input("Enter the number: "))

if num > 0:
    print(f'Number {num} is positive')
if num == 0:
    print(f'Number is 0')
if num < 0:
    print(f'Number {num} is negative')