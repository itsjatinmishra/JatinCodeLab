def twoSum(nums, target):
        my_hmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in my_hmap:
                return [my_hmap[complement], i]
            
            my_hmap[nums[i]] = i

nums = [1,7,3,2]
target = 9
print(twoSum(nums, target))