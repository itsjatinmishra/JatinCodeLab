from collections import deque

def maxSlidingWindow(nums, k):
    # Edge case handling
    if not nums or k <= 0:
        return []

    n = len(nums)
    result = [0] * (n - k + 1)   # Output array
    dq = deque()  # Will store indices

    for i in range(n):
        # 1. Remove indices out of current window
        # Window range: [i-k+1, i]
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # 2. Remove elements smaller than current element
        # because they will never be maximum
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 3. Add current index
        dq.append(i)

        # 4. Add max element to result when window is formed
        if i >= k - 1:
            result[i - k + 1] = nums[dq[0]]

    return result


nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums,k))