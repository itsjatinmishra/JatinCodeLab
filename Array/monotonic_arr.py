nums = [6,5,4,4]

increasing = True
decreasing = True

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        decreasing = False
    if nums[i] < nums[i - 1]:
        increasing = False

result = increasing or decreasing

print(result)