###
# Program that calculates price after discount
# And the difference before and after discount
#

price = float(input("Enter product price: "))
discount = 0.01 * float(input("enter discount in %: "))
price_after_discount = price - price*discount
reduction =price - price_after_discount
print(f"Price after discount is equal {price_after_discount}")
print(f"the reduction of price in that product is equal {reduction}")
