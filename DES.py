from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b"A1B2C3D4"
cipher = DES.new(key, DES.MODE_ECB)
message = b"Confidential Data"

ciphertext = cipher.encrypt(pad(message, DES.block_size))
print("Ciphertext(hex):", ciphertext.hex())

decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Decrypted message:", decrypted.decode())