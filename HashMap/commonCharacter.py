def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    # Count frequency of characters in first word
    common = {}

    for ch in words[0]:
        common[ch] = common.get(ch, 0) + 1

    # Compare with remaining words
    for word in words[1:]:

        temp = {}

        # Count chars in current word
        for ch in word:
            temp[ch] = temp.get(ch, 0) + 1

        # Keep minimum frequency
        for ch in list(common.keys()):
            if ch in temp:
                common[ch] = min(common[ch], temp[ch])
            else:
                common[ch] = 0

    # Build answer
    result = []

    for ch, freq in common.items():
        result.extend([ch] * freq)

    return result


# Example
print(commonChars(["bella", "label", "roller"]))
# Output: ['e', 'l', 'l']

print(commonChars(["cool", "lock", "cook"]))
# Output: ['c', 'o']