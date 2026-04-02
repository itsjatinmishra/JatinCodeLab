from collections import deque

def maxSlidingWindow(nums, k):
    # ---------------- EDGE CASE ----------------
    # If array is empty OR window size is invalid
    if not nums or k <= 0:
        return []

    n = len(nums)

    # Result array size = number of windows possible
    # Example: n=8, k=3 → 8-3+1 = 6 windows
    result = [0] * (n - k + 1)

    # Deque will store INDICES (not values)
    # Why indices? → So we can:
    # 1. Check if index is out of window
    # 2. Access actual value using nums[index]
    dq = deque()

    # ---------------- MAIN LOOP ----------------
    for i in range(n):

        # ==========================================================
        # STEP 1: REMOVE ELEMENTS OUTSIDE THE WINDOW
        # Window range = [i-k+1 ... i]
        # If index < (i-k+1), it means it's outside → remove it
        # ==========================================================
        while dq and dq[0] < i - k + 1:
            dq.popleft()   # remove from front (oldest element)

        # ==========================================================
        # STEP 2: REMOVE SMALLER ELEMENTS (IMPORTANT LOGIC)
        # If current element is greater than elements in deque,
        # those smaller elements will NEVER be maximum again
        # So we remove them from BACK
        # ==========================================================
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()   # remove smaller elements from back

        # ==========================================================
        # STEP 3: ADD CURRENT INDEX
        # After cleaning deque, add current element index
        # ==========================================================
        dq.append(i)

        # ==========================================================
        # STEP 4: STORE RESULT (WHEN WINDOW IS FULL)
        # Window is valid only when i >= k-1
        # Maximum element is always at FRONT of deque
        # ==========================================================
        if i >= k - 1:
            result[i - k + 1] = nums[dq[0]]

    return result


# ---------------- DRIVER CODE ----------------
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(nums, k))