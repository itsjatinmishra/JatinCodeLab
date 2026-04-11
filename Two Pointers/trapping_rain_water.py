# def trap(height):
#     # Step 1: Create arrays to store left max and right max
#     l_max = [0] * len(height)
#     r_max = [0] * len(height)

#     # Step 2: Initialize variables to track max values
#     l_max_value = 0
#     r_max_value = 0

#     output = 0

#     # Step 3: Fill left max array
#     # l_max[i] = max height from 0 to i
#     for i in range(len(height)):
#         l_max_value = max(height[i], l_max_value)
#         l_max[i] = l_max_value

#     # Step 4: Fill right max array
#     # r_max[i] = max height from i to end
#     for i in range(len(height) - 1, -1, -1):
#         r_max_value = max(height[i], r_max_value)
#         r_max[i] = r_max_value

#     # Step 5: Calculate trapped water
#     for i in range(len(height)):
#         # Water stored at index i
#         value = min(l_max[i], r_max[i]) - height[i]

#         # Only add if positive
#         if value > 0:
#             output += value

#     # Step 6: Return result
#     return output






def trap(height):
    # Step 1: Initialize two pointers
    left = 0                      # start from left
    right = len(height) - 1       # start from right

    total = 0                     # total trapped water

    # Step 2: Initialize left max and right max
    leftMax = height[left]        # max height from left side
    rightMax = height[right]      # max height from right side

    # Step 3: Traverse until both pointers meet
    while left < right:

        # Case 1: Left height is smaller
        if height[left] < height[right]:

            # Update left max
            leftMax = max(leftMax, height[left])

            # Water stored = leftMax - current height
            # Only positive values matter
            total += leftMax - height[left]

            # Move left pointer forward
            left += 1

        # Case 2: Right height is smaller or equal
        else:
            # Update right max
            rightMax = max(rightMax, height[right])

            # Water stored = rightMax - current height
            total += rightMax - height[right]

            # Move right pointer backward (IMPORTANT FIX)
            right -= 1

    return total


# Input
height = [0,1,0,2,1,0,1,3,2,1,2,1]

# Output
print(trap(height))