def wordPattern(pattern, s):
    words = s.split()
    
    # Step 1: length check
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for c, w in zip(pattern, words):
        
        # Case 1: if mapping already exists
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        
        else:
            char_to_word[c] = w
        
        # Case 2: reverse mapping check
        if w in word_to_char:
            if word_to_char[w] != c:
                return False
        
        else:
            word_to_char[w] = c
    
    return True