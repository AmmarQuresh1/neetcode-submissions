class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsdict:
                return [numsdict[complement], i]
            else:
                numsdict[nums[i]] = i