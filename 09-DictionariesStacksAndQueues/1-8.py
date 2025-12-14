price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

total_price_before = 0
for key, item in price_list.items():
    print(key," ",item)
    total_price_before += item
print(total_price_before)


for key, item in price_list.items():
    price_list[key]= item*0.90

total_price_before = 0
for key, item in price_list.items():
    print(key," ",item)
    total_price_before += item
print(total_price_before)