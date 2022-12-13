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
    
    # A test for the above function (ignore this)
    # for x in range(10000):
    #   if is_prime(x):
    #       print(f"{x} is prime")
    
    return True

def generate_prime_number():
    """ Generates a prime number by generating a random number and checking if it is prime """
    
    # This may be innefficient, but it works :D
    # (It is fast enough for our purposes)
    while True:
        num = random.randint(2, 1000)
        if is_prime(num):
            return num
        
def greatest_common_divisor(a:int, b:int):
    """ Finds the greatest common divisor of two numbers """
    while b: # while b is not 0
        
        a, b = b, a % b 
    return a
    
# to create a key we must first generate two prime numbers
p = generate_prime_number()
q = generate_prime_number()

# then we multiply them to get n
n = p * q
# n is one part of the public key


# https://www.thefreedictionary.com/totient
_totient = "(Mathematics) a quantity of numbers less than, and sharing no common factors with, a given number"
# '-> a prime number that is coprime to n

_coprime = "when two numbers have no common factors other than 1."
# '-> https://www.mathsisfun.com/definitions/coprime.html
# two numbers are coprime if their greatest common divisor is 1

# then we need to find the "totient"
totient = (p - 1) * (q - 1)

print(f"p: {p}, q: {q}, n: {n}, totient: {totient}")