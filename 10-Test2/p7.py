import re
def f(array):

    regex = r'^[a-z\d_]{4,12}$'
    counter = 0

    for i in array:
            if re.match(regex,i):
                counter += 1

    return counter

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))