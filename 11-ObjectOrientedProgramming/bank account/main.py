import prog

def main():
    account1 = prog.Account("12 3456 5555 9090 1111 0000 7722")
    account1.display_balance()
    account1.deposit(25.30)
    account1.display_balance()
    account1.withdraw(31.70)
    account1.display_balance()
    account1.withdraw(14)
    account1.display_balance()


if __name__ == "__main__":
   main() 