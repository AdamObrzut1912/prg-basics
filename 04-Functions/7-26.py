def f(text):

    counter = 0
    separatedText = ""
    for i in text:
    
        if counter == len(text)-1:
            separatedText = separatedText  + i
        else: 
            separatedText = separatedText  + i + "-"
        counter += 1

    return separatedText

print(f("University"))
print(f("UE"))
print(f("x"))
print("")