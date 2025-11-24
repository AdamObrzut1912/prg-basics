def f(name):
    find_1 = name.find(" ")
    name_2 = name[find_1 + 1:] 
    find_2 = name_2.find("")
    new = name[0] + name[find_1 +1] + name_2[find_1 +1]
    return new

print(f("internet of things"))