class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet > 0:
                    k -= 1
                elif triplet < 0:
                    j += 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    break
        
        return output
                