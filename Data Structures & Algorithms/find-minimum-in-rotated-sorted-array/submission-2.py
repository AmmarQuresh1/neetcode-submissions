class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:

            mid = (l+r)//2
            res = min(nums[mid], res)

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid - 1
        
        return res