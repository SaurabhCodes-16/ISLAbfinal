from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# -----------------------
# 1. Generate RSA Key Pair
# -----------------------
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Private Key:", private_key.decode()[:100], "...\n")
print("Public Key:", public_key.decode()[:100], "...\n")

# -----------------------
# 2. Document to sign
# -----------------------
document = "This is a confidential patient report."
document_bytes = document.encode('utf-8')

# -----------------------
# 3. Create hash of document
# -----------------------
hash_doc = SHA256.new(document_bytes)

# -----------------------
# 4. Sign the document using private key
# -----------------------
private_rsa = RSA.import_key(private_key)
signature = pkcs1_15.new(private_rsa).sign(hash_doc)

print("Digital Signature (hex):", signature.hex()[:100], "...")

# -----------------------
# 5. Verify signature using public key
# -----------------------
public_rsa = RSA.import_key(public_key)
hash_doc_verify = SHA256.new(document_bytes)

try:
    pkcs1_15.new(public_rsa).verify(hash_doc_verify, signature)
    print("\nVerification Success: The document is authentic and untampered.")
except (ValueError, TypeError):
    print("\nVerification Failed: The document may have been tampered with.")
