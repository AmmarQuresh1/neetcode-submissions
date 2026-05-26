import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_eating_rate = float("inf")

        while l <= r:
            mid = (l + r) // 2 
            eating_time = 0

            for bananas in piles:
                eating_time += math.ceil(bananas / mid)
            
            if eating_time <= h:
                min_eating_rate = min(min_eating_rate, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_eating_rate if min_eating_rate != float("inf") else -1