class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, inclusion_count = 0, 0

        for R in range(len(s2)):
            if s2[R] in s1:
                L = R
                inclusion_count += 1
        
        if inclusion_count == len(s1):
            return True
        return False

            