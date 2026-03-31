def checkInclusion(s1, s2):
    # If s1 is longer than s2, permutation is not possible
    if len(s1) > len(s2):
        return False

    # Frequency arrays for s1 and current window in s2
    s1Map = [0] * 26
    windowMap = [0] * 26

    # Fill frequency for s1 and first window of s2
    for i in range(len(s1)):
        s1Map[ord(s1[i]) - ord('a')] += 1
        windowMap[ord(s2[i]) - ord('a')] += 1

    # Slide window across s2
    for i in range(len(s2) - len(s1)):
        # If both frequency maps match → permutation found
        if matches(s1Map, windowMap):
            return True

        # Add next character to window
        windowMap[ord(s2[i + len(s1)]) - ord('a')] += 1

        # Remove leftmost character from window
        windowMap[ord(s2[i]) - ord('a')] -= 1

    # Final check for last window
    return matches(s1Map, windowMap)


def matches(map1, map2):
    # Compare both frequency arrays
    for i in range(26):
        if map1[i] != map2[i]:
            return False
    return True


# Test
s = "ab"
k = "eidbaooo"
print(checkInclusion(s, k))   # Output: True