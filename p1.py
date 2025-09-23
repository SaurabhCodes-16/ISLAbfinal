from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# -------------------------
# Sender side (encryption)
# -------------------------

# 16-byte key for AES-128
key = b'ThisIsA16ByteKey'  # Must be exactly 16 bytes

# Message to encrypt
message = b"Project Alpha details!!"

# Generate a random 16-byte IV for CBC mode
iv = get_random_bytes(16)

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the message to make its length a multiple of 16 bytes
ciphertext = cipher.encrypt(pad(message, AES.block_size))
print ("original message:", message)
print("Ciphertext (hex):", ciphertext.hex())
print("IV (hex):", iv.hex())

# -------------------------
# Receiver side (decryption)
# -------------------------

# Create AES cipher again with same key and IV
decipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and unpad the message
decrypted_message = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message by bob", decrypted_message.decode())


from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime, inverse
from Crypto.Random import random


def generate_keys(key_size=256):
    """
    Generate ElGamal public and private keys.
    Returns: (p, g, h, x)
    """
    p = getPrime(key_size, randfunc=get_random_bytes)
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)  # private key
    h = pow(g, x, p)              # public key component
    return p, g, h, x

def encrypt(message, p, g, h):
    """
    Encrypt a string message using ElGamal encryption.
    Returns: ciphertext tuple (c1, c2)
    """
    m = int.from_bytes(message.encode(), 'big')
    y = random.randint(1, p - 2)  # session key
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (m * s) % p
    return c1, c2

def decrypt(ciphertext, p, x):
    """
    Decrypt ElGamal ciphertext using private key x.
    Returns: decrypted string message
    """
    c1, c2 = ciphertext
    s_dec = pow(c1, x, p)
    s_inv = inverse(s_dec, p)
    decrypted_m = (c2 * s_inv) % p
    decrypted_message = decrypted_m.to_bytes((decrypted_m.bit_length() + 7) // 8, 'big').decode()
    return decrypted_message

# =========================
# Example usage
# =========================

# Generate keys
p, g, h, x = generate_keys()

message = "Task Completed!"
ciphertext = encrypt(message, p, g, h)
decrypted = decrypt(ciphertext, p, x)

print("Public Key (p, g, h):", p, g, h)
print("Private Key (x):", x)
print("Original Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted)

