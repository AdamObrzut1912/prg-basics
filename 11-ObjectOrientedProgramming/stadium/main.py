from stadium import C

def main():
    stadium1 = C({"A":120,"D":150,"G":90,"K":110})
    stadium1.m1("G",130)
    print(stadium1.m2("GD"))
    print(stadium1.m2("KEJ"))


if __name__ == "__main__":
    main()