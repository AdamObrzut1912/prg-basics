#Bar code program
code = (input("Enter the EAN-13 (European Article Number)"))
print(f"Enter EAN-13 article number: {code}")
if len(code) == 13:
    print("Article number is correct")
    if code[:3] == '590':
        print("Article manufactured in Poland")
    