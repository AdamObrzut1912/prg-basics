def f(number,even):
    number_str = str(number)
    new_num = 0
    if even == True:
        for i in number_str:
            if int(i) % 2 == 0:
                new_num += int(i)
            else:
                continue
    else:
         for i in number_str:
            if int(i) % 2 != 0:
                new_num += int(i)
            else:
                continue
    return new_num

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))