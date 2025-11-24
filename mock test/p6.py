def f(number,even):
    counter = 0
    number_str = str(number)
    if even == True:
        for i in number_str:
            if int(i) % 2 ==0:
                counter = counter + int(i)
            else:
                continue
    else:
        for i in number_str:
            if int(i) % 2 != 0:
                counter = counter + int(i)
            else:
                continue

    return counter

if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))