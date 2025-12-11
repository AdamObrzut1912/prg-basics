names = ["Genowefa", "Oufry", "Celestyna", "Alojzy", "Pankracy"]
longest = " "
for name in names:
    if len(name) > len(longest):
        longest = name
    
print(longest)