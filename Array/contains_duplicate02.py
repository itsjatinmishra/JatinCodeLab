def containsDuplicate(nums, k):
    my_set = set()

    for i in range(len(nums)):
        if nums[i] in my_set:
            return True
        
        my_set.add(nums[i])
        
        # Maintain window of size k
        if i >= k:
            my_set.remove(nums[i - k])
    
    return False


# Test cases
print(containsDuplicate([1,2,3,1], 3))   # True
print(containsDuplicate([1,0,1,1], 1))   # True
print(containsDuplicate([1,2,3,1,2,3], 2))  # False