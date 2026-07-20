# QUESTION : 1  Write a lambda function to convert a list of song titles from Spotify to all lowercase letters and use map() to apply it to ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita'], printing the cleaned list :

songs =['Shape Of You','Blinding Lights','Levitating','Senorita']

lower_songs =list(map(lambda song:song.lower(),songs))
print(lower_songs)


# QUESTION : 2  Given a list of Zomato restaurant ratings [4.2, 3.8, 4.5, 2.9, 3.5], use filter() with a lambda to find and print only the restaurants with ratings above 4.0 : 

ratings =[4.2,3.8,4.5,2.9,3.5]

high_ratings =list(filter(lambda rating:rating > 4.0, ratings))
print(high_ratings)


# QUESTION : 3  Use reduce() from functools to calculate the total price of items in a Flipkart shopping cart: [499, 1299, 299, 799]. Print the final total.<br><br><em><strong>Hint:</strong> Import reduce from functools and use a lambda to sum two numbers.</em> : 

from functools import reduce

cart =[499,1299,299,799]

total_price=reduce(lambda x,y: x + y,cart)
print("Total Price:", total_price)


# QUESTION : 4  Create a function format_followers that takes a number and returns it in 'K' or 'M' format (e.g., 1500 → '1.5K', 1200000 → '1.2M'), then use map() to apply it to a list of follower counts: [950, 1500, 25000, 1200000] : 


def format_followers(number):
    if number>=1000000:
        return str(number / 1000000)+"M"
    elif number>=1000:
        return str(number / 1000) +"K"
    else:
        return str(number)

followers =[950,1500,25000,1200000]

formatted =list(map(format_followers,followers))
print(formatted)


# QUESTION : 5  Use an AI tool like ChatGPT or Copilot to generate a lambda function that filters out all odd numbers from a list of IPL scores [101, 98, 120, 77, 88], then test the code in your Python environment and paste the working code here :

ipl_scores = [101, 98, 120, 77, 88]

odd_scores = list(filter(lambda score: score % 2 != 0, ipl_scores))

print(odd_scores)