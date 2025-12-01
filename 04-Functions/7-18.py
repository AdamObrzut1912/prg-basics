def f(sentence):
    new_word= ""
    for i in sentence:
        if i != " ":
            new_word = new_word + i
        else:
            continue

    return new_word

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writingcomputer programs"))