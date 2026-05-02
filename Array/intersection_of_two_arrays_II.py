nums1 = [1,2,2,1]
nums2 = [2,2]

# Step 1: Count elements of nums2
nums2_dict = {}
for i in nums2:
    nums2_dict[i] = nums2_dict.get(i, 0) + 1

# Step 2: Find intersection
result = []
for i in nums1:
    if i in nums2_dict and nums2_dict[i] > 0:
        result.append(i)
        nums2_dict[i] -= 1   # decrease count

print(result)