class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap = {}
        for i in range(len(nums)):
            if nums[i] in countmap:
                return True
            else:
                countmap[nums[i]] = 0
        return False