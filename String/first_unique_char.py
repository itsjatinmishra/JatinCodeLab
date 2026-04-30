def firstUniqChar(s):
    unique = {}

    # Count frequency of each character
    for char in s:
        if char in unique:
            unique[char] += 1
        else:
            unique[char] = 1

    # Find first character with frequency 1
    for index in range(len(s)):
        if unique[s[index]] == 1:
            return index

    return -1


# Example usage
s = "leetcode"
print(firstUniqChar(s))