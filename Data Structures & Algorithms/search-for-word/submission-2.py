class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word, seen):
            if not word:
                return True

            if i < 0 or i >= len(board):
                return False
            
            if j < 0 or j >= len(board[0]):
                return False
            
            if (i, j) in seen:
                return False
            seen.add((i,j))

            if board[i][j] != word[0]:
                return False
            
            
            if dfs(i+1, j, word[1:], seen):
                return True
            if dfs(i-1, j, word[1:], seen):
                return True
            if dfs(i, j+1, word[1:], seen):
                return True
            if dfs(i, j-1, word[1:], seen):
                return True

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word, set()):
                    return True
        
        return False
