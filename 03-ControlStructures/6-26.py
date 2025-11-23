# Pin check
counter = 0
for i in range(3):
    attempt = (input("Enter the PIN code:"))
    if attempt == '0805':
        print("Correct")
        break
    elif attempt != '0805':
        print("Incorrect")
        counter += 1
        continue
if counter == 3:
    print("Sorry, your payment card has been blocked.")
