class Solution:
    def trap(self, height: List[int]) -> int:
        # move pointers from ends inwards
        # keep track of each pointers max height 
        totalArea = 0
        L, R = 0, len(height) - 1
        lmax, rmax = 0, 0
        while L < R:
            if height[L] > lmax:
                lmax = height[L]
            if height[R] > rmax:
                rmax = height[R]

            if height[L] < lmax:
                totalArea += lmax - height[L]
            if height[R] < rmax:
                totalArea += rmax - height[R]
            
            # move lowest pointer
            if height[L] < height[R]:
                L+=1
            else:
                R-=1
        return totalArea