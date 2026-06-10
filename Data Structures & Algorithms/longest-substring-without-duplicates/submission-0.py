class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L, longest_substring = 0, 0

        for R in range(len(s)):
            while s[R] in window:
                longest_substring = max(R - L, longest_substring)
                window.remove(s[L])
                L += 1
            
            window.add(s[R])

        return longest_substring
