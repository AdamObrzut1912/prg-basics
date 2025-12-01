def f(ammount_to_pay):
    counter = 0
    while ammount_to_pay != 0:
        if ammount_to_pay - 5 >= 0:
            counter += 1
            ammount_to_pay -= 5
        elif ammount_to_pay - 2 >= 0:
            counter += 1
            ammount_to_pay -= 2
        elif ammount_to_pay - 1 >= 0:
            counter += 1
            ammount_to_pay -= 1
        else:
            break
        
    return counter
    
if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))
       