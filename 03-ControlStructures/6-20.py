# A program that convers decimal number to binary
decimal = input("Enter a decimal number: ")
decimal_int = int(decimal)
binary = ''

while decimal_int != 0:
    binary = str(decimal_int % 2) + binary
    decimal_int = decimal_int // 2
print(f"{decimal}(10) = {binary}(2)")
   