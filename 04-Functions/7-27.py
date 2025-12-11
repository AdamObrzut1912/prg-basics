def f(product_code):
    counter = 0
    suma = 0
    is_True = False
    for i in product_code:
        suma += int(i)
        counter += 1
        if counter >= 3:
            break

    forthDigit = product_code[3]
    expression = suma % 7
    if expression == int(forthDigit):
        is_True = True

    return is_True

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))