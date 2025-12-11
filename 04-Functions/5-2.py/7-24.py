def factorial(n):
    # Warunek Bazowy: 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1
        
    # Krok Rekurencyjny: n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)

# Uruchomienie programu
n = 5
wynik = factorial(n)

print(f"Silnia z {n}! wynosi: {wynik}")