# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]


# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   day_meal = []
   for item in meal_plan[day_number-1]:
        day_meal.append(item)
        day_meal_string = ", ".join(day_meal)
      
   return day_meal_string

# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("Breakfast, Lunch, Dinner")
print("====================")
print(weekday(1), day_meal_plan(meal_plan, 1))
...
...