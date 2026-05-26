class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 1
        while R <= len(nums) - 1:
            if nums[L] == nums[R]:
                nums.remove(nums[R])
            else:
                L += 1
                R += 1
        return len(nums)