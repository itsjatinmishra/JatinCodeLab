def maxArea(height):
    # Step 1: Initialize two pointers
    # l starts from beginning, r starts from end
    l = 0
    r = len(height) - 1

    # This will store the maximum water found so far
    max_water = 0

    # Step 2: Run loop until both pointers meet
    while l < r:

        # Step 3: Find the height of container
        # Water depends on the smaller wall
        length = min(height[l], height[r])

        # Step 4: Find width (distance between two walls)
        width = r - l

        # Step 5: Calculate area (water stored)
        area = length * width

        # Step 6: Update maximum water if current area is bigger
        max_water = max(max_water, area)

        # Step 7: Move pointer strategically
        # IMPORTANT LOGIC:
        # Move the pointer which has smaller height
        # Because moving bigger height won't help increase area

        if height[l] < height[r]:
            # Left wall is smaller → move left pointer forward
            l += 1
        else:
            # Right wall is smaller or equal → move right pointer backward
            r -= 1

    # Step 8: Return the maximum water found
    return max_water


# Input array (heights of vertical lines)
height = [1,8,6,2,5,4,8,3,7]

# Function call
print(maxArea(height))