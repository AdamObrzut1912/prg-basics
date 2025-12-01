def f(palindrome):
    check = True
    new_word = ""
    for i in palindrome:
        new_word = i + new_word
    if new_word == palindrome:
        check = True
    else:
        check = False
    return check

print(f("radar"))
print(f("12-11-21"))
print(f("book"))