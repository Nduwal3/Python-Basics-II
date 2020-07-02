# Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it. 
# Make more tuples with the corresponding information from your friends and append them to the list. Sort the list.
# When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age. 


tuple1 = ("Niru", "Duwal", 23)
my_list = []
my_list.append(tuple1)
tuple2 = ("Sony", "Chhetri", 27)
tuple3 = ("Mony", "kusma", 25)
tuple4 = ("Neesan", "Duwal", 18)
my_list.append(tuple2)
my_list.append(tuple3)
my_list.append(tuple4)
print(sorted(my_list))
# sort by lastname
print(sorted(my_list, key=lambda tup:tup[1]))

# sort by firstnamw
print(sorted(my_list, key=lambda tup:tup[2]))