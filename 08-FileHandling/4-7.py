import re
def vowels_counter(text):
    num_vowels = 0
    text_reg = r'[aeiouy]'
    
    num_vowels = len(re.findall(text_reg,text))

    return num_vowels

print(vowels_counter("kosdsf dsf sadf sadf sdaf"))