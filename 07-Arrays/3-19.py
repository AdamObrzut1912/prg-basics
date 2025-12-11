arr1 = [2,5,3,2,6,5,3,0,5,3]

number = int(input("Podaj iliczbę"))

graterNumbers = 0

for i in arr1:
    if i > number:
        graterNumbers += 1

print(graterNumbers)