import csv
with open("clothing.csv", "r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row["Price"]) < 60 and float(row["Stock_Quantity"]) < 40:
            for key, value in row.items():
                print(value, end=" ")
            print()