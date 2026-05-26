class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_freq = defaultdict(int)

        for i in range(len(s1)):
            s1_char_freq[s1[i]] += 1
        
        L = 0
        s2_char_freq = defaultdict(int)
    
        for R in range(len(s2)):

            s2_char_freq[s2[R]] += 1

            if R - L + 1 > len(s1):
                s2_char_freq[s2[L]] -= 1
                if s2_char_freq[s2[L]] == 0:
                    s2_char_freq.pop(s2[L])
                L += 1

            if s2_char_freq == s1_char_freq:
                return True

        return False