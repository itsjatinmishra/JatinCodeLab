def countSubstrings(s):
    ans = 0

    for i in range(len(s)):
        # Odd-length palindromes
        ans += checkPalindrome(s, i, i)
        # Even-length palindromes
        ans += checkPalindrome(s, i, i + 1)
    
    return ans


def checkPalindrome(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

print(countSubstrings("cabba"))