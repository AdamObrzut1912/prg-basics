import re

def f(first_letter, last_letter):
    words_counter = 0
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:
            line_splited =  line.split() 

            
            for word in line_splited:
                word = word.lower()
                word = (word).strip(',.!?')
                if word.startswith(first_letter) and word.endswith(last_letter):
                    print(word)
                    words_counter += 1

    return words_counter

print(f("w","d"))