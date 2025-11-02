#
### Program that comunicates if diced number is special
# and print the diced number
import random

num = random.randint(1,6)
num_special = num == 6 or num == 1
print(f"Dice rolled {num}")
print(f"Dice rolled special: {num_special}")

