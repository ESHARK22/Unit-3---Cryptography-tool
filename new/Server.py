import socket
from random import randint as rand
from time import sleep

from connect import (HOST, PORT, connect, disconnect, receive, send,
                     send_public_key, wait_for_client, wait_for_mod,
                     wait_for_public_key, wait_for_y, create_server)
from main import (Keys, decrypt, encrypt, generate_defaults,
                  generate_public_key, generate_shared_key, mod,
                  one_way_function)


# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Listening on port " + str(PORT))

# Wait for a client to connect
client, addr = server.accept()
print("Connected to client")

send(client, "Hello")

MOD, Y = generate_defaults()
MOD, Y = int(MOD), int(Y)

mod_and_y = str(MOD) + "|" + str(Y) 
send(client, mod_and_y)

# Receive the public key from the client
client_public_key = receive(client)
# print("CLient public key: " + str(client_public_key))

# Generate a public key
private = rand(10000, MOD)
public_key = generate_public_key(private, MOD, Y)
# print("Generated public key: " + str(public_key))
send(client, public_key)

# Generate the shared key
shared_key = generate_shared_key(int(private), int(client_public_key), int(MOD))
print("Shared key: " + str(shared_key))




