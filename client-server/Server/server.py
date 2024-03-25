import socket

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address
    s.bind((HOST, PORT))
    
    # Listen for incoming connections
    s.listen()
    print('Server listening on', HOST, PORT)
    
    # Accept connection
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
        # Receive data from client
        data = conn.recv(1024)
        print('Received:', data.decode())
        
        # Send response to client
        conn.sendall(b'Hello, World!')
