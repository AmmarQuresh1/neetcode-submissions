class Solution:
    def maxArea(self, height: List[int]) -> int:
        # keep track of biggest container as you go along
        largest_size = 0
        L, R = 0, len(height) - 1
        while L < R:
            current_size = (R - L) * min(height[L], height[R])
            largest_size = max(current_size, largest_size)
            if height[L] < height[R]:
                L+=1
            else:
                R-=1
        return largest_size