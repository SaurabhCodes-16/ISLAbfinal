from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key (8 bytes for DES)
key = b"A1B2C3D4"

# Initialization Vector (8 bytes)
iv = b"12345678"

# Message to encrypt
message = b"Secure Communication"

# Create DES cipher in CBC mode
cipher = DES.new(key, DES.MODE_CBC, iv)

# Encrypt (pad to block size of 8)
ciphertext = cipher.encrypt(pad(message, DES.block_size))
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt
decipher = DES.new(key, DES.MODE_CBC, iv)
plaintext = unpad(decipher.decrypt(ciphertext), DES.block_size)
print("Decrypted text:", plaintext.decode())
