# A program that recomends a product if the discount is over 10%
current_product_price = 140.00
previous_product_price = 200.00
discount = 100-(current_product_price/previous_product_price*100)

print(f"Current product price: {current_product_price}")
print(f"Previous product price: {previous_product_price}")

if discount > 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(discount)} %")
