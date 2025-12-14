def f(cards1,cards2):
    values = {
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "T":10,
        "J":10,
        "Q":10,
        "K":10,
        "A":10
    }


    cards1_total = 0
    cards2_total = 0

    for i in cards1:
        cards1_total += values[i]


    for i in cards2:
        cards2_total += values[i]
    
    true_false = False

    if cards1_total >= cards2_total:
        true_false = True

    return true_false

print(f("AJ972","AQT72"))
print(f("9532","K8"))