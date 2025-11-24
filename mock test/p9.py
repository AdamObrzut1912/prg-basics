def f(sentence):
    samo = "aeiouy"
    counter = 0
    for i in sentence:
        if i in samo:
            counter += 1
        else:
            continue
    return counter

if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))