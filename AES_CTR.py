from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

# Key and nonce
key = b"0123456789ABCDEF0123456789ABCDEF"  # 16-byte AES-128 key
nonce = b"00000000"  # 8 bytes (rest will be counter)

# Define counter with nonce
ctr = Counter.new(64, prefix=nonce, initial_value=0)

# Create AES cipher in CTR mode
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

# Plaintext
plaintext = b"Cryptography Lab Exercise"

# Encrypt
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())

# Decrypt (need fresh counter object)
ctr_dec = Counter.new(64, prefix=nonce, initial_value=0)
decipher = AES.new(key, AES.MODE_CTR, counter=ctr_dec)
decrypted = decipher.decrypt(ciphertext)

print("Decrypted text:", decrypted.decode())
