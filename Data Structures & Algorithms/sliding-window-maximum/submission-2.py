class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = []
        output = []

        for r in range(len(nums)):
            if r - l == k:
                window.remove(nums[l])
                l += 1
            
            window.append(nums[r])

            if r - l + 1 == k:
                output.append(max(window))
        
        return output