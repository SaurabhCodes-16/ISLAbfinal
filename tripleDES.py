from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

# 24-byte (192-bit) key given in the problem
key = bytes.fromhex("1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF")

# Triple DES requires key length = 16 or 24 bytes, adjusted for parity
key = DES3.adjust_key_parity(key)

# Create cipher (ECB mode for simplicity)
cipher = DES3.new(key, DES3.MODE_ECB)

# Message
plaintext = b"Classified Text"

# Pad plaintext to multiple of 8 bytes (DES block size = 8)
padded_text = pad(plaintext, DES3.block_size)

# Encrypt
ciphertext = cipher.encrypt(padded_text)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt
decipher = DES3.new(key, DES3.MODE_ECB)
decrypted_padded = decipher.decrypt(ciphertext)

# Remove padding
decrypted_text = unpad(decrypted_padded, DES3.block_size)

print("Decrypted text:", decrypted_text.decode())
