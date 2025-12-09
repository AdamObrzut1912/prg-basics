with open("pets.txt", "r") as file:
    content = file.read()
    list_of_words = content.replace("\n"," ").split(" ")

    print(len(list_of_words))