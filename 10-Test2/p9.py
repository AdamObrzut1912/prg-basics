import csv

def f(value):
    emp_num = 0
    with open("data.csv", "r", encoding="utf-8") as file:
        dane = csv.DictReader(file)
        for line in dane:
            if int(line["Salary"])>value:
                emp_num += 1
    return emp_num

print(f(9200))
print(f(11640))