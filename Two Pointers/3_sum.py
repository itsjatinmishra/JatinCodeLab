# class Solution:
#     def threeSum(self, nums):
#         nums.sort()  # Step 1: Sort the array
#         result = []  # This will store the final list of triplets

#         # Step 2: Loop through the array
#         for i in range(len(nums)):
            
#             # If the current number is greater than 0,
#             # we can't get sum = 0 anymore (since array is sorted)
#             if nums[i] > 0:
#                 break

#             # Skip duplicate values for i to avoid repeating triplets
#             if i == 0 or nums[i] != nums[i - 1]:
#                 # Call helper function to find pairs
#                 self.two_sum(nums, i, result)

#         return result

#     def two_sum(self, nums, i, result):
#         left = i + 1              # Pointer just after i
#         right = len(nums) - 1     # Pointer at the end

#         # Step 3: Use two pointers to find pairs
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]

#             # If sum is too small → move left pointer right
#             if total < 0:
#                 left += 1

#             # If sum is too large → move right pointer left
#             elif total > 0:
#                 right -= 1

#             # If sum == 0 → we found a valid triplet
#             else:
#                 result.append([nums[i], nums[left], nums[right]])

#                 # Move both pointers
#                 left += 1
#                 right -= 1

#                 # Skip duplicate values for left pointer
#                 # to avoid repeating same triplet
#                 while left < right and nums[left] == nums[left - 1]:
#                     left += 1


### short answer and this function is solved in one function only
def threeSum(nums):
    # Step 1: Sort the array
    # Why? So we can use two-pointer technique and easily skip duplicates
    nums.sort()

    # This will store all unique triplets whose sum = 0
    result = []

    # Step 2: Fix one number (nums[i]) and find two others
    for i in range(len(nums)):

        # Step 2.1: Skip duplicate values for i
        # If current number is same as previous, skip it to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Step 3: Use two pointers to find remaining two numbers
        left = i + 1                  # Start just after i
        right = len(nums) - 1         # Start from end of array

        # Loop until left pointer crosses right
        while left < right:

            # Calculate sum of current triplet
            total = nums[i] + nums[left] + nums[right]

            # Case 1: If sum is 0 → valid triplet found
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Step 4: Skip duplicate values for left pointer
                # Move left forward while next value is same
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicate values for right pointer
                # Move right backward while previous value is same
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers after finding a valid triplet
                left += 1
                right -= 1

            # Case 2: If sum is less than 0 → need bigger value
            elif total < 0:
                left += 1  # move left forward to increase sum

            # Case 3: If sum is greater than 0 → need smaller value
            else:
                right -= 1  # move right backward to decrease sum

    # Return all unique triplets
    return result


# Test input
nums = [-5, 0, -3, 5, 1, -5, 0, 2, 1]

# Function call
print(threeSum(nums))