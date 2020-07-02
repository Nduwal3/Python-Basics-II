# Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list.
#  What is the first item on the list? What is the second item on the list? 

my_list = []
print(id(my_list))
my_list.append('Niru')
my_list.append('Rewoti')
print(id(my_list))
print(sorted(my_list))

# the id of the list before and after appending data is same because list is mutable
# while sorting the list the elements got sorted based on alphabets from A-Z
