# QUESTION : 1  Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers (use their usernames as keys and follower counts as values). Print the dictionary : 

insta_followers={
    "Virat Kohli":271000000,
    "Shraddha Kappor":94500000,
    "Alia Bhatt":86500000,
    "Carryminati":22500000,
    "Mrbeast":410000000
}
print(insta_followers)
print(type(insta_followers))


# QUESTION : 2  Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. Then, delete one influencer from the dictionary and print the updated dictionary :


insta_followers["Techburner"] =6000000                   #Adding new influencer...

insta_followers["Alia Bhatt"] =87000000                 #Update follower count...

del insta_followers["Carryminati"]                       #Delete one influencer

print(insta_followers)


# QUESTION : 3  Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display all items that cost more than ₹200 :

food_prices ={
    "Pizza":299,
    "Burger":149,
    "Biryani":250,
    "Pasta":220,
    "Sandwich":180
}

print("Food items Costing More Than ₹200....:")
for item,price in food_prices.items():
    if price > 200:
        print(item,"--->",price) 


# QUESTION : 4  Create two sets....flipkart_users and myntra_users, each containing 5 unique usernames. Find and print the set of users who have accounts on both platforms using set intersection :


flipkart_Users ={"Vivek","Rahul","Amit","Kavyansh","Prince"}

myntra_Users ={"Priya","Vivek","karan","Kavyansh","Amit"}

Common_Users_Is =flipkart_Users.intersection(myntra_Users)

print(f"Common_User_Is--->{Common_Users_Is}")

 
# QUESTION : 5  Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a set of all unique artists across both playlists (set union).<br><br><em><strong>Hint:</strong> Use the union() method or the | operator for sets.</em> :


def get_unique_artists(spotify_playlist1,spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1 ={"Arijit Singh","Osman Mir","Shreya Ghoshal"}

playlist2 ={"Shreya Ghoshal","Sonu Nigam","Osman Mir"}

result =get_unique_artists(playlist1, playlist2)
print("Unique Artists---->", result)