class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        twonums = [0 for x in range(len(nums)*2)]
        for i in range (0, len(twonums)):
            twonums[i] = nums[i%len(nums)]
        return twonums