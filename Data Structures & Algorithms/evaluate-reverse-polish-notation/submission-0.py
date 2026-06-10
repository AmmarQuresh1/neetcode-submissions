class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        result = 0
        for t in tokens:
            if t == '+':
                while operands:
                    a = operands.pop()
                    b = operands.pop() if operands else 0
                    result += a + b
            elif t == '-':
                while operands:
                    a = operands.pop()
                    b = operands.pop() if operands else 0
                    result -= a - b
            elif t == '*':
                while operands:
                    a = operands.pop()
                    b = operands.pop() if operands else 1
                    result *= a * b
            elif t == '/':
                while operands:
                    a = operands.pop()
                    b = operands.pop() if operands else 1
                    result /= a / b
            else:
                operands.append(int(t))

        return result
