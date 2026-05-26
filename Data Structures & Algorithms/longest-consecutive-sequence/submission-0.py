class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longestLength = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                currentNum = num
                while currentNum + 1 in nums_set:
                    currentNum += 1
                    length += 1
                longestLength = max(length, longestLength)
        
        return longestLength