def encode(strs):
    encoded_str = ""
    for i in strs:
        encoded_str += i + "#"
    
    return encoded_str

def decode(encoded_str):
    result = []
    element = ""
    for i in range(len(encoded_str)):
        if encoded_str[i] != "#":
            element += encoded_str[i]
        else:
            result.append(element)
            element = ""
    return result

strs = ["ab", "b", "c", "abc"]
encoded_str = encode(strs)
print(encoded_str)

print(decode(encoded_str))