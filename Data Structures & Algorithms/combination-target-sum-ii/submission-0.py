class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur, res = [], []
        candidates.sort()
        def dfs(start, remaining):
            if remaining < 0:
                return
            if remaining == 0:
                res.append(cur[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                dfs(i+1, remaining - candidates[i])
                cur.pop()
        
        dfs(0, target)
        return res

