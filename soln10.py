# Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased). 
# Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.


def snake_case_to_camel_case(camel_cased_string):
    snake_cased  = camel_cased_string
    for char in camel_cased_string:       
        if(char.isupper()):
            snake_cased =  snake_cased.replace(char , '_' + char.lower())
    print(snake_cased.strip('_'))

snake_case_to_camel_case('ThisIsSnakeCased')

def case_convert(input_string , separator):
    result_string = input_string
    for char in input_string:
        if (char.isupper()):
            result_string = result_string.replace(char , separator + char.lower())
    result_string = result_string.strip(separator)
    return result_string

print(case_convert("ThisIsKebabCased", '-'))

