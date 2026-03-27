class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []
        for i in range(len(s)-1,-1,-1):
            if stack and s[i] == " ":
                return len(stack)
            if s[i] != " ":
                stack.append(s[i])
        
        return len(stack)