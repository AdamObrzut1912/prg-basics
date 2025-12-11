def f(name):
    newWord = name.split(" ")
    newWord1 = ""
    for i in range(len(newWord)):
        newWord1 += (newWord[i][0])

    return newWord1


print(f("Internet f Things"))
print(f("For your Information"))
print(f("Python"))