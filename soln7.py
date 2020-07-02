# Create a list of tuples of first name, last name, and age for your friends and colleagues. 
# If you don't know the age, put in None. Calculate the average age, skipping over any None values. 
# Print out each name, followed by old or young if they are above or below the average age. 


tuple1 = ("Subash", "Maharjan", None)
tuple2 = ("Sony", "Chhetri", 27)
tuple3 = ("Mony", "kusma", 25)
tuple4 = ("Neesan", "Duwal", 18)
tuple5 = ("rewoti", "Maharjan", None)

my_list = []
total_sum  = 0
no_of_people_with_known_ages = 0
my_list.append(tuple1)
my_list.append(tuple2)
my_list.append(tuple3)
my_list.append(tuple4)
my_list.append(tuple5)

# calculate average of not none
for tup in my_list:
    if(tup[2]):
        total_sum +=  tup[2]
        no_of_people_with_known_ages += 1 
averge_age = round(total_sum/no_of_people_with_known_ages)

for tup in my_list:
    if (tup[2]):
        if((tup[2]) < averge_age):
            print('{} : young'.format(tup[0]))
        else:
             print('{} : old'.format(tup[0]))

