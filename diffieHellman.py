from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

# ---------------------------
# Step 1: Public DH parameters
# ---------------------------
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1
g = 2

# ---------------------------
# Step 2: Each party generates private & public key
# ---------------------------
import random

def dh_generate_keys(p, g):
    private = random.randint(2, p - 2)
    public = pow(g, private, p)
    return private, public

# Hospital side
priv_h, pub_h = dh_generate_keys(p, g)
# Server side
priv_s, pub_s = dh_generate_keys(p, g)

# ---------------------------
# Step 3: Exchange public keys and compute shared secret
# ---------------------------
shared_h = pow(pub_s, priv_h, p)  # Hospital computes
shared_s = pow(pub_h, priv_s, p)  # Server computes
assert shared_h == shared_s
shared_secret = shared_h.to_bytes((shared_h.bit_length()+7)//8, 'big')

# Derive AES key from shared secret using SHA256
key = SHA256.new(shared_secret).digest()[:16]  # AES-128

# ---------------------------
# Step 4: Encrypt message
# ---------------------------
message = b"Secure patient report"
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, AES.block_size))
print("Ciphertext (hex):", ciphertext.hex())

# ---------------------------
# Step 5: Decrypt message
# ---------------------------
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted message:", decrypted.decode())
