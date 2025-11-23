### A program that calculates a parking fee
hours = int(input("Enter the ammount of hours you were parking for: "))
if hours >= 6:
    print("Your charge is 20 PLN")
elif hours >= 3:
    print("Your charge is 15 PLN")
else:
    print("Your charge is 5 PLN")