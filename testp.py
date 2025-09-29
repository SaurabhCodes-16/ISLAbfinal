from math import gcd


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            result += chr(((a * x + b) % 26) + base)
        else:
            result += char
    return result


def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Invalid key 'a'. It must be coprime with 26.")
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            result += chr(((a_inv * (y - b)) % 26) + base)
        else:
            result += char
    return result




text = "PATIENTSUGAR120"
a, b = 7, 9   # keys (a must be coprime with 26)

encrypted = affine_encrypt(text, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print("Original Text:", text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# -------------------------
# Sender side (encryption)
# -------------------------

# 16-byte key for AES-128
key = b'1234567890ABCDEF'  # Must be exactly 16 bytes

# Message to encrypt
message = b"KJMNLWMFTZJY120"

# Generate a random 16-byte IV for CBC mode
iv = get_random_bytes(16)

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_ECB)

# Pad the message to make its length a multiple of 16 bytes
ciphertext = cipher.encrypt(pad(message, AES.block_size))

print("Ciphertext (hex):", ciphertext.hex())
print("IV (hex):", iv.hex())

# -------------------------
# Receiver side (decryption)
# -------------------------

# Create AES cipher again with same key and IV
decipher = AES.new(key, AES.MODE_ECB)

# Decrypt and unpad the message
decrypted_message = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message:", decrypted_message.decode())

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

message = "1234567890ABCDEF"
ciphertext = encrypt(message, p, g, h)
decrypted = decrypt(ciphertext, p, x)

print("Public Key (p, g, h):", p, g, h)
print("Private Key (x):", x)
print("Original Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted)

