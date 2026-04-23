def reverseVowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)   # convert string to list

    left = 0
    right = len(s) - 1

    while left < right:
        # move left pointer
        while left < right and s[left] not in vowels:
            left += 1

        # move right pointer
        while left < right and s[right] not in vowels:
            right -= 1

        # swap vowels
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return "".join(s)


s1 = "IceCreAm"
s2 = "leetcode"
print(reverseVowels(s1))