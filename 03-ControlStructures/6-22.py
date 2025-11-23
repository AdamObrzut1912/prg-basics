# printing program

count = ''

for i in range(1,30):
    if i % 5 == 0 and i % 3 == 0:
        count = count + "BINGO "
    elif i % 5 == 0:
        count = count + "FIVE "
    elif i % 3 == 0:
        count = count + "THREE "
    else:
        count = count + str(i) + " "
print(count)