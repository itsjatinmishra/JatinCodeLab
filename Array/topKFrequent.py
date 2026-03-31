import heapq

def topKFrequent(nums, k):
    pq = []  # min-heap to store (frequency, number)

    # If k equals total elements, just return nums
    if k == len(nums):
        return nums

    count = {}

    # Step 1: Count frequency of each number
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    # Step 2: Push elements into heap
    for key, value in count.items():
        # Push (frequency, number)
        heapq.heappush(pq, (value, key))

        # Keep heap size at most k
        if len(pq) > k:
            # Remove the element with smallest frequency
            heapq.heappop(pq)

    # Step 3: Extract elements from heap
    result = []
    while pq:
        # heappop returns (frequency, number)
        # [1] means we take only the number, not frequency
        result.append(heapq.heappop(pq)[1])

    return result


nums = [1,2,2,4,4,4,3,3,3]
k = 3
print(topKFrequent(nums, k))