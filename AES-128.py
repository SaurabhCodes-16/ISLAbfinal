from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# -------------------------
# Sender side (encryption)
# -------------------------

# 16-byte key for AES-128
key = b'ThisIsA16ByteKey'  # Must be exactly 16 bytes

# Message to encrypt
message = b"Hello, this is a secret message!"

# Generate a random 16-byte IV for CBC mode
iv = get_random_bytes(16)

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the message to make its length a multiple of 16 bytes
ciphertext = cipher.encrypt(pad(message, AES.block_size))

print("Ciphertext (hex):", ciphertext.hex())
print("IV (hex):", iv.hex())

# -------------------------
# Receiver side (decryption)
# -------------------------

# Create AES cipher again with same key and IV
decipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and unpad the message
decrypted_message = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message:", decrypted_message.decode())
