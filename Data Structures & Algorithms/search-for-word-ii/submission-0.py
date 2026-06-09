class Node:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.is_end = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(pos, node, res):
            (r, c) = pos
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == '#':
                return

            if board[r][c] not in node.next:
                return

            node = node.next[board[r][c]]

            if node.is_end:
                res.append(node.word)
                node.is_end = False

            temp = board[r][c]
            board[r][c] = '#'
            
            dfs((r+1, c), node, res)
            dfs((r, c+1), node, res)
            dfs((r-1, c), node, res)
            dfs((r, c-1), node, res)
            
            board[r][c] = temp
            
            return False
        
        # build trie
        root = Node("")
        for word in words:
            cur = root
            for c in word:
                if c not in cur.next:
                    cur.next[c] = Node(c)
                cur = cur.next[c]
            cur.is_end = True
            cur.word = word
        
        res = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                word = dfs((r, c), root, res)

        return res
            
        