class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        import heapq
        
        time = 0

        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        
        max_heap = []
        for k, v in task_count.items():
            max_heap.append(-v)
        
        heapq.heapify(max_heap)

        q = deque()

        while max_heap or q:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count < 0:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time