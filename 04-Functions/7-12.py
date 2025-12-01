def f(n):
    string = ""
    for i in range(n):
        string = string + "*"
        if n > 1:
            string = string + "/"
    return string

  
print(f(11))
print(f(1))
