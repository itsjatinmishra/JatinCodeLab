def containsDuplicate(nums):
    my_set = set()

    for i in nums:
        if i in my_set:
            return True
        
        my_set.add(i)
    
    return False


nums = [1,2,3,4,4]

print(containsDuplicate(nums))