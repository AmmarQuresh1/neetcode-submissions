class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = set()
        output = []

        for r in range(len(nums)):
            if r - l == k:
                if nums[l] in window:
                    window.remove(nums[l])
                l += 1
            
            window.add(nums[r])

            if r - l + 1 == k:
                output.append(max(window))
        
        return output