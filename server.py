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


SERVER_NUM = random.randint(10000, 1000000)
SERVER_PUB = one_way_function(Y, _mod, SERVER_NUM)
print(f"Server's public key: {SERVER_PUB}")

CLIENT_PUB = int(input("Enter the clients's public key: "))
RESULT = one_way_function(CLIENT_PUB, _mod, SERVER_NUM)

print(f"Result: {RESULT}")

