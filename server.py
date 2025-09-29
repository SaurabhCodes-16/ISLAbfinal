import socket

# Custom hash function (same as before)
def custom_hash(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value * 33) + ord(char)) & 0xFFFFFFFF
        hash_value = ((hash_value << 5) ^ (hash_value >> 27)) & 0xFFFFFFFF
    return hash_value

# Server setup
HOST = '127.0.0.1'  # localhost
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on", PORT)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024).decode('utf-8')
        print("Received data:", data)
        
        # Compute hash of received data
        data_hash = custom_hash(data)
        print("Computed hash:", data_hash)
        
        # Send hash back to client
        conn.send(str(data_hash).encode('utf-8'))
