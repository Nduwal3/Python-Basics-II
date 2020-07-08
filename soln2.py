# Write an if statement to determine whether a variable holding a year 
# is a leap year. 

given_year = int(input("Enter a year to check if it is leap or not:: "))
if(given_year % 4 == 0):
    if(given_year % 100 != 0):
        if( given_year % 400 == 0 ):
            print('{} is a leap year'.format(given_year))
        else:
            print('{} is not a leap year'.format(given_year))
    else:
         print('{} is a leap year'.format(given_year))
else:
    print('{} is not a leap year'.format(given_year))

