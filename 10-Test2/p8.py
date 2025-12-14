# def f(expression):
#     expression_sliced = expression.split()
#     stos = []
#     cos = 0
#     for i in expression_sliced:
#         if i != "-" and i !="+":
#             stos.append(int(i))
#         elif i == "-":
#             cos = stos[len(stos)-2] - stos[len(stos)-1]
#             stos.append(cos)
#             del(stos[len(stos)-3])
#             del(stos[len(stos)-2])
            
#         elif i == "+":
#             cos = int(stos[len(stos)-2]) + int(stos[len(stos)-1]) 
#             stos.append(cos)
#             del(stos[len(stos)-3])
#             del(stos[len(stos)-2])

#     return stos[0]

# print(f("2 3 +"))
# print(f("2 6 + 4 5 - +"))
# print(f("11 7 + 15 - 14 +"))




def f(expression):
    expression_sliced = expression.split()
    stos = []
    
    for i in expression_sliced:
        # Jeśli to liczba, wrzucamy na stos
        if i != "-" and i != "+":
            stos.append(int(i))
            
        # Jeśli operator, zdejmujemy (i usuwamy) dwie ostatnie liczby
        elif i == "-":
            # Kolejność jest kluczowa! Najpierw zdejmujemy to co było na górze (prawa strona)
            b = stos.pop() 
            a = stos.pop()
            stos.append(a - b)
            
        elif i == "+":
            b = stos.pop()
            a = stos.pop()
            stos.append(a + b)

    # Wynikiem jest jedyny element, który został na stosie
    return stos[0]

# Testy
print(f("2 3 +"))             # Wynik: 5
print(f("2 6 + 4 5 - +"))     # Wynik: 7
print(f("11 7 + 15 - 14 +"))  # Wynik: 17