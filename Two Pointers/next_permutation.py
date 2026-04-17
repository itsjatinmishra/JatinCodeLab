def nextPermutation(nums):
    i = len(nums) - 2

    # find breakpoint
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # swap with next greater
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)

    # reverse suffix
    reverse(nums, i + 1)


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def reverse(nums, i):
    nums[i:] = reversed(nums[i:])


nums = [1, 2, 3]

nextPermutation(nums)   # function modifies nums
print(nums)             # now print updated list