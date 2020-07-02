# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid 


class ParenthesesValidity:
    count_small_open_parentheses = 0
    count_small_close_parentheses = 0
    count_curly_open_parentheses = 0
    count_curly_close_parentheses = 0
    count_large_open_parentheses = 0
    count_large_close_parentheses = 0


    def __init__(self, parentheses_string):
        self.parentheses_string  = parentheses_string
    
    def count_parentheses(self):        
        for char in self.parentheses_string:
            if (char == '('):
                self.count_small_open_parentheses += 1
            elif (char == ')'):
                self.count_small_close_parentheses += 1
            elif (char == '{'):
                self.count_curly_open_parentheses += 1
            elif (char == '}'):
                self.count_curly_close_parentheses += 1
            elif (char == '['):
                self.count_large_open_parentheses += 1
            elif (char == ']'):
                self.count_large_close_parentheses += 1
            else:
                continue

    def check_validity(self):
        if(self.count_small_open_parentheses == self.count_small_close_parentheses 
        and self.count_curly_open_parentheses == self.count_curly_close_parentheses 
        and self.count_large_open_parentheses == self.count_large_close_parentheses):
            print("valid parentheses string")
        else:
            print("invalid parentheses string")

class_obj = ParenthesesValidity("()[]{[}")
class_obj.count_parentheses()
class_obj.check_validity()