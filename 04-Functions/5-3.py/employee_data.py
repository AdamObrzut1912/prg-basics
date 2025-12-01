###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard1 # your own defined module

# Reads employee's data from keyboard
first_name = keyboard1.input_string('Enter name: ')
last_name = keyboard1.input_string('Enter surname: ')
age = keyboard1.input_integer('Enter age: ')
salary = keyboard1.input_real('Enter salary: ')
is_salary_hidden = keyboard1.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('Name: ', first_name)
print('Surname: ', last_name)
print('Age: ', age)

if is_salary_hidden == 1:
    print('Salary')