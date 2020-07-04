# Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names, and each subsequent row as values for those keys.
#  For the data in the previous example it would 
# return: [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name': 'John', 'address': '54 Love Ave', 'age': 21}] 

import csv


def read_csv(filename):
    try:
        with open (filename, 'r') as csv_file:
            data = csv.DictReader(csv_file, delimiter= ',')
            my_list = []
            for row in data:
                my_list.append(row)
            return (my_list)
    except FileNotFoundError:
        print("file not found")

print(read_csv('files/test.csv'))
   
