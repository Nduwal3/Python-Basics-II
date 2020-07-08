# Write an if statement to determine whether a variable holding a year 
# is a leap year. 

year = int(input("Enter a year to check if it is leap or not:: "))
if (( year % 400 == 0 ) or ( year % 4 == 0 and  year % 100 != 0 )):
    print("leap year")
else:
    print("not leap year")

