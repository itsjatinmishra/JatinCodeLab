class Solution:
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        result = []  # This will store the final list of triplets

        # Step 2: Loop through the array
        for i in range(len(nums)):
            
            # If the current number is greater than 0,
            # we can't get sum = 0 anymore (since array is sorted)
            if nums[i] > 0:
                break

            # Skip duplicate values for i to avoid repeating triplets
            if i == 0 or nums[i] != nums[i - 1]:
                # Call helper function to find pairs
                self.two_sum(nums, i, result)

        return result

    def two_sum(self, nums, i, result):
        left = i + 1              # Pointer just after i
        right = len(nums) - 1     # Pointer at the end

        # Step 3: Use two pointers to find pairs
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            # If sum is too small → move left pointer right
            if total < 0:
                left += 1

            # If sum is too large → move right pointer left
            elif total > 0:
                right -= 1

            # If sum == 0 → we found a valid triplet
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Move both pointers
                left += 1
                right -= 1

                # Skip duplicate values for left pointer
                # to avoid repeating same triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1