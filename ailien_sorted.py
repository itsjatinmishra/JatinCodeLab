def isAlienSorted(words, order):
        # Step 1: Create order map
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i

        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Compare characters
            for j in range(len(word1)):
                
                # Case: word2 is shorter but same prefix
                if j >= len(word2):
                    return False

                # If characters are different
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    break  # valid order, move to next pair

        return True


