class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        total_oranges = 0

        # total oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    total_oranges += 1
                    q.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    total_oranges += 1
        
        time = 0
        rotten_oranges = 0
        while q:
            rotten_oranges += len(q)
            print(q)
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or
                        nr == ROWS or
                        nc == COLS or
                        grid[nr][nc] == 0 or
                        (nr, nc) in visit):
                        continue
                    
                    q.append((nr, nc))
                    visit.add((nr, nc))
            #print(q)
            if q:
                time += 1
        print(rotten_oranges, total_oranges)

        return time if rotten_oranges == total_oranges else -1