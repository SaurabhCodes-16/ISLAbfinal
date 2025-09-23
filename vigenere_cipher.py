plaintext = "thehouseisbeingsoldtonight".upper()
key = "DOLLARS"
def char_to_num(c):
    return ord(c) - ord('A')
def num_to_char(n):
    return chr(n + ord('A'))
def repeat_key(key, length):
    return (key*(length//len(key)+1))[:length]
def vigenere_encrypt(plaintext, key):
    key = repeat_key(key, len(plaintext))
    return ''.join(num_to_char((char_to_num(p)+char_to_num(k))%26) for p, k in zip(plaintext, key))
def vigenere_decrypt(cipher, key):
    key = repeat_key(key, len(cipher))
    return ''.join(num_to_char((char_to_num(c)-char_to_num(k))%26) for c, k in zip(cipher, key))

print(vigenere_encrypt(plaintext, key))
decry = vigenere_encrypt(plaintext, key)
print(vigenere_decrypt(decry, key))