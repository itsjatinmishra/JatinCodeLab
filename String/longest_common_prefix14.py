def longestCommonPrefix(strs):
    # Step 1: Take the first string as initial prefix
    first_str = strs[0]

    # Step 2: Start comparing from second string
    i = 1

    # Step 3: Loop through all strings
    while i < len(strs):

        # Step 4: Check if current string starts with first_str
        # If not, keep reducing the prefix
        while strs[i].find(first_str) != 0:
            first_str = first_str[:-1]   # remove last character

            # Step 5: If prefix becomes empty → no common prefix
            if first_str == "":
                return ""

        # Move to next string
        i += 1

    # Step 6: Return the final common prefix
    return first_str


# Calling function
result = longestCommonPrefix(["flower","flow","flight","abc"])
print(result)