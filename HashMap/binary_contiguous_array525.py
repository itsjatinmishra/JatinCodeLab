def findMaxLength(nums):
    # Step 1: Convert 0 → -1 and 1 → +1
    # This helps us reduce the problem to finding longest subarray with sum = 0
    new_nums = []
    for num in nums:
        if num == 0:
            new_nums.append(-1)
        else:
            new_nums.append(1)

    # Step 2: Initialize variables
    max_len = 0
    running_sum = 0
    seen = {}  # stores first occurrence of running_sum

    # Step 3: Traverse array
    for i in range(len(new_nums)):
        running_sum += new_nums[i]

        # If sum becomes 0 → valid subarray from 0 to i
        if running_sum == 0:
            max_len = i + 1

        # If running_sum seen before → subarray in between has sum 0
        if running_sum in seen:
            length = i - seen[running_sum]
            max_len = max(max_len, length)
        else:
            # store first occurrence only
            seen[running_sum] = i

    return max_len


# Example test
nums = [0, 1, 0, 1]
print(findMaxLength(nums))  # Output: 4