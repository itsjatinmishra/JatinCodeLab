def nextPermutation(nums):
    # Step 1: Start from second last index
    # We move from right → left to find the "break point"
    i = len(nums) - 2

    # Step 2: Find the first element which is smaller than its next element
    # This is where the next permutation change should happen
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 3: If such an element is found (i >= 0)
    # we need to replace it with the just bigger element from right side
    if i >= 0:
        j = len(nums) - 1

        # Find the smallest number greater than nums[i] from right side
        while nums[j] <= nums[i]:
            j -= 1

        # Swap both values
        swap(nums, i, j)

    # Step 4: Reverse the part after index i
    # This makes the right side smallest (ascending order)
    reverse(nums, i + 1)


def swap(nums, i, j):
    # Swap two elements using Python tuple unpacking
    nums[i], nums[j] = nums[j], nums[i]


def reverse(nums, i):
    # Reverse the subarray from index i to end
    # This converts decreasing order → increasing order
    nums[i:] = reversed(nums[i:])


nums = [1, 2, 3]

nextPermutation(nums)   # function modifies nums
print(nums)             # now print updated list