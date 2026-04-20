def countSubstrings(s):
    # Initialize the answer to 0. This will store the total number of palindromic substrings.
    ans = 0

    # Loop through each character in the string.
    # We will treat each character (and the gap between characters) as the center of a potential palindrome.
    for i in range(len(s)):
        # 1. Check for odd-length palindromes centered at index i.
        # Example: "aba" has center at 'b'.
        ans += checkPalindrome(s, i, i)

        # 2. Check for even-length palindromes centered between index i and i+1.
        # Example: "bb" has center between the two 'b's.
        ans += checkPalindrome(s, i, i + 1)
    
    # Return the total count of palindromic substrings.
    return ans


def checkPalindrome(s, left, right):
    # Initialize count of palindromes found from this center
    count = 0

    # Expand outwards from the center as long as:
    # 1. left index is not negative (stays in bounds)
    # 2. right index is within string length (stays in bounds)
    # 3. characters at left and right are the same (palindrome condition)
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # Found a palindrome, increment count
        count += 1
        # Expand the window outwards
        left -= 1
        right += 1
    
    # Return the number of palindromes found from this center
    return count


# Test the function with an example string
print(countSubstrings("cabba"))
# Expected output: 7
# Explanation of palindromes in "cabba":
# "c", "a", "b", "b", "a", "bb", "abba"