# Write a function, is_prime, that takes an integer and returns True if 
# the number is prime and False if the number is not prime

def is_prime(num):
    num_is_prime = False
    if num > 1:
        for n in range(2, num ):
            if(num % n) == 0:
                num_is_prime = False 
                break               
            else:
                num_is_prime = True
    else:
        num_is_prime = False
    return num_is_prime

print(is_prime(1))
print(is_prime(4))
print(is_prime(5))
print(is_prime(313))

