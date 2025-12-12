file_to_check = input("enter file name")
content = ""
num_lines = 0
num_char = 0
num_words = 0
try: 
    with open(file_to_check, "r", encoding="utf-8") as file:
        for line in file:
           
            content += line
            num_lines += 1
            num_words += len(line.split())
            num_char += len(line)
        
    

    print(content)
    print(num_lines)
    print(num_words)
    print(num_char)

except FileNotFoundError:
    print("podaj dobry plik")