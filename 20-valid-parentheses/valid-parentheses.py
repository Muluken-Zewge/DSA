class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ')':'(', ']':'[','}':'{' }
        stack = []

        for char in s:
            if char in set(']})') and stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
