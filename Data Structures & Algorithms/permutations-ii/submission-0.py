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
                if i>0 and nums[i-1] == nums[i] and used[i-1] == used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])
                print("append", cur, i, used)
                dfs()
                cur.pop()
                print("pop", cur, i, used)
                used[i] = False
                
        
        dfs()
        return res