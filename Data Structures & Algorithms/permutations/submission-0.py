class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur, res, used = [], [], [False] * len(nums)
        def dfs():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs()
                cur.pop()
                used[i] = False
        
        dfs()
        return res
        