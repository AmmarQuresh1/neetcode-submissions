class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur, res = [], []
        def dfs(start):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(start, n+1):
                cur.append(i)
                dfs(i+1)
                cur.pop()
        
        dfs(1)
        return res
