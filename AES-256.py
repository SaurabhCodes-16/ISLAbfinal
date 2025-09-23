from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 32-byte key (256 bits)
key = b"0123456789ABCDEF0123456789ABCDEF"  

# Message
message = b"Encryption Strength"

# Create AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
ciphertext = cipher.encrypt(pad(message, AES.block_size))
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted message:", plaintext.decode())
