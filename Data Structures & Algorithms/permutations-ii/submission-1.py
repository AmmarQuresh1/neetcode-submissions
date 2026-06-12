class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur, res, used = [], [], [False] * len(nums)
        def dfs():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i-1] == nums[i] and not used[i-1]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs()
                cur.pop()
                used[i] = False
                
        
        dfs()
        return res