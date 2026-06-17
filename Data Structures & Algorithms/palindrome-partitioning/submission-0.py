class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur, res = [], []
        def is_palindrome(L, R):
            while L < R:
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                else:
                    return False
            return True


        def dfs(start):
            if start == len(s):
                res.append(cur[:])
                return
            
            for i in range(start, len(s)):
                L, R = start, i
                
                if is_palindrome(L, R):
                    cur.append(s[start:i+1])
                    dfs(i+1)
                    cur.pop()

        
        dfs(0)
        return res
        