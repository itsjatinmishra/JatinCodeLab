# def thirdMax(nums):
#     first = second = third = float('-inf')

#     for num in nums:
#         # ignore duplicates
#         if num == first or num == second or num == third:
#             continue

#         if num > first:
#             third = second
#             second = first
#             first = num

#         elif num > second:
#             third = second
#             second = num

#         elif num > third:
#             third = num

#     if third == float('-inf'):
#         return first
#     return third


### More easy code solution

def thirdMax(nums):
    nums = list(set(nums))   # remove duplicates
    nums.sort(reverse=True)  # sort descending

    if len(nums) < 3:
        return nums[0]
    return nums[2]


nums = [2, 2, 3, 1]
print(thirdMax(nums))