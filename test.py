
key = 132456748945676453423


def encrypt(key, message):
    # Reorganise alphabet to be in key order and replace spaces
    
    alphabet = {}
    
    


        
        
        
    # Encrypt message
    encrypted_message = ""
    for letter in message:
        encrypted_message += alphabet[letter]
    return encrypted_message



def decrypt(key, message):
    pass
message = "hello world"
encrypted = encrypt(key, message)
# decrypted = decrypt(key, encrypted)

print(f"Message: {message}")
print(f"Encrypted: {encrypted}")
# print(f"Decrypted: {decrypted}")