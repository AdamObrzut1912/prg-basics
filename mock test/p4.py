def f(card_number):
    card_number_1 = card_number[0:2]
    card_number_2 = card_number[-4:]

    masked = card_number_1 + "**********" + card_number_2


    return(masked)
if __name__ == "__main__":
    print(f("524444444444444444"))
