#Brute Force Approach
def longestConsecutive(nums):
    longest = 0

    for num in nums:
        current = num
        count = 1

        # check next numbers
        while current + 1 in nums:
            current += 1
            count += 1

        longest = max(longest, count)

    return longest

# test
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))