def f(number):
    lista = {}
    number_str = str(number)
    suma = 0

    for i in number_str:
        
        if i in lista.keys():
            lista[i] += 1
        else:
            lista[i] = 1

    for klucz, wartosc in lista.items():
            if wartosc > 1:
                suma = suma + int(klucz)*wartosc
            else:
                continue
    

    return suma
print(f(1027))
print(f(230335))
print(f(513553007))