from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

# --- 1. Define Message, Key, and Parameters ---
MESSAGE_TEXT = "Top Secret Data"
KEY_HEX = "FEDCBA9876543210FEDCBA9876543210" # 192-bit (24 bytes)
MODE = AES.MODE_ECB # Simplest mode for demonstrating core AES steps

print(f"--- AES-192 Encryption Details ---")
print(f"Original Message: '{MESSAGE_TEXT}'")
print(f"Key (Hex): {KEY_HEX}")
print("-" * 40)

# --- Convert inputs to bytes ---
key = binascii.unhexlify(KEY_HEX)
data = MESSAGE_TEXT.encode('utf-8')

# --- 2. Key Expansion and Initialization ---
# AES-192 requires 12 rounds of encryption. The key expansion derives 13 
# round keys (1 initial + 12 rounds) from the 192-bit master key.
# The cipher object handles this internal key expansion.
try:
    cipher = AES.new(key, MODE)
    print("Step 1: Key Expansion complete (handled internally by AES.new()).")
    print(f"Key Size: {len(key) * 8} bits.")
except ValueError as e:
    print(f"Error initializing cipher: {e}")
    exit()

# --- 3. Padding (PKCS#7) ---
# AES is a block cipher, and the data must be a multiple of the block size (16 bytes).
# PKCS#7 padding is used to fill the block.
padded_data = pad(data, AES.block_size, style='pkcs7')
print(f"Step 2: Padding (PKCS#7) applied.")
print(f"Original data length: {len(data)} bytes.")
print(f"Padded data (Hex): {binascii.hexlify(padded_data).decode()}")
print(f"Padding: {len(padded_data) - len(data)} bytes of value 0x{hex(len(padded_data) - len(data))[2:].zfill(2)}.")
print("-" * 40)

# --- 4. Encryption Rounds ---
# This is the core process (AddRoundKey, SubBytes, ShiftRows, MixColumns).
# AES-192 performs 12 rounds.
ciphertext_bytes = cipher.encrypt(padded_data)

print(f"Step 3: Encryption completed over 12 rounds:")
print(f"  - Initial Round: AddRoundKey")
print(f"  - Rounds 1-11: SubBytes -> ShiftRows -> MixColumns -> AddRoundKey")
print(f"  - Final Round 12: SubBytes -> ShiftRows -> AddRoundKey (MixColumns skipped)")

# --- 5. Final Ciphertext ---
ciphertext_hex = binascii.hexlify(ciphertext_bytes).decode().upper()

print("-" * 40)
print(f"Ciphertext (Hex): {ciphertext_hex}")