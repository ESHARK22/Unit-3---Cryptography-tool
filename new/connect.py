HOST = 'localhost'
PORT = 5010
import socket
def connect(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket    

def disconnect(client_socket):
    client_socket.close()
    
def send(client_socket , data):
    client_socket.sendall(str(data).encode())
    client_socket
def receive(client_socket):
    return client_socket.recv(1024).decode()


def create_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    return server

# wait for the client to connect
def wait_for_client(server):
    
    print("Waiting for the client to connect...")
    client, addr = server.accept()
    print("Client connected!")
    return client

# wait for the client to send the public key
def wait_for_public_key(client):
    print("Waiting for the client to send the public key...")
    public_key = int(receive(client))
    print(f"Client's public key: {public_key}")
    return public_key

# send the public key to the client
def send_public_key(client, public_key):
    print(f"Sending public key: {public_key}")
    send(client, str(public_key))
    
def wait_for_mod(client):
    print("Waiting for the client to send the mod...")
    mod = int(receive(client))
    print(f"Client's mod: {mod}")
    return mod
def wait_for_y(client):
    print("Waiting for the client to send the y...")
    y = int(receive(client))
    print(f"Client's y: {y}")
    return y
    
def send_mod(client, mod):
    print(f"Sending mod: {mod}")
    send(client, str(mod))
    
def send_y(client, y):
    print(f"Sending y: {y}")
    send(client, str(y))


