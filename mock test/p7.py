def f(n):
    counter = 0
    for i in range(0, n-2):
        counter += i
    return counter

if __name__ == "__main__":
    print(f(5))
    print(f(9))