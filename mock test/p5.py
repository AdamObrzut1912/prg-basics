def f(binary_number):
    counter = 0
    binary_number_str = str(binary_number)
    for i in binary_number_str:
        if i == '1' or i == '0':
            counter += 1
        else:
            continue
    if counter == len(binary_number_str):
        value = True
    else:
        value = False
    return value

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))

