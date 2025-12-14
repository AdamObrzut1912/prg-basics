import json
def f(years,course,average_grade):
    valids = ""
    with open("data.json", "r", encoding="utf-8") as file:
        text = json.load(file)

        total = 0
        counter = 0
        people_counter = 0

        for line in text:

            for grade in line["grades"].values():
            
                total += grade
                counter +=1
            avg = total/counter

            

            if line["age"] >= years and line["course"] == course and avg >= average_grade:
                people_counter += 1
    return people_counter
print(f(21, "statistics", 4))