import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        lookup_points = dict()

        for p in points:
            distances.append((math.sqrt(p[0]**2 + p[1]**2), p))

        heapq.heapify(distances)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        
        return res