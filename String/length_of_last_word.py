class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Step 1: Remove extra spaces from both ends
        # Example: "   hello world  " -> "hello world"
        s = s.strip()

        # Step 2: Initialize counter for last word length
        length = 0

        # Step 3: Traverse string from the end
        # We go backwards because we only care about the LAST word
        for i in range(len(s) - 1, -1, -1):

            # If current character is not space → part of last word
            if s[i] != ' ':
                length += 1
            else:
                # If we hit a space AFTER counting letters → stop
                break

        # Step 4: Return length of last word
        return length