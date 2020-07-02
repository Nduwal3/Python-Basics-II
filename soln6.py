# Create a list with the names of friends and colleagues. Search for the 
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it. 

friends_list = ['Subash', 'sneha', 'Poonam', 'Rabi', 'john']
is_found = False
for friend in friends_list:
    friend = friend.capitalize()
    if friend == 'John':
        is_found = True
        break
if(not is_found):
    print("not found")

        
