class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        length = 0

        for ch in s:
            if ch in seen:
                length += 2
                seen.remove(ch)
            else:
                seen.add(ch)

        # One odd character can be placed in center
        if seen:
            length += 1

        return length