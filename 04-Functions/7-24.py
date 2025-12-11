def f(expression):
    result = int(expression[0])
    counter = 0
    for i in expression:
        counter += 1
        if i == "-":
            result -= int(expression[counter])
        elif i == "+":
            result += int(expression[counter])

    return result

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))