# send data to localhost:5789

import socket
import time
import random
HOST = 'localhost'
PORT = 5789

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
s.connect((HOST, PORT)) # Connect to the server

while True:
    # A bunch of random data of strings and numbers
    random_data = ""
    for x in range(random.randint(1, 10000)):
        random_data += chr(random.randint(0, 10000))

    random_data = bytes(random_data, "UTF-8")
    # make it 1024 bytes long
    if len(random_data) > 1024:
        for x in range(1024 - len(random_data)):
            # send random data to the server in small chunks
            s.sendall(random_data[x:x+1])
        
    else:
        while len(random_data) < 1024:
            random_data += b" "
        s.sendall(random_data)
        
    time.sleep(0.1) # wait 0.1 seconds
    
    
    
#     # Listen on localhost at port 5789 for incoming connections which will send messages separated by "[EOL]".

# import socket

# HOST = 'localhost'
# PORT = 5789

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
# s.bind((HOST, PORT)) # Bind to the port
# s.listen(1) # Tells the socket to listen for incoming connections
# conn, addr = s.accept() # Accepts the connection
# print('Connected by', addr) # Prints the address of the client

# while True:
#     data = conn.recv(1024) # Receives the data
#     if not data:
#         break
#     print(data.decode("utf-8")) # Prints the data
    
# conn.close() # Closes the connection

