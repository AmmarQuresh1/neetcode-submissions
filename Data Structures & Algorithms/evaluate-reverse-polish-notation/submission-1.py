class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop() 
                    stack.append(a + b)
            elif t == '-':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop() 
                    stack.append(a - b)
            elif t == '*':
                if len(stack) >= 2:
                    a = stack.pop() 
                    b = stack.pop() 
                    stack.append(a * b)
            elif t == '/':
                if len(stack) >= 2:
                    a = stack.pop() 
                    b = stack.pop() 
                    stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[-1]
