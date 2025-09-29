import socket

# Custom hash function (must match server)
def custom_hash(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value * 33) + ord(char)) & 0xFFFFFFFF
        hash_value = ((hash_value << 5) ^ (hash_value >> 27)) & 0xFFFFFFFF
    return hash_value

HOST = '127.0.0.1'
PORT = 65432

# Input data from user
data_to_send = input("Enter some data to send: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Send data
    s.send(data_to_send.encode('utf-8'))
    
    # Compute local hash
    local_hash = custom_hash(data_to_send)
    
    # Receive server hash
    server_hash = int(s.recv(1024).decode('utf-8'))
    
    print("Local hash:", local_hash)
    print("Server hash:", server_hash)
    
    # Verify integrity
    if local_hash == server_hash:
        print("✅ Data integrity verified! No tampering detected.")
    else:
        print("❌ Data corrupted or tampered during transmission!")
