class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r] and nums[r] > target:
                l = mid + 1
            else:
                r = mid
        
        return -1