class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet > 0:
                    k -= 1
                elif triplet < 0:
                    j += 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    # [-2, -2, 0, 0, 2, 2]
                    j += 1
                    while nums[j] == nums[j-1]:
                        j+=1
                
        
        return output
                