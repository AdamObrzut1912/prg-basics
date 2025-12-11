def f(n):
    counter = 0
    primeNumbers = []
    for i in range(2,100):
        for y in range(1,100):
            if i % y == 0:
                counter += 1
        if counter == 2:
            primeNumbers.append(i)
        counter = 0
    return primeNumbers[n-1]

print(f(1))
print(f(5))