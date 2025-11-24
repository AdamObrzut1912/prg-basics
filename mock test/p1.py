def f(amount_to_pay):
    counter = 0
    while amount_to_pay != 0:
        if amount_to_pay - 5 >= 0:
            amount_to_pay -= 5
            counter += 1
        elif amount_to_pay - 2 >= 0:
            amount_to_pay -= 2
            counter += 1
        elif amount_to_pay - 1 >= 0:
            amount_to_pay -= 1
            counter += 1
        else:
            break
    return(counter)


if __name__ == "__main__":
    print(f(23))
    print(f(8))