def intersection(nums1, nums2):
    # Create empty sets to store unique elements from both lists
    nums1_set = set()
    nums2_set = set()

    # Loop through nums1 and add each element to nums1_set
    # Sets automatically remove duplicate values
    for i in nums1:
        nums1_set.add(i)

    # Loop through nums2 and add each element to nums2_set
    for i in nums2:
        nums2_set.add(i)

    # Find the common elements between both sets
    # This is called "intersection"
    result = nums1_set.intersection(nums2_set)

    # Convert the result (which is a set) into a list and return it
    return list(result)


# Example usage
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# Call the function and print the result
print(intersection(nums1, nums2))