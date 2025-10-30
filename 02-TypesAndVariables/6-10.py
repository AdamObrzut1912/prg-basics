###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print("name in capital letters:" , movie.upper())

# print title in small letters
print("name in small letters" , movie.lower())

# print how many times the vowel "e" appears in the title
print('"e" appears ', movie.count("e"), "times")

# print where in the text is the word "Lord"
print("word 'lord' appears since", movie.find("Lord"), "th char")

# print where in the text is the word "dragon"
print("word 'dragon' appears since", movie.find("dragon"))
