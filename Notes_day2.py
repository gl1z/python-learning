STRINGS & OPERATORS

# Today I focused on:
# - Strings
# - String concatenation
# - Multi-line strings
# - += operator
# - Exponents (**)
# - Modulo (%)
# - Small practice projects


# STRINGS

# A string is text wrapped in quotes.
# Python does not care if I use single or double quotes,
# but I must close them properly or I get a SyntaxError.

first_name = "Tom"
last_name = "Smith"

print(first_name)
print(last_name)


# STRING CONCATENATION

# I can combine strings using the + operator.
# Python does NOT add strings like numbers.
# It joins them.

full_name = first_name + " " + last_name
print(full_name)

# Important:
# I must manually add spaces when combining strings.

# USING += WITH STRINGS

# += updates a variable by adding to its current value.

greeting = "Hello"
greeting += " Tom"

print(greeting)

# This is the same as:
# greeting = greeting + " Tom"

# MULTI-LINE STRINGS

# Triple quotes allow me to write text across multiple lines.
# Very useful for ASCII art or formatted output.

quote = """
Learning Python step by step.
One concept at a time.
Consistency > motivation.
"""

print(quote)

# NUMBERS REVIEW

# Exponent operator (**)
# Raises a number to a power.

squared = 2 ** 4
print(squared)  # 16

# Modulo operator (%)
# Returns the remainder after division.

remainder = 14 % 4
print(remainder)  # 2

# PRACTICE EXERCISES

# 1) Create a sentence using variables

age = 21
sentence = "I am " + str(age) + " years old."
print(sentence)

# Note:
# I had to convert age to string using str()
# because Python cannot combine string + integer directly.


# 2) Use += with numbers

counter = 0
counter += 5
counter += 3

print(counter)  # 8


# 3) Small challenge:
# Check if a number is even or odd using modulo

number = 10

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")



# TAKEAWAYS

# - Strings must always be properly closed
# - + joins strings, it does not add them numerically
# - += makes updating variables cleaner
# - % is very useful for checking patterns (like even/odd)
# - Python is strict about mixing data types
# - Small mistakes (like missing quotes) break everything
