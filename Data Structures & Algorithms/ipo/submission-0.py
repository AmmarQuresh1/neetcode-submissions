class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        profits = [-x for x in profits]
        heap1 = list(zip(profits, capital))
        heapq.heapify(heap1)
        heap2 = []

        for _ in range(k):
            next_project = None
            while(next_project == None):
                if heap1 and heap2:
                    (project1_profit, project1_capital) = heap1[0]
                    project1_profit = -project1_profit
                    (project2_profit, project2_capital) = heap2[0]
                    project2_profit = -project2_profit

                    # next project can be picked 
                    if w >= project1_capital and w >= project2_capital:
                        if project1_profit >= project2_profit:
                            next_project = heapq.heappop(heap1)
                        elif project2_profit > project1_profit:
                            next_project = heapq.heappop(heap2)
                    elif w >= project1_capital:
                        next_project = heapq.heappop(heap1)
                    elif w >= project2_capital:
                        next_project = heapq.heappop(heap2)
                    else: # next project cannot be picked
                        heapq.heappush(heap2, heapq.heappop(heap1))
                        continue
                        
                elif heap1:
                    (project1_profit, project1_capital) = heap1[0]
                    project1_profit = -project1_profit

                    if w >= project1_capital:
                        next_project = heapq.heappop(heap1)
                    else:
                        heapq.heappush(heap2, heapq.heappop(heap1))
                        continue

                elif heap2:
                    (project2_profit, project2_capital) = heap2[0]
                    project2_profit = -project2_profit

                    if w >= project2_capital:
                        next_project = heapq.heappop(heap2)
                    else:
                        heapq.heappush(heap1, heapq.heappop(heap2))
                        continue

                else:
                    return w

                w += -next_project[0]
                
                if next_project == (0, 0):
                    print("w: ",w)
                    print("No project selected")
                    print("heap1:", heap1)
                    print("heap2:", heap2)
                else:
                    print("w: ",w)
                    print("next_project:", next_project)
                    print("heap1:", heap1)
                    print("heap2:", heap2)

        return w
