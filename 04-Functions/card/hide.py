def card(card_numbers):
    hidden = card_numbers[0:2] + "**********" + card_numbers[-4:]
    return hidden