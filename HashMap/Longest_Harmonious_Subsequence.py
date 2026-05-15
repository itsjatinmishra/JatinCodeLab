def findLHS(nums):
    frequency = {}

    for i in nums:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    frequency_arr = []

    for i in frequency.keys():
        frequency_arr.append(i)

    frequency_arr.sort()

    max_val = 0
    i = 0

    for j in range(1, len(frequency_arr)):

        if frequency_arr[j] - frequency_arr[i] == 1:
            max_temp = frequency[frequency_arr[i]] + frequency[frequency_arr[j]]
            max_val = max(max_val, max_temp)

        i += 1

    return max_val


nums = [1,3,2,2,5,2,3,7]

print(findLHS(nums))