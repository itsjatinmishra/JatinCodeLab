### Minimal Optimal Solution

nums = [2,0,2,1,1,0]

countOfZero = countOfOne = countOfTwo = 0

for i in nums:
    if i == 0:
        countOfZero += 1
    elif i == 1:
        countOfOne += 1
    elif i == 2:
        countOfTwo += 1

# print(countOfZero, countOfOne, countOfTwo)

idx = 0

for i in range(countOfZero):
    nums[idx] = 0
    idx += 1
for i in range(countOfOne):
    nums[idx] = 1
    idx += 1
for i in range(countOfTwo):
    nums[idx] = 2
    idx += 1

print(nums)