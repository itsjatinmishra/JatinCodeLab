#Brute Force Approach
# def longestConsecutive(nums):
#     longest = 0

#     for num in nums:
#         current = num
#         count = 1

#         # check next numbers
#         while current + 1 in nums:
#             current += 1
#             count += 1

#         longest = max(longest, count)

#     return longest

#Optimal Solution
def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longestSub = 0

    for num in num_set:
        if num - 1 not in num_set:
            currNum = num
            currSub = 1

            while currNum + 1 in num_set:
                currNum += 1
                currSub += 1

            longestSub = max(longestSub, currSub)

    return longestSub


# test
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))