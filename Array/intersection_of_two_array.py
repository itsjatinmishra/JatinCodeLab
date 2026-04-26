def intersection(nums1, nums2):
    nums1_set = set()
    nums2_set = set()

    for i in nums1:
        nums1_set.add(i)

    for i in nums2:
        nums2_set.add(i)

    result = nums1_set.intersection(nums2_set)
    return list(result)


# Example usage
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(intersection(nums1, nums2))