# A program that prints a survey of three questions
comp_science = input("Are you interested in computer science? (y/n): ")
games = input("Do you like playing computer games? (y/n): ")
ig = input("Do you have an Instagram account? (y/n): ")

if comp_science == "y":
    comp_science = True
elif comp_science == "n":
    comp_science = False
else:
    print("Enter y/n !")

if games == "y":
    games = True
elif games == "n":
    games = False
else:
    print("Enter y/n !")

if ig == "y":
    ig = True
elif ig == "n":
    ig = False
else:
    print("Enter y/n !")

if (comp_science == True):
    print("SURVEY RESULTS Interested in computer science: Yes")
elif (comp_science == False):
    print("SURVEY RESULTS Interested in computer science: No")

if (games == True):
    print("Playing computer games: Yes")
elif (games == False):
    print("Playing computer games: No")

if (ig == True):
    print("Has an Instagram account: Yes")
elif (ig == False):
    print("Has an Instagram account: No")






