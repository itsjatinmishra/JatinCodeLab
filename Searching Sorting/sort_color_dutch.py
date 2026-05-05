# ### Minimal Optimal Solution

# nums = [2,0,2,1,1,0]

# countOfZero = countOfOne = countOfTwo = 0

# for i in nums:
#     if i == 0:
#         countOfZero += 1
#     elif i == 1:
#         countOfOne += 1
#     elif i == 2:
#         countOfTwo += 1

# # print(countOfZero, countOfOne, countOfTwo)

# idx = 0

# for i in range(countOfZero):
#     nums[idx] = 0
#     idx += 1
# for i in range(countOfOne):
#     nums[idx] = 1
#     idx += 1
# for i in range(countOfTwo):
#     nums[idx] = 2
#     idx += 1

# print(nums)


### much more optimal solution

def sortColors(nums):
    # l → position where next 0 should go
    # m → current element we are checking
    l = m = 0
    
    # h → position where next 2 should go (from the end)
    h = len(nums) - 1

    # loop until middle pointer crosses high pointer
    while m <= h:

        # CASE 1: current element is 0
        if nums[m] == 0:
            # swap current element with left position
            nums[l], nums[m] = nums[m], nums[l]

            # move both pointers forward
            # because left side is now correct (0 placed)
            l += 1
            m += 1

        # CASE 2: current element is 1
        elif nums[m] == 1:
            # 1 is already in correct middle region
            # just move forward
            m += 1

        # CASE 3: current element is 2
        elif nums[m] == 2:
            # swap with high position
            nums[m], nums[h] = nums[h], nums[m]

            # decrease high pointer
            h -= 1

            # IMPORTANT:
            # we DO NOT increase m here
            # because the new element at nums[m]
            # (after swap) is not checked yet

    return nums


nums = [2,0,2,1,1,0]
print(sortColors(nums))
