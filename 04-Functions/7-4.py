def letters_in_word(expression, letter):
    counter = 0
    for i in expression:
        if i == letter:
            counter += 1
        else:
            continue
    return counter

print(f"The number of letter e: {letters_in_word('You never get a second chance to make a first impression', 'e')}")