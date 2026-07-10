# QUESTION : 1  Declare four variables in Python: your age as an int, your height in centimeters as a float, your name as a str, and whether you have a Spotify account as a bool. Print each variable and use the type() function to display its data type

age =int(input("enter a age :"))   
print(f"Age: {age}")
print("Type:-->",type(age))

height =float(input("enter a height in float :"))   
print(f"Height: {height}")
print("Type:-->",type(height))

name =str(input("enter a name :"))      
print(f"Name: {name}")
print("Type:-->",type(name))

has_spotify_account =bool(input("true / false :"))     
print(f"Spotify Account: {has_spotify_account}")
print("Type:-->",type(has_spotify_account))


# Question : 2  Write a function total_cart_amount(prices) that takes a list of product prices as strings (like ['199.99', '49', '350.75']) and returns the total as a float. Print the result for a sample Flipkart-style cart.<br><br><em><strong>Hint:</strong> Use float() to convert each string before summing.</em>

def total_cart_amount(prices):
    total=0.0
    for total_price in prices:
        total+=float(total_price)
    return total

cart=['199.99','49','350.75']
print(f"Total Cart Amount:{total_cart_amount(cart)}")
    

# Question : 3  Create a script that asks the user to input their cricket score as a string, converts it to an int, and prints 'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.<br><br><em><strong>Constraint:</strong> Use input(), int(), and if-else.</em>

Score= input("Enter your cricket score: ")
Score= int(Score)

if Score>= 50:
    print(f"Half-century! your score is {Score}")
else:
    print(f"Keep going! your score is {Score}")


# Question : 4   Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and print its type.<br><br><em><strong>Hint:</strong> The bool() function alone won’t work as expected. Think about string comparison.</em>

is_premium= 'True'
is_premium= (is_premium=='True')
print(type(is_premium))