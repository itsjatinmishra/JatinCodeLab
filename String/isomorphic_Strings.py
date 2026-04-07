def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # Dictionary to store mapping from s -> t
    mapST = {}

    # Dictionary to store mapping from t -> s
    # (this ensures no two characters from s map to same character in t)
    mapTS = {}

    # Loop through each character of both strings
    for i in range(len(s)):

        # Current character from string s
        c1 = s[i]

        # Corresponding character from string t
        c2 = t[i]

        # ----------- CHECK 1: s -> t mapping -----------

        # If c1 is already mapped before
        if c1 in mapST:
            # Check if it maps to the same character c2
            if mapST[c1] != c2:
                # Conflict found → mapping not consistent
                return False
        else:
            # If not mapped before, create new mapping
            mapST[c1] = c2

        # ----------- CHECK 2: t -> s mapping -----------

        # If c2 is already mapped before
        if c2 in mapTS:
            # Check if it maps back to the same character c1
            if mapTS[c2] != c1:
                # Conflict found → multiple characters mapping to same char
                return False
        else:
            # If not mapped before, create reverse mapping
            mapTS[c2] = c1

    # If loop completes without conflict → strings are isomorphic
    return True