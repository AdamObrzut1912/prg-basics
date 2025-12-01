def f(number):
    numb = 0
    word = ""

    for i in str(number):
        
        if i in word:
            numb += int(i)
        word = word + i
    return numb

print(f(1027))
print(f(230335))
print(f(513553007))