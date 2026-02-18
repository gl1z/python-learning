# PROJECT – Receipts for Lovely Loveseats

# This project practices:
# - Variables
# - Strings
# - Numbers
# - Updating variables
# - Basic calculations
# - Printing formatted output


# STORE CATALOG

# Item 1
lovely_loveseat_description = (
    "Lovely Loveseat. Tufted polyester blend on wood. "
    "32 inches high x 40 inches wide x 30 inches deep. Red or white.\n"
)
lovely_loveseat_price = 254.00


# Item 2
stylish_settee_description = (
    "Stylish Settee. Faux leather on birch. "
    "29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n"
)
stylish_settee_price = 180.50


# Item 3
luxurious_lamp_description = (
    "Luxurious Lamp. Glass and iron. "
    "36 inches tall. Brown with cream shade.\n"
)
luxurious_lamp_price = 52.15


# Sales tax (8.8%)
sales_tax = 0.088


# CUSTOMER ONE

# Customer starts with nothing
customer_one_total = 0
customer_one_itemization = ""


# Customer buys Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description


# Customer buys Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description


# CALCULATING TAX

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax


# PRINTING THE RECEIPT

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)


# PERSONAL NOTES

# - += makes totals much cleaner to manage
# - Strings can be built step by step
# - Always define variables BEFORE using them
# - Numbers and strings behave very differently
# - Real-world problems = just variables + math + output