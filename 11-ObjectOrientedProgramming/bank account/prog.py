class Account():
    def __init__(self, bank_account):
        self.balance = 0
        self.bank_account = bank_account
    
    def deposit(self, ammount):
        self.balance += ammount
    
    def withdraw(self, ammount):
        if self.balance > ammount:
            self.balance -= ammount
        else:
            print("Insufficient funds on the account")

    def display_balance(self):
        print(f"Bank account: {self.bank_account}")
        print(f"Balance: {self.balance}")