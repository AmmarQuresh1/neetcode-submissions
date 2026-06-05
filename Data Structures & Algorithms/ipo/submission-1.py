class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq

        capital_heap = list(zip(capital, profits))
        heapq.heapify(capital_heap)

        profit_heap = []

        for _ in range(k):
            while capital_heap and (w >= capital_heap[0][0]):
                (profit_c, profit_p) = heapq.heappop(capital_heap)
                heapq.heappush_max(profit_heap, (profit_p, profit_c))

            if profit_heap:
                w += heapq.heappop_max(profit_heap)[0]
            else:
                break

        return w
