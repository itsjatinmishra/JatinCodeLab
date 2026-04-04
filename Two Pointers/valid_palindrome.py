def isPalindrome(s):
    # Initialize two pointers
    left = 0
    right = len(s) - 1

    # Loop until the pointers meet
    while left < right:

        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right
        elif not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        elif s[left].lower() != s[right].lower():
            return False  # Not a palindrome

        else:
            # Move both pointers inward if characters match
            left += 1
            right -= 1

    # If all checks pass, it's a palindrome
    return True