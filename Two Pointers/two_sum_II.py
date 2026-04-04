def twoSum(numbers, target):
    # Initialize two pointers
    l = 0                      # left pointer starts from beginning
    r = len(numbers) - 1       # right pointer starts from end

    # Loop until pointers meet
    while l < r:
        current_sum = numbers[l] + numbers[r]   # calculate sum of two numbers

        # If sum is greater than target → move right pointer left
        if current_sum > target:
            r -= 1

        # If sum is smaller than target → move left pointer right
        elif current_sum < target:
            l += 1

        # If sum equals target → return 1-based indices
        else:
            return [l + 1, r + 1]

    # If no pair found (though problem usually guarantees one solution)
    return [-1]


# Example usage
numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))