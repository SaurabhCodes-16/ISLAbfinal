from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = "Hello Saurabh, RSA with pycryptodome!"
rsa_key = RSA.import_key(public_key)
cipher = PKCS1_OAEP.new(rsa_key)
ciphertext = cipher.encrypt(message.encode())
print("Encrypted:", base64.b64encode(ciphertext).decode())

rsa_key = RSA.import_key(private_key)
cipher = PKCS1_OAEP.new(rsa_key)
decrypted = cipher.decrypt(ciphertext)
print("decrypted:", decrypted.decode())
