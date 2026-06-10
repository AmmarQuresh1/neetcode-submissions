class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # i:[2, 1, 1, 3]
        # o:[3, 2, 1, 0]

        stack = []
        result = []
        counter = 0
        length = len(temps)
        for i in range(length-1, -1, -1):
            if i == length-1:
                result.append(0)
                stack.append(temps[i])
                continue
            elif temps[i] > stack[-1]:
                result.append(0)
                stack.append(temps[i])
                continue
            else:
                for t2 in stack:
                    counter+=1
                    if t2 > temps[i]:
                        result.append(counter)
                        counter = 0
                        break
                    else:
                        result.append(0)
                        break

        result.reverse()
        return result