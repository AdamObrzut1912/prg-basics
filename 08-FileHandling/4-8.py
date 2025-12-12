import re
file_re = r'.+(\.\w{4}$)'

corr_progr = []

with open("files.txt","r") as file:
    for item in file:
        if re.match(file_re, item):
            print(item)