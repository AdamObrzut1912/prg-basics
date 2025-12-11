def star(n):
    word = ""
    for i in range(0,n):
        word = "*"*n
    return word

print(star(2))
print(star(6))
print(star(4))
print(star(9))
print(star(7))