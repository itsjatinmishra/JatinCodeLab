## 1st method but its too simple

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# i = 0
# j = 0
# result = []

# while i < len(list1) and j < len(list2):
#     #if element in list1 is smaller or equal
#     if list1[i] <= list2[j]:
#         result.append(list1[i])
#         i += 1
#     else:
#         result.append(list2[j])
#         j += 1

# while i < len(list1):
#     result.append(list1[i])
#     i += 1

# while j < len(list2):
#     result.append(list2[j])
#     j += 1

# print(result)



def merge(nums1, m, nums2, n):
    # i → last valid element index of nums1 (ignore extra 0s)
    i = m - 1  

    # j → last element index of nums2
    j = n - 1  

    # back → last index of nums1 (where we start filling from end)
    back = len(nums1) - 1  

    # Step 1: Compare elements from the end of both arrays
    while i >= 0 and j >= 0:
        
        # If nums1 element is bigger, place it at the back
        if nums1[i] > nums2[j]:
            nums1[back] = nums1[i]
            i -= 1  # move i left
        
        # Otherwise place nums2 element at the back
        else:
            nums1[back] = nums2[j]
            j -= 1  # move j left
        
        # Move back pointer after placing element
        back -= 1  

    # Step 2: If nums2 still has elements left
    # (this happens when nums1 elements are already used)
    while j >= 0:
        nums1[back] = nums2[j]   # copy remaining nums2 elements
        j -= 1
        back -= 1

    # No need to copy remaining nums1 elements
    # because they are already in correct position

    return nums1   # return for printing/testing


# Test
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))