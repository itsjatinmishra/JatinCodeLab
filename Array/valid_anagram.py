def valid_anagram(s, t):
    charCount = [0]*26

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        charCount[ord(s[i]) - ord('a')] += 1
        charCount[ord(t[i]) - ord('a')] -= 1
    
    for i in charCount:
        if i != 0:
            return False
    
    return True


s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))