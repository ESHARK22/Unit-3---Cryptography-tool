ALICE_num = 3
BOB_num = 6

# One way function vars
MOD = 11
Y = 7

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

# Alice and Bob both have the same mod
# Alice and Bob both have the same number
# Alice and Bob both have the same one way function
# They can both calculate the same result
# But they can't reverse the result to get the number

# Alice generates her public key
ALICE_public_key = one_way_function(Y, MOD, BOB_num)
BOB_public_key = one_way_function(Y, MOD, ALICE_num)

print(ALICE_public_key)
print(BOB_public_key)

# Alice sends her public key to Bob
# Bob sends his public key to Alice

# They can both calculate the same result
ALICE_result = one_way_function(ALICE_public_key, MOD, ALICE_num)
BOB_result = one_way_function(BOB_public_key, MOD, BOB_num)

print(ALICE_result)
print(BOB_result)