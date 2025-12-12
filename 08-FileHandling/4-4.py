import os
dirPath = os.path.dirname(__file__)
counter = 0
with open("it_company.csv", "r", encoding="utf-8") as file:
    for item in file:
        print(item)
        counter += 1
        if counter == 5:
            nextLines = input("Press Enter key")
            if nextLines == "":
                counter = 0
