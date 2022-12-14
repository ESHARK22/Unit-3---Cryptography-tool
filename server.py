# Create a server that listens on port 6573

import socket
from time import sleep

from new.main import \
    one_way_function, mod, \
    encrypt, decrypt, \
        generate_defaults, \
        generate_public_key, \
        generate_shared_key

from random import randint as rand

# Encryption functions



# Generate the defaults
MOD, Y = generate_defaults()

# Generate the private key
private_key = rand(10000, MOD)


def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 6573))
    server.listen(1)
    client, address = server.accept()
    print("Connected to client")
    return client


def receive(client):
    message = client.recv(1024).decode("utf-8").strip()
    return message


def send(client, message:str):
    # make message 1024 bytes
    message = message + " " * (1024 - len(message))
    
    
    client.send(message.encode("utf-8"))
    
    
# encrypt the message with the one way function
def exchange_keys(client, private_key:int, MOD:int, Y:int):
    public_key = "PUB_KEY{" + str(generate_public_key(private_key, MOD, Y)) + "}"
    print("Public key:", public_key)
    send(client, str(public_key))
    return int(str(receive(client)).replace("PUB_KEY{", "").replace("}", ""))

def main():
    client = connect()
    public_key = exchange_keys(client, private_key, MOD, Y)
    shared_key = generate_shared_key(public_key, private_key, MOD)
    print("Shared key:", shared_key)
    while True:
        message = receive(client)
        
        decrypted_message = decrypt(message, shared_key, MOD)
        print("Received message:", message)
        print("Decrypted message:", decrypted_message)
        sleep(1)


main()