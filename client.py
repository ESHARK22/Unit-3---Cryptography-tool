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

def create_PublicPrivate_key(Y:int, _mod:int):
    """
    Creates a public key which can be shared.
    """

    private = random.randint(0, 100)
    public_key = one_way_function(Y, _mod, private)

    return public_key, private

def calc_shared_secret(public_key:int, private_key:int, _mod:int):
    """
    Calculates the shared secret using the public key and private key.
    """

    return one_way_function(public_key, _mod, private_key)

Y, _mod = random.randint(20, 100), random.randint(500, 1000)

ALICE_public_key, ALICE_private_key = create_PublicPrivate_key(Y, _mod)
BOB_public_key, BOB_private_key = create_PublicPrivate_key(Y, _mod)

# Alice sends her public key to Bob
# Bob sends his public key to Alice

print(f"Alice's public key: {ALICE_public_key} | Bob's public key: {BOB_public_key}")
print(f"Alice's private key: {ALICE_private_key} | Bob's private key: {BOB_private_key}")

ALICE_shared_secret = calc_shared_secret(BOB_public_key, ALICE_private_key, _mod)
BOB_shared_secret = calc_shared_secret(ALICE_public_key, BOB_private_key, _mod)

print(f"Alice's shared secret: {ALICE_shared_secret} | Bob's shared secret: {BOB_shared_secret}")
