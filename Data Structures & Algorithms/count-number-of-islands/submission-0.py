class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == '0' or
                (r, c) in visit):
                return
            
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands