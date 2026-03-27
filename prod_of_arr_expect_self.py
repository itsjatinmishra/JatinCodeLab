# Brute-force approach (for understanding)
# Time Complexity: O(n^2)
# Not efficient for large inputs

# arr = [1,2,3,4]
# n = len(arr)
# ans = [0]*n
#
# for i in range(n):
#     product = 1
#     for j in range(n):
#         if j == i:
#             continue   # skip the current index
#         product *= arr[j]
#     ans[i] = product
#
# print(ans)


# Optimized Approach (Prefix & Suffix Product)
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)

def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize result array with 1
    result = [1] * n

    # Prefix product (left side)
    # pre stores product of all elements before index i
    pre = 1
    for i in range(n):
        result[i] = pre          # store prefix product
        pre = pre * nums[i]      # update prefix

    # Suffix product (right side)
    # post stores product of all elements after index i
    post = 1
    for i in range(n - 1, -1, -1):   # correct reverse loop
        result[i] = result[i] * post  # multiply with suffix
        post = post * nums[i]         # update suffix

    return result


# Example usage
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))