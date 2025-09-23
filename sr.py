from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# =========================
# Receiver generates key pair
# =========================
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Export public key in PEM format (to share with sender)
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Receiver's Public Key (Share this with sender):\n", pem_public.decode())

# =========================
# Sender side
# =========================
# Sender loads the receiver's public key (simulating input)
public_key_loaded = serialization.load_pem_public_key(pem_public)

# Sender enters message
message = input("Sender, enter the message you want to send: ").encode()

# Encrypt with receiver’s public key
ciphertext = public_key_loaded.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nEncrypted Message (Send this to receiver):", ciphertext)

# =========================
# Receiver side: Decrypt
# =========================
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nReceiver Decrypted Message:", plaintext.decode())
