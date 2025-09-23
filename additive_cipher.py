plaintext = "HELLOSaurabh".upper()
def char_to_num(c):
    return ord(c) - ord('A')
def num_to_char(n):
    return chr(n+ord('A'))

def Additive_cipher(text, key):
    return ''.join(num_to_char((char_to_num(c)+key)%26) for c in text)
def Additive_decrypt(cipher, key):
    return ''.join(num_to_char((char_to_num(c)-key)%26) for c in cipher)
add_cipher = Additive_cipher(plaintext, 20)
print("Additive cipher:", add_cipher)
print("Decrypted:", Additive_decrypt(add_cipher, 20))