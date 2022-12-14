import socket
from random import randint as rand
from time import sleep

from connect import (HOST, PORT, connect, disconnect, receive, send,
                     send_public_key, wait_for_client, wait_for_mod,
                     wait_for_public_key, wait_for_y)
from main import (decrypt, encrypt, generate_defaults, generate_public_key,
                  generate_shared_key, mod, one_way_function)

# Connect to the server
server = connect(HOST, PORT)
print("Connected to server")

# Wait for the sserver to send Hello
server.recv(1024)

# Receive the modulus from the server
mod_and_y = receive(server).split("|")
MOD = int(mod_and_y[0])
Y = int(mod_and_y[1])



# print("Modulus: " + str(MOD))
# print("Y: " + str(Y))

# Generate a public key
private = rand(10000, int(MOD))
public_key = generate_public_key(private, MOD, Y)
# print("Generated public key: " + str(public_key))
send(server, public_key)

# Receive the public key from the server
server_public_key = receive(server)

# print("Server public key: " + str(server_public_key))

# Generate the shared key
shared_key = generate_shared_key(int(private), int(server_public_key), int(MOD))
print("Shared key: " + str(shared_key))
