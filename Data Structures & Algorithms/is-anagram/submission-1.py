class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = dict()

        for c in s:
            charCount[c] = charCount.get(c, 0) + 1
        
        for c in t:
            if t.count(c) != charCount.get(c):
                return False
        
        return True