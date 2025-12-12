###
# Makes a copy of a text file
#
import os

dirPlace = os.path.dirname(__file__)

# file names
original_file = dirPlace + '\\healthy_lifestyle.txt'
target_file = dirPlace + '\\copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, "r", encoding="utf-8") as file:
   content = file.read()

print(content)

# write the content to the target file (copy)
with open(target_file, "w", encoding="utf-8") as file:
    file.write(content)

with open(target_file, "r", encoding="utf-8") as file:
   content = file.read()
print(content)