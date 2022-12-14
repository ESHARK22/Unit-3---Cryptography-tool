import random
from random import randint as rand

def mod(mod:int, num:int):
    """ 
    Returns the mod of a number
    (the remainder of the number divided by the mod)
    Modular arithmatics goes in circles, like a clock
    7 o'clock + 8 = 3  o'clock 
    7 + 8 = 3 (mod 12)
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


def encrypt(message:str, key:int, _mod:int):
    """
    split the key up so that every letter uses a different key
    """
    key = str(key)
    message_length = len(message)
    key_length = len(key)

    # Split the key up so that every letter uses a different key
    if key_length < message_length:
        key = key * (message_length // key_length) + key[:message_length % key_length]
    elif key_length > message_length:
        key = key[:message_length]
        
    encrypted_message = ""
    for i in range(message_length):
        
        encrypted_letter = chr(mod( _mod, ord(message[i]) + int(key[i]) ))
        
        # if the encrypted letter is not in the ASCII table
        # then subtract the mod from the encrypted letter
        if ord(encrypted_letter) > 55295:
            encrypted_letter = chr(mod( _mod, ord(message[i]) + int(key[i]) - _mod ))
            
            
        encrypted_message += encrypted_letter
    return encrypted_message

def decrypt(message:str, key:int, _mod:int):
    """
    split the key up so that every letter uses a different key
    """
    key = str(key)
    message_length = len(message)
    key_length = len(key)

    # Split the key up so that every letter uses a different key
    if key_length < message_length:
        key = key * (message_length // key_length) + key[:message_length % key_length]
    elif key_length > message_length:
        key = key[:message_length]
        
    decrypted_message = ""
    for i in range(message_length):
        decrypted_letter = chr(mod( _mod, ord(message[i]) - int(key[i]) ))
        decrypted_message += decrypted_letter
    return decrypted_message



def generate_defaults():
    # The mod and Y can be shared to everyone
    MOD = rand(100000, 100000000)
    Y = rand(1, MOD) # Y must be smaller than the mod
    return MOD, Y

def generate_public_key(private_key:int, MOD:int, Y:int):
    return one_way_function(Y, MOD, private_key)

def generate_shared_key(public_key:int, private_key:int, MOD:int):
    return one_way_function(public_key, MOD, private_key)


class Keys:
    def __init__(self, MOD, Y):
        self.MOD = MOD
        self.Y = Y
        
        self.private_key = rand(10000, self.MOD)
        self.public_key = generate_public_key(self.private_key, self.MOD, self.Y)
        self.shared_key = None
        
    def get_public_key(self):
        return self.public_key

    def get_shared_key(self, public_key):
        self.shared_key = generate_shared_key(public_key, self.private_key, self.MOD)
        return self.shared_key

    def set_mod(self, MOD):
        self.MOD = MOD
        
    def set_y(self, Y):
        self.Y = Y

    def get_mod(self):
        return self.MOD

    def get_y(self):
        return self.Y


def main():    
    """
    All the theory in this was all taken from a book called "the code book" by .
    
    """
    
    ALICE_num = rand(10000 , 100000000)
    BOB_num = rand(10000 , 100000000)

    # One way function vars
    MOD, Y = generate_defaults()

    ALICE_public_key = generate_public_key(ALICE_num, MOD, Y)
    BOB_public_key = generate_public_key(BOB_num, MOD, Y)

    
    # Alice sends her public key to Bob
    # Bob sends his public key to Alice

    # They can both calculate the same result
    ALICE_result = generate_shared_key(BOB_public_key, ALICE_num, MOD)
    BOB_result = generate_shared_key(ALICE_public_key, BOB_num, MOD)

    print(f"Alice's number: {ALICE_num} | Bob's number: {BOB_num}")
    print(f"Alice's public key: {ALICE_public_key} | Bob's public key: {BOB_public_key}")
    print(f"Alice's result: {ALICE_result} | Bob's result: {BOB_result}")

    print("\n\n")
    
    message = "Hello World!"
    encrypted_message = encrypt(message, ALICE_result, MOD)
    decrypted_message = decrypt(encrypted_message, BOB_result, MOD)
    
    print(f"Message: {message}")    
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
    
def exapmle_with_keys_class():
    Client_test = Keys(100000, 2)
    Server_test = Keys(100000, 2)


    print("Client public key:", Client_test.get_public_key())
    print("Server public key:", Server_test.get_public_key())

    print("\n")

    # Client_test.set_shared_key(Server_test.get_public_key())
    # Server_test.set_shared_key(Client_test.get_public_key())

    print("Client shared key:", Client_test.get_shared_key(Server_test.get_public_key()))
    print("Server shared key:", Server_test.get_shared_key(Client_test.get_public_key()))

    print("\n")


    
    
if __name__ == "__main__":
    main()
    
    
    