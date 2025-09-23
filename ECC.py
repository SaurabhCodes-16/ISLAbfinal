from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def generate_ecc_keys():
    """
    Generate ECC private/public key pair
    Returns: (private_key, public_key)
    """
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def ecies_encrypt(message, receiver_public_key):
    """
    Encrypt message using ECC (ECIES style) + AES-GCM
    Returns: (ciphertext, ephemeral_public_key, iv, tag)
    """
    # Generate ephemeral private key
    ephemeral_private = ec.generate_private_key(ec.SECP256R1(), default_backend())
    shared_key = ephemeral_private.exchange(ec.ECDH(), receiver_public_key)

    # Derive AES key
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ecies-demo",
    ).derive(shared_key)

    # AES-GCM encryption
    iv = os.urandom(12)
    encryptor = Cipher(
        algorithms.AES(derived_key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    ciphertext = encryptor.update(message) + encryptor.finalize()

    return ciphertext, ephemeral_private.public_key(), iv, encryptor.tag

def ecies_decrypt(ciphertext, ephemeral_public_key, iv, tag, receiver_private_key):
    """
    Decrypt ECIES ciphertext using receiver's private key
    Returns: plaintext bytes
    """
    shared_key = receiver_private_key.exchange(ec.ECDH(), ephemeral_public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ecies-demo",
    ).derive(shared_key)

    decryptor = Cipher(
        algorithms.AES(derived_key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# ===========================
# Example usage
# ===========================

# 1️⃣ Generate receiver's ECC keys
receiver_private, receiver_public = generate_ecc_keys()

# 2️⃣ Encrypt message
message = b"Secure Transactions"
ciphertext, ephemeral_pub, iv, tag = ecies_encrypt(message, receiver_public)
print("Ciphertext:", ciphertext)

# 3️⃣ Decrypt message
decrypted = ecies_decrypt(ciphertext, ephemeral_pub, iv, tag, receiver_private)
print("Decrypted Message:", decrypted.decode())
