categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

maxExpense = max(expenses)
dig = expenses.index(maxExpense)
print(categories[dig])