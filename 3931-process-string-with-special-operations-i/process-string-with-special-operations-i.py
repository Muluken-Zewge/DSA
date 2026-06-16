class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            elif c == '#':
                stack += stack
            elif c == '%':
                stack = stack[::-1]
            else:
                stack.append(c)
        
        return "".join(stack)