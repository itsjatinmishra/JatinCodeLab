def groupAnagrams(strs):
            # Edge case: if input list is empty
        if len(strs) == 0:
            return []

        # Dictionary to store grouped anagrams
        # key -> character frequency pattern
        # value -> list of anagrams
        ans_map = {}

        for s in strs:
            # Step 1: Create frequency array for 26 letters
            count = [0] * 26

            # Step 2: Count each character in string
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Step 3: Convert count array into a unique key
            # Example: "eat" -> "#1#0#0#0...#1#0#...#1"
            key = ''
            for i in range(26):
                key += '#' + str(count[i])

            # Step 4: Store in hashmap
            if key not in ans_map:
                ans_map[key] = []

            ans_map[key].append(s)

        # Step 5: Return grouped anagrams
        return list(ans_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))