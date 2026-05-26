class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # i:[2, 1, 1, 3]
        # o:[3, 2, 1, 0]
        stack = []
        result = [0] * len(temps)
        for i, t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return result
