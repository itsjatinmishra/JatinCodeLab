def longestPalindrome(s):
    # This will store the longest palindrome found so far
    result = ""

    # Loop through each index of the string
    # Treat every index as a "center"
    for i in range(len(s)):

        # -------------------------------
        # CASE 1: ODD LENGTH PALINDROME
        # Example: "aba"
        # Center is at index i
        # -------------------------------
        odd = expand(s, i, i)

        # -------------------------------
        # CASE 2: EVEN LENGTH PALINDROME
        # Example: "bb"
        # Center is between i and i+1
        # -------------------------------
        even = expand(s, i, i + 1)

        # -----------------------------------------
        # Choose the longer palindrome
        # -----------------------------------------
        if len(odd) > len(even):
            longer = odd
        else:
            longer = even

        # -----------------------------------------
        # Update result if current is longer
        # -----------------------------------------
        if len(longer) > len(result):
            result = longer

    # Return final longest palindrome
    return result


def expand(s, left, right):
    # Expand around the center while it's a palindrome

    while left >= 0 and right < len(s) and s[left] == s[right]:
        # Move left pointer to left
        left -= 1

        # Move right pointer to right
        right += 1

    # IMPORTANT:
    # Loop stops AFTER breaking condition,
    # so we return last valid palindrome

    return s[left + 1:right]


# -------------------------------
# 🔥 Test the function
# -------------------------------
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"