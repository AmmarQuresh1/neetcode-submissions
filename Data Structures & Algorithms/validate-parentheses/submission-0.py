class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, c in enumerate(s):
            if c in ("(", "{", "["):
                stack.append(c)
            elif c in (")", "}", "]"):
                stack.pop()
        
        if len(stack) == 0:
            return True
        return False