#  Write a program that serves as a basic calculator. 
#  It asks for two numbers, then it asks for an operator.
#   Gracefully deal with input that doesn't cleanly convert to numbers.
#    Deal with division by zero errors. 


def get_user_input():
    try:
        num1 = int(input("enter first number:: \n"))
        num2 = int(input("enter second number:: \n"))
    except ValueError:
        raise  ValueError("value must be an int")
    else:
        return num1, num2   

def get_operation_to_be_performed():
    try:
        operation = int(input("""Enter 
                        1 for Add
                        2 for Subtract
                        3 for Multiplication
                        4 for Division::: \n """))
    except ValueError:
        raise ValueError("not an integer")
    if operation > 5:
        raise ValueError("not an valid option")
    else:
        return operation

def add(num1, num2):
    total_sum = num1 + num2
    print('sum of {0} and {1} is {2}'.format(num1, num1, total_sum))

def subtract(num1, num2):
    total_difference = num1 - num2
    print('{0} minus {1} is {2}'.format(num1, num2,  total_difference))

def multiply(num1, num2):
    result = num1 * num2
    print('{0} multiply by {1} is {2}'.format(num1, num2,  result))

def division(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        raise ZeroDivisionError("Zero Division Error")
    else:
        print('{0} divide by {1} is {2}'.format(num1, num2,  result))


num1, num2 = get_user_input()

operation = get_operation_to_be_performed()
if(operation == 1):
    add(num1, num2)
if(operation == 2):
    subtract(num1, num2)
if(operation == 3):
    multiply(num1, num2)
if(operation == 4):
    division(num1, num2)