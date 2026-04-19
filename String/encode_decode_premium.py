def encode(strs):
    # This function takes a list of strings and joins them into one string
    # using '#' as a separator
    encoded_str = ""
    
    for s in strs:
        encoded_str += s + "#"   # Add each string followed by '#'
    
    return encoded_str


def decode(encoded_str):
    # This function converts the encoded string back into a list of strings
    result = []
    element = ""
    
    for char in encoded_str:
        if char != "#":
            element += char   # Build the current word character by character
        else:
            result.append(element)  # Word ends when '#' is found
            element = ""            # Reset for next word
    
    return result


# Input list
strs = ["ab", "b", "c", "abc"]

# Encode the list into a single string
encoded_str = encode(strs)
print("Encoded:", encoded_str)

# Decode the string back into list
decoded_list = decode(encoded_str)
print("Decoded:", decoded_list)