### BruteForce Approach
def searchRange(nums, target):
    start = -1
    end = -1

    for i in range(len(nums)):
        if nums[i] == target:
            if start == -1: #it means its first time
                start = i
            end = i #keep updating last position until its same
    
    return [start, end]

# def searchRange(nums, target):
#     start = 0
#     end = len(nums) - 1

#     while start <= end:
#         mid = (start + end) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             end = mid - 1
#         elif nums[mid] < target:
#             start = mid + 1
    
#     return [-1,-1]

nums = [5,7,7,8,8,10]
target = 8

print(searchRange(nums, target))