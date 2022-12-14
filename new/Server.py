import socket
from random import randint as rand
from time import sleep

from connect import (HOST, PORT, connect, disconnect, receive, send,
                     send_public_key, wait_for_client, wait_for_mod,
                     wait_for_public_key, wait_for_y, create_server)
from main import (Keys, decrypt, encrypt, generate_defaults,
                  generate_public_key, generate_shared_key, mod,
                  one_way_function)

DEBUG = True

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Listening on port " + str(PORT))

# Wait for a client to connect
client, addr = server.accept()
print("Connected to client")

send(client, "Hello")
# print("Sent Hello")
sleep(1)
MOD, Y = generate_defaults()
MOD, Y = int(MOD), int(Y)

mod_and_y = str(MOD) + "|" + str(Y) 
send(client, mod_and_y)
# print("Sent modulus and y")

# Receive the public key from the client
client_public_key = receive(client)
# print("CLient public key: " + str(client_public_key))

# Generate a public key
private = rand(10, MOD)
Server_shared_key = generate_public_key(private, MOD, Y)
# print("Generated public key: " + str(public_key))
send(client, Server_shared_key)

if DEBUG:
    # Generate the shared key
    print(f"Server public key: {Server_shared_key}")
    print(f"Cient public key: {client_public_key}")
    print(f"mod: {MOD}")
    print(f"y: {Y}")


# Generate the shared key where the client is BOB and the server is ALICE
Server_shared_key = generate_shared_key(int(client_public_key), int(private), int(MOD))
print(f"Shared key: {Server_shared_key}")

def send_message(message):
    encrypted_message = encrypt(message, Server_shared_key, MOD)
    send(client, encrypted_message)

def receive_message(return_encrypted=False):
    encrypted_message = receive(client)
    message = decrypt(encrypted_message, Server_shared_key, MOD)
    if return_encrypted:
        return encrypted_message, message
    return message

while True:
    print("Waiting for messages...")
    message = receive_message(return_encrypted=True)
    print(f"Received encrypted message: {message[0]}")
    print(f"> Decrypted message: {message[1]}")
    print("Sending message back...")

    new_message = input("Enter a message to send: ")
    send_message(new_message)
    print("Sent message")   

    if new_message == "exit":
        break

# Disconnect from the client
disconnect(client)


