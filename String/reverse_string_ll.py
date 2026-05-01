def reverseStr(s, k):
    s = list(s)  # convert string to list (mutable)

    for i in range(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k])

    return "".join(s)


# Example
s = "abcdefg"
k = 2
print(reverseStr(s, k))