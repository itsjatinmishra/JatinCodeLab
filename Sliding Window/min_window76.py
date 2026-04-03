def minWindow(s,t):
    t_hash = {}
    sub_hash = {}
    unique = 0
    create = 0

    #sliding window pointers
    left = 0
    right = 0

    sub_len = float("inf")
    ans = ""

    if len(s) == 0 or len(t) == 0:
        return ""
    
    for i in t:
        if i in t_hash:
            t_hash[i] += 1
        else:
            t_hash[i] = 1
    
    unique = len(t_hash.keys())

    for right in range(len(s)):
        #add current character into window
        char = s[right]
        if char in sub_hash:
            sub_hash[char] += 1
        else:
            sub_hash[char] = 1
        
        if char in t_hash and sub_hash[char] == t_hash[char]:
            create += 1
        
        while left <= right and create == unique:
            if (right - left + 1) < sub_len:
                sub_len = right - left + 1
                ans = s[left:right+1]
            
            sub_hash[s[left]] -= 1
        
            if s[left] in t_hash and sub_hash[s[left]] < t_hash[s[left]]:
                create -= 1
            
            left += 1
    
    return ans


s = "ABAXCBAC"
t = "ABC"
print(minWindow(s,t))