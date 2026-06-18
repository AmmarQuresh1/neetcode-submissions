class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, queens = [], []

        def restricted(pos):
            for i in range(len(queens)):
                # horizontal
                if pos//n == queens[i]//n:
                    return True
                # vertical
                if pos % n == queens[i] % n:
                    return True
                # diagonal
                if abs(pos//n - queens[i]//n) == abs(pos%n - queens[i]%n):
                    return True
            return False

        def dfs(start): # pos ref to list position flattened 
            if len(queens) == n:
                res.append(queens[:])
                return

            # place queen (if pos not restricted) 
            for i in range(start, n * n):
                r, c = i // n, i % n
                # calculate restricted 
                if not restricted(i):
                    queens.append(i)
                    dfs(i+1)
                    # unchoose (try another position)
                    queens.pop()
                else:
                    continue
        

        dfs(0)
        
        # convert positions to board string
        output = []
        for i in range(len(res)):
            board = []
            for y in range(len(res[0])):
                r, c = res[i][y] // n, res[i][y] % n
                char = ['.' for _ in range(n)]
                char[c] = 'Q'
                board.append(''.join(char))
            output.append(board)
        
        return output
        