def containsDuplicate(nums, k):
    my_set = set()

    for i in range(len(nums)):
        if nums[i] in my_set:
            return True
        
        my_set.add(nums[i])
        
        if len(my_set) > k:
            my_set.discard(nums[i-k])
    return False



nums = [1,2,3,4,5]
k = 3
print(containsDuplicate(nums, k))