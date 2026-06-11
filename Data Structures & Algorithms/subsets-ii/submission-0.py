class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur, res = [], []
        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            dfs(i+1) 
        
        dfs(0)
        return res