class Solution:
    def climbStairs(self, n: int) -> int:

        def _dfs(i):
            if i >= n:
                return i == n
            return _dfs(i + 1) + _dfs(i + 2)
        
        return _dfs(0)
