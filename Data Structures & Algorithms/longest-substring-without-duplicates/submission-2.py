class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L, longest_substring = 0, 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            longest_substring = max(R - L + 1, longest_substring)
            window.add(s[R])

        return longest_substring
