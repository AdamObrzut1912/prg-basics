# A program that shows as few coins as possible
money = input("Enter the amount in PLN")
counter = int(money)
coin_5 = 0
coin_2 = 0
coin_1  = 0

while counter > 0:
    if counter  >= 5:
        coin_5 += 1
        counter = counter - 5
    elif counter >= 2:
        coin_2 += 1
        counter = counter - 2
    elif counter >= 1:
        coin_1 += 1
        counter -= 1
print(f"5 PLN coin: {coin_5}")
print(f"2 PLN coin: {coin_2}")
print(f"1 PLN coin: {coin_1}")