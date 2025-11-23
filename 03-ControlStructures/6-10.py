# A program that calculates dog's age in dog's years
age = float(input("Enter dog's age"))
age_in_dogs_years = 0
if age > 2:
    age_in_dogs_years = 2*10.5 + (age-2)*4
else:
    age_in_dogs_years = age * 10.5

print(f"{age} in dog's years is {age_in_dogs_years}")