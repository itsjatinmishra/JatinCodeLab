def removeDuplicates(nums):
    # Pointer to place the next unique element
    insertIndex = 1

    # Loop starts from index 1 (second element)
    # because we compare current element with previous one
    for i in range(1, len(nums)):

        # If current element is different from previous
        # it means it's a new unique element
        if nums[i - 1] != nums[i]:

            # Place the unique element at insertIndex position
            nums[insertIndex] = nums[i]

            # Move insertIndex forward for next unique element
            insertIndex += 1
    
    # Return the count of unique elements
    return insertIndex


# Input array (must be sorted)
nums = [0,0,1,1,1,2,2,3,3,4]

# Function call
result = removeDuplicates(nums)

# Print number of unique elements
print(result)

# Optional: Print updated array (only first 'result' elements are valid)
print(nums[:result])