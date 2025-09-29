from math import gcd

# Function to compute modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Affine Cipher Encryption
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            result += chr(((a * x + b) % 26) + base)
        else:
            result += char
    return result

# Affine Cipher Decryption
def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Invalid key 'a'. It must be coprime with 26.")
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            result += chr(((a_inv * (y - b)) % 26) + base)
        else:
            result += char
    return result


# Example usage
if __name__ == "__main__":
    text = "Affine Cipher"
    a, b = 5, 8   # keys (a must be coprime with 26)

    encrypted = affine_encrypt(text, a, b)
    decrypted = affine_decrypt(encrypted, a, b)

    print("Original Text:", text)
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
