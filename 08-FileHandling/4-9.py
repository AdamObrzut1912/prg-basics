import csv

with open("it_company.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Job Title"] == "Graphic Designer":
            print(row["First Name"], row["Last Name"], row["Email"])
        
