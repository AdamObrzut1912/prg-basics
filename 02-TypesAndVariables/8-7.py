###
# Progrma converting numerical systems from decimal
# to binary and hexadecimal
num_dec = int(input("Enter the number in decimal system: "))
num_bin = bin(num_dec)
num_hex = hex(num_dec)
print(f"{num_dec} in decimal system is equal {num_bin} in binary system")
print(f"{num_dec} in decimal system is equal {num_hex} in hexadecimal system")