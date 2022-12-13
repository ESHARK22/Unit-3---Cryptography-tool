import random
from main import one_way_function, mod

while True:
    try:
        _mod = int(input("Enter the mod: "))
        Y = int(input("Enter Y: "))
        break # if the user enters a number, break the while loop
    
    except ValueError:
        print("Only numbers are allowed!")
        continue # if the user enters a string or other , ask for a number again

    
# Get the client's public key
CLIENT_NUM = random.randint(10000, 1000000)
CLIENT_PUB = one_way_function(Y, _mod, CLIENT_NUM)
print(f"Client's public key: {CLIENT_PUB}")

# Get the server's public key
SERVER_PUB = int(input("Enter the servers's public key: "))
RESULT = one_way_function(SERVER_PUB, _mod, CLIENT_NUM)
print(f"Result: {RESULT}")

# Encrypt "Hello World" using the result



