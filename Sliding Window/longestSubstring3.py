def lengthOfLongestSubstring(s):
    # Left pointer of sliding window
    left = 0
    
    # Stores maximum length found
    max_length = 0
    
    # Set to keep track of unique characters in current window
    seen = set()

    # Right pointer expands the window
    for right in range(len(s)):

        # If duplicate character found, shrink window
        while s[right] in seen:
            seen.remove(s[left])  # remove leftmost character
            left += 1             # move left pointer forward

        # Add current character to set
        seen.add(s[right])

        # Update maximum length of substring
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abatman"
print(lengthOfLongestSubstring(s))