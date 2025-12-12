import csv

with open("books.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Genre"] == "Fantasy":
            with open("books_fantasy.csv", "a", encoding="utf-8") as file:
                writter = csv.DictWriter(row["Title"],row["Author"],row["Genre"],row["Year"])
                writter.writerow(file)
                    