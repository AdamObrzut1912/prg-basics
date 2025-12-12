with open("powers.txt", "w") as file:
        for i in range(1,101):
            file.write(f"{i},{i**2},{i**3}\n")

with open("powers.txt", "r") as file:
    for row in file:
        print(row)

