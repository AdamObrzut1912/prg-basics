###
# Calculates the sum of the digits in a number
#
import math

total = 0
def sum_digits(number):
    number = abs(number)
    number_char = str(number)

    for char in number_char:
        total = total + int(char)

    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')