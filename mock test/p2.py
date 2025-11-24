def f(n1,n2,n3):
    val = True
    if n1 != n2 and n1 != n3 and n2 != n3:
        val = True
    else:
        val = False
    return(val)

if __name__ == "__main__":
    print(f(4,8,5))
    print(f(2,9,2))