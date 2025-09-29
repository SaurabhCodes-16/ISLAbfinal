def custom_hash(input_string):
    # Initialize hash value
    hash_value = 5381
    
    # Iterate through each character in the string
    for char in input_string:
        # Multiply by 33 and add ASCII value of character
        hash_value = ((hash_value * 33) + ord(char)) & 0xFFFFFFFF  # ensure 32-bit
        # Optional bitwise mixing for better distribution
        hash_value = ((hash_value << 5) ^ (hash_value >> 27)) & 0xFFFFFFFF
    
    return hash_value

# Example usage
s = "HelloWorld"
print(f"Hash of '{s}' is: {custom_hash(s)}")
