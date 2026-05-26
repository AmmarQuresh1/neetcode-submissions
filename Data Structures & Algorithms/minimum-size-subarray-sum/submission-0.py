class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0 
        min_array_length = float("inf")
        running_sum = 0

        for R in range(len(nums)):
            running_sum += nums[R]
            while running_sum >= target:
                min_array_length = min(min_array_length, R - L + 1)
                running_sum -= nums[L]
                L += 1
        
        return 0 if min_array_length == float("inf") else min_array_length
