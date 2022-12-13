import random

def is_prime(number:int):
    """Checks if a number is prime"""

    # Make sure number is positive
    if not number > 1:
        return False
    
    # Check if number is divisible by any number between 2 and itself
    for i in range(2, number): 
        if (number % i) == 0: 
            return False
    
    return True

    # A test for the above function (ignore this)
    # for x in range(10000):
    #   if is_prime(x):
    #       print(f"{x} is prime")

def generate_prime_number():
    """ Generates a prime number by generating a random number and checking if it is prime """
    
    # This may be innefficient, but it works :D
    # (It is fast enough for our purposes)
    while True:
        num = random.randint(2, 1000)
        if is_prime(num):
            return num
        
    
        


