def f(subjects):
    max_val = 0
    new_max_value = 0
    result = ""
    for key, value in subjects.items():
        for i in value:
            new_max_value += i
            avg = new_max_value/len(value)
        if avg > max_val:
            max_val = avg
            result = key
        new_max_value = 0

    return result

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))