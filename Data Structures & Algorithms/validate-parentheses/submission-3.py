class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for i, c in enumerate(s):
            if c in pairs.values():
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == pairs[c]:
                stack.pop()
        
        if len(stack) == 0:
            return True
        return False