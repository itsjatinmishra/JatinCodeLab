def binary_search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2  # find middle index

        if nums[mid] == target:
            return mid            # target found
        elif nums[mid] > target:
            end = mid - 1         # search left
        else:
            start = mid + 1       # search right

    return -1                     # target not found


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binary_search(nums, target))