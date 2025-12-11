car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]


###
# Bubble sort
#
def bubble_sort(arr):

    for i in range(len(arr)-1):
        for y in range(0,len(arr)-i-1):
            if arr[y]>arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
                
                
    return arr

car_fuel_consumption = car_fuel_consumption
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)
print("\n")
bank_transactions = bank_transactions
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)
...