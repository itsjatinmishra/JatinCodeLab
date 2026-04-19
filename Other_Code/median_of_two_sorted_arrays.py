def findMedianSortedArrays(nums1, nums2):
    # Step 1: Merge nums2 into nums1
    nums1.extend(nums2)

    # Step 2: Sort the merged array
    nums1.sort()

    # Step 3: Get total number of elements
    n = len(nums1)

    # Step 4: Check if length is even or odd
    if n % 2 == 0:
        # EVEN: average of two middle elements
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (nums1[mid1] + nums1[mid2]) / 2.0
    else:
        # ODD: return the middle element
        return float(nums1[n // 2])


# Example usage:
nums1 = [1, 3]
nums2 = [2]

print(findMedianSortedArrays(nums1, nums2))