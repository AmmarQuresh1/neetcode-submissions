class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word):
            if not word:
                return True

            if i < 0 or i >= len(board):
                return False
            
            if j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[0]:
                return False
            
            
            if dfs(i+1, j, word[1:]):
                return True
            if dfs(i-1, j, word[1:]):
                return True
            if dfs(i, j+1, word[1:]):
                return True
            if dfs(i, j-1, word[1:]):
                return True

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
        
        return False
