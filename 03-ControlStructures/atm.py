###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code
is_digit = pin.isdigit()
pin_lenght = len(pin)
print(pin_lenght)

if is_digit == True and pin_lenght == 4:
    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. CHange PIN")

        choice = input("Choose an option (1-5): ")
        print()

        if choice == '1':
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop
        elif choice == '5':
            changed = False
            while changed == False:
                old_pin = int(input("Enter old pin: "))
                if old_pin == int(pin):
                    new_pin = (input("Enter a new PIN: "))
                    if len((new_pin)) == 4:
                        if new_pin.isdigit() == True:
                            print("Pin changed")
                            break
                        else:
                            print("enter only digits")
                    else:
                        print("enter the pin that contains only 4 numbers")
                else:
                    print("Enter the correct PIN")
            changed = True
        else:
            print("Invalid option. Please try again.")
