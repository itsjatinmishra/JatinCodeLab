def find_missing_positive(nums):
    # Dictionary to store numbers
    # Key = number from array
    # Value = same number (or -1 for non-positive numbers)
    my_dict = {}

    # Step 1: Fill dictionary
    for i in range(len(nums)):
        # If number is negative or zero
        if nums[i] <= 0 or nums[i] > len(nums):
            # Store it with value -1 (just marking it)
            my_dict[nums[i]] = -1
        else:
            # Store positive number as key and value
            my_dict[nums[i]] = nums[i]

    # Step 2: Start checking from 1 (smallest positive number)
    i = 1

    # We check till len(nums) + 1
    # Because missing number will always be in this range
    while i < len(nums) + 2:
        # If number exists in dictionary
        if i in my_dict:
            # Move to next number
            i += 1
        else:
            # First missing positive number found
            return i

    return len(nums) + 1


# Example usage
nums = [3, 4, -1, 1]
result = find_missing_positive(nums)
print(result)