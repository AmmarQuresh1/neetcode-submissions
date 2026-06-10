class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False

        return True