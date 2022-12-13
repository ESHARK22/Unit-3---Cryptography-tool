def is_prime(number:int):
    """Checks if a number is prime"""
    if number > 1: # Make sure number is bigger than 1
        
        # Check if number is divisible by any number between 2 and number
        for i in range(2, number): 
            if (number % i) == 0: 
                return False
        else:
            return True
    else:
        return False
    
for x in range(1000):
    if is_prime(x):
        print(x)