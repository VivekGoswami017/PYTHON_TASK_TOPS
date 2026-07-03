# Question : 1  Create three variables in Python named item_price, delivery_fee, and coupon_discount, and assign them values representing a Swiggy order (e.g., 250, 30, 20) Print each variable.

# Swiggy _order_details:

item_price =250
delivery_fee =30
coupon_discount =20

print(f"Item Price:{item_price}")
print(f"Delivery Fee:{ delivery_fee}")
print(f"Coupon Discount:{coupon_discount}")

# Question : 2  Write a Python script that uses indentation correctly to check if a Flipkart product's price is above 1000; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.<br><br><em><strong>Hint:</strong> Use an if-else block and make sure your indentation is consistent.</em>

# Flipkart_product_price
product_price =int(input("enter product price"))
if product_price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")


# Question : 3  Add both single-line and multi-line comments in your script explaining what each section does, using # for single-line and triple quotes for multi-line comments.

# This line is defining single line comment and his program demonstrates variables, comments, and if-else statements.

"""
This is a multi-line comment using triple quotes
It explains the purpose of the program.
The program uses Swiggy and Flipkart examples.

""" 

# Question : 4  Create variables for an IPL match: team_name, runs_scored, and overs_played. Assign appropriate values and print them using the correct naming conventions for Python variables.<br><br><em><strong>Constraint:</strong> Use snake_case for all variable names.</em>

# IPL _match_details
team_name = "RCB"
runs_scored = 250
overs_played = 20

print("Team Name:", team_name)
print("Runs Scored:", runs_scored)
print("Overs Played:", overs_played)
