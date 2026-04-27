def move_zeros(nums):
    pos = 0  # position to place next non-zero

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    return nums

nums = [0,1,0,3,12]
print(move_zeros(nums))