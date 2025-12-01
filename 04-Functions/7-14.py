def f(detector):
    check = 0
    true_false = False
    for i in detector:
        if i == "+":
            check +=1
        else:
            check -= 1

        if check == 3:
            true_false = True
            break
        else:
            true_false = False
                
    return true_false

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
