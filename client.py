from new.main import \
    one_way_function, mod, \
    encrypt, decrypt, \
        generate_defaults, \
        generate_public_key, \
        generate_shared_key
    
import random
from random import randint as rand
import socket
from time import sleep

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 6573))
    return client

def send(client, message:str):
    message = message + " " * (1024 - len(message))
    client.send(message.encode("utf-8"))
    
def receive(client):
    message = client.recv(1024).decode("utf-8")
    return message
# encrypt the message with the one way function
def exchange_keys(client, private_key:int, MOD:int, Y:int):
    public_key = "PUB_KEY{" + str(generate_public_key(private_key, MOD, Y)) + "}"
    print("Public key:", public_key)
    send(client, str(public_key))
    return int(str(receive(client)).replace("PUB_KEY{", "").replace("}", ""))

def main():
    client = connect()
    print("Connected to server")
    MOD, Y = generate_defaults()
    private_key = rand(10000, MOD)
    public_key = exchange_keys(client, private_key, MOD, Y)
    shared_key = generate_shared_key(public_key, private_key, MOD)
    print("Shared key:", shared_key)
    while True:
        message = input("Message: ")
        encrypted_message = encrypt(message, shared_key, MOD)
        send(client, encrypted_message)
        print("Encrypted message:", encrypted_message)
        decrypted_message = decrypt(encrypted_message, shared_key, MOD)
        sleep(1)






if __name__ == "__main__":
    
    try:
        main()
    except KeyboardInterrupt:
        print("Client closed")
        
    except ConnectionRefusedError:
        print("Server is not running")

    sleep(1)