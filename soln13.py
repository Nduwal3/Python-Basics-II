# Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples as parameters. 
# The tuples should have a name, address, and age. 
# The file should create a header row followed by a row for each tuple.
#  If the following list of tuples was passed in: [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)] it should write the following in the file: 
# name,address,age 
# George,4312 Abbey Road,22 
# John,54 Love Ave,21

def create_csv(filename , tuple_list):
    file = open(filename , 'w')
    file.write("name, address, age\n")
    for tup in tuple_list:
        file.write('{}, {}, {}\n'.format(tup[0] , tup[1] , tup[2]))
    file.close()

create_csv('files/test.csv', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)] ) 