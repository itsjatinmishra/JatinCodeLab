def trap(height):
    # Step 1: Create arrays to store left max and right max
    l_max = [0] * len(height)
    r_max = [0] * len(height)

    # Step 2: Initialize variables to track max values
    l_max_value = 0
    r_max_value = 0

    output = 0

    # Step 3: Fill left max array
    # l_max[i] = max height from 0 to i
    for i in range(len(height)):
        l_max_value = max(height[i], l_max_value)
        l_max[i] = l_max_value

    # Step 4: Fill right max array
    # r_max[i] = max height from i to end
    for i in range(len(height) - 1, -1, -1):
        r_max_value = max(height[i], r_max_value)
        r_max[i] = r_max_value

    # Step 5: Calculate trapped water
    for i in range(len(height)):
        # Water stored at index i
        value = min(l_max[i], r_max[i]) - height[i]

        # Only add if positive
        if value > 0:
            output += value

    # Step 6: Return result
    return output


# Input
height = [0,1,0,2,1,0,1,3,2,1,2,1]

# Output
print(trap(height))