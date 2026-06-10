class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        def dfs(start, remaining_target):
            if remaining_target < 0:
                return
            if remaining_target == 0:
                res.append(cur[:])
                return
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i, remaining_target - nums[i])
                cur.pop()
        
        dfs(0, target)
        return res

