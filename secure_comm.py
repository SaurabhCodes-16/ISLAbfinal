from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib

# --------------------------
# 1. RSA Key Generation
# --------------------------
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

# --------------------------
# 2. RSA Encryption/Decryption
# --------------------------
def rsa_encrypt(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message.encode())

def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(ciphertext).decode()

# --------------------------
# 3. Diffie-Hellman Key Exchange
# --------------------------
def diffie_hellman_generate(private, g, p):
    return pow(g, private, p)

def diffie_hellman_shared_key(their_public, my_private, p):
    return pow(their_public, my_private, p)

# --------------------------
# 4. AES Encryption/Decryption using shared key
# --------------------------
def aes_encrypt(message, key):
    key_bytes = hashlib.sha256(str(key).encode()).digest()[:16]  # 128-bit AES
    iv = get_random_bytes(16)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return ciphertext, iv

def aes_decrypt(ciphertext, key, iv):
    key_bytes = hashlib.sha256(str(key).encode()).digest()[:16]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

# --------------------------
# Example Communication
# --------------------------

# Subsystems: Finance (A), HR (B), Supply Chain (C)

# 1️⃣ Generate RSA keys for all subsystems
private_a, public_a = generate_rsa_keys()
private_b, public_b = generate_rsa_keys()
private_c, public_c = generate_rsa_keys()

# 2️⃣ Diffie-Hellman parameters
p = 30803  # large prime
g = 2      # generator

# Each subsystem chooses private DH key
private_dh_a = 1234
private_dh_b = 5678

# Exchange public DH values
public_dh_a = diffie_hellman_generate(private_dh_a, g, p)
public_dh_b = diffie_hellman_generate(private_dh_b, g, p)

# Shared secret
shared_key_ab = diffie_hellman_shared_key(public_dh_b, private_dh_a, p)
shared_key_ba = diffie_hellman_shared_key(public_dh_a, private_dh_b, p)

print("Shared key (A<->B):", shared_key_ab)
assert shared_key_ab == shared_key_ba

# 3️⃣ Secure message from Finance (A) to HR (B)
message = "Payroll report for September"
cipher_aes, iv = aes_encrypt(message, shared_key_ab)
print("\nAES Encrypted message (A->B):", cipher_aes.hex())

# HR decrypts
decrypted_msg = aes_decrypt(cipher_aes, shared_key_ba, iv)
print("Decrypted message at HR:", decrypted_msg)

# 4️⃣ RSA Encryption example: HR sends employee contract to Supply Chain
contract = "Employee Contract: John Doe"
rsa_cipher = rsa_encrypt(contract, public_c)
print("\nRSA Encrypted contract (B->C):", rsa_cipher.hex())

# Supply Chain decrypts
decrypted_contract = rsa_decrypt(rsa_cipher, private_c)
print("Decrypted contract at Supply Chain:", decrypted_contract)
