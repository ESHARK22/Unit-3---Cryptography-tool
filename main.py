import random


def mod(mod:int, num:int):
    """ 
    Returns the mod of a number
    (the remainder of the number divided by the mod)
    Modular arithmatics goes in circles, like a clock
    5 o'clock + 2 = 7 o'clock 
    5 + 2 = 7 (mod 12)
    """
    return num % mod # returns the remainder of the number divided by the mod


def one_way_function(Y:int, _mod:int, num:int):
    """
    A one way function is a function that is easy to compute, but hard to reverse.
    This function is one way because it is easy to calculate a number powered (mod x) 
        but hard to calculate the number that powered (mod x) to get the result.
        Currently the only known way to reverse this function is to brute force it.
    """
    # y^x (mod _mod)
    # Note: Y must be smaller than the mod
    
    powered = Y ** num # Y to the power of num
    return mod(_mod, powered) # powered (mod _mod)




while True:
    
    ALICE_num = random.randint(0, 100)
    BOB_num = random.randint(0, 100)

    # One way function vars
    MOD = random.randint(500, 1000)
    Y = random.randint(20, MOD) # Y must be smaller than the mod

    ALICE_public_key = one_way_function(Y, MOD, BOB_num)
    BOB_public_key = one_way_function(Y, MOD, ALICE_num)

    
    # Alice sends her public key to Bob
    # Bob sends his public key to Alice

    # They can both calculate the same result
    ALICE_result = one_way_function(ALICE_public_key, MOD, ALICE_num)
    BOB_result = one_way_function(BOB_public_key, MOD, BOB_num)

    print(f"Alice's number: {ALICE_num} | Bob's number: {BOB_num}")
    print(f"Alice's public key: {ALICE_public_key} | Bob's public key: {BOB_public_key}")
    print(f"Alice's result: {ALICE_result} | Bob's result: {BOB_result}")

    print("\n\n")