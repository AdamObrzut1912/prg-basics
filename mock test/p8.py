def f(palindrom):
    opposite = ""
    value = True
    for i in palindrom:
        opposite = i + opposite
    if(opposite == palindrom):
        value = True
    else:
        value = False

    return(value)

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))