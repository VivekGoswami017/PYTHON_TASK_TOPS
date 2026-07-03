# Question : 1  Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.

playlist_ids= [101,295,309,412,518]

print(playlist_ids)


# Question : 2  Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>

playlist_ids= [101,295,309,412,518]

playlist_ids.append(777)    
print(playlist_ids)

playlist_ids.extend([788, 888]) 
print(playlist_ids)

# Question : 3  Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist

playlist_ids= [101,295,309,412,518,777,788,888]

removed_last_song= playlist_ids.pop()
print(f"Removed Song Id Is... {removed_last_song}")
print(f"Remaining Playlist Is... {playlist_ids}")


# Question : 4  Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>

insta_filters= ("Paris","Oslo","Tokyo","Melbourne")

insta_filters[0]= "Lagos"  #TypeError:'tuple' object does not support item assignment
                           #Tuple is Immutable...we can not change the elements
print(insta_filters)


# Question : 5  Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints which one should use a list and which should use a tuple, explaining your choice in a comment.

zomato_orders= ["Pizza","Burger","Momos","Coffee","Sandwich"]

ipl_teams= ("MI","CSK","RCB","KKR","GT","RR","DC","PBKS","LSG","SRH")

print(f"Recent Zomato Orders: {zomato_orders}")
print(f"IPL Teams: {ipl_teams}")

# Reason :
# Use list for zomato orders because orders can be added or removed | available or not available so...
# Use tuple for ipl team names because they are fixed.