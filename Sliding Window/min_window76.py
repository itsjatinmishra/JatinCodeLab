def minWindow(s, t):
    t_hash = {}      # stores frequency of characters in t
    sub_hash = {}    # stores frequency of current window in s
    unique = 0       # total unique characters required from t
    create = 0       # how many characters are currently matched correctly

    # sliding window pointers
    left = 0
    right = 0

    sub_len = float("inf")   # store minimum window length
    ans = ""                 # store final answer (minimum substring)

    # edge case: if any string is empty
    if len(s) == 0 or len(t) == 0:
        return ""
    
    # build frequency map for string t
    for i in t:
        if i in t_hash:
            t_hash[i] += 1
        else:
            t_hash[i] = 1
    
    unique = len(t_hash.keys())  # number of unique characters we need

    # start expanding the window using right pointer
    for right in range(len(s)):
        # add current character into window
        char = s[right]
        if char in sub_hash:
            sub_hash[char] += 1
        else:
            sub_hash[char] = 1
        
        # if current character matches required frequency in t
        if char in t_hash and sub_hash[char] == t_hash[char]:
            create += 1   # increase matched count
        
        # try to shrink window when all required characters are matched
        while left <= right and create == unique:
            
            # update answer if current window is smaller
            if (right - left + 1) < sub_len:
                sub_len = right - left + 1
                ans = s[left:right+1]
            
            # remove left character from window
            sub_hash[s[left]] -= 1
        
            # if removing breaks required condition, decrease create
            if s[left] in t_hash and sub_hash[s[left]] < t_hash[s[left]]:
                create -= 1
            
            # move left pointer to shrink window
            left += 1
    
    return ans

s = "ABAXCBAC"
t = "ABC"
print(minWindow(s,t))