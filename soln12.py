# Create a function, is_palindrome, to determine if a supplied word is 
# the same if the letters are reversed.


def is_palindrome(input_string):
    return input_string == "".join(reversed(input_string))


print(is_palindrome("honey"))
print(is_palindrome("rotator"))
