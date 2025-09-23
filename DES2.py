from Crypto.Cipher import DES

key = b"A1B2C3D4" 
cipher = DES.new(key, DES.MODE_ECB)


block1 = "54686973206973206120636f6e666964656e7469616c206d657373616765"
block2 = "416e64207468697320697320746865207365636f6e6420626c6f636b"


data1 = bytes.fromhex(block1)
data2 = bytes.fromhex(block2)


enc1 = cipher.encrypt(data1[:8])  
enc2 = cipher.encrypt(data2[:8])

print("Encrypted Block1:", enc1.hex())
print("Encrypted Block2:", enc2.hex())

k
dec1 = cipher.decrypt(enc1)
dec2 = cipher.decrypt(enc2)

print("Decrypted Block1:", dec1.decode(errors="ignore"))
print("Decrypted Block2:", dec2.decode(errors="ignore"))
