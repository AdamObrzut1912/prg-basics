### A program that calculates amaunt to be paid
product_num = float(input("Enter the number of products: "))
product_price = float(input("Emter the product price: "))
total_price = 0

if (product_price > 2):
    discount = 0.25
    products_over_two = (product_num - 2) * product_price
    total_price = 2 * product_price + products_over_two - products_over_two*discount
else:
    total_price = product_price * product_num
print(f"Number of products purchased: {product_num}")
print(f"Product price: {product_price}")
print(f"Amount to pay: {total_price}")