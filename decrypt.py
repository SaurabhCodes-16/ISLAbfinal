def mod_inverse(a, m):
    for x in range(1, m):
        if(a*x)%m == 1:
            return x
    return None

def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n+ord('A'))

def decrypt(text, k1, k2):
    inv = mod_inverse(k1, 26)
    return ''.join(num_to_char(((char_to_num(c)-k2)*inv)%26) for c in text)
text = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"
print(decrypt(text, 5, 6))        