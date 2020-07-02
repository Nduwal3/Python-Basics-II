# Create a function, is_palindrome, to determine if a supplied word is 
# the same if the letters are reversed.


def is_palindrome(input_string):
    if( input_string == input_string[::-1]):
       return True
    else:
        return False


print(is_palindrome("honey"))
print(is_palindrome("rotator"))
