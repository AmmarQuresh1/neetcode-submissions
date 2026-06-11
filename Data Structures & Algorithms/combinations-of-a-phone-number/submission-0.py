class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        cur, res = [], []
        d_list = list(digits)
        d_map = {"2":"abc", 
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}

        for i in range(len(d_list)):
            d_list[i] = d_map[d_list[i]]

        def dfs(start):
            if len(cur) == len(d_list):
                res.append("".join(cur[:]))
                return
            if start == len(d_list):
                return
            for i in range(len(d_list[start])):
                cur.append(d_list[start][i])
                dfs(start+1)
                cur.pop()
        
        dfs(0)
        return res
