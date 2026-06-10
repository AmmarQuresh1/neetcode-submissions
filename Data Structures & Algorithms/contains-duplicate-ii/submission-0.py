class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if nums[R] in window:
                return True
            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1
            
            window.add(nums[R])
        
        return False