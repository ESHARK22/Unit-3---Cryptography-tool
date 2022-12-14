import socket
from random import randint as rand
from time import sleep

from connect import (HOST, PORT, connect, disconnect, receive, send,
                     send_public_key, wait_for_client, wait_for_mod,
                     wait_for_public_key, wait_for_y)
from main import (decrypt, encrypt, generate_defaults, generate_public_key,
                  generate_shared_key, mod, one_way_function)

DEBUG = True

# Connect to the server
server = connect(HOST, PORT)
print("Connected to server")

# Wait for the sserver to send Hello
server.recv(1024)
# print("Received Hello")
# Receive the modulus from the server
mod_and_y = receive(server).split("|")
MOD = int(mod_and_y[0])
Y = int(mod_and_y[1])



# print("Modulus: " + str(MOD))
# print("Y: " + str(Y))

# Generate a public key
private = rand(10, int(MOD))
Client_shared_key = generate_public_key(private, MOD, Y)
# print("Generated public key: " + str(public_key))
send(server, Client_shared_key)

# Receive the public key from the server
server_public_key = receive(server)

# print("Server public key: " + str(server_public_key))

if DEBUG:
    # Generate the shared key
    print(f"Server public key: {server_public_key}")
    print(f"Client public key: {Client_shared_key}")
    print(f"mod: {MOD}")
    print(f"y: {Y}")

# Generate the shared key where the client is BOB and the server is ALICE
Client_shared_key = generate_shared_key(int(server_public_key), int(private), int(MOD))
print(f"Shared key: {Client_shared_key}")

def send_message(message):
    encrypted_message = encrypt(message, Client_shared_key, MOD)
    send(server, encrypted_message)

def receive_message(return_encrypted=False):
    encrypted_message = receive(server)
    message = decrypt(encrypted_message, Client_shared_key, MOD)
    if return_encrypted:
        return encrypted_message, message
    return message


while True:
    message = input("Enter message: ")
    send_message(message)
    if message == "exit":
        break
    
    print("Sent message")
    print("Waiting for response...")
    response = receive_message(return_encrypted=True)
    print(f"Received encrypted message: {response[0]}")
    print(f"> Decrypted Message: {response[1]}")

# Close the connection
disconnect(server)