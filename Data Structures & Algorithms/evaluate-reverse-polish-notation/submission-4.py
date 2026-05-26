class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop() 
                    stack.append(b + a)
            elif t == '-':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop() 
                    stack.append(b - a)
            elif t == '*':
                if len(stack) >= 2:
                    a = stack.pop() 
                    b = stack.pop() 
                    stack.append(b * a)
            elif t == '/':
                if len(stack) >= 2:
                    a = stack.pop() 
                    b = stack.pop() 
                    if b == 0:
                        stack.append(0)
                    else:
                        stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[-1]
