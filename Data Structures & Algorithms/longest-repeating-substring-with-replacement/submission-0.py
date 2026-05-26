class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        L, max_freq, largest_window = 0, 0, 0

        for R in range(len(s)):
            char_counts[s[R]] += 1

            max_freq = max(char_counts[s[R]], max_freq)

            if (R - L + 1) - max_freq > k:
                char_counts[s[L]] -= 1
                L += 1

            largest_window = max(R - L + 1, largest_window)

        return largest_window
