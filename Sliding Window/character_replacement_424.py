def characterReplacement(s, k):
    # Step 1: Create frequency array for A-Z
    count = [0] * 26
    
    # Step 2: Initialize pointers and variables
    left = 0
    max_occurrence = 0   # stores max frequency of any character in window
    ans = 0              # stores final answer

    # Step 3: Start sliding window
    for right in range(len(s)):
        
        # Add current character to frequency array
        count[ord(s[right]) - ord('A')] += 1

        # Update max frequency in current window
        max_occurrence = max(max_occurrence, count[ord(s[right]) - ord('A')])

        # Check if window is invalid
        # (window size - most frequent char) > k → too many replacements needed
        if (right - left + 1) - max_occurrence > k:
            
            # Remove leftmost character from window
            count[ord(s[left]) - ord('A')] -= 1
            
            # Move left pointer forward
            left += 1
        
        # Update maximum valid window size
        ans = max(ans, right - left + 1)
    
    # Step 4: Return result
    return ans


# Example
s = "ABAB"
k = 2
print(characterReplacement(s, k))