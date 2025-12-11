def f(dice):
    numDict = {
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0
    }

    numList = []
    for i in dice:
        numList.append(i)

    counter = 0

    for num in dice:

        counter += 1
        if num == numList[counter-1]:
            numDict[num] += 1
        else:
            numDict[num] = 0

    maxValue = max(numDict, key=numDict.get)
    return int(maxValue)

    return maxValue


print(f("2133"))