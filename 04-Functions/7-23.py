def f(password):
    litery = set()
    is_true = False

    for i in password:
        litery.add(i)

    counter = 0

    for i in password:
        if i in litery:
            counter += 1
    if counter == len(litery) and len(password) >= 6:
        is_true = True
    
    return is_true

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))
