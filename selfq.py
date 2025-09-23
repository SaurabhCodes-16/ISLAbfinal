from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = "Bhai kya kar rha hai"
rsa_key = RSA.import_key(public_key)
cipher = PKCS1_OAEP.new(rsa_key)
ciphertext = cipher.encrypt(message.encode())
print("Saurabh:", message)
print("Saurabh:", base64.b64encode(ciphertext).decode())

rsa_key = RSA.import_key(private_key)
cipher = PKCS1_OAEP.new(rsa_key)
decrypted = cipher.decrypt(ciphertext)
print("Arth:", decrypted.decode())

# message2 = "Kuch nhi bhai"
# rsa_key = RSA.import_key(public_key)
# cipher = PKCS1_OAEP.new(rsa_key)
# ciphertext = cipher.encrypt(message2.encode())
# print("Arth:", message2)
# print("Arth:", base64.b64encode(ciphertext).decode())

# rsa_key = RSA.import_key(private_key)
# cipher = PKCS1_OAEP.new(rsa_key)
# decrypted = cipher.decrypt(ciphertext)
# print("Saurabh:", decrypted.decode())

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b"A1B2C3D4"
cipher = DES.new(key, DES.MODE_ECB)
message3 = b"kya haa'l hai batle 16/100"

ciphertext = cipher.encrypt(pad(message3, DES.block_size))
print("Ciphertext(hex) by Arth:", ciphertext.hex())

decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Decrypted message at Dev:", decrypted.decode())