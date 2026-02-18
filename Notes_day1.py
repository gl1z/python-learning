# VARIABLES

# A variable stores data
# Assign a variable using =

meal = "Pizza"

# I can update (reassign) a variable
meal = "Hot Dog"
# variable naming rules:
# -Cannot start with number
# -Can contain letters, numbers, underscore
# -Case sensitive (Meal != meal)

# ERRORS

# SyntaxError example (commented so it doesn't break)
# print ("Hello")

# NameError example
#print (my_variable)

# Correct version
my_variable = "Hello"
print(my_variable)

# NUMBERS
# Integer (int) -> Whole Number
age = 21
# Float -> Decimal number
rating = 4.5
# Type Checking
print(type(age)) # <class 'int'>
print(type(rating)) # <class 'float'>

# Arithmetic operators
# + addition
# - substraction
# * multiplication
# / division (always returns float in Python 3)

print(5 + 3)
print(10 - 2)
print(5 * 3)
print(10 / 2) #5.0 (returns float)

# Order of operations (PEMDAS)
print(25 * 68 + 13 / 28)
# Division by zero causes error
# print(10 / 0) # ZeroDivisionError

# VARIABLES WITH NUMBERS
 coffee_price = 2.50
 number_of_coffees = 4
 total = coffee_price * number_of_coffees
 print(total)

 # Updating a variable
 coffee_price = 3.50
print (coffee_price * number_of_coffees)

# Important:
# Doing math does NOT change the variable unless I reassign it
x = 5
x + 3 # x is still 5
x = x + 3 # now x becomes 8

# Variables used in calculations

quilt_width = 8
quilt_length = 12

# Area formula
quilt_area = quilt_width * quilt_length
print(quilt_area) #96

# KEY TAKEAWAYS:
# - Variables store data
# - Use = to assign
# - Strings needs quotes
# - int = Whole number
# - float = decimal number
# - Python is case sensitive
